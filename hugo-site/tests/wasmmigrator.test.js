import { describe, it, expect, beforeEach, afterEach } from "vitest";
import { Yace } from "yace";
import { highlightJson } from "../static/js/highlighters.js";

describe("highlightJson highlighter", () => {
  it("highlights a JSON string with s2 span", () => {
    const input = '"hello world"';
    const result = highlightJson(input);
    expect(result).toBe('<span class="s2">"hello world"</span>');
  });

  it("highlights a number with mi span", () => {
    const input = "42";
    const result = highlightJson(input);
    expect(result).toBe('<span class="mi">42</span>');
  });

  it("highlights a negative float with mi span", () => {
    const input = "-3.14";
    const result = highlightJson(input);
    expect(result).toBe('<span class="mi">-3.14</span>');
  });

  it("highlights scientific notation with mi span", () => {
    const input = "2.5e10";
    const result = highlightJson(input);
    expect(result).toBe('<span class="mi">2.5e10</span>');
  });

  it("highlights null with kc span", () => {
    const input = "null";
    const result = highlightJson(input);
    expect(result).toBe('<span class="kc">null</span>');
  });

  it("highlights true with kc span", () => {
    const input = "true";
    const result = highlightJson(input);
    expect(result).toBe('<span class="kc">true</span>');
  });

  it("highlights false with kc span", () => {
    const input = "false";
    const result = highlightJson(input);
    expect(result).toBe('<span class="kc">false</span>');
  });

  it("handles HTML special characters", () => {
    const input = '"a&b<c>"';
    const result = highlightJson(input);
    expect(result).toContain("&amp;");
    expect(result).toContain("&lt;");
    expect(result).toContain("&gt;");
  });

  it("highlights a complete JSON object with mixed types", () => {
    const input = JSON.stringify({ name: "test", count: 42, active: true, data: null });
    const result = highlightJson(input);
    expect(result).toContain('class="s2"');
    expect(result).toContain('class="mi"');
    expect(result).toContain('class="kc"');
    expect(result).toContain('"test"');
    expect(result).toContain("42");
    expect(result).toContain("true");
    expect(result).toContain("null");
  });
});

describe("yace integration with highlightJson", () => {
  let root;

  beforeEach(() => {
    root = document.createElement("div");
    document.body.appendChild(root);
  });

  afterEach(() => {
    root.remove();
  });

  it("creates textarea and pre elements", () => {
    const editor = new Yace(root, { highlighters: [highlightJson] });
    expect(editor.textarea).toBeInstanceOf(HTMLTextAreaElement);
    expect(editor.pre).toBeInstanceOf(HTMLPreElement);
    expect(root.querySelector("textarea")).toBe(editor.textarea);
    expect(root.querySelector("pre")).toBe(editor.pre);
  });

  it("renders initial empty value without error", () => {
    const editor = new Yace(root, { highlighters: [highlightJson] });
    expect(editor.value).toBe("");
    expect(editor.pre.innerHTML).toBeDefined();
  });

  it("renders syntax-highlighted JSON in pre element", () => {
    const editor = new Yace(root, { highlighters: [highlightJson] });
    editor.update({ value: '{"key": "value", "num": 42, "ok": true}' });
    const html = editor.pre.innerHTML;
    expect(html).toContain('<span class="s2">');
    expect(html).toContain('<span class="mi">');
    expect(html).toContain('<span class="kc">');
    expect(html).toContain('"key"');
    expect(html).toContain('"value"');
    expect(html).toContain("42");
    expect(html).toContain("true");
  });

  it("updates textarea value and pre synchronously", () => {
    const editor = new Yace(root, { highlighters: [highlightJson] });
    const json = '{"a":1}';
    editor.update({ value: json });
    expect(editor.textarea.value).toBe(json);
    expect(editor.pre.innerHTML).toContain('<span class="s2">');
    expect(editor.pre.innerHTML).toContain('<span class="mi">');
  });

  it("handles multiple rapid updates", () => {
    const editor = new Yace(root, { highlighters: [highlightJson] });
    editor.update({ value: "1" });
    editor.update({ value: '"hello"' });
    editor.update({ value: "true" });
    expect(editor.value).toBe("true");
    expect(editor.pre.innerHTML).toContain('class="kc"');
  });
});
