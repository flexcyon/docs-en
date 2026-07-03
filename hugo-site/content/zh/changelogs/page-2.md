---
title: 2.x.x 版本 
---

## 2.0.x 版本 

### 2.0.0 版本: 蜕变

#### 功能
- 改进了无障碍, 您现在可以调整主题颜色的对比度, 亮度, 饱和度和色温.
- 主题的颜色现在大多使用 `oklch` 颜色空间, 以获得更精确的显色效果
    - 覆盖了代码库中的一些默认硬编码值，以使用“oklch”颜色等效值
- 样式设置
    - 添加了防止意外取消固定, 通过单击固定图标禁用取消固定.
    若要在启用此设置的情况下取消固定, 请使用右键单击菜单或 Ctrl+W.
    - 添加编辑器顶部边距
    - 添加 Callout 水平边距
    - 添加禁用 Vim 块光标闪烁
    - 在 "样式设置" 中添加了 "隐藏关键点链" 项
    - 添加滚动条宽度的样式设置选项, 将现有滚动条移动到 "设置" 中不显示滚动条 `flexcyon://Editor > Scrollbar`
- 添加了对 Banners Reloaded 插件的支持
- 主题现在有自己的 flexcyon Multi-Column 实现 (FMCi)
    - 这里的关键字表示 Callout 类型和 Callout 元数据
    - 支持使用 `>[!col]` 或 `>[!multi-column]` 关键字. 如果列项不适合放在同一列中, 可以与 `wrap` callout
    关键字一起使用, 以换行列项, 例如 `>[!col|wrap]`.
	- 支持 `wide-0` 到 `wide-100` 关键字
	- [有关更多详细信息, 请参阅文档](../../styling/callout-metadata/fmci)
- 添加了 callout 关键字别名 `capitalize`, 用于将文本大写应用于文本内容 (以前只支持缩写 "caps")
- 添加了对 Lemons Search 插件的支持
    - 在搜索结果预览中添加填充
    - 使用可读的行长度
- 由于 `@Onev` 对翻译的贡献, 我们现在有了韩语文档

#### 变化
- 改进了样式设置, 使用 [迁移工具](../2.0-migration) 将旧样式设置带到 flexcyon 2.0.
    - 下所有与不透明度相关的样式设置 `flexcyon://Editor` 合并并移至其下的专用部门 `flexcyon://Editor > Animations`.
    - 编写样式设置迁移器脚本, 更改 ID, 例如将 `flexcyon` 更改为 `flexcyon-a11y`, 以进行与可访问性相关的样式设置
    - 重命名了许多样式设置选项, 以更好地反映其目的
	- Removed unused base grey tab, base grey token, base grey scroll, base grey scroll hover variables.
	- "Relative and normal line numbers on different lines" defaults to true now
	- Pl10k workspace layout no longer set by Flex Max, "Select Workspace Layout" now defaults to Pl10k workspace layout
	- Make dimmed file extensions and wrap long filenames default to true and no longer set by Flex Max
    - 默认情况下, "设置中不显示滚动条" 已启用, 而 Flex Max 模式未将其设置为启用
    - 删除了未使用的基本灰色选项卡, 基本灰色标记, 基本灰色滚动, 基本灰色滑动悬停变量
    - "不同行上的相对行号和正常行号" 现在默认为 true
    - Flex Max 不再设置 Pl10k 工作区布局, "选择工作区布局" 现在默认为 Pl10k 的工作区布局
    - 将暗显的文件扩展名和换行长文件名默认设置为 true, 不再由 Flex Max 设置

- Improved ASCII icons, a set of icons complementary to the existing UI. Shoutout to Floodlight on OMG for inspiring this.
- Enforcement of scale system for font size, line height etc. Theme should look more consistent and cohesive.
- Make ASCII and Clip Path checkboxes better conform to alternate checkboxes reference set where possible (or deemed necessary).
	- ASCII checkboxes are now enabled by default, clip path checkboxes are disabled by default
	- Some icon definitions have been remapped for better compatibility, please refer to the updated icon set if your checkboxes are not rendering properly.
	- Please note that ASCII/Clip Path checkboxes are case sensitive
	- Some new icons are added
	- Double quote and single quote ASCII checkboxes no longer use Unicode, whether rendered quotation marks have slight "cursive" will depend your font family
- Improved light and dark theme colours for improved constrast and readability
- You can now specify base callout types that come with Obsidian in callout metadata instead of callout type. E.g. `>[!tip|a]` and `>[!a|tip]` looks the same.
	- Question callouts are now green instead of orange (inherits theme's colours)
	- Important callouts are now purple instead of cyan (inherits theme's colours). They also use `lucide-star` instead of `lucide-fire` for their default icon.
	- Error callouts now use `lucide-circle-alert` instead of `luicde-zap` for their default icon for their default icon.
	- Callout icon alignment is slightly tweaked for better alignment with title text
- Mermaid, Canvas styling fixes
- Other small QOL tweaks in the theme

#### 修复
- Banner snippet live preview fix
- pl10k Status bar fix
- Novel Word Count plugin compatibility with dimmed file extensions, thanks to `@psolkaiyn` on the OMG Discord server
- Fixed ASCII art rendering and direction. Do update your ASCII art of choice if required.
- "Background for add before empty state title" `linear-gradient` logic now uses the correct direction.
- Attempts to improve performance and clean up parts of the codebase
- Fixed Revert to Pre 1.11 UI
