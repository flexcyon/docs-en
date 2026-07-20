import { Yace } from "./yace/index.js";
import { highlightJson } from "./highlighters.js";

const CONFIG = window.__MIGRATOR_CONFIG;
const { i18n, pythonScriptUrl, vendoredIndexUrl } = CONFIG;

let pyodide;
let uploadedFileName = null;

async function initPyodide() {
  const btn = document.getElementById("migrateBtn");
  const spinner = document.getElementById("migrateBtnSpinner");
  const btnText = document.getElementById("migrateBtnText");
  if (!btn) return;

  try {
    pyodide = await loadPyodide({ indexURL: vendoredIndexUrl });

    const response = await fetch(pythonScriptUrl);
    if (!response.ok) throw new Error("Could not fetch migrator.py");
    const pythonCode = await response.text();

    await pyodide.runPythonAsync('__name__ = "migrator"\n' + pythonCode);

    btnText.innerText = i18n.btnRun;
    btn.disabled = false;
    spinner.style.display = "none";
  } catch (err) {
    console.error("Pyodide Initialization Error: ", err);
    if (btn) btnText.innerText = i18n.failedInit;
    spinner.style.display = "none";
  }
}

function setLoadingState(loading) {
  const btn = document.getElementById("migrateBtn");
  const spinner = document.getElementById("migrateBtnSpinner");
  const btnText = document.getElementById("migrateBtnText");
  if (!btn) return;
  btn.disabled = loading;
  spinner.style.display = loading ? "inline-block" : "none";
  btnText.innerText = loading ? i18n.migrating : i18n.btnRun;
}

function showToast(el, msg, duration) {
  if (!el) return;
  el.textContent = msg;
  el.style.display = "inline";
  clearTimeout(el._hideTimer);
  el._hideTimer = setTimeout(() => { el.style.display = "none"; }, duration || 2000);
}

async function clipboardCopy(text) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch { /* fall through */ }
  }
  try {
    const ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    ta.style.pointerEvents = "none";
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    const ok = document.execCommand("copy");
    document.body.removeChild(ta);
    return ok;
  } catch {
    return false;
  }
}

async function clipboardPaste() {
  if (navigator.clipboard && navigator.clipboard.readText) {
    try {
      const text = await navigator.clipboard.readText();
      return text;
    } catch { /* fall through */ }
  }
  return null;
}

function triggerDownload(content) {
  const a = document.createElement("a");
  a.href = "data:application/json;charset=utf-8," + encodeURIComponent(content);
  const base = uploadedFileName;
  a.download = base
    ? base.replace(/(\.json)?$/i, "_migrated.json")
    : i18n.downloadFilename;
  a.click();
  a.remove();
}

window.addEventListener("DOMContentLoaded", () => {
  if (typeof loadPyodide !== "undefined") {
    initPyodide();
  } else {
    const scriptTag = document.querySelector('script[src*="pyodide.js"]');
    if (scriptTag) scriptTag.onload = initPyodide;
  }

  const inputEditor = new Yace("#inputJsonEditor", {
    value: "",
    highlighters: [highlightJson],
  });
  inputEditor.textarea.placeholder = '{ "flexcyon-rtz-mode": true }';

  const outputEditor = new Yace("#outputJsonEditor", {
    value: "",
    highlighters: [highlightJson],
  });
  outputEditor.textarea.readOnly = true;

  const fileInput = document.getElementById("jsonFileInput");
  const browseBtn = document.getElementById("browseBtn");
  const fileNameDisplay = document.getElementById("fileNameDisplay");
  const clearFileBtn = document.getElementById("clearFileBtn");

  if (browseBtn && fileInput) {
    browseBtn.addEventListener("click", () => fileInput.click());
  }

  if (fileInput) {
    fileInput.addEventListener("change", function(e) {
      const file = e.target.files[0];
      if (!file) return;
      uploadedFileName = file.name;
      if (fileNameDisplay) fileNameDisplay.textContent = file.name;
      if (clearFileBtn) clearFileBtn.style.display = "inline-flex";
      const reader = new FileReader();
      reader.onload = function(evt) {
        inputEditor.update({ value: evt.target.result });
      };
      reader.readAsText(file);
    });
  }

  if (clearFileBtn) {
    clearFileBtn.addEventListener("click", function() {
      if (fileInput) fileInput.value = "";
      uploadedFileName = null;
      if (fileNameDisplay) fileNameDisplay.textContent = i18n.noFile;
      clearFileBtn.style.display = "none";
      inputEditor.update({ value: "" });
    });
  }

  const clearInputBtn = document.getElementById("clearInputBtn");
  if (clearInputBtn) {
    clearInputBtn.addEventListener("click", function() {
      if (fileInput) fileInput.value = "";
      uploadedFileName = null;
      if (fileNameDisplay) fileNameDisplay.textContent = i18n.noFile;
      if (clearFileBtn) clearFileBtn.style.display = "none";
      inputEditor.update({ value: "" });
      inputEditor.textarea.focus();
    });
  }

  const pasteBtn = document.getElementById("pasteBtn");
  if (pasteBtn) {
    pasteBtn.addEventListener("click", async () => {
      const fb = document.getElementById("pasteFeedback");
      const text = await clipboardPaste();
      if (text !== null) {
        inputEditor.textarea.focus();
        const start = inputEditor.textarea.selectionStart;
        const end = inputEditor.textarea.selectionEnd;
        const current = inputEditor.value;
        const newVal = current.slice(0, start) + text + current.slice(end);
        const pos = start + text.length;
        inputEditor.update({ value: newVal, selectionStart: pos, selectionEnd: pos });
        showToast(fb, i18n.toastPasted);
      } else {
        showToast(fb, i18n.toastPasteBlocked, 3000);
      }
    });
  }

  const copyBtn = document.getElementById("copyBtn");
  if (copyBtn) {
    copyBtn.addEventListener("click", async () => {
      const text = outputEditor.value;
      if (!text) return;
      const fb = document.getElementById("copyFeedback");
      const ok = await clipboardCopy(text);
      showToast(fb, ok ? i18n.toastCopied : i18n.toastCopyFailed, 3000);
    });
  }

  const migrateBtn = document.getElementById("migrateBtn");
  if (migrateBtn) {
    migrateBtn.addEventListener("click", async () => {
      const placeholder = '{ "flexcyon-rtz-mode": true }';
      const inputVal = inputEditor.value.trim() || placeholder;
      const outputSection = document.getElementById("outputSection");
      const downloadBtn = document.getElementById("downloadBtn");
      const outputEditorEl = document.getElementById("outputJsonEditor");
      const copyBtn = document.getElementById("copyBtn");

      outputSection.style.display = "";
      setLoadingState(true);

      try {
        pyodide.globals.set("js_input_string", inputVal);

        const resultJson = await pyodide.runPythonAsync(`
import json
valid, err = validate_json_with_ast(js_input_string)
if not valid:
    raise Exception(err)

mapper = SettingsMapper(get_mapping_config())
parsed_input = json.loads(js_input_string)
migrated_output = mapper.map_settings(parsed_input)

json.dumps(migrated_output, indent=2)
        `);

        outputEditor.update({ value: resultJson });
        outputEditorEl.style.display = "";
        document.getElementById("langBadge").style.display = "inline";

        downloadBtn.style.display = "inline-block";
        downloadBtn.disabled = false;
        downloadBtn.onclick = () => triggerDownload(resultJson);
        copyBtn.style.display = "inline-flex";
      } catch (error) {
        outputEditor.update({ value: i18n.errorPrefix + error.message });
        outputEditorEl.style.display = "";
        downloadBtn.style.display = "none";
        document.getElementById("langBadge").style.display = "none";
        copyBtn.style.display = "none";
      } finally {
        setLoadingState(false);
      }
    });
  }
});
