---
name: sks-nav-html-template
title: "三棵树导航式汇报模板（HTML 交互版）"
description: 三棵树/马上住风格的 16:9 网页汇报模板——左侧绿色导航栏（含二级子项）、右上角 logo + 两行标语、PPT 式缩略图导航、全屏放映模式（含全屏失败降级与「浏览器打开」逃生口）、悬浮目录（点标题跳页）、章节可增删改、选中态白底+绿三角、全元素可点选可拖动、localStorage 持久化，单文件自包含可直接发给同事。当用户要「三棵树风格汇报页」「带左侧导航的 HTML 汇报」「可翻页可编辑的网页版 PPT」「要放映模式/悬浮目录」「马上住模板」时使用本技能。
version: 1.9.29
agent_created: true
---

# 三棵树导航式汇报模板（HTML 交互版）

还原自《【260803更新】马上住焕新事业部-马上住网点分析.pptx》实测规格。
**单文件 HTML**（≈1289KB，图片已 base64 内联，并内联 pptxgenjs + html2canvas + jsPDF，离线即可导出 PDF / PPT），双击即开，可交互改章节，可直接发给别人。

## 何时使用
- 「做个三棵树风格的汇报页 / 网页版 PPT」
- 「要左侧绿色导航栏、右上角 logo 标语那种模板」
- 「马上住 / 网点分析 / 事业部汇报」类材料
- 需要**可编辑、可翻页、能发微信/邮件给同事**的交付物
- 需要**撤销 / 保存 / 子项独立成页 / 放映时也能快速跳转章节**的交互

## ⚠️ 调用后第一步：需求接入（必须按序追问，一次只问一个）

用户一调用本 skill，**不要立刻复制模板/出报告**。先走下面三步接入，每问只问一个、等用户答完再问下一个。
（对应「严禁臆造事实」铁律：章节结构、内容、页数都必须从用户处取确认，不能自作主张编。）

### 第 1 问：有没有现成大纲 / 章节结构？
先给他一个**示例大纲**，让他知道该给到什么粒度：

```
示例大纲（一级章 + 二级子项，可直接复制改）：
01 经营总览          （1 页）
   1.1 核心指标速览
   1.2 本期亮点与风险
02 门店网点分析      （1 页）
   2.1 网点分布与覆盖
   2.2 专卖店 vs 非专卖店
03 投流效率诊断      （1 页）
   3.1 单客 vs 单店口径校准
   3.2 增量门槛达成情况
04 客户分层与策略    （1 页）
   4.1 高价值客户分层
   4.2 针对性运营动作
05 结论与下一步      （1 页）
```
- 用户**有**大纲 → 侧边栏章节**严格按他给的来**（含二级子项、编号、命名），不擅自增删改名；
- 用户**没有**大纲 → 基于他口述的诉求，你**先生成一稿章节结构草案**呈现给他确认（编号 `01/02…`、子项 `1.1/1.2…`），确认后再落地。

### 第 2 问：每页想呈现什么内容？（结合诉求 + 他提供的数据）
- 让用户把**数据 / 素材**（Excel、表格、截图、文字结论）贴进来或指向文件；
- 明确每一页 / 每个子项的**核心结论**，不要堆原始数字；
- 由诉求 + 数据决定每页用「卡片 + KPI 行 + 图表 + 洞察卡」里的哪几种组合（见文末「可编辑元素清单」）。
- **图表类型（v1.9.27 起共 9 种，全部内联 SVG、可编辑数据）**：`bar` / `horizontalBar` / `line` / `pie` / `doughnut` / **`radar`（雷达，传 `max`）** / **`gauge`（仪表盘，单值+`max`+`unit`）** / **`area`（面积趋势）** / **`divergingBar`（双向条形，正绿负红，适合同比增速）**。调用 `makeChart(type, data, opts)`，例：`makeChart('radar',[{label:'营收',value:9}],{max:10,width:420,height:330})`。

### 第 3 问：总页数大约多少？
- 拿到总页数后，对**内容密度与篇幅做把控**：页数少 → 每页撑满、结论凝练；页数多 → 合理拆子项、避免单页过载；
- 把总页数与第 1 问的章节结构对齐（主章节数、每章子项数），必要时回第 1 问核对。

### 第 4 问：要不要「章节过渡页」？
- 先问用户是否要给每个**主章节**加一页过渡页（章节扉页）。有 → 用 `.rc-cover` 章节扉页版式（默认样式：**A 极简留白为主**——**深绿章节号（`#007F00`，58px，在流内、位于标题上方，切勿做成会被标题压住的大号居中水印）** + 居中章节名（34px） + 绿短横线 + **一行导读徽章**（`.rc-cover-sub`，浅绿底 `#EAF5EA` + 深绿字 `#1f6b2e` + 左侧 4px 深绿竖条），**下方加 D 式的子项入口卡片**，列出本章 2 个子项名）；不要 → 主章节页直接放内容，不加扉页。CSS 已内置在成品模板 `三棵树汇报模板.html`，直接给主章节页 body 套 `.rc-cover` 结构即可。
  - ⚠️ 字号取 34/58 是"偏大"反馈后收敛的结果；`.rc-cover` 用 `justify-content:center` 保证整块垂直居中（勿用绝对定位把簇顶到上方）。
  - ⚠️ 章节号务必**在流内**（`position:relative`，作为 flex 首个元素）。曾用「大号数字绝对定位居中水印 + 标题 z-index 盖在上面」，结果数字被标题/绿线/徽章从中间劈开、看起来"被遮住"。
- 注意页数口径：加过渡页后，总页数 = 主章节页数 + 子项页数（子项在模板里也是独立页）。用户说"10 页"时先确认他指的是「内容页（子项）」还是「全部页（含过渡页）」。
- 扉页样式可按用户偏好调整（A 极简留白 / B 左侧色块 / C 大数字海报 / D 上下分带，或组合），改 `.rc-cover` 系列 CSS + 各主章节页 body。

> 四问都答完，再开始：复制模板 → 改 `DEFAULT.pages`（或改成品 HTML 的章节）→ 填内容 → `pack.py` 重打包（或直接交付改好的成品 HTML）。

## 文件清单（skill 根目录）

| 文件 | 用途 |
|---|---|
| `三棵树汇报模板.html` | **成品**（v1.9.29，≈1.29MB，已内联 logo + pptxgenjs + html2canvas + jsPDF），直接复制改名即可用 |
| `三棵树汇报模板-v1.5-备份.html` | 旧成品留档（v1.5.x，≈119KB，无 PPT/PDF 导出能力），**不要用**，仅备查 |
| `template.html` | 源模板（引用 `assets/`；**注意：这是 v1.5.x 遗留源码**，`pack.py` 由它打包出的仍是旧版，别拿它覆盖上面那份 v1.9.29 成品） |
| `assets/nav_logo_x2.png` | 侧栏 logo（原稿内嵌图放大版，640×306） |
| `assets/skshu_logo.png` | 右上角品牌 logo（官网 SVG 转 PNG） |
| `scripts/pack.py` | 把 `template.html` 打包成自包含单文件 |

## 两条使用路径

**A. 直接交付（80% 场景，推荐）**
```bash
cp "三棵树汇报模板.html" "<工作区>/<报告名>.html"
```
不用跑脚本、不用带 `assets/`。对方双击即开。

> **⚠️ 别只用 `present_files` 的预览面板验证全屏 / 跳页这类交互。**
> 预览面板把页面装在 **iframe** 里（走的 `http://127.0.0.1:<临时端口>/static-html/<hash>/<文件名>.html`），
> iframe 没被授予 `allow="fullscreen"`，任何全屏功能到那儿**必然失败**，用户会来问「怎么不是全屏」。
>
> 正确动作：交付 HTML 时**顺手把可在真实浏览器打开的地址一起给用户**（二选一，都能拿到顶层页面）：
> 1. `present_files` 回包里的 `previewed` 那条 `http://127.0.0.1:.../static-html/...html` —— 直接粘进 Chrome 地址栏
>    （中文文件名已 URL 编码，可原样复制；端口随服务重启会变，限本机）
> 2. `file:///C:/<绝对路径>/<文件名>.html` —— 永久有效、可发给同事，中文建议 URL 编码成 `%E4%B8%89...`
>
> 也可以提示用户用文件里的 **⧉ 浏览器打开** 按钮，效果一样。

**B. 改了模板源码（或要预置章节）后重打包**
```bash
# 1) 编辑 template.html：改 DEFAULT.pages 预置章节 / 改配色 / 改默认文案
# 2) 打包（把两张 logo 转 base64 内联 → 单文件）
python scripts/pack.py "<工作区>/<报告名>.html"
```

## 实测规格（改版时别改坏这些值）

画布 1280×720（`PX = 96`，1in = 96px），对应 PPT 13.333×7.5 in。

| 元素 | 关键值 |
|---|---|
| 侧栏底板 `.sb-bg` | left −2px, width **125px**, height 720px, `#007F00` |
| 导航区 `.nav` | left 0, width **124px**, `z-index:2`, **`pointer-events:none`**（否则整块挡住白线/logo） |
| 一级条目 `.item` | width 113px, height 28px, `padding-left:9px`, 13.3px/**700**, 白色 |
| 选中条目 `.item.sel` | 14.7px, 色 `#007E00` |
| 选中白底 `.pill` | left 2px, width 113px, height 29px, 白, `z-index:1` |
| 绿三角 `.tri` | left **103px**, 12×12px, `z-index:6`, 内联 SVG `<polygon>` |
| 子项 `.subs` | width 138px, 10.7px/**700**, `padding-left:9px`（与一级同为 9px） |
| 两根白线 | `#line1` left10/top77/w98/**h2**；`#line2` left0/top500/w121/**h3** |
| 右上角 `.brand` | left **1013px**, top 12px, gap 19px；img 108×45 |
| 标语 `.sg` | width **103px**, **700**, 绿色, line-height 1.30, **padding:0**, `white-space:nowrap` |
| 标语文字 | 第一行 `三棵树　马上住`（**全角空格 U+3000**）；第二行 `更健康的中国漆` |

数据模型（`template.html`）：
```js
const KEY = 'sks_tpl_v6';   // 结构升级要升版本号，避免旧 localStorage 脏数据破坏布局
pages:[
  {id:'...', num:'01', label:'集团分析', h:0.296, pt:10, body:'<p>...', title:'...'},
  {id:'...', num:'', label:'1.1  示例子项', parent:'01的id', h:0.20, pt:9, body:'...'},
  ...
]
extra:{ line1w:98, line2w:121, triColor:'#007F00', lineColor:'#FFFFFF', line1h:2, line2h:3 }
```
> 子项是**真正的独立页**：`parent` 指向父章节 `id`，侧栏渲染时归到父条目下方，点击即跳到该页，删子项会连同那一页一起删。
> 旧版 `subs:['3.1 ...','3.2 ...']` 数组在 `load()` 时会通过 `normalize()` 自动迁移成独立子页（兼容 v5 存档）。

侧栏自动布局常量（英寸）：`NAV_TOP0=1.298, ITEM_GAP=0.254, SUB_TOP=0.10, SUB_LH=0.20, SUB_BOT=0.10, PILL_H=0.302, TRI_H=0.125`；
子项专用：`SUB_TRI_H=0.094`（子项三角 9px，配 10.7px 的子项字）、`SUB_PILL_H=0.24`（子项选中白底）；
白底几何：`PILL_L=2, PILL_W=113`（px），三角右端恒等于 `PILL_L+PILL_W`，缩放时 `left` 跟着右移。

## 交互功能（成品自带）
- 左侧 **PPT 式缩略图**列出全部页面（含子项页），点即切换；缩略图可拖拽调章节顺序
- 选中态＝白底 + 绿三角 + **绿字**；子项页被选中时白底落在子项行上，**该行文字转绿**（否则白底白字看不见）
- **左侧点到哪跳到哪**：导航条目（含主章节 / 子项）**单击文字或空白都直接切页**；要改名字则**双击**，文字变白底绿字进入编辑，回车保存、Esc 取消
- **右侧内容不影响左栏**：右侧大标题 / 正文只存进该页的 `title` / `body`，**不回写左栏 `num` / `label`**；左栏章节名的唯一入口是双击左栏文字
- 条目上 `＋` 加子项、`×` 删章节；子项上 `×` 删子项 → **删子项同时删页，下方章节自动重排**
- 双击任意文字（含标语）直接改，改完自动存 `localStorage`；**每页正文独立保存，切页不丢**
- 工具条「**↶ 撤销**（Ctrl+Z）」与「**↷ 重做**（Ctrl+Y / Ctrl+Shift+Z）」，撤销栈覆盖增删改、改字、拖位置；新动作会清空重做栈
- 工具条「**－ 删除子项**」删除当前子项页（停在主章节页上时该按钮变淡并提示先切到子项）；删除后同章其余子项**自动续号并上移**，下方章节自动上移
- **两根白线（侧栏上下短横）自动跟随首 / 末条目**：第一项上方、最后一项下方，加删章节或子项后自动上下移动；手动拖过的位置存成「相对偏移」，保留微调且仍能跟随
- 「**💾 保存**（Ctrl+S）」立即写盘，其实每次改动都已自动保存到 `localStorage`
- 「＋ 新增章节」弹窗**选模板页**，新页面沿用该页的 `h / pt / 子项行数`；新增 / 删除 / 拖拽排序后章节自动按 `01 / 02 / 03…` 重编号，子项前缀跟着父章节走（如 3.1、3.2）
- 默认打开即为 **5 个主章节，每章 1 个子项**（共 10 页），左栏第一项上方 / 最后一项下方各有一根白线
- 顶部工具条：编辑模式 / 撤销 / 保存 / 恢复默认 / 导出 PDF（纯前端 html2canvas+jsPDF·原样多页·无页码条·无页眉页脚·无页缝·图表保留·动画强制终态）/ **导出 PPT（全可编辑·原生对象；v1.9.28 起：图表=原生 chart 可双击改数据、表格=原生 tbl 可逐格改字、卡片/KPI/横幅=原生形状+文字、logo=内嵌图片、侧栏=绿底矩形+文字，全部在 PowerPoint 里点得动改得了）** / ⬡ 图形·图标（内置 15 矢量图标 + 上传图片）
- `fit()` 自适应窗口缩放；键盘 ←/→ 翻页

### 放映模式（v1.2 新增）
顶部「**▶ 放映**」按钮 → `startPresent()`：
- `body.present` 隐藏 `.bar / .thumbs / #insp / #hint`，`.stage` 底色转 `#0d0f0d`，幻灯片整屏居中
- **放映态还要藏掉编辑饰件**（用户实际反馈「那些加减号不用显示」）：`.item .acts`（条目上的 ＋加子项 / ×删章节）、
  `.subs .sdel`（子项右侧 ×删子项）、`.lb` 的 `outline`（contenteditable 残留的聚焦描边）、
  并把 `[contenteditable]` 的 `cursor` 归位。**这两块本来就写在 `@media print` 的隐藏清单里，但放映态漏了** ——
  凡是打印时要藏的编辑类元素，放映态几乎都要同步藏，加样式时对着两份一起改。
  验证：`--dump-dom` 探针读 `getComputedStyle(document.querySelector('.item .acts')).display`，
  期望 **普通态 `flex/block`、放映态 `none/none`**（编辑照样能用，放映干净）。

#### 三态显隐规则（v1.3 定稿，用户明确要的行为）
`＋ / ×` 这类**编辑辅助元素**按三档走，用 `body` 上的类分档：
```css
.item .acts{opacity:0;pointer-events:none}            /* ① 默认：看不见也点不到 */
body.editing .item .acts{opacity:.55;pointer-events:auto}   /* ② 编辑模式：可见可点 */
body.present .item .acts{display:none!important}      /* ③ 放映：彻底移除（import 覆盖） */
```
`document.body.classList.toggle('editing', editMode)` 在 `$('bEdit').onclick` 里同步，
**`startPresent()` 里关闭 editMode 时也要记得一并 remove('editing')**。
> 别用 `display:none` 做①：那样没有 hover 过渡；也不要只改 opacity——`pointer-events:none` 必须一起给，
> 否则"看不见但能点到"会变成隐形按钮。
> 探针验证三态：`默认[flex|op0|penone]  编辑模式[flex|op0.55|peauto]  放映[none|op0|penone]`。

#### 操作说明集中写在一处（用户明确要求：底部不要堆说明）
页面上**不再保留任何常驻的底部说明条**（原 `#hint`，已删除），
所有用法只写在 `#help`（顶部「? 怎么用」弹窗）里。删它时要清干净四处：
CSS 定义、`body.present` 隐藏列表、`@media print` 隐藏列表、HTML 节点本身（无 JS 引用）。
改 `/ ×` 的触发条件时，**帮助文案要同步改**（否则写着"鼠标移上去点 ×"，实际却要先进编辑模式）。
- 申请浏览器全屏 `requestFullscreen()`；失败**必须给用户可见提示**（v1.2 修正，见下）
- 键盘：`← →` / 空格 / PageUp·PageDown / ↑↓ 翻页，`Home`·`End` 跳首尾，`D` 开关目录，`F` 全屏切换，`Esc` 退出
- **点画面 = 下一页**（`#nav` 与 `.pager` 除外，侧栏导航和右下角章节选择器会自己跳页）
- 放映时页面**右下角有「跳到」章节圆点**（`body.present .pager` 上移并加深样式），鼠标移动即出现；
  点圆点跳页，不会被点画面翻页逻辑覆盖
- 底部悬浮控制条 `#pvbar`（上/下页 · 目录 · 页码 · **⛶ 全屏** · **⧉ 浏览器打开** · 退出放映），
  鼠标静止 2.6s 自动淡出；顶部 `#pvprog` 细进度条。按钮多了记得 `flex-wrap:wrap; max-width:94vw`
- 进入时 `setEditable(false)` 关掉所有 `contenteditable`，防止演示中误改文字；退出时恢复
- `fullscreenchange` 兜底：全屏被系统 Esc 关掉时同步退出放映态；回调里 `syncFsBtn()` 同步按钮文案

#### ⚠️ 全屏失败是常态，绝不能静默（v1.2 踩坑）
「放映模式」= `body.present` 布局（换深色、藏工具条）**＋** 浏览器 Fullscreen API，两者独立。
只做前者 = **假全屏**：地址栏/标签栏还在，用户会问「怎么不是全屏」。
而 `requestFullscreen()` 在三种情况下必然失败：
1. **页面在 iframe / 预览面板里**（`window.self !== window.top`）—— 宿主没给 `allow="fullscreen"` 就拒绝。这是最常见的场景；
2. 调用不在用户手势的同步调用栈内；
3. 浏览器策略限制（部分嵌入式内核）。

因此正确写法（`reqFs()` / `fsFailMsg()` / `syncFsBtn()`）：
- 用 `try{ fn.call(el) }catch{}` 包住（iframe 未授权时**同步抛异常**，不是只 reject Promise），
  并且 `promise.catch()` 里也要**再次判断 `!hasFs()` 才提示** —— 否则会把「用户自己按 Esc 退出」误报成全屏失败；
- 失败文案要**区分场景**：在 iframe 里 → 「点 ⧉ 浏览器打开，在新标签里再点 ▶ 放映」；
  非 iframe → 「再点一次 ⛶，或按 F11」；
- 控制条上加 **⧉ 浏览器打开** 按钮（`window.open(location.href,'_blank')`）作为逃生口，
  并处理弹窗被拦截的情况；
- 兼容前缀：`el.requestFullscreen || el.webkitRequestFullscreen || el.msRequestFullscreen`，
  状态用 `document.fullscreenElement || document.webkitFullscreenElement`。

#### ⚠️ 全屏后幻灯片不放大（v1.3 踩坑，用户实际反馈）
症状：进了真全屏，但幻灯片仍是 **1280×720 原始大小、贴在左上角**，右边和下边一整片黑。
根因在 `fit()` 里的一行「缩得下才缩放」：
```js
const k=Math.min((st.clientWidth-16)/1280,(st.clientHeight-16)/720);
s.style.transform=(k<1?`scale(${k})`:'none');   // ← k≥1 时 transform:none
```
大屏上 `k` 恒 >1（1920 宽窗口 k≈1.4），于是**既不放大也不居中**（`marginLeft` 用 `Math.max(0,…)` 也归零）。
正确写法：
```js
const pad=presenting?0:16;                       // 放映不留边
const raw=Math.min((st.clientWidth-pad)/1280,(st.clientHeight-pad)/720);
const k=presenting ? raw : Math.min(raw,1);      // 放映允许放大铺满；编辑态最多 1:1
s.style.transform=(Math.abs(k-1)>0.002)?`scale(${k})`:'none';
```
另外两处必须补：
1. **`requestFullscreen()` 是异步的** —— 尺寸在它之后才变。`startPresent()` 里算的那次 `fit()` 用的是旧尺寸，
   要再 `setTimeout(fit,60)` + `setTimeout(fit,320)` 兜底；
2. **`window.resize` 不保证在全屏切换时触发** —— 加 `ResizeObserver` 监听 `#stage` 尺寸变化重算 `fit()`
   （`fit()` 改的是 slide 的 transform/margin，不动 stage 尺寸，不会自激循环）。
验证口径：探针读 `slide.getBoundingClientRect().height / stage.clientHeight`，放映态应为 **100%**。
1920×1080 实测：`stage=1894x980 scale=1.361 slideRect=1742x980 cover=100.0%`。
> 左侧那条绿色导航（`.sb-bg` / `.nav`）是**幻灯片内部的元素**，会跟着缩放，别去给它做「放映时隐藏」。

### 悬浮目录 `#toc`（v1.2 新增）
- 左下角 `#tocBtn`「**☰ 目录**」按钮，点开/收起；普通态与放映态通用（放映态自动换深色皮肤）
- `renderToc()` 列出**全部章节 + 子项**，当前页绿底高亮；点任意一条 `go(i)` 跳页，放映时跳完自动收起
- 定位：按钮 `left:16px; bottom:56px`，面板 `bottom:96px` —— 刻意避开左下角 `#hint` 与右下角 `#insp`

### 可编辑元素清单（点「编辑模式」后）

| 元素 | 可改属性 | 可自由拖动 |
|---|---|---|
| 章节条目（每个 01–05） | 左右 / 上下 / 宽 / 高 / 字号 / 字色 | ✅ |
| 子项区（3.1 / 3.2 那块） | 左右 / 上下 / 字号 / 字色 | ✅ |
| 侧栏 logo | 宽 / 高 / 左右 / 上下 | ✅ |
| 右上角 logo | logo 宽 / logo 高 / 左右 / 上下 | ✅ |
| 标语（三棵树 马上住） | 字号 / 字色 / 宽 / 左右 / 上下 | ✅ |
| 白线（上 / 下） | 长度 / 粗细 / 颜色 / 左右 / 上下 | ✅ |
| 选中态白底 | 宽 / 高 / 底色 | —（用选择器选中） |
| 选中态三角 | 颜色 / 大小 | —（用选择器选中） |
| 侧栏底板 | 底色 | — |
| 卡片 / KPI / 横幅 / 图表卡（`.rc-*`，v1.9.21 前即支持） | — | ✅（编辑模式下单击单独选中，8 个橙柄拖动缩放） |
| 插入的表格（`.el.tbl`，v1.9.21 起） | — | ✅（v1.9.21 前高度被锁死，现只锁图表高度） |
| 插入的图形 / 图标（`.fig`，v1.9.21 新增） | 宽 / 高 / 左右 / 上下 / 填充色 | ✅（双击不进文字编辑） |
| 侧栏章节名（导出 PPT 时，v1.9.21 新增） | 在 **PowerPoint 里**直接改 | — |

> 属性面板已移到**右下角**（避免挡住右上角品牌区）。
> 面板顶部有「**切换元素**」下拉（底板/两个 logo/两根白线/白底/三角/标语/各章节/子项区），
> 白底、三角这类被文字盖住的元素，**从这里一点即选中**。
> 章节拖乱了可用面板里的「恢复自动排列」一键归位。

## 自定义指南
| 想改什么 | 改哪里 |
|---|---|
| 默认章节 | `DEFAULT.pages` 数组（改完清 localStorage 才生效） |
| 换 logo | 替换 `assets/` 同名 png，跑 `pack.py` |
| 品牌绿 | CSS 变量 `--green`（`#007F00`）、选中字色 `--seltx`（`#007E00`） |
| 标语 | HTML 里 `.l1` / `.l2`（保持 **7 个全角字符**才两端齐平） |
| 字体 | `--font`（默认 微软雅黑） |

## 踩坑清单（别重复踩）

1. **标语两行必须等宽**：「更健康的中国漆」是 **7** 个全角汉字，「三棵树马上住」只有 6 个 →
   第一行必须写成 `三棵树　马上住`（中间 **全角空格 U+3000**），凑成 7 个全角字符，
   两行自然两端齐平。**不要用 justify / letter-spacing 硬撑**，跨浏览器不可靠。
2. **标语不要加 `padding`**：为做点击热区加 padding 会把文字挤偏（右移/下移）。
   要热区用 `cursor:pointer` + outline 选中态即可，实测 `padding:0` 才与 logo 相对位置正确。
3. **删除类操作不能用原生 `confirm()`**：在嵌入预览/部分浏览器里被拦截且不弹窗，
   表现就是「点了删除没反应」。本模板已内置自定义确认框 `ask(msg, sub, cb, okText)` +
   `#ask` 弹层，新增删除逻辑一律用 `ask()`。
4. **动态元素（章节条目/子项区）绑不上事件**：它们是 `renderNav()` 里创建的，
   初始化时一次性绑定无效 → 必须用**事件委托**（见 `#slide` 的 `mousedown` 监听）。
5. **拖动位置不落盘**：拖完只调 `save()` 不够，要 `persistPos(el)` 把 left/top 写回 `S`；
   且静态元素 `style.left` 可能为空 → 用 `posOf()`（`offsetLeft/Top` 兜底）才不会算出 NaN。
6. **子项与一级条目对齐**：`.item` 和 `.subs` 的 `padding-left` **都要 9px**（= 0.090in×96）。
   子项设成 15px 会多缩进一格，是常见 bug。
7. **三角不要用 CSS 边框旋转画**：跨渲染器会歪。用内联 SVG `<polygon>`，
   改颜色时读写 `polygon` 的 `fill`（不是 `border-color`）。
8. **层级**：`.nav / .subs` 用 `z-index:2` 且 `.nav` 设 `pointer-events:none`；
   `.pill` `z-index:1`（永远在文字下层不遮字）；`.tri` `z-index:6`（否则被条目 ＋/× 按钮盖住）。
9. **白底/三角/文字三者共中心**：以 `cy = top + h/2` 对齐，差值为 0 才不歪。
10. **细线难点中**：白线只有 1~3px 高 → 加透明热区（`.sb-line::before`，上下各扩 7px）。
11. 单位换算常记：**1in = 96px**，0.090in ≈ 8.64px ≈ 9px。
12. **`#toast` 别压在放映控制条上**：toast 默认 `bottom:34px`，与 `#pvbar`（`bottom:22px`）重叠。
    已加 `body.present #toast{top:64px;bottom:auto}` —— 新增放映态浮层时先确认不会互相遮挡。
13. **放映态要关 `contenteditable`**：只靠 CSS `pointer-events:none` 挡不住 Tab 聚焦 / 键盘输入，
    必须遍历 `[contenteditable]` 显式设成 `false`，退出时再还原。
14. **选中态白底会「吃掉」侧栏文字**（用户实测反馈「白框把字挡住了」）：
    `z-index` 只保证文字在白底**之上**，但**颜色**不对照样看不见——`.subs` 默认 `color:#fff`，
    子项页被选中时白底 pill 盖上去就是**白底白字**。
    修法：`.subs .sub.cur{color:var(--seltx)}` + `.subs .sub.cur .lb{color:var(--seltx)}`，
    并去掉 `.sub.cur` 原本的 `rgba(255,255,255,.2)` 半透明白底（会和 pill 叠成一块脏白）。
    主章节同理加保险：`.item.sel .lb{color:var(--seltx)!important}`，
    因为条目若被手动改过颜色会写成**内联 style**，优先级高于 class，选中时会变回白字。
    → **凡是「白底/色块 + 文字」的组合，改配色后一定要回到选中态实测颜色，别只看层级。**
15. **子项三角要单独缩小 + 用 DOM 实测中心**：
    - 主章节字 14.7px 配 12px 三角，子项字只有 10.7px → 三角要按字号比例缩到 9px（`SUB_TRI_H=0.094`），
      并且 `width/height` 一起改、右端贴 `PILL_L+PILL_W`（115px），否则缩小后会往左飘。
      手动拖过三角时（`S.extra.triX!=null`）不要覆盖 `left`。
    - **子项的「行」真实高度 ≠ `SUB_LH`**：`SUB_LH=0.20in(19.2px)` 里包含 `.sub{margin-bottom:3px}`，
      实际行盒只有约 16px。用 `top + SUB_LH/2` 算中心会偏低 ~1.5px，
      必须量 DOM：`(rect.top-slideRect.top)/scale + height/scale/2`（注意除掉舞台 `fit()` 的缩放）。
16. **双击改名必须用「事件委托 + `e.detail`」，不能把 `dblclick` 绑在动态节点上**：
    - 单击跳页 → `renderAll()` → 侧栏整块重建，双击的**第二下落在已被替换掉的旧节点**上；
      对它 `focus()` 完全无效（探针里能看到 `contentEditable=true` 但焦点不在条目上 —— 用户体感就是"双击没反应"）。
    - 解法：委托到不会被重建的 `#nav` 上，用 `click` 且 `e.detail>=2` 判定双击（`detail` 由浏览器按点击次数给出，
      **与 DOM 是否被重建无关**，比 `dblclick` 可靠）；拿到 `host.dataset.i / .gi` 后
      **回 DOM 里重新查当前那个 `.lb`** 再 `focus()`。`dblclick` 只作为兜底再绑一次。
    - 顺带：`contenteditable` 平时设为 `false`（只读），只有进入编辑才改 `true`，这样"点文字＝跳页、双击＝改名"才不打架。
17. **右侧页面大标题绝不要回写左栏 `num` / `label`**：早期版本为了"改标题=改章节名"在 `elPtitle` 的 blur 里
    做了 `S.pages[cur].num/label = 解析(标题)`，用户明确反对 —— **右侧任何改动都不该动左栏**。
    标题只存 `p.title`，渲染时 `p.title || (p.parent? p.label : num+' '+label)` 兜底即可。
18. **删子项后要自动续号 + 自动上移**：子项 `label` 形如 `"3.1   名称"`，删掉中间一个后，后面子项要重新编号
    （3.1 / 3.2 / 3.3 删掉 3.2 → 3.1 / 3.2）。用 `renumberSubs(pid)` 遍历同父节点，按顺序重贴前缀；
    同时 `delete pp.subsTop; pp.fixedSub=false`，让 `layout()` 按新的子项数量重新计算子项区高度，自动上移。
    顶部工具条单独加「删除子项」按钮，主章节页上变淡提示（不猜测用户意图）。
19. **白线要锚定首 / 末条目**：侧栏上下两根短横不能写死 `top`，否则加删章节后它会孤零零停在原地。
    用 `layout()` 取首项 `top` 和末项 `bottom`，反推间距 `LINE_TOP_GAP / LINE_BOT_GAP`，每次 `renderAll()` 后重算。
    手动拖过的位置要存成「相对偏移」，而不是绝对 `Y`，否则用户微调后，章节一变化白线又飞了。
20. **localStorage 脏数据会让"默认模板"看起来不生效**：每次改结构必须升 `localStorage` 的 KEY（`sks_tpl_v9`）。
    恢复默认时必须把所有历史 KEY（`v5 ~ v9`）一起清掉，否则旧版本里存的 31 页还在，用户会以为模板有 bug。

21. **导出 PDF 别再走 `window.print()`（v1.9.17 关键改动）**：图表是内联 SVG，扇形/柱体整组包在 `<g filter="url(#rcSh)">`（feDropShadow 投影）。
    走打印克隆容器时 `#rcSh` 定义留在被隐藏的原始页，`url(#rcSh)` 解析失败 → 整组 `<g>` 被丢弃 → **图表在 PDF 里整块消失**；
    且打印对话框自带的日期/标题页眉、文件路径/页码页脚、页间灰色缝隙，**CSS 改不掉**（依赖用户手动取消勾选、还常被切成 A4）。
    **修法**：导出 PDF 改为**纯前端逐页整页截图（html2canvas）+ jsPDF 拼装**（已内联 jsPDF 2.5.1 UMD），
    `unit:'in', format:[13.333,7.5]` 保证每页精确 960×540pt（16:9，零缩放失真）；截图前给 `body` 加 `exporting` 类冻结
    `#elPtitle/#elContent` 为 `opacity:1;animation:none`、隐藏 `.pager`。无打印对话框 → 页眉/页脚/页缝天然消失，
    图表在真实渲染里天然带 `filter` → 截图后完整。防御：手动 Ctrl+P 路径的 `_ppBuildPrintRoot()` 克隆体里去除 `[filter]` 属性。

22. **导出「可编辑 PPT」崩溃/挂起（v1.9.18 修复）**：`exportPptEditable()` 用 `_ppWalk()` 递归遍历 `#elContent` 把 DOM 转 pptxgenjs 原生对象。三处坑：
  - ① **SVG 子元素 `className` 是对象不是字符串**：原 `var cls=ch.className||''` 对 SVG 元素取到 `SVGAnimatedString`（对象），下一行 `cls.indexOf('rh')` 抛 `TypeError: cls.indexOf is not a function`，直接 abort 整个导出（图片版/PDF 不走 DOM 遍历所以不中招，表现即「只有可编辑 PPT 导不出」）。修法：`cls=typeof ch.className==='string'?ch.className:(ch.getAttribute?ch.getAttribute('class')||'':'')`。
  - ② **`requestAnimationFrame` 在无头/后台态不触发 → 导出挂起**：每页 `await _ppRaf()` 等 rAF 回调；Chrome `--headless=new`（`--virtual-time-budget`）或标签页被节流/隐藏时 rAF 可能不 fire，`await` 永远不 resolve。修法：`_ppRaf()` 内 `requestAnimationFrame(fin)` 外加 `setTimeout(fin,32)` 兜底（先到先得）。
  - ③ **缺 `fit()` + 未复位 transform → 坐标全错**：早期版本没像图片版那样先 `fit()` 并 `slide.style.transform='none'`，`getBoundingClientRect()` 拿到缩放后尺寸（≈441×248），所有对象坐标错位。修法：每页循环补 `fit()` + transform/margin 复位，导出完还原 `slide` 的 style。
  - 验证：真实 Chrome 无头跑 `loadSample → exportPptEditable`，捕获 `this.write('base64')` 解码 → testzip 通过、5 页、111 个 `<a:t>` 文本片段、每页 19~32 个原生形状、图表以 PNG 嵌入（每页 1 张 `p:pic`）；另注入 `<table>` 单页导出确认生成原生 `<a:tbl>`（graphicFrame + 单元格文字均可在 PowerPoint 改）。

23. **导出「可编辑 PPT」颜色变了 / 图标没了 / 图表没了（v1.9.19 改混合式）**：v1.9.18 的可编辑版是「用 PowerPoint 原生对象**重建**版式」——形状取写死的近似色、图表把裸 `<svg>` 序列化后画进 `<img>`（脱离文档 CSS → 渐变/填充丢失，变空白或黑块）、logo/装饰图标根本没重建。而用户已认可的 PDF/图片版走 html2canvas **整页截图**，天然保真。
    **修法（整页截图作底 + 原生文字叠原位）**：
    - 每页 `html2canvas(slideEl,{scale:2})` 截整页作幻灯片背景 → 颜色/图标/logo/图表/渐变/左侧绿栏 **100% 还原**（复用 PDF/图片版已验证管线）。`ps.addImage({data:cvs.toDataURL('image/png'),x:0,y:0,w:13.333,h:7.5})`。
    - `onclone` 只把**可编辑区域**文字变透明：`#elContent *,#elPtitle,#elPtitle *,#elBrand,#elBrand *{color:transparent !important;-webkit-text-fill-color:transparent !important}`；图表用**更高权重**规则强行保留：`#elContent .chart,#elContent .chart *{color:#000 !important;-webkit-text-fill-color:#000 !important}`（权重 `#id.class`(0,1,1,0) > `#id *`(0,1,0,0)，否则被透明规则盖掉、图表文字消失）。
    - `_ppWalk(slide,root,R,skipVisual=true)`：跳过所有形状/SVG 重绘（背景截图已覆盖），只叠文字（含 `addTable` / 卡片 / KPI / 横幅文字）；`elPtitle`/`elBrand` 在外层单独叠加。
    - **坑①（nav 重复/丢标签）**：若用 `*{color:transparent !important}` 隐藏「全部」文字，**左侧导航整条只剩当前章节**——`.item.cur .lb{color:var(--seltx)!important}` 是 `!important` 且选择器权重 (0,0,3,0) 高于 `*`(0)，同等 `!important` 下 `*` **输**，当前章节文字残留进截图，与原位叠加的原生文字**重复**；而其余章节标签被隐藏后**没被叠加 → 整条侧栏空白**。因此**只隐藏 `#elContent/#elPtitle/#elBrand` 三个区域**，侧栏导航整条（全部章节标签）原样留在截图里，单份、不重复、不空白。
    - **坑②（探针注入踩空）**：本文件正文里还有一处 `</body>` 字符串，`html.replace("</body>", …)` 会命中它、把注入脚本插进 jsPDF 块内**永不执行** → 必须用 `html.rfind("</body>")` 定位真正的闭合标签。
    - 验证：真实 Chrome 无头 `loadSample → exportPptEditable` → `data-pp` 报 `OK wrote=… b64len=1532804`；解码后 `zipfile.testzip()` 通过、5 页、每页 1 张整页背景图 + 原生文本段（16/26/27/23/13）；抽出各页背景图目视：**5 个章节标签全在**、环形图（图例 咨询焕新192/施工交付168/售后维保120、中心合计480、35/25/40%）与折线图（Q1–Q4，1.2→2.3 亿，绿色渐变+数据点）颜色/图标/图表完整。
    - **补充（v1.9.20 实测订正）**：图表文字**用的是 SVG `fill` 属性、不是 CSS `color`**（`makeChart` 里 `<text fill="#243a2a">` 等），所以 `color:transparent` 本就盖不到它——那条 `#elContent .chart{color:#000}` 其实是**冗余**（实测环形图白字 `35%/25%/40%` 未被改黑，证明它对 `fill` 无效）。留着无害，但别以为它「救了图表」；真正的原因是 SVG 用 fill。

24. **导出「可编辑 PPT」= 一张图片，用户要「全部可编辑」（v1.9.28 回归原生对象）**：用户反馈「可编辑 PPT 导出来怎么是图片」——根因是 v1.9.19 起走「整页截图打底 + 只叠文字」混合式，图表/卡片/表格/logo 全烤死在背景图里，PowerPoint 里点不动，观感就是「一张图」。用户明确要**全部元素都能原生编辑**（图表双击改数据、表格逐格改字、卡片/KPI/logo 都点得动）。
    **修法（弃混合式，改纯原生对象重建）**：
    - **删掉整页 html2canvas 截图**，改画纯色背景 `FCFDFC` + 原生侧栏：`elBg` 绿底 `addShape('rect',{fill:007F00})`；`elNavLogo` 的 `<img src=data:image/png;base64…>` 直接 `ps.addImage({data:logo.src})` 内嵌。
    - `_ppWalk(ps,content,R,false)`（**skipVisual=false**，让形状底块也画）。
    - **表格**改走 `_ppTable` 原生 `<a:tbl>`：`_ppWalk` 开头 `if(root.tagName==='TABLE'){ _ppTable(...) }`（旧代码这里是 `return` 跳过）。
    - **图表**新增 `_ppChart(slide,wrap,R)`：读 `.chart-wrap` 的 `data-chart`（`makeChart` 存的 `{type,data,opts}`），用 pptxgenjs `slide.addChart()` 原生图表对象重建——`bar/line/pie/doughnut/radar` 直接对应，`area→line`、`gauge→doughnut(值+剩余)`、`divergingBar→bar`；可在 PowerPoint 双击改数据。
    - **过渡页 `.rc-cover` 系列**加专门分支（章节号/标题/绿线/导读徽章/子项卡片），避免丢失徽章底色与子项裸文本。
    - **坑（`.rc-col-chart` 被 `.rc-col` 提前截胡）**：`cls.indexOf('rc-col')>=0` 会**命中 `rc-col-chart`**（含 `rc-col` 子串），导致图表分支永远走不到、`chart=0`。必须把 `.rc-col-chart` 判断提到 `.rc-2col`/`.rc-col` **之前**。同理 `.rc-cover-subs` 会被 `.rc-cover-sub` 前缀误命中，须先判 `subitem`→`subs`→`sub`。
    - **坑（混合内容丢裸文本）**：`_ppWalk` 用 `root.children` 只遍历元素节点，`<b>1.1</b>产品矩阵…` 里 `<b>` 之外的裸文本「产品矩阵…」会丢。过渡页子项卡片改用 `ch.innerText` 取全量文字。
    - **验证**：真实 Chromium 触发 `exportPptEditable`，`pptx.write('base64')` 抓回解码 → `zipfile` 解析：10 个内容页各 1 个 `chartRef`、5 个含表格页 `tbl=1`、每页 `pic=2`（侧栏 logo + 右上 logo）、侧栏绿底 `rect fill=007F00`、图表类型 radar/line/bar/doughnut 映射正确、gauge 值 `67/33` 正确。**PowerPoint COM 导出 PNG 被公司 EDR 加密（文件头非 `\x89PNG`），无法目视校验**，只能 XML 层断言。

24. **导出「可编辑 PPT」偶发文字错位 / 重叠（乱码，v1.9.20 修复）**：可编辑版叠文字时，坐标换算的**基准**早期是「进入本页循环时取一次 `sr=slideEl.getBoundingClientRect()`」，而元素矩形在 `html2canvas` **之后**才测量。二者之间只要页面发生**任何重排**（字体加载、滚动条出现、`html2canvas` 克隆体回流、甚至**测试探针往 body 追加了一个巨大的截图 `<img>`**），`sr` 就**过期**：元素与舞台不再同一坐标系 → 该页**所有文字整体偏移、互相重叠**（典型表现：某一页标题/品牌行跑到左下角挤成一团）。
    - **修法（根治）**：`R()` 里**每个元素都重新取一次当下舞台矩形**——`var s=slideEl.getBoundingClientRect(); if(s.width<2||s.height<2) s=sr; var r=el.getBoundingClientRect();`。「元素矩形」与「舞台矩形」在同一次**同步**调用里取得 → 二者必属同一坐标系；无重排时 `s≡sr`（输出不变），有重排时也不再错位。
    - **连带教训（本 skill 的探针也要干净）**：验证用的注入探针**绝不能在导出循环进行时改动 DOM**（当时为了抓背景图，往 `<body>` 追加了一个巨大 `<img>`，正是它让第 2 页错位——产品代码当时其实是对的，是**探针**污染了结果）。要么把结果写进 `<title>`/`<body>` 属性（不改布局），要么在导出**结束后**再插可视化元素。
    - 验证：干净探针重跑 → 解码 5 页；**逐页坐标校验**：5 页标题/品牌行均 `y=0.30/0.36`（无左下角）；再把 PPTX 原生文本框按坐标**合成回导出背景图**截图目视：标题/品牌/横幅/表格单元格/KPI/脚注逐一落在各自形状内、无重叠。

25. **表格「线丢 / 字错位」+ 侧栏章节名可改 + 图形图标插入（v1.9.21）**：用户要求 ① 修表格线丢/字错位；② 删掉冗余的「图片版 PPT」导出；③ 白色底块（卡片）能单独拖动缩放；④ 插入的表格也能拖动缩放；补 ⑤ 侧栏章节名也要能在 PPT 里改；⑥ 所有图形/图标都要能加。
    - ① **表格改为整张烤进背景**（保真优先）：`_ppWalk` 里遇 `TABLE` 直接 `continue`（不再生成原生 `addTable`——原生表格正是「线丢 + 行高/对齐不一致」的根源）；`onclone` 里表格文字从 `inherit`（在 live DOM `getComputedStyle` 会塌成 `rgba(0,0,0,0)`，但在 html2canvas 克隆体实际渲染里其实可见——**以像素为准，别信 live DOM 的 computed 值**）改为显式色，更稳妥。
    - ② 删除 `exportPptImage()` 整段 + 工具栏 `bPptx` 按钮；原「导出可编辑 PPT」`bPptxEdit` 改名「导出 PPT」。
    - ③④ 白色底块（`.rc-card/.rc-kpi/.rc-banner/.rc-col-chart`）本就在 `GFX_SEL`（编辑模式单击单独选中、橙柄拖动缩放）；**表格高度解锁**：`startResize` 里 `if(el.dataset.el==='chart') nh=sh;`（原来 `chart|table` 都锁，现只锁 chart），插入的 `.tbl` 内部 `<table>` 设 `height:100%`。
    - ⑤ **侧栏章节名可编辑**：`onclone` 加 `#nav *{color:transparent!important;-webkit-text-fill-color:transparent!important}` 把侧栏文字从背景隐藏，再用 `nav.querySelectorAll('.item')` 逐条 `addText` 叠原生文本框（当前章节取绿、其余白）→ PowerPoint 里可改章节名（**推翻了 v1.9.19「侧栏整条留在截图里」的旧决定**，因为用户现在要求可改）。
    - ⑥ **图形/图标**：工具栏「⬡ 图形/图标」+ `#iconPicker` 面板；`ICONS` 15 个矢量图标（viewBox 0 0 48 48，占位 `__C__` 换色）；插入元素 `.fig`（`contenteditable=false`，`GFX_SEL` 纳入）可拖动/缩放/改填充色/删除；`dblclick` 对 `.fig` 直接 `return`（不进文字编辑）。
    - **图标必须用显式 `fill` 而非 `currentColor`**：否则导出时 `#elContent *{color:transparent}` 会让图标整体透明消失。
    - 验证：真实 Chrome 无头 `loadSample → 插入 .fig → exportPptEditable`，解码后 5 页、每页 1 张 2560×1440 背景 + 原生文本；**侧栏章节名**逐页叠成原生文本（navChapterRuns 2~3/页）；4 个内联 script 块 `vm.Script` 全过。

26. **表格「还是没有边框」——其实是颜色太浅 + 折叠边框（v1.9.22）**：v1.9.21 把表格烤进背景后，用户仍反馈「表格还是没有边框」。
    - **根因（务必先量再改）**：边框**一直都在渲染**，只是色 `#cfe0c8`（207,224,200）在**白底上对比度只有约 19%**，肉眼/投影下≈不可见。用导出背景 PNG 横切采样，列分隔线（x=588/920/1244）与行分隔线都能采到 `#cfe0c8` 像素 → html2canvas 早把线烤出来了，问题纯粹是**颜色太浅**。
    - **两个动作**：① 边框色 `#cfe0c8`（全局 `.content/.tbox table`）与插入表格的 `#c9d3c9` 统一改成明显可见的绿 **`#9CB894`**（156,184,148）；② `border-collapse:collapse` → **`separate` + `border-spacing:0`**（html2canvas 对折叠边框渲染不稳），单元格只画「上 + 左」、表格补「右 + 下」→ 干净 1px 网格（避免分离边框常见的双线加粗）。
    - **验证要目视 + 采样**：把导出背景裁剪放大目视（横竖格线 + 外框清晰）；再横切采样确认列分隔线处像素接近 `#9CB894`。**别只用「边框色像素计数」——先把检测色域对准新色**（复用了旧色域 `185<r<225` 时，新色 R=156 落在域外，计数几乎不变，会误判「没修好」）。背景是 **PNG 无损**，排除「JPEG 压缩抹线」。
    - **「插入型表格行被截」的假象**：探针把 `.el.tbl` 用 `position:absolute` 硬贴到 `#elContent` 边缘时，可能被 `.content` 容器的 `height:547px;overflow:auto` 裁行；真实插入路径是 `execCommand('insertHTML')` 插进正文**流**里，不受影响——别把它当回归。

27. **表格网格被自己的白卡片盖掉 + 逐格文字重复（v1.9.23 修复）**：v1.9.22 改完边框色后，用户**第三次**反馈「样例还是没有表格」。
    - **别再只看背景图！必须按 PPTX 的图层 z 序看**。背景 PNG 是**对的**（网格、表头浅绿、`1:6.8` 单行全在），问题出在**叠在它上面的原生对象**。用 python 解析 `ppt/slides/slideN.xml` 按文档顺序列出 `<p:pic>/<p:sp>`，一眼看到：
      - **`<p:pic>` 背景图在最底**（满幅 `12191695×6858000`）✓；
      - 但紧跟着一个 **`prstGeom prst="roundRect"` + `solidFill FFFFFF` 的不透明卡片**，位置正好等于表格卡片 → **把背景里的网格整片糊掉**（所以「卡片外框能看见、格线看不见」）；
      - 还有 **sp12–sp27 逐格文字**，其中 `1:6.8`（`<b>`）的框只有 `cx=322949`（≈0.24in = 文本自身宽度）→ PowerPoint 里折成三行，就是「字错位」。
    - **根因是 `skipVisual` 没贯穿递归**：调用处明明写的是 `_ppWalk(ps, content, R, true)`（截图已保真，不该再画任何形状），但 `_ppWalk(slide, root, R, skipVisual)` 内部**所有递归调用都只传 3 个参数** → 深层节点 `skipVisual=undefined` → `!skipVisual` 成立 → 卡片白块 / KPI 底块 / banner 底块**又被画了一遍**，压住背景。修复：**递归一律透传第 4 参**（4 处：`rc-2col|rc-col`、`rc-card` 的 children 循环、`rc-col-chart` 的 children 循环、末梢 `else`）。
    - **表格另要「整张烤背景 + 不叠任何格子文字」**：`_ppWalk` 开头加 `if(root && root.tagName==='TABLE') return;`。只在 `ch.tagName==='TABLE'` 判断**没用**——表格常嵌在 `.rc-card` 里，是以 `root` 身份被递归进来的，那个判断永远命中不了（v1.9.21 的 `continue` 因此形同虚设，逐格文字一直在重复叠加，双份文字 + 极小框折行）。
    - **验证口径（升级版，必做）**：① 硬断言每页 `a:tbl==0`、**「`roundRect`+`solidFill FFFFFF` 的不透明遮盖块」计数==0**、每页 `blip==1`、表格专属文字（如 `4,800`/`获客数`）**不再出现**在任何 slide XML 里；② 再用 PIL 按 `slideN.xml` 的**文档顺序**把各 `<p:sp>` 的 off/ext/填充/文字合成为一张「放映观感预览」目视（形状填充只读 `<p:txBody>` **之前**的 `solidFill`，否则会把「绿色文字」误当「绿色填充块」画成色条）；③ 别忘抽查**没有表格的页**（KPI/侧栏/图表是否因去掉叠加而缺块）——背景含全部形状，去掉叠加不会丢东西。

28. **导出期间必须冻结 `fit()`，否则「第 1 页整页截图被拍成缩略图」（v1.9.24 修复）**：用户第 4 次反馈「还有乱码」，症状是第 1 页背景变小、与原位文字错位叠成重影。
    - **现象定位**：把 `slide1.xml` 按图层序拆开 + 单独抠出 `image-1-1.png` → **背景图本身就是坏的**：内容缩在左上角一小块（非白像素包围盒只占画布 **34% 宽 / 34% 高**），其余全白；而 2~5 页背景都是 98%/100% 满幅 → 只有第 1 页中招。
    - **根因**：两条导出路径（`exportPptEditable` / `exportPdf`）每页循环都是 `renderAll(); fit();` → `slide.style.transform='none'` → 两次 `_ppRaf()` → `html2canvas()`。第 1 轮 `renderAll()` 之前刚改过 body class（去 `editing`/`present`、加 `exporting`）→ `#stage` 尺寸变化 → 挂在 `#stage` 上的 `ResizeObserver` 触发 `setTimeout(fit,0)`，正好落在「已清 `transform`」**之后**、截图**之前** → 缩放被加回来。第 2 页起布局稳定、RO 不再触发，所以只坏第 1 页。
    - **修法**：① `fit()` 开头加 `if(document.body && document.body.classList.contains('exporting')) return;`（两条导出路径共用，因为都加 `exporting`）；② 截图前（两次 `_ppRaf()` 之后）**再确认一次** `transform='none'; transformOrigin='top left'; marginLeft=marginTop='0'`；③ 导出结束**先** `classList.remove('exporting')` **再** `renderAll(); fit();`，否则桌面上的缩放还原不回来。
    - **验证口径（务必用这条，别再骗自己）**：**「图片尺寸 2560×1440」不能证明没被缩放** —— html2canvas 传了固定 `width/height`，画布尺寸永远是 2560×1440，缩放只体现在**内容包围盒**上。正确做法：量每页背景 PNG 的**非白像素包围盒**（PIL：`im.convert('L').point(lambda v:255 if v<246 else 0).getbbox()`），要求 `maxx > 0.85*W` 且 `maxy > 0.55*H`。修复前 slide1 `x[0..864] y[0..495]` → SHRUNK；修复后 5 页全 `x[0..2511] y[0..1439]` → **5/5 满幅**。
    - **加一条结构证据**：给 `fit()` 装计数器（比较调用**前后** `slide.style.transform` 是否真的被改成 `scale(...)`），用 `--window-size=1200,700` 强制 `scale<1` 复现，要求「导出期间实际改动缩放的次数 == 0」。
    - **副带教训（测量假象）**：计数器第一版写成「调用后 `transform` 里含 `scale` 就 +1」，会**误报 1 次** —— 因为第 1 轮读到的 `transform` 还残留着**进入导出前屏幕上**的 `scale(...)`。计数器必须比较调用**前后是否发生变化**，不能只看调用后的值。
    - **历史教训闭环**：v1.9.21 曾把「第 1 页背景文件更小」当成「标题页留白多、压缩率高」而**误判为假报警**（当时只比了 2560×1440 的画布尺寸），实际那正是本 bug。**尺寸相同 ≠ 未缩放。**

29. **示例内容「太空」→ 用「flex 列布局 + 洞察卡」撑满（v1.9.25）**：用户反馈示例每页只有一半内容。两招：① **排版**——`.rc-2col` 两栏改 `flex-direction:column` 撑满、`.rc-col-chart` 由 `align-items:center` 改 `stretch` 让图表卡与左栏等高、图表高度 250→330、`chart-wrap svg` 的 `max-height` 280→400；新增 `.rc-insight`「洞察/建议」卡（浅绿渐变 + 虚线框，`margin-top:auto` 自动沉底）。② **内容**——每页左栏补第二张卡片/KPI 行/洞察卡、右栏图表下方补洞察卡，数据写得更具体。验证口径：量 `.content` 的 `scrollHeight === clientHeight`（零溢出）且左右栏 `getBoundingClientRect().height` 相等；导出背景按四段垂直分区数非白像素，确认「中下段(50~75%)」不再空白。**注意：`makeChart` 里图表是写死 `width/height` 的 SVG，`chart-wrap svg` 的 `max-height` 必须同步放大，否则图表撑不高。**

30. **「能拖动、但不能缩放」= 缩放手柄样式挂错了图层（v1.9.26 修复）**：用户报「白色卡片底还是不能拖动」→ 随即澄清「可以拖动、是**不能缩放**」。**这类"能拖不能缩"的分裂现象，几乎一定是手柄层的问题，不是拖动/缩放的 JS 逻辑问题。**
    - **两套图层共用一份手柄 CSS**：正文小图形（`.rc-*` / `.fig`）的 8 个橙色手柄由 `showGfxHandles()` 追加到 **`#gfxHandles`**（`z-index:59`，父层 `pointer-events:none`）；而手柄的可见/可点样式只写在 **`#handles .rh` / `#handles .rh-del`**（那是「顶层元素选中」的另一层）。选择器对不上 → `#gfxHandles` 里的手柄算不出 `width/height/border`，也拿不到 `pointer-events:auto` → **0 尺寸 + 不可命中**。**拖动不经手柄**（`startGfxDrag` 绑在元素本体 mousedown 上），所以拖正常、缩失效。
    - **修法**：把 `#gfxHandles .rh` / `#gfxHandles .rh-del`（含 `:hover` 与 8 个方向 `cursor`）**并入 `#handles` 同一组选择器**。
    - **验证要用 `elementFromPoint`（关键）**：程序化 `dispatchEvent` 到 0 尺寸手柄**仍会触发**（它绕过命中测试），所以**不能**用"直接派发事件看宽高变化"来验证——必须用 `document.elementFromPoint(手柄x,手柄y)` 取"浏览器真实会命中的元素"，再对其派发 mousedown。修复前命中 `DIV.sb-bg`（背景）→ `RESIZED=false`；修复后命中 `DIV.rh.se`（手柄）→ 卡片 `666×169→930×375`。**另一条铁律**：新增/移动任何"覆盖层里的交互子元素"（手柄、浮层按钮），都要**同步检查它的 CSS 选择器是否覆盖了实际所在的那个 layer id**。

31. **导出「原生对象但内容错乱/丢失」= async 叶子块被当布尔判真 + 富文本丢了（v1.9.29 修复）**：用户在 v1.9.28（已回归原生对象）基础上反馈「导出来乱乱的，侧边栏也不全，有的错位，有的消失」。根因五点，按致命度排序：
    - **①（最致命）`async` 叶子块被当布尔判真 → 整页内容层全丢**：把块识别抽成独立 `async function _ppLeafBlock(slide,ch,R,skipVisual)`，但调用处写成 `if(_ppLeafBlock(...)) return;` —— **async 函数返回的是 Promise，永远是 truthy**，于是 `if` 恒真、`_ppWalk` 一进循环就 `return`，所有正文/卡片/图表/表格/列表全部跳过，只留下侧栏。这就是「有的消失 + 乱乱的」。**修法**：两处调用都加 `await` → `if(await _ppLeafBlock(...)) return;`（顶层 root 入口一处、`_ppWalk` 子循环一处）。**验证铁律**：凡是把 `async function` 当布尔条件用，先检查返回值是不是 Promise；诊断脚本里 `console.log('LEAF content el ent-fade =>', await _ppLeafBlock(...))` 打出来是 `[object Promise]` 就是中招信号。
    - **② `rc-ul` 的 `<li>` 文字丢了，只剩 `rc-tag` 小标签**：`rc-card` 会经 `_ppWalk` 递归进子节点，于是 `.rc-ul` 是以 **`root` 身份**被父级递归进来的，原本写在 `_ppWalk` 子循环里的 `rc-ul` 分支永远命中不了（和 v1.9.21 表格 `continue` 失效同一类坑），`<li>` 正文全被当成普通文本折行、和标签挤在一起。抽成叶子块后 `_ppWalk` 顶层先 `if(await _ppLeafBlock(root,...)) return;` 即可命中。
    - **③ `rc-insight`「洞察卡」丢了渐变底 + 绿点 + 项目符号**：原本没有专门分支，整块被当成普通文本。新增 `.rc-insight` 分支：`addShape('roundRect',{fill:F2F8F2,line:DBEAD9})` + 标题前 `addShape('ellipse',{fill:4CAF50})` 绿点 + 列表用 **逐段对象** `{text, options:{bullet:{indent:14}}}` 传 `addText`（注意：`bullet` 必须放在每段 `options` 里，不能放在字符串数组顶层，否则 pptxgenjs 报「Cannot create property 'options' on string」）。
    - **④ `rc-tag` 颜色丢了（绿/橙/红）**：原本整块按单色导出，标签的三色语义（ok→`1B7A2F` / note→`E65100` / warn→`C62828`）没了。新增 `_ppNodeRuns(el)` 把 `.rc-tag` 和 `<b>/<strong>` 拆成富文本 run：`slide.addText([{text, options:{color,bold}}, ...])`，颜色按 class 映射。
    - **⑤ 侧栏/导航窄文字被 `margin` 挤折行错位**：pptxgenjs `addText` 默认 `margin≈0.05in`，窄栏文字（章节名、KPI 数值、横幅标题）被挤成两行、缩进错位。统一在导出 `addText` 上加 `margin:0`，并给单行场景补 `wrap:false` + `valign:'middle'`；`rc-banner-t` / `rc-card-h` / `rc-kpi .v/.l` 等内联 `addText` 同样补 `margin:0`。
    - **Z 序**：白底高亮胶囊 `#elPill` 必须在章节名文字**之前** `addShape`，否则文字被盖住（侧栏「不全」的一例）。
    - **验证口径（必须真跑，别信无头截图）**：无头 `ent-fade` 会把 `#elContent` 留在 `opacity:0`，探针必须**手动强制 `opacity:1`** 再 `_ppWalk`，否则会误以为「又丢了」；但**真实导出**靠 `body.exporting #elContent{opacity:1!important}` 强制可见，无需手动。正确验证 = playwright 钩住 pptxgenjs 的 `addText/addShape/addChart/addTable/addImage`，跑 `exportPptEditable()`，统计每页对象数 + 抽查关键文本：15 页应得 **647 个对象、0 报错**；抽查应命中 `rc-ul` 全文（如「内墙涂料、外墙涂料：贡献 58.7% 营收」）、`rc-tag` 三色、`addChart` 雷达、`rc-insight` 底+点+项目符号、`rc-cover` 封面字段。


## 分享给别人

**发成品给别人（最常见）**
- 只发 `三棵树汇报模板.html` 一个文件（v1.9.29 ≈1.29MB，已内联全部依赖），**不用附带 assets 文件夹**
- 对方双击即开（Chrome / Edge / 360 均可），无需装 Office、无需联网
- ⚠️ **改动存在各自浏览器 localStorage 里，不会随文件走**：
  你在自己电脑上改的章节，同事打开仍是默认 5 章。
  要把内容一起给同事 → 改完点顶部「**导出 PDF**」；
  或让 agent 改 `DEFAULT.pages` 后跑 `pack.py` 重新打包。

**共享 skill 本身**
把整个 `sks-nav-html-template/` 目录打包发给对方，放到其 `~/.workbuddy/skills/` 下即生效。

## 校验方法（改完源码必做）
无 playwright/selenium 时，用 Chrome headless + 注入探针脚本：
```bash
# 复制 template.html → 末尾注入 <script>：派发 MouseEvent 模拟点击、
# 读 getBoundingClientRect / getComputedStyle → 结果写进 document.title
# → --dump-dom 后正则抓 <title>
"/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu \
  --window-size=1680,1050 --virtual-time-budget=4000 --dump-dom _test.html > dump.txt
```
比截图可靠（能读到精确 px）。重点校验：白线/三角/logo/标语是否 `elementFromPoint` 命中、
两行标语右端差是否 0.00、层级顺序是否正确。

**改完源码的三步自检（v1.2 实测有效，快且够用）**

```bash
# 1) JS 语法 + 新增元素是否齐全（正则抠出 <script> 交给 node --check）
python -c "import re;s=open('template.html',encoding='utf-8').read();open('_chk.js','w',encoding='utf-8').write(re.search(r'<script>(.*?)</script>',s,re.S).group(1))"
node --check _chk.js && echo "JS SYNTAX OK"

# 2) 视觉冒烟：复制成品 → 末尾注入要验证的状态 → headless 截图 → 肉眼看图
#    例如验证放映态：'</body>' 前插 <script>setToc(true);go(2);startPresent();</script>
chrome.exe --headless=new --disable-gpu --hide-scrollbars --window-size=1600,900 \
  --screenshot="C:\...\play.png" "file:///C:/.../_smoke_play.html"

# 3) 状态探针：headless 里截图看不见的运行时状态（toast 文案 / 按钮文案 / 是否在 iframe），
#    用 --dump-dom + 延时把结果写进 body 属性再 grep 出来
#    末尾插：<script>setTimeout(()=>startPresent(),50);
#             setTimeout(()=>{document.body.setAttribute("data-probe",
#               "TOAST="+document.getElementById("toast").textContent+" |FSBTN="+
#               document.getElementById("pvFs").textContent+" |INFRAME="+inFrame());},1200);</script>
chrome.exe --headless=new --disable-gpu --virtual-time-budget=5000 --dump-dom "file:///C:/.../_sm3.html" \
  | grep -o 'data-probe="[^"]*"'
# ⇒ 期望：TOAST=全屏被浏览器拒绝了：再点一次 ⛶ 全屏，或直接按 F11 |FSBTN=⛶ 全屏 |INFRAME=false
```

> 注意 `--screenshot` 用 `--virtual-time-budget` 才有意义地推进定时器；纯截图不用。
> 探针法专治「截图看不出来的逻辑」——toast 是否弹出、文案是否正确，比人眼看图可靠。
> 但 **headless 无法验证真全屏是否成功**（无用户手势，必然被拒），只能验证降级分支；
> 真全屏必须在真实浏览器里手点一次 ▶ 放映 确认。

> headless 下 `requestFullscreen()` 不生效，但 `body.present` 的布局效果**照样能验证** ——
> 这正是把「全屏状态」与「放映布局」分开（CSS 类 + 浏览器全屏 API）的好处。
> 截图旁会出现 `libpng warning: tRNS: invalid with alpha channel`，是 logo PNG 的固有告警，可忽略。
> 临时文件删除：沙箱的 `rm` 对 git-bash 风格 `/c/...` 路径会报 relative path rejected，
> 改用 `python -c "import os;os.remove(r'C:\绝对路径')"`。
