# PDF_Chapter_5

### Page/Slide 1



### 1. 文字与公式提取  
**标题与章节**  
- `Chapter 5 Choice`  

**核心文字内容**  
- 消费者选择理论：将预算约束与偏好（无差异曲线）结合，求解效用最大化商品组合。  
- 最优选择的三种可能情形：  
  (i) 无差异曲线与预算线相切；  
  (ii) 无差异曲线存在拐点；  
  (iii) 角解（仅消费单一商品）。  
- 切点条件：无差异曲线斜率（边际替代率 $ MRS $）等于预算线斜率。  
- 求解方法：  
  - 切点条件方程：$\frac{MU_1(x_1, x_2)}{MU_2(x_1, x_2)} = \frac{p_1}{p_2}$  
  - 预算约束方程：$p_1 x_1 + p_2 x_2 = m$  

**公式与示例**  
- 边际替代率：  
  $$
  MRS = -\frac{MU_1(x_1, x_2)}{MU_2(x_1, x_2)}
  $$  
- 预算线斜率：$-\frac{p_1}{p_2}$  
- **示例数据**：  
  - 效用函数：$U(x_1, x_2) = x_1^2 x_2$  
  - 价格与收入：$p_1 = 1$, $p_2 = 3$, $m = 180$  
  - 边际效用：  
    $$
    MU_1 = 2x_1 x_2,\quad MU_2 = x_1^2
    $$  
  - 边际替代率：  
    $$
    MRS = -\frac{2x_2}{x_1}
    $$  
  - 切点条件：  
    $$
    \frac{2x_2}{x_1} = \frac{1}{3} \implies 6x_2 = x_1
    $$  
  - 预算约束：  
    $$
    x_1 + 3x_2 = 180
    $$  
  - 解得：$x_1 = 120$, $x_2 = 20$  

**脚注补充**  
- $MRS$ 的符号问题：$-\frac{MU_1}{MU_2}$ 与 $-\frac{MU_2}{MU_1}$ 的混淆不影响核心逻辑，关键条件是边际效用比例等于价格比例。  

---

### 2. 知识点解析  
#### **切点条件的经济学意义**  
- 无差异曲线与预算线相切时，消费者达到**效用最大化**。此时：  
  $$
  \frac{MU_1}{MU_2} = \frac{p_1}{p_2}
  $$  
  **含义**：消费者对商品1和商品2的边际效用之比等于市场价格比，表明单位货币支出带来的边际效用相等（即“性价比”均衡）。  

#### **示例的逻辑推导**  
1. **边际替代率与价格比联立**：  
   通过效用函数求出 $MU_1$ 和 $MU_2$，代入切点条件 $\frac{MU_1}{MU_2} = \frac{p_1}{p_2}$，得到 $x_1$ 与 $x_2$ 的线性关系（$6x_2 = x_1$）。  
2. **预算约束代入求解**：  
   将 $x_1 = 6x_2$ 代入预算方程 $x_1 + 3x_2 = 180$，直接解出最优消费组合 $(120, 20)$。  
   **验证**：  
   $$
   120 + 3 \times 20 = 180 \quad (\text{满足预算约束})
   $$  

#### **与上文知识点的连续性**  
- 本节延续了上文“预算线”与“无差异曲线”的分析框架，将两者结合为**消费者选择问题**的核心模型。  
- 切点条件本质上是**边际分析**的应用：当 $ \frac{MU_1}{p_1} \neq \frac{MU_2}{p_2} $ 时，消费者可通过调整消费组合提升效用，直至达到均衡。  

> **关键结论**：效用最大化点必满足“边际效用-价格比例均衡”，且必须位于预算线上（否则存在未耗尽收入的改进空间）。

---
### Page/Slide 2



### 1. 文字与公式提取  
**核心文字内容**  
- 消费者选择梯度边界（kinks）或角点（corners）均衡：无需无差异曲线斜率等于预算线斜率，仅需预算约束方程与角点条件方程联立求解。  
- 示例：效用函数 $U(x_1, x_2) = \min\{x_1, 3x_2\}$，价格 $p_1 = 2$，$p_2 = 1$，收入 $m = 140$。无差异曲线为L形，折点位于 $x_1 = 3x_2$。预算约束为 $2x_1 + x_2 = 140$，解得最优组合 $(x_1, x_2) = (60, 20)$。  
- 学习目标列表：  
  - 计算切点均衡下的最优消费束；  
  - 求解拐点无差异曲线的最优束；  
  - 识别角解案例；  
  - 绘制均衡图示；  
  - 应用于非线性预算。  
- 后续习题：以Charlie为例（效用函数 $U(x_A, x_B) = x_A x_B$，$p_A = 1$，$p_B = 2$，$m = 40$），要求绘制预算线及效用水平 $U=150$、$U=300$ 的无差异曲线。  

**公式**  
- 最优消费束：  
  $$
  (x_1, x_2) = (120, 20),\quad (x_1, x_2) = (60, 20)
  $$  
- 效用函数：  
  $$
  U(x_1, x_2) = \min\{x_1, 3x_2\},\quad U(x_A, x_B) = x_A x_B
  $$  
- 角点条件：  
  $$
  x_1 = 3x_2
  $$  
- 预算约束：  
  $$
  2x_1 + x_2 = 140
  $$  

---

### 2. 知识点解析  
#### **角解与拐点均衡的求解逻辑**  
- **核心机制**：  
  - 与切点条件不同，角解（如L形无差异曲线）无需满足 $MRS = p_1 / p_2$。**替代关系**：  
    - 切点情形：需 $MU_1 / MU_2 = p_1 / p_2$（单位货币边际效用均衡）；  
    - 角解情形：**直接利用无差异曲线折点约束**（如 $\min$ 函数中 $x_1 = k x_2$）联立预算约束，跳过斜率比较。  
  - 本例中，$U = \min\{x_1, 3x_2\}$ 暗示消费者仅在 $x_1 = 3x_2$ 时实现最优（因超额消费任一商品不增加效用），此即**折点方程**，与预算线 $2x_1 + x_2 = 140$ 联立得解。  

- **经济含义验证**：  
  - 代入 $x_1 = 3x_2$ 至预算约束：  
    $$
    2(3x_2) + x_2 = 140 \implies 7x_2 = 140 \implies x_2 = 20,\ x_1 = 60
    $$  
  - **意义**：完全互补品要求固定消费比例（此处 $x_1:x_2 = 3:1$），若偏离此比例（如多消费 $x_2$），收入将被浪费，效用无法提升。这呼应了上文"角解"定义，但需注意：**角解不等价于单一商品消费（如 Cobb-Douglas 模型的严格角解）**，此处是**成比例消费的边界最优**。  

#### **与上文知识点的连续性**  
- **对三种情形的深化**：  
  - 上文指出最优解第三类情形为"角解"，但未展开数学细节。本例具体化 **$\min$ 函数的角解逻辑**：无差异曲线的非凸性（L形）使切点条件失效，转而依赖**折点位置方程**（$x_1 = 3x_2$）作为替代工具。  
  - **关键对比**：  
    | 情形         | 切点条件适用 | 角解条件适用 |  
    |--------------|--------------|--------------|  
    | 上文示例     | 是（$U=x_1^2x_2$） | 否           |  
    | 本例         | 否           | 是（$U=\min\{x_1,3x_2\}$） |  
- **学习目标的衔接**：  
  - 列出的5项目标（如求解拐点组合、识别角解场景）**直接延伸上文求解框架**：  
    - 切点求解依赖边际效用方程，角解求解依赖**几何特征方程**（无差异曲线折点或边界），二者均需结合预算约束，**统一于"最优解必在预算线上"的连续约束基础**。  
  - 习题中Charlie的例子 ($U = x_A x_B$) 将回归切点分析，形成**知识闭环**：先展示角解（特殊）、再复习切点（一般）。  

> **核心新知**：角解问题的本质是**预算约束与无差异曲线几何特性**的直接互动（如L形曲线的折点线），无需边际替代率计算，但**求解逻辑仍服从效用最大化**——通过约束条件消去自由度，确保收入无闲置。

---
### Page/Slide 3



### 当前图片解析

#### 1. 提取所有文字和公式
**图表内文字与标记：**  
- **坐标轴：**  
  - X轴：Apples（0 至 40）  
  - Y轴：Bananas（0 至 40）  
- **曲线与标签：**  
  - "Red curves"（红色曲线）  
  - "Black curve"（黑色曲线）  
  - "Pencil line"（铅笔线）  
  - "Blue budget line"（蓝色预算线）  
  - 点标记："e"（位于预算线与某曲线交点，约 (20, 10)），"a"（位于预算线上，约 (30, 5)）  

**图表下方文字：**  
> (b) Can Charlie afford any bundles that give him a utility of 150? **Yes**.  
> (c) Can Charlie afford any bundles that give him a utility of 300? **No**.  
> (d) On your graph, mark a point that Charlie can afford and that gives him a higher utility than 150. Label that point A.  
> (e) Neither of the indifference curves that you drew is tangent to Charlie’s budget line. Let’s try to find one that is. At any point, $(x_A, x_B)$, Charlie’s marginal rate of substitution is a function of $x_A$ and $x_B$. In fact, if you calculate the ratio of marginal utilities for Charlie’s utility function, you will find that Charlie’s marginal rate of substitution is $MRS(x_A, x_B) = -x_B / x_A$. This is the slope of his indifference curve at $(x_A, x_B)$. The slope of Charlie’s budget line is $-1/2$ (give a numerical answer).  
> (f) Write an equation that implies that the budget line is tangent to an indifference curve at $(x_A, x_B)$. $-x_B / x_A = -1/2$. There are many solutions to this equation. Each of these solutions corresponds to a point on a different indifference curve. Use pencil to draw a line that passes through all of these points.  

**提取公式：**  
- 边际替代率斜率：  
  $$
  MRS(x_A, x_B) = -\frac{x_B}{x_A}
  $$  
- 预算线斜率：  
  $$
  \text{Slope} = -\frac{1}{2}
  $$  
- 切点条件方程：  
  $$
  -\frac{x_B}{x_A} = -\frac{1}{2}
  $$

---

#### 2. 图表解析：结合上文知识点的经济含义  
本图表针对上文知识点总结中Charlie的后续习题（效用函数 $U(x_A, x_B) = x_A x_B$，价格 $p_A = 1$，$p_B = 2$，收入 $m = 40$），**展示切点均衡的求解逻辑**。需与上文“角解”案例（如L形无差异曲线）对比，突出知识连续性：**切点情形依赖 $MRS = p_1 / p_2$，而角解依赖几何约束（如 $x_1 = 3x_2$）**。  

##### **核心要素解读**  
- **蓝色预算线（Blue budget line）**：  
  方程为 $x_A + 2x_B = 40$，斜率为 $-1/2$。  
  - *上文逻辑衔接*：上文强调最优解必在预算线上，此处预算线是约束边界。切点均衡需在此线上满足 $MRS = p_A / p_B$（而非角解的折点方程）。  
  - *经济含义*：预算线截距 $(40, 0)$ 和 $(0, 20)$ 表明Charlie可选择全消费苹果或香蕉，但效用最大化需组合。  

- **红色曲线（Red curves）**：  
  对应 $U = 150$ 和 $U = 300$ 的无差异曲线（$x_A x_B = 150$ 和 $x_A x_B = 300$）。  
  - *变化含义*：  
    - $U = 150$ 的曲线（如点 $(15, 10)$）与预算线相交（问题 (b) "Yes"），代表**可负担但非最优**（上文学习目标"识别角解"的延伸：切点情形下，交点非解）。  
    - $U = 300$ 的曲线（如点 $(30, 10)$）完全在预算线外（问题 (c) "No"），因最大效用为 $U^* = 200$（由切点解得），呼应上文"边界最优"概念——收入无法支持更高效用。  
  - *上文对比*：上文L形曲线（角解）无交点问题（仅需折点联立预算线），此处Cobb-Douglas曲线的凸性导致**交点存在但需切点条件筛选**。  

- **黑色曲线（Black curve）和铅笔线（Pencil line）**：  
  - Black curve：代表切点均衡的无差异曲线（$U = 200$），点 $e$ 为切点 $(20, 10)$。  
  - Pencil line：由方程 $x_B / x_A = 1/2$（即 $x_A = 2x_B$）定义，是**收入-消费曲线**。  
    - *推导*：切点条件 $-x_B / x_A = -1/2$ 化简为 $x_B / x_A = 1/2$，代入预算线 $x_A + 2x_B = 40$ 得最优解 $(x_A^*, x_B^*) = (20, 10)$。  
    - *经济含义*：所有切点路径形成此线，表示当收入变化时，Charlie的最优组合沿 $x_B = \frac{1}{2} x_A$ 比例调整（上文学习目标"绘制均衡图示"的实证）。  
  - *上文衔接*：上问中角解无此线（因折点比例固定），切点情形需显式求解 $MRS = p_1 / p_2$，体现"切点条件适用"的分类逻辑。  

##### **关键变化的经济含义**  
1. **问题 (e) 和 (f) 的切点逻辑**：  
   - 无差异曲线斜率 $-\frac{x_B}{x_A}$ 与预算线斜率 $-\frac{1}{2}$ 相等时，达到**内部均衡**（切点条件）。  
   - 这与上文角解案例（如 $U = \min\{x_1, 3x_2\}$）**本质区分**：  
     - 角解：L形曲线下，**切点条件失效**，需直接用折点方程 $x_1 = 3x_2$ 联立预算线。  
     - 此处：光滑凸曲线，**切点条件是必要且充分**的，确保边际效用按价格比例分配（单位货币效用均衡）。  
   - *知识连续性*：上文强调"求解拐点无差异曲线的最优束"需跳过斜率比较，而此处切点分析需严格应用斜率条件，形成对比案例库。  

2. **点 $a$ 和点 $e$ 的对比**：  
   - 点 $a$（约 $(30, 5)$）：位于预算线上但 $MRS = -5/30 = -0.167 \neq -0.5$，效用 $U = 150 < 200$。  
   - 点 $e$（切点）：满足 $MRS = -10/20 = -0.5$，效用 $U = 200$ 为最大。  
   - *含义*：验证上文"角解不等价于单一商品消费"——此处最优解为内部点，而角解（如L形）可能为成比例边界点，但均需**效用最大化下收入无闲置**。  

3. **铅笔线（收入-消费曲线）的作用**：  
   - 方程 $x_B / x_A = 1/2$ 表示需求函数 $x_A = m / (2p_A)$、$x_B = m / (2p_B)$ 的几何轨迹。  
   - *上文延伸*：上文习题要求"应用于非线性预算"，此处线性预算下该线为直线；若预算非线性（如数量折扣），则需分段求解切点，深化"角解与拐点均衡的求解逻辑"。  

此图表完整实现上文"学习目标"：  
- 切点均衡计算：通过 $MRS = p_A / p_B$ 得 $(20, 10)$。  
- 识别非最优点：红色曲线与预算线交点（如 $a$）被排除。  
- 图表绘制：预算线、无差异曲线、收入-消费曲线齐备。  
**核心新知**：切点分析依赖边际替代率与价格比一致，而角解依赖几何特征，但二者均以"预算约束内效用最大化"为统一框架，呼应上文"角解问题的本质是预算约束与无差异曲线几何特性的直接互动"。

---
### Page/Slide 4



### 当前图片解析

#### 1. 文字与公式提取
- **文字内容**:
  - `(g) The best bundle that Charlie can afford must lie somewhere on the line you just penciled in. It must also lie on his budget line. If the point is outside of his budget line, he can't afford it. If the point lies inside of his budget line, he can afford to do better by buying more of both goods. On your graph, label this best affordable bundle with an E. This happens where \( x_A = 20 \) and \( x_B = 10 \). Verify your answer by solving the two simultaneous equations given by his budget equation and the tangency condition.`
  - `(h) What is Charlie's utility if he consumes the bundle (20,10)? 200.`
  - `(i) On the graph above, use red ink to draw his indifference curve through (20,10). Does this indifference curve cross Charlie's budget line, just touch it, or never touch it? Just touch it.`
  - `5.2 (0) Clara’s utility function is \( U(X, Y) = (X + 2)(Y + 1) \), where \( X \) is her consumption of good \( X \) and \( Y \) is her consumption of good \( Y \).`
  - `(a) Write an equation for Clara’s indifference curve that goes through the point \( (X, Y) = (2,8) \). \( Y = \frac{36}{X+2} - 1 \). On the axes below, sketch Clara’s indifference curve for \( U = 36 \).`
  - `(b) Suppose that the price of each good is 1 and that Clara has an income of 11. Draw in her budget line. Can Clara achieve a utility of 36 with this budget? Yes.`
  
- **公式**:
  - Clara效用函数：\( U(X, Y) = (X + 2)(Y + 1) \)
  - 无差异曲线方程（\( U = 36 \)）：\( Y = \frac{36}{X+2} - 1 \)

#### 2. 图表解析
当前图片包含**Clara的无差异曲线图**，对应上文知识点总结中Cobb-Douglas效用函数的延伸分析。图表细节：
- **坐标系**：  
  - \( X \)-轴（横轴）：范围 0–16，刻度标记 0, 4, 8, 11, 12, 16。  
  - \( Y \)-轴（纵轴）：范围 0–16，刻度标记 0, 4, 8, 11, 12, 16。  
- **曲线**：  
  - 标记为 \( U = 36 \) 的凸曲线（从左上向右下递减），通过点 \( (2, 8) \)（验证：\( (2+2)(8+1) = 36 \)）。  
  - 曲线形状：因效用函数变形，**与标准Cobb-Douglas相似但有位移**（核心在 \(\bar{X} = X + 2\), \(\bar{Y} = Y + 1\) 的变换），仍保持严格凸性与光滑性。  

##### 结合上文的变化含义
- **与Charlie案例的连续性分析**：  
  - 上文知识点总结强调，Cobb-Douglas型效用（如Charlie的 \( U = x_A x_B \)) 的均衡依赖 **切点条件（\( MRS = \text{price ratio} \))**，而角解适用于L形曲线。此处Clara的效用函数 \( U = (X + 2)(Y + 1) \) 是**位移版Cobb-Douglas**，需通过坐标变换纳入统一框架：  
    - 定义虚拟变量 \(\bar{X} = X + 2\), \(\bar{Y} = Y + 1\)，则 \( U = \bar{X} \bar{Y} \)（标准形式），但预算约束变为 \( X + Y = 11 \rightarrow (\bar{X} - 2) + (\bar{Y} - 1) = 11 \)，即 \( \bar{X} + \bar{Y} = 14 \)（等效收入增加）。  
    - **关键延续**：切点条件仍适用（\( MRS = -\frac{\bar{Y}}{\bar{X}} = -\frac{p_X}{p_Y} \)），呼应上文"切点条件是必要且充分"的结论（非角解）。  
  - 问题 (b) 中预算线 \( X + Y = 11 \) 与 \( U = 36 \) 曲线**相交**（如点 (2,8) 满足 \( X + Y = 10 < 11 \)，位于预算线内），表明 \( U = 36 \) 可负担。  
    - **对比上文红色曲线**：类似Charlie案例中 \( U = 150 \) 曲线与预算线相交（"可负担但非最优"），此现象验证"交点存在需切点条件筛选"的逻辑——相交点不直接导出最优解，因边际替代率未匹配价格比（例如在 (2,8)，\( MRS = -\frac{8+1}{2+2} = -2.25 \neq -1 \)）。

- **经济含义的深化**：  
  - **位移项的作用**：常数项 +2 和 +1 意味着"虚拟基础消费"，导致无差异曲线向左下平移，但**不改变切点分析的本质**。  
    - 例如，最优解需解 \( \frac{Y+1}{X+2} = 1 \)（因 \( p_X/p_Y = 1 \)) 和 \( X + Y = 11 \)，得 \( X^* = 5 \), \( Y^* = 6 \)（\( U^* = 49 \)），最大效用高于 36。  
    - **知识连续性**：上文习题强调"收入-消费曲线依赖价格比"，此处若收入变化，Clara的最优路径仍沿 \( Y + 1 = k(X + 2) \) 比例调整（与Charlie的铅笔线逻辑一致）。  
  - **图表缺失的隐含信息**：  
    - 预算线 \( X + Y = 11 \)（若画出）会与 \( U = 36 \) 曲线**相交（非相切）**，确认上文关于"交点非最优解"的论断：实现 \( U = 36 \) 有冗余收入，而真最优需切点（\( U^* = 49 \)）。  
    - **边界情形**：若收入过低（如 \( m < \) 虚拟基础成本），可能出现角解，但本例中 \( m = 11 \) 充裕，验证上文"切点条件适用"的分类标准。

- **与上文关键变化的呼应**：  
  - 点 (2,8) 在预算线内（成本 10 < 11），**类比Charlie的点 \( a \)（30,5）**——已知效用非最大（\( U = 36 < 49 \)），强化"内部点均衡需MRS匹配价格"的核心原理。  
  - 无差异曲线"仅触碰"预算线（问题 (i)）的解答，与本图表相交情形形成对比，体现**同一框架下不同参数导致的均衡位置差异**（可负担性 vs 最优性）。  

> **核心延续**：Clara案例延续上文"效用最大化统一框架"，位移项仅需预算约束调整，但**切点条件逻辑不变**，深化"角解与切点取决于无差异曲线几何特性"的结论。

---
### Page/Slide 5



# Clara与Ambrose的效用最大化分析

## 一、图片内容提取

### Clara部分（求解过程）
- **(c)** 点 $(X,Y)$ 处，Clara的边际替代率为 $-\frac{Y+1}{X+2}$
- **(d)** 设MRS绝对值等于价格比：$\frac{Y+1}{X+2} = 1$
- **(e)** 预算方程：$X + Y = 11$
- **(f)** 联立方程解得：$X = 5$ 和 $Y = 6$

### Ambrose部分（新案例）
- **效用函数**：$U(x_1,x_2) = 4\sqrt{x_1} + x_2$（$x_1$为坚果，$x_2$为浆果）
- **(a)** $U=20$ 的等效点：$(25,0)$, $(16,4)$, $(9,8)$, $(4,12)$, $(1,16)$, $(0,20)$
- **(b)** 价格 $p_1=1$, $p_2=2$, 收入 $m=24$ → 最优坚果消费：$16$ 单位
- **(c)** 浆果消费：$4$ 单位
- **(e)** 收入增至 $34$ → 坚果仍 $16$ 单位，浆果增至 $9$ 单位

---

## 二、与上文的连续性分析

### Clara案例：位移版Cobb-Douglas的验证
- **求解逻辑的实现**：图片中(f)的解 $X^*=5$, $Y^*=6$ 对应 **上文推断的最优解**，效用 $U^*=(5+2)(6+1)=49$ 超过 $U=36$，验证上文"相交点(2,8)位于预算线内且非最优"的结论（因该点 $X+Y=10<11$ 有收入冗余）。
- **切点条件的准确性**：公式(d)中 $\frac{Y+1}{X+2}=1$ 直接应用了上文核心思想——通过变量替换 $\bar{X}=X+2$, $\bar{Y}=Y+1$ 将效用函数转化为标准Cobb-Douglas形式 $U=\bar{X}\bar{Y}$，此时切点条件简化为 $\frac{\bar{Y}}{\bar{X}}=\frac{p_X}{p_Y}=1$。

### Ambrose案例：准线性效用的对比深化
- **结构差异**：效用函数 $U=4\sqrt{x_1}+x_2$ 与Clara的位移版Cobb-Douglas有本质区别——**X₂的边际效用为常数1**，导致无差异曲线呈"平行移动"特征（不同于凸性递减的Cobb-Douglas）。
- **角解与内点解的关键**：
  - 当收入 $m=24$，最优解 $(16,4)$ 是内部解（MRS=$\frac{2}{\sqrt{x_1}}=0.5=p_1/p_2$）；
  - 当收入增至 $34$，最优解 $(16,9)$ **仍保持 $x_1=16$ 不变**，体现准线性效用的典型特征：
    - 坚果消费仅由价格比决定（$x_1^* = \left(\frac{2p_2}{p_1}\right)^2 = 16$）；
    - 剩余收入全部用于浆果（$x_2^* = m - p_1x_1^*$）。
- **与上文的呼应**：此结果强化了上文"切点条件适用性依赖于无差异曲线几何特性"的结论——与Clara的位移Cobb-Douglas（严格凸）不同，准线性效用可能在**收入变化时出现消费饱和**（坚果消费固定），这恰是上文"收入-消费曲线"分类讨论的延伸案例。

---

## 三、知识深化说明

- **Clara的求解验证**：图片中(f)的解 $X^*=5$ 与上文推导一致，表明虚拟变量法（$\bar{X}+\bar{Y}=14$）严格适用于位移效用函数，且**收入充裕性**（$m=11>$虚拟基础成本 $2+1=3$）确保了无角解。
- **Ambrose的对比价值**：其效用函数展示了 **"非凸偏好"的特殊情况**（准线性），揭示了：
  - 当某商品边际效用恒定时，**价格比决定该商品饱和消费水平**，与Cobb-Douglas中消费比例由价格比决定的逻辑形成对比；
  - 收入增加仅影响非饱和商品（浆果）的消费，这扩展了上文"收入-消费曲线依赖价格比"的讨论维度。

---
### Page/Slide 6



# 【当前图片】微观经济学解析

## 一、图片内容提取

### 图表信息
- **横轴**: Nuts（0–30 单位）
- **纵轴**: Berries（0–20 单位）
- **关键线条**:
  - `Blue line`: 预算线（标注"blue line"，通过点(0,4.5)和(9,0)）
  - `Red curve`: 通过边界点(9,0)的无差异曲线（标注"red curve"）
  - `Pencil line`: 辅助参考线（标注"pencil line"，未参与核心计算）

### 文字内容
- **(f)** Now let us explore a case where there is a “boundary solution.” Suppose that the price of nuts is still 1 and the price of berries is 2, but Ambrose’s income is only 9. Draw his budget line (in blue). Sketch the indifference curve that passes through the point (9,0). What is the slope of his indifference curve at the point (9,0)? **–2/3**.
- **(g)** What is the slope of his budget line at this point? **–1/2**.
- **(h)** Which is steeper at this point, the budget line or the indifference curve? **Indifference curve**.
- **(i)** Can Ambrose afford any bundles that he likes better than the point (9,0)? **No**.

### 公式与关键值
- 无差异曲线斜率（点(9,0)）：**$ -\frac{2}{3} $**
- 预算线斜率：**$ -\frac{p_1}{p_2} = -\frac{1}{2} $**
- 收入约束：**$ m = 9 $**，价格 **$ p_1 = 1 $**（nuts），**$ p_2 = 2 $**（berries）

## 二、图表与上文知识的连续性分析

### 边界解的几何验证
- **核心对比上文原理**：  
  上文强调 **"角解与切点取决于无差异曲线几何特性"**，本图通过Ambrose在低收入（$m=9$）下的行为实证这一原理：  
  - 在点$(9,0)$，$\text{MRS} = -\frac{2}{\sqrt{x_1}} = -\frac{2}{3}$（绝对值$ \frac{2}{3} $），  
    预算线斜率绝对值 $ \frac{p_1}{p_2} = \frac{1}{2} $。  
    由于 **$ \left| \text{MRS} \right| > \frac{p_1}{p_2} $**，无差异曲线比预算线更陡（问题(h)），  
    驱使消费者偏好增加$x_1$，但**预算约束固化边界**（$m=9$仅支持$x_1=9$），促成角解。

- **与上文案例的衔接**：  
  上文Ambrose在$m=24$时为内点解（$\text{MRS} = \frac{p_1}{p_2}$），本图展示**同一效用函数** ($U=4\sqrt{x_1}+x_2$) 在**收入阈值以下**的行为：  
  - 当 $m < \left(\frac{2p_2}{p_1}\right)^2 \cdot p_1 = 16$（$x_1^* = 16$ 的成本），  
    内部解失效，均衡退化为边界点$(m,0)$。  
  - 此现象强化上文结论：**准线性效用的角解源于"偏好驱动消费"与"收入刚性约束"的冲突**，而非无差异曲线形态缺陷。

### 对"最优性"原理的深化
- **区分"可负担性"与"最优性"**：  
  上文Charlie的点$(30,5)$因**可负担性不足**（效用<最大值）被排除，  
  本图点$(9,0)$则因**收入-偏好错配**成为最优：  
  - 效用 $U = 4\sqrt{9} + 0 = 12$ 在可行集内最大（如尝试$(8,0.5)$成本$9$，但$U \approx 11.58 < 12$），  
  - 验证问题(i)的"**No**"——边界点无更优可行束，**角解在此情境下即最优解**。  
  - 此结果呼应上文核心延续：**切点条件仅在内部点适用；角解无需MRS匹配价格，但严格依赖预算约束的几何交点**。

- **收入-消费曲线的临界场景**：  
  上文讨论Ambrose收入增加时坚果消费饱和（$x_1^*=16$），本图补充**低收入临界点**：  
  - 横轴截距 $m = 9 < 16$ 时，收入-消费曲线**完全沿边界移动**（$x_1=m, x_2=0$），  
  - 直至 $m \geq 16$ 才跳转为内部解（$x_1^*=16$）。  
  此动态明确界定上文"无差异曲线几何特性"的作用域——**准线性效用仅在特定收入区间产生内点解**。

## 三、知识逻辑整合
- **框架统一性**：  
  Clara（位移Cobb-Douglas内点解）与本图（准线性角解）共同印证 **"效用最大化统一框架"**：  
  - Clara案例中虚拟变量转换保证内部均衡可行性，  
  - 本图展示当转换后虚拟收入低于基础成本时，**角解成为自然衍生结果**。  
- **教学递进价值**：  
  本图是上文Charlie非最优点$(30,5)$的**逻辑终点**——通过展示**边界点如何从"非可行"（Charlie情境）演变为"最优解"**（本图），  
  系统收束"MRS匹配价格仅适用于内点均衡"的核心原理，避免学生混淆"点不在边界"与"点非最优"的区别。

---
### Page/Slide 7



### 文字与公式提取  
#### 图表元素  
- **坐标轴**:  
  - 横轴: `Score on test 1` (范围 0–120)  
  - 纵轴: `Score on test 2` (范围 0–80)  
- **标注**:  
  - 虚线: `Budget line`  
  - 折线: `“L” shaped indifference curves`  
  - 交点: `a` (预算线与无差异曲线拐点的切点)  

#### 文字与公式  
- **(b)** 无差异曲线拐点线方程: `\( x_1 = x_2 \)`.  
- **(c)** 预算线方程: `\( 10x_1 + 20x_2 = 1,200 \)`.  
- **(d)** 最优点: `\( (x_1, x_2) = (40, 40) \)`.  
- **(e)** 时间分配:  
  - 花 `400` 分钟学习第一次考试 (对应 \( x_1 = 40 \))  
  - 花 `800` 分钟学习第二次考试 (对应 \( x_2 = 40 \))  
- **隐含信息**:  
  - 每单位分数成本: Test 1 需 10 分钟/分, Test 2 需 20 分钟/分.  
  - 总学习时间约束: 1,200 分钟.  

---

### 图表解析：结合上文的连续性分析  
#### 1. **无差异曲线与预算线的几何关系**  
- **L形无差异曲线的含义**:  
  与上文Ambrose的**准线性效用**（凸无差异曲线）不同，本图展示**完全互补偏好**（Leontief效用）。L形无差异曲线表示Nancy仅当 \( x_1 = x_2 \) 时获得最大效用，即两种考试分数必须严格相等（拐点线 \( x_1 = x_2 \)）。  
  - **连续性深化**: 上文强调"切点条件仅在内部点适用"，但本例中**无切点**（因无差异曲线不可微）。最优解直接发生在拐点，而非MRS=价格比的平滑切点。这补充了上文的"角解"逻辑——当偏好非凸时，均衡可能**固化在几何拐点**，而非边界。  

- **预算线斜率与成本结构**:  
  预算线 \( 10x_1 + 20x_2 = 1,200 \) 可化为 \( x_2 = 60 - 0.5x_1 \)，斜率为 \( -1/2 \)。  
  - **对比上文**:  
    - 上文Ambrose案例中预算线斜率（\( -\frac{p_1}{p_2} = -\frac{1}{2} \)）决定角解条件（当 |MRS| > |预算线斜率| 时退化到边界）。  
    - 本图中，**斜率值本身不驱动均衡**，因L形偏好使MRS未定义（拐点处MRS从0跳至∞）。均衡仅由**拐点线与预算线交点**决定（即 \( x_1 = x_2 \) 与 \( 10x_1 + 20x_2 = 1,200 \) 联立）。  
  - **关键差异**: 上文是"收入约束导致边界解"，本图是"偏好结构强制拐点解"；两者共同印证"效用最大化条件必须匹配无差异曲线几何特性"。  

#### 2. **最优点 (40,40) 的经济含义**  
- **最优性验证**:  
  在 \( (x_1, x_2) = (40, 40) \)，时间分配（400分钟 + 800分钟 = 1,200分钟）恰好耗尽预算。  
  - **连续性衔接上文**:  
    - 上文Ambrose在边界点 (9,0) 无法找到更优束（问题(i) "No"），因收入-偏好冲突使内点解不可行。  
    - 本图中，若尝试偏离拐点（如 \( (41,40) \)）：  
      - 成本超支（\( 10 \times 41 + 20 \times 40 = 1,210 > 1,200 \)）  
      - 或效用不增（L形曲线中，非拐点组合 \( x_1 \neq x_2 \) 不提升效用）  
    → 与上文逻辑一致：**当约束与偏好结构绑定时，非切点解仍为严格最优**（无需MRS匹配价格）。  

- **收入-消费路径的临界性**:  
  上文讨论Ambrose在低收入时沿边界移动（\( x_1 = m, x_2 = 0 \)），本图展示**完全互补偏好的收入-消费路径**：  
  - 若总时间低于 800 分钟（如 400 分钟），预算线 \( 10x_1 + 20x_2 = 400 \) 与 \( x_1 = x_2 \) 交于 \( (40/3, 40/3) \)，解存在但分数更低。  
  - **本图贡献**: 明确界定"收入阈值"（本例中 1,200 分钟）下，L形模型如何**取代切点条件**——这是对上文"角解源于收入刚性约束"的互补案例：  
    > 准线性模型（上文）→ 角解由收入不足触发；  
    > 完全互补模型（本图）→ 角解内生于偏好结构，收入仅影响规模。  

#### 3. **教学框架的整合价值**  
- **统一"非切点均衡"理论**:  
  上文Ambrose（准线性）与本图Nancy（Leontief）共同构建**效用最大化框架的全谱**:  
  | 模型类型       | 无差异曲线形状 | 均衡条件               | 本图新增洞见                     |  
  |----------------|----------------|------------------------|----------------------------------|  
  | **准线性** (上文) | 凸曲线         | 内点解需 MRS = p₁/p₂   | 边界解源于收入-偏好错配         |  
  | **Leontief** (本图) | L形拐点        | 拐点解需 \( x_1 = x_2 \) | 拐点解内生于偏好，需几何交点    |  
  - **关键延续**: 上文聚焦"为何边界是最优"，本图解释"为何拐点即最优"，二者合力证明——**当偏好不满足光滑性时，切点条件失效，但预算约束仍主导可行集边界优化**。  
- **避免学生认知陷阱**:  
  上文以非最优内点（Charlie的 (30,5)）警示可负担性陷阱，本图用**可行拐点解**说明：  
  > "无切点" ≠ "非最优" → L形案例中拐点恰是唯一最优，强化上文"角解在此情境下即最优解"的结论。

---
### Page/Slide 8



#### 提取图片内容
##### 文字与公式
- **题目文本**:
  - "for the first examination, her score on this exam will be \( x_1 = m_1 / 5 \). If she spends \( m_2 \) minutes studying for the second examination, her score on this exam will be \( x_2 = m_2 / 10 \)."
  - "(a) On the graph below, draw a 'budget line' showing the various combinations of scores on the two exams that she can achieve with a total of 400 minutes of studying. On the same graph, draw two or three 'indifference curves' for Nancy. On your graph, find the point on Nancy’s budget line that gives her the best overall score in the course."
  - "(b) Given that she spends a total of 400 minutes studying, Nancy will maximize her overall score by achieving a score of \( 80 \) on the first examination and \( 0 \) on the second examination."
  - "(c) Her overall score for the course will then be \( 80 \)."
  - "5.6 (0) Elmer’s utility function is \( U(x,y) = \min\{x, y^2\} \)."
  - "(a) If Elmer consumes 4 units of \( x \) and 3 units of \( y \), his utility is \( 4 \)."
  - "(b) If Elmer consumes 4 units of \( x \) and 2 units of \( y \), his utility is \( 4 \)."
  - "(c) If Elmer consumes 5 units of \( x \) and 2 units of \( y \), his utility is \( 4 \)."
  - "(d) On the graph below, use blue ink to draw the indifference curve for Elmer that contains the bundles that he likes exactly as well as the bundle \( (4, 2) \)."
- **图表标注**:
  - x-axis: "Score on test 1"
  - y-axis: "Score on test 2"
  - Labels: "Preference direction" (arrow), "Max. overall score" (point at (80,0))
- **公式**:
  - \( x_1 = m_1 / 5 \)
  - \( x_2 = m_2 / 10 \)
  - \( U(x,y) = \min\{x, y^2\} \)

##### 图表结构
- **坐标系**: 
  - x-axis: Score on test 1 (0 to 80)
  - y-axis: Score on test 2 (0 to 80)
- **预算线**: 虚线，从 (80, 0) 到 (0, 40)，方程为 \( 5x_1 + 10x_2 = 400 \) 或简化 \( x_1 + 2x_2 = 80 \)。
- **无差异曲线**: 多条实线L形曲线，kink点位于垂直段（表明沿x₁方向的高MRS区域）。
- **关键点**: 
  - 最优解标记于 (80, 0)，标注 "Max. overall score"。
  - 箭头 "Preference direction" 指向右上方，表示效用递增方向。

---

#### 图表解析（结合上文知识点）
##### 预算线斜率与均衡条件
- **预算线方程**：由时间约束导出 \( m_1 + m_2 = 400 \)，代入 \( m_1 = 5x_1 \)、\( m_2 = 10x_2 \) 得 \( 5x_1 + 10x_2 = 400 \)，即 \( x_1 + 2x_2 = 80 \)。斜率为 \( -\frac{1}{2} \)（或 \( \left| \frac{p_1}{p_2} \right| = 0.5 \)），与上文Ambrose案例中预算线斜率 \( -\frac{1}{2} \) 形式一致，但此处 **斜率不驱动均衡**。  
- **关键差异**：上文L形偏好案例（Nancy with 1,200 minutes）中，最优解由拐点线 \( x_1 = x_2 \) 与预算线交点决定；而本图预算线斜率 **触发边界解**——因边际时间成本差异（每单位test 1分数耗时5分钟，test 2耗时10分钟），导致 \( \left| \text{MRS} \right| > 0.5 \) 的区域集中在左端（由L形曲线垂直段体现）。这印证上文逻辑：**当 \( |\text{MRS}| > |\text{预算线斜率}| \) 时，退化到边界解**，而非依赖偏好几何（如L形拐点）。

##### 无差异曲线形态与最优解含义
- **L形曲线的特殊性**：曲线kink点位于垂直段（非对称位置），反映Nancy对test 1的边际效用远高于test 2。与上文完全互补偏好（需 \( x_1 = x_2 \)）不同，此处L形曲线 **未约束内点解**，而是因预算紧张，**唯一可行高MRS区域为垂直段**，迫使均衡退至边界。  
- **最优解 (80, 0) 的经济逻辑**：
  - 能耗尽预算：全部400分钟分配至test 1（\( m_1 = 400 \), \( x_1 = 400 / 5 = 80 \)), test 2无投入。
  - **收入约束主导**：上文Ambrose在低收入时沿 \( x_1 = m, x_2 = 0 \) 移动；本图将此抽象为 **"收入阈值" 现象**——当总时间 < 800 分钟时（本例 400 分钟），无法负担test 2的分数，验证上文"角解源于收入-偏好冲突"。若时间提升至800分钟，预算线外移，可能实现内点解（如上文L形偏好案例）。
  - **非切点最优性**：无差异曲线在 (80,0) 的kink处不可微（MRS未定义），但点位于预算线端点，且任何非零 \( x_2 \) 会降低 \( x_1 \)（如 \( x_2 = 1 \) 时 \( x_1 = 78 \)），效用不增。这强化上文结论：**角解在预算约束紧张时即为严格最优，无需MRS匹配价格**。

##### 与上文知识链的衔接
- **统一"非切点均衡"框架**：  
  | 模型类型       | 预算约束场景 | 均衡条件 | 本图核心洞见 |
  |----------------|--------------|----------|--------------|
  | **上文准线性** | 低收入       | \( x_2 = 0 \) | 边界解由收入不足触发 |
  | **本图L形**    | 紧约束（400分钟） | \( x_2 = 0 \) | 边界解源于偏好-成本错配，但偏好未强制拐点解 |
  
  上文讨论L形偏好（1,200分钟）时收入充足导致**偏好结构驱动**拐点解；本图收入稀缺导致**成本结构驱动**边界解，二者共同说明：**当预算线斜率超过偏好内禀阈值时，收入约束覆盖偏好特性**，使角解成为唯一逻辑均衡。

- **认知陷阱规避**：  
  上文以Charlie的(30,5)警示可负担性陷阱（内点解可行但非最优）；本图（80,0）则直观展示 **"可负担预算线端点即最优"** ——在低收入情境下，角解高效用源于资源分配效率（单位时间test 1边际收益更高），而非无差异曲线属性。这延续上文"为何边界是最优"的讨论，但凸显收入维度的关键作用。

---
### Page/Slide 9



### 提取当前图片中的文字与公式

#### 文字内容
- **页眉与题号**:  
  `NAME ______________ 57`  
  `(e) On the same graph, use blue ink to draw the indifference curve for Elmer that contains bundles that he likes exactly as well as the bundle (1,1) and the indifference curve that passes through the point (16,5).`  
  `(f) On your graph, use black ink to show the locus of points at which Elmer’s indifference curves have kinks. What is the equation for this curve?`  
  `(g) On the same graph, use black ink to draw Elmer’s budget line when the price of x is 1, the price of y is 2, and his income is 8. What bundle does Elmer choose in this situation?`  
  `(h) Suppose that the price of x is 10 and the price of y is 15 and Elmer buys 100 units of x. What is Elmer’s income? (Hint: At first you might think there is too little information to answer this question. But think about how much y he must be demanding if he chooses 100 units of x.)`  
  `5.7 (0) Linus has the utility function U(x,y) = x + 3y.`  
  `(a) On the graph below, use blue ink to draw the indifference curve passing through the point (x,y) = (3,3). Use black ink to sketch the indifference curve connecting bundles that give Linus a utility of 6.`

- **图表标注**:  
  `y` (vertical axis), `x` (horizontal axis),  
  `Blue curves` (label for indifference curves through (1,1)),  
  `Black line` (label for kink locus curve),  
  `Chosen bundle` (label for optimal point),  
  `Blue curve` (label for indifference curve through (16,5)),  
  `Black curve` (label for another indifference curve),  
  ` (16,5) ` (point marked on graph)

#### 公式与数据
- 无差异曲线kink locus方程： **\( x = y^2 \)**  
- 预算线约束： **\( x + 2y = 8 \)** （由 \( p_x=1, p_y=2, \text{income}=8 \) 导出）  
- 最优消费束： **(4, 2)**  
- Elmer的收入计算： **1,150** （当 \( p_x=10, p_y=15, x=100 \) 时）  
- Linus效用函数： **\( U(x,y) = x + 3y \)**

---

### 图表解析（结合上文知识点总结）

#### 图表结构概述
- **坐标轴与数据点**：  
  - x轴范围 [0, 24]，y轴范围 [0, 16]，网格化。  
  - 关键点：  
    - `(16,5)`：标记在“Black curve”上，是高消费束（非预算约束内，因 \(16 + 2 \times 5 = 26 > 8\)）；  
    - `Chosen bundle (4,2)`：预算线与kink locus交点（\(4 + 2 \times 2 = 8\)，满足预算约束）；  
    - `(1,1)`：蓝线无差异曲线通过点（隐含偏好基准）。  
- **曲线类型**：  
  - **Kink locus**：黑线 \( x = y^2 \)（垂直直线？ 根据方程应为抛物线，但图中简化为近似垂直段），代表L形无差异曲线的拐点轨迹；  
  - **无差异曲线**：  
    - 蓝线曲线（`Blue curves`）：通过(1,1)，反映低消费水平的L形偏好（垂直段隐含高MRS）；  
    - 黑线曲线（`Black curve`）：通过(16,5)，显示偏好结构一致性；  
  - **预算线**：虚线，斜率为 \( -\frac{p_x}{p_y} = -\frac{1}{2} \)，与上文**预算线斜率一致**（上文为 \( |\text{斜率}| = 0.5 \)）。

#### 与上文知识链的衔接与变化含义
1. **均衡点的内点解性质**：  
   - 上文强调，当**收入充足时，偏好结构驱动kink点解**（如Nancy在1,200分钟预算下，最优解由 \( x_1 = x_2 \) 与预算线交点决定）。  
   - 本图中，预算线 \( x + 2y = 8 \) 与kink locus \( x = y^2 \) 精确相交于 **(4,2)**，验证上文逻辑：  
     - 解方程 \( y^2 + 2y = 8 \) 得 \( y=2 \)（舍负根），\( x=4 \)；  
     - 此点效用最高，因L形偏好要求最优解必须位于kink（无差异曲线不可微点）。  
   - **关键延续性**：本图直接示例上文所述的“收入-偏好协调场景”——当预算约束覆盖偏好阈值（e.g., 收入8 > 阈值），**内点kink解成为均衡**，而非边界解。这与上文“Nancy with 1,200 minutes”案例同构，强化“收入充足时偏好主导均衡”的结论。

2. **预算线斜率与均衡条件**：  
   - 预算线斜率 \( -\frac{1}{2} \) 与上文**完全一致**（上文 \( x_1 + 2x_2 = 80 \) 斜率为 \( -0.5 \)），但此处**斜率未触发边界解**。  
     - 原因：kink locus \( x = y^2 \) 在(4,2)处的“隐含MRS”与价格比匹配（L形偏好在拐点处MRS跳跃，但价格比适配其垂直段）。  
   - 对比上文边界解案例（最优在(80,0)）：  
     - 上文因收入稀缺（400分钟 < 800分钟阈值），成本结构（ \( p_{x_1}/p_{x_2} = 0.5 \) ）使 \( |\text{MRS}| > 0.5 \) 成立，退化为边界解；  
     - 本图收入8虽小，但偏好阈值更低（kink locus更陡峭），使预算线与kink点相交，**避免边界解**。  
   - **深化认知**：本图证明上文框架的普适性——均衡类型由**收入水平与偏好阈值的相对位置**决定，预算线斜率仅提供约束条件。

3. **最优解的经济含义**：  
   - **(4,2)的严格最优性**：  
     - 处于预算线与kink locus切点，效用不可提升（任何偏离如 \( (3,2.5) \) 违反L形偏好凸性）；  
     - 反驳“可负担性陷阱”：上文警告内点解可行但非最优（如Charlie的(30,5)），但本图中(4,2)是**唯一逻辑均衡**，因偏好强制kink为最优。  
   - **收入维度的作用**：  
     - 若收入降至4，预算线 \( x + 2y = 4 \) 与 \( x = y^2 \) 无正交点（ \( y^2 + 2y -4=0 \) 解为负），将退化为边界解（如上文(80,0)）；  
     - 这直接验证上文“**收入阈值**”理论：本例收入8恰好触达kink点，是内点解存在的最低阈值。

#### 与上文知识链的统一框架
| 场景                | 预算约束强度 | 均衡类型      | 关键驱动因素       | 本图启示                  |
|---------------------|--------------|---------------|--------------------|--------------------------|
| 上文边界解 (Nancy)  | 紧张 (400分钟) | 边界解 (80,0) | 收入-成本冲突      | 收入不足时，偏好结构被覆盖 |
| 本图内点解 (Elmer)  | 临界 (income=8) | kink解 (4,2) | 偏好-收入协调      | 收入达标时，偏好精确主导 |

- **核心延续性**：本图实证上文核心结论——**非切点均衡的根源在于预算-偏好互动**。当收入大于偏好阈值（本例收入≥8），即使预算线斜率相同，kink解替代边界解；反之则回归角点。这消解了“偏好决定一切”的误区，凸显**收入作为均衡分类器**的作用。

---
### Page/Slide 10



### 图表与文字提取  
#### 文字提取  
- 页眉：`58 CHOICE (Ch. 5)`  
- 图表标注：  
  - `Y` (纵轴)  
  - `X` (横轴)  
  - `Red line` (箭头指向点 `(3,3)`)  
  - `Black curve` (箭头指向曲线)  
  - `Blue curve` (箭头指向曲线)  
- 下方文本：  
  - `(b) On the same graph, use red ink to draw Linus’s budget line if the price of x is 1 and the price of y is 2 and his income is 8. What bundle does Linus choose in this situation? (0,4).`  
  - `(c) What bundle would Linus choose if the price of x is 1, the price of y is 4, and his income is 8? (8,0).`  
  - `5.8 (2) Remember our friend Ralph Rigid from Chapter 3? His favorite diner, Food for Thought, has adopted the following policy to reduce the crowds at lunch time: if you show up for lunch t hours before or after 12 noon, you get to deduct t dollars from your bill. (This holds for any fraction of an hour as well.)`  

#### 公式与关键点  
- **预算约束 (b)**：\( x + 2y = 8 \)（斜率 \( -\frac{p_x}{p_y} = -0.5 \)，与上文一致）  
- **预算约束 (c)**：\( x + 4y = 8 \)  
- **关键点**：`(3,3)`（图表中标注）  
- **均衡选择**：  
  - (b) 中 LDL 均衡：`(0,4)`  
  - (c) 中 LDL 均衡：`(8,0)`  

### 图表解析与上文知识链衔接  
#### 1. **图表结构与均衡含义**  
- **Blue curve** 和 **Black curve** 延续上文：  
  - Blue curve 通过 `(1,1)`，反映低消费水平的 L 形偏好（垂直段隐含高 MRS）；  
  - Black curve 通过 `(16,5)`，体现偏好结构的一致性，与上文 **偏好结构驱动均衡** 的逻辑同构。  
- **`Red line` 与点 `(3,3)`**：  
  - 图表中 `Red line` 标注指向 `(3,3)`，结合 (b) 题要求绘制预算线，可推断 `(3,3)` 是 Linus 偏好的 **kink locus 临界点**（kink 点）。  
  - 对于预算线 \( x + 2y = 8 \)，点 `(3,3)` 的成本为 \( 1 \times 3 + 2 \times 3 = 9 > 8 \)，**不可行**。这直接印证上文 **“收入阈值理论”**：  
    - 若收入低于 kink 点成本（本例阈值为 9），预算线无法覆盖偏好阈值；  
    - 导致 **边界解出现**（此处选择 `(0,4)`），与上文 Nancy 在 400 分钟案例（收入稀缺）逻辑一致。  

#### 2. **预算线斜率与均衡变化的含义**  
- **预算线斜率 \( -0.5 \) 的未触发效应**：  
  - 与上文 Elmer 案例（相同预算线 \( x + 2y = 8 \)）对比：  
    - Elmer 因 kink locus \( x = y^2 \) 与预算线精确交于 `(4,2)`（成本 = 8），实现 **内点 kink 解**；  
    - Linus 因 kink locus 位于更高消费水平（成本 = 9 > 8），预算线 **无法触及 kink 点**，退化为 **边界解 `(0,4)`**。  
  - **突破性解释**：预算线斜率本身不决定均衡类型，而是 **收入-偏好阈值相对位置** 的函数。收入不足时，即使价格比适配，偏好结构仍被预算约束覆盖（强化上文“收入作为均衡分类器”结论）。  

- **价格变化 (c) 的对比分析**：  
  - 当 \( p_y \) 升至 4（预算线 \( x + 4y = 8 \)，斜率 \( -0.25 \)），Linus 选择 `(8,0)`：  
    - kink 点 `(3,3)` 成本升至 \( 1 \times 3 + 4 \times 3 = 15 > 8 \)，收入进一步低于阈值；  
    - **偏好结构失效**，解切换至另一边界点（类似上文 Nancy 案例中价格比引发边界解）。  
  - **核心延续性**：本例验证上文统一框架——当 **收入 < 偏好阈值成本**，无论价格比如何，边界解必然出现；当收入 ≥ 阈值（如 Elmer 案例），偏好才主导内点解。  

#### 3. **经济含义深化**  
- **`(0,4)` 与 `(8,0)` 的严格边界特性**：  
  - 均衡点位于预算线端点，效用受资源约束最大化；但若存在可行 kink 点（如 Elmer 的 `(4,2)`），边界解存在 **无谓损失**（如 Linus 无法达到 `(3,3)` 的潜在效用）。  
  - 反驳“偏好唯一决定论”：Linus 与 Elmer 有相似 L 形偏好萌芽（图表中存在 Blue/Black 曲线），但 **收入阈值差异** 导致完全相反的均衡结果。  
- **阈值成本的作用**：  
  - Linus 临界收入阈值为 9（kink 点成本），而 Elmer 为 8（`x=y^2` 在 `(4,2)` 成本）；  
  - 当收入 = 8，Linus 处于 **阈值下方（边界解）**，Elmer 处于 **阈值上方（内点解）**。这量化上文模糊表述，证明 **“偏好阈值”需用成本衡量而非抽象水平**。  

#### 知识链精炼总结  
| 场景                | 预算约束强度 | 均衡类型 | 关键差异                 | 本图贡献                             |  
|---------------------|--------------|----------|--------------------------|--------------------------------------|  
| 上文 (Elmer)       | 充足 (I=8)   | 内点解   | kink locus 成本 = 8      | 展示临界协调场景                     |  
| **本图 (Linus)**   | **不足 (I=8)** | **边界解** | **kink locus 成本 = 9 > 8** | **验证阈值成本量化，凸显收入刚性约束** |  

- **连续性结论**：本图以具体数值量化上文理论——**边界解发生当且仅当收入 < kink locus 成本**（\( I < p_x \cdot a + p_y \cdot b \)，其中 `(a,b)` 为 kink 点）。消除了“收入充足”的模糊性，完善预算-偏好互动框架。

---
### Page/Slide 11



# 图表详细解析

## 1. 文字与公式提取

### 图表部分
- 顶部标签：`NAME _______________ 59`
- 纵轴标签：`Money`（刻度0-20）
- 横轴标签：`Time`（刻度10-2点）
- 图例文字：`Red curves`、`Blue budget set`

### 文本问题部分
- **(a)** Use blue ink to show Ralph's budget set. On this graph, the horizontal axis measures the time of day that he eats lunch, and the vertical axis measures the amount of money that he will have to spend on things other than lunch. Assume that he has $20 total to spend and that lunch at noon costs $10. (Hint: How much money would he have left if he ate at noon? at 1 P.M.? at 11 A.M.?)
- **(b)** Recall that Ralph's preferred lunch time is 12 noon, but that he is willing to eat at another time if the food is sufficiently cheap. Draw some red indifference curves for Ralph that would be consistent with his choosing to eat at 11 A.M.
- **5.9 (0)** Joe Grad has just arrived at the big U. He has a fellowship that covers his tuition and the rent on an apartment. In order to get by, Joe has become a grader in intermediate price theory, earning $100 a month. Out of this $100 he must pay for his food and utilities in his apartment. His utilities expenses consist of heating costs when he heats his apartment and air-conditioning costs when he cools it. To raise the temperature of his apartment by one degree, it costs $2 per month (or $20 per month to raise it ten degrees). To use air-conditioning to cool his apartment by a degree, it costs $3 per month. Whatever is left over after paying the utilities, he uses to buy food at $1 per unit.

## 2. 图表变化含义解析

### 预算集特征解读
- **Blue budget set（蓝色预算集）** 实际为Ralph面临的预算约束区域，其形状表明：
  - 在12点（12:00）吃午餐时，剩余消费金额为$10（总预算$20 - $10午餐费）
  - 在11点左右吃午餐时，剩余消费金额达到局部最大值
  - 预算边界呈现**非线性U型**，表示**时间-价格替代效应**

-关键经济特征**：横轴不同时间点对应不同的午餐价格，这与上文 "kink locus" 概念形成映射：
  - 12:00 是Ralph的**偏好临界点**（类比Linus的(3,3)点）
  - 实际选择11:00表明**价格敏感度**导致需求点偏离偏好核心

### 红色无差异曲线解析
- **Red curves** 展示了Ralph在时间-金钱维度上的偏好结构：
  - 无差异曲线在12:00附近呈现**凸起特征**，标识该点为**偏好峰值**（对应上文描述的"偏好结构"）
  - 曲线**向11:00侧倾斜**，说明在较低午餐价格（较高剩余资金）时，消费者愿意偏离心仪时间
  - 这验证了上文的**收入-偏好阈值理论**：当偏离偏好核心能获取更高剩余消费能力时，消费者会接受替代选择

### 与上文知识链的联系
1. **预算约束强度分析**：
   - 图中预算集最高点低于20（约16-17），表明**时间-价格组合**导致实际可支配收入不足
   - 这与上文Linus案例中 **收入 < kink locus成本（9）** 直接对应：$20总预算中，满足偏好核心(12:00)需要支付$10，但其他时间可能只需支付$8-$9

2. **边界解形成的机制**：
   - Ralph选择11:00而非12:00，属于**替代边界解**（非端点边界解）
   - 此现象印证上文结论：**预算约束使偏好"折叠"**。类似Linus无法触及kink点(3,3)，Ralph因价格因素不能实现偏好峰值

3. **收入-偏好互动的新维度**：
   - 此案例引入**时序价格歧视**，将上文二维选择扩展至时间维度
   - 价格的时序差异强化了 "kink locus成本" 的概念：12:00对应的等效成本 = $10 > 其他时间成本
   - 当剩余资金（纵轴增加值）超过特定阈值，消费者即放弃偏好核心（如选择11:00），与上文"收入阈值"理论完全一致

### 数值验证逻辑
基于问题提示：
- 中午吃午餐后剩余：$20 - $10 = $10
- 1PM吃午餐剩余：通过图中预算边界，估计约$11-$12
- 11AM吃午餐剩余：约$14，印证"食物更便宜"
- 将使选择11AM，当且仅当：$U(11AM, $14) > $U(12PM, $10)$

这构成上文具体化应用——**当非偏好点的剩余资金使其效用超过偏好点时，边界解（11AM）取代内点解（12PM）**，精确验证"收入-偏好阈值相对位置决定均衡类型"的核心命题。

---
### Page/Slide 12



# 温度-食物消费选择模型解析

## 1. 提取图片内容

### 文字与公式
- **图表标注**：Food(纵轴0-120), Temperature(横轴0-100), December, September, August, Blue budget constraint, Black budget constraint, Red budget constraint
- **问题描述**：
  - (a) 9月室内初始温度60度：无加热/冷却 → $100食物；加热至70度 → $80食物；冷却至50度 → $70食物
  - (b) 12月室外温度30度，8月室外温度85度
  - (c) 要求绘制满足以下条件的无差异曲线：
    - (i) 无成本时最佳温度65度
    - (ii) 12月选择加热，8月选择制冷，9月无调节
    - (iii) 12月比8月状况更好
  - (d) 斜率相等月份：**August and December**

### 隐含公式
- **加热成本**：10度温差 = $20 → $2/度
- **冷却成本**：10度温差 = $30 → $3/度
- **预算约束方程**：
  - 加热区域：Food = 100 - 2(T - 60) (T ≥ 60)
  - 冷却区域：Food = 100 - 3(60 - T) (T ≤ 60)

## 2. 图表变化含义解析

### 预算约束的多重折点特征
- **黑色预算线(9月)** 明确展示**双斜率预算约束**：
  - 60度为**自然温度点**（无调节成本）
  - 右侧(T>60)：斜率为-2（加热成本低）
  - 左侧(T<60)：斜率为-3（冷却成本高）
  - 此折点构成**kink locus**，与上文Linus案例中的(3,3)点概念同源

- **蓝色预算线(12月)** 偏向左侧：
  - 30度室外低温导致**加热需求增加**
  - 预算线始于低温区域，验证"温度外部冲击对预算集偏移"理论
  - 比9月预算线左移，表明**寒冷月份等效收入下降**（需额外支出维持适宜温度）

- **红色预算线(8月)** 偏向右侧：
  - 85度室外高温导致**冷却需求增加**
  - 预算线始于高温区域，成本结构与加热对称
  - 8月预算线位置低于12月，体现**高温环境的更高调节成本**

### 与上文知识链的精准对接
1. **非线性预算约束形成机制**：
   - 本图替代上文的"时间-价格"维度为"温度-食物"维度
   - 9月预算线在60度处的转折（kink）直接对应上文"偏好临界点"概念
   - **关键发现**：不同温度调节方向的单元成本差异($2 vs $3)导致预算集边界的"不对称折叠"

2. **边界解的形成逻辑**：
   - 题目(c)(ii)要求"12月用炉子，8月用空调，9月无调节"，印证**角点解形成条件**：
     - 12月：室外30℃ → 自然温度低于理想值 → 必须加热
     - 8月：室外85℃ → 自然温度高于理想值 → 必须制冷
     - 9月：初始60℃接近理想65℃ → 预算集的转折点成为最优选择
   - 这验证了上文"预算约束使偏好折叠"的核心机制

3. **收入-偏好交互的新实证**：
   - 题目(c)(iii)"12月比8月状况更好"揭示：
     - 相同名义收入$100在不同环境的实际购买力差异
     - **温度禀赋价值**：寒冷环境调节成本较低（$2/度 < $3/度）
   - 直接应用上文"收入阈值"理论：同等支出下，12月获得的效用更高

### 数值验证框架
- **9月预算验证**：
  | 温度变化 | 成本  | 剩余食物 |
  |----------|-------|----------|
  | 60→70(↑) | $20   | $80      |
  | 60→50(↓) | $30   | $70      |

- **季节性对比**：
  - 12月预算线在低价调节区（加热）延伸更远 → **寒冷月份预算效率更高**
  - 8月预算线在高价调节区（冷却）被压缩 → **高温月份实际可支配收入减少**

### 均衡条件深化说明
题目(d)指出**8月和12月**预算线斜率等于无差异曲线斜率，表明：
- 这两个月存在**内点解**（消费者同时选择温度调节和食物）
- 与上文"边界解"形成互补：9月因自然温度接近理想值而成为**角点解**
- 验证"预算约束的相对位置决定均衡类型"理论：
  - 当外部温度远离理想值 → 内点解
  - 当外部温度接近理想值 → 角点解

此案例完美展示上文理论框架对**多维约束系统**的适用性，证实消费者选择理论在不同维度（时间/温度）下的一致性。

---
### Page/Slide 13



### 当前图片内容提取

#### 文字与公式
- **(e)** In December Joe’s marginal rate of substitution between food and degrees Fahrenheit is **-2**. In August, his MRS is **3**.  
- **(f)** Since Joe neither heats nor cools his apartment in September, we cannot determine his marginal rate of substitution exactly, but we do know that it must be no smaller than **-2** and no larger than **3**. (Hint: Look carefully at your graph.)  
- **5.10 (0)** Central High School has $60,000 to spend on computers and other stuff, so its budget equation is **$C + X = 60,000$**, where $C$ is expenditure on computers and $X$ is expenditures on other things. C.H.S. currently plans to spend $20,000$ on computers.  
  - **Plan A**: This plan would give a grant of $10,000$ to each high school in the state that the school could spend as it wished.  
  - **Plan B**: This plan would give a $10,000$ grant to any high school, so long as the school spent at least $10,000$ more than it currently spends on computers. Any high school can choose not to participate, in which case it does not receive the grant, but it doesn’t have to increase its expenditure on computers.  
  - **Plan C**: Plan C is a “matching grant.” For every dollar’s worth of computers that a high school orders, the state will give the school 50 cents.  
  - **Plan D**: This plan is like plan C, except that the maximum amount of matching funds that any high school could get from the state would be limited to $10,000$.  
- **(a)** Write an equation for Central High School’s budget if plan A is adopted. **$C + X = 70,000$**. Use black ink to draw the budget line for Central High School if plan A is adopted.  
- **(b)** If plan B is adopted, the boundary of Central High School’s budget set has two separate downward-sloping line segments. One of these segments describes the cases where C.H.S. spends at least $30,000$ on computers. This line segment runs from the point **$(C,X) = (70,000, 0)$** to the point **$(C,X) = (30,000, 40,000)$**.  
- **(c)** Another line segment corresponds to the cases where C.H.S. spends less than $30,000$ on computers. This line segment runs from **$(C,X) = (30,000, 30,000)$** to the point **$(C,X) = (0, 60,000)$**. Use red ink to draw these two line segments.  

#### 关键公式与坐标
- 基础预算方程：$C + X = 60,000$  
- Plan A 预算方程：$C + X = 70,000$  
- Plan B 线段坐标：  
  - 高支出段（$C \geq 30,000$）：起点 $(70,000, 0)$, 终点 $(30,000, 40,000)$  
  - 低支出段（$C < 30,000$）：起点 $(30,000, 30,000)$, 终点 $(0, 60,000)$  

---

### 图表变化含义解析（基于文本描述）

#### (e) 和 (f) 部分：MRS 数值与上文理论的实证验证
- **含义深化**：  
  上文知识点指出，12月和8月预算约束斜率与无差异曲线斜率相等（即内点解条件），直接表现为 (e) 中 MRS 的精确数值。  
  - **12月 MRS = -2**：匹配上文加热区域预算约束斜率（$d\text{Food}/dT = -2$），验证寒冷月份（室外30°）的内点解存在。消费者在加热调节中平衡食物与温度，表明 **预算线斜率主导边际替代率**，符合上文“斜率相等月份”结论。  
  - **8月 MRS = 3**：匹配冷却区域预算约束斜率（$d\text{Food}/dT = 3$，因 $T \leq 60$ 时 Food 增随 T 增），验证高温月份（室外85°）的内点解。**3 > | -2 |** 的斜率差异，印证上文“高温调节成本更高”，导致8月预算线更陡、实际购买力更低。  
  - **9月 MRS 介于 -2 和 3 之间**（f）：反映上文“自然温度60°处无调节”的角点解。MRS 落入预算约束转折点的斜率区间（[ -2, 3 ]），使消费者选择折点而非内点，强化了 **“边界解形成的关键是偏好与约束的斜率匹配”** 这一上文核心机制。  

  此实证数据为上文“非线性预算约束决定均衡类型”提供量化解析：当外部温度使最优解远离自然点（12月/8月），内点解成立；当接近自然点（9月），角点解收敛。

#### 5.10 部分：学校预算约束与上文知识点的延伸拓展
当前问题以 **政策冲击**（赠款计划）重构预算集，延续上文“非线性预算约束”框架，但将维度转换为 **$(C, X)$ 空间**（计算机支出 vs 其他支出），凸显理论普适性。

- **Plan A：收入效应的经典案例**  
  - 预算线外移至 $C + X = 70,000$，斜率维持 -1，体现 **无条件转移等价于名义收入增加**。  
  - **与上文衔接**：类比上文12月预算线左移，但此处为扩张（因外部冲击为收入增益）。验证上文“实际购买力变化”理论——若学校偏好均衡点 $C=20,000$，Plan A 使食谱扩张（类似食物预算增加），但无结构变化，**不生成折点**，故通常为内点解。

- **Plan B：非线性约束的突变点与决策逻辑**  
  - **预算线转折机制**：  
    - 低支出段（$C < 30,000$）：无赠款，预算约束 $C + X = 60,000$（斜率 -1），对应上文“自然状态”（如9月60°）。  
    - 高支出段（$C \geq 30,000$）：获 $10,000$ 赠款，预算约束 $C + X = 70,000$（斜率 -1），但**与低段在 $C=30,000$ 处形成垂直跳跃**（从 $X=30,000$ 到 $X=40,000$）。  
    - **核心特征**：虽两段斜率相同（-1），但**跳跃幅度创造等效转折点**，使预算边界在 $(30,000, 30,000)$ 与 $(30,000, 40,000)$ 间“断裂”。  
  - **与上文深度类比**：  
    | **维度**       | 上文（温度-食物）                     | 5.10 (Plan B)                     |  
    |----------------|-------------------------------------|----------------------------------|  
    | **转折触发**   | 介质成本不对称（加热 $2/°$ vs 冷却 $3/°$） | 政策条件（支出增 $10,000$ 才获赠款） |  
    | **转折点**     | $T=60°$（自然温度）                | $C=30,000$（临界支出）         |  
    | **约束变化**   | 斜率突变（-2 → +3）                | 水平跳跃（X 跳升 $10,000$）     |  
    | **均衡影响**   | 9月角点解（MRS ∈ [-2,3]）         | 可能导致角点解（若 MRS = ±∞ 或 连续偏好中断） |  
    **关键延续**：Plan B 的“跳跃”等价于上文“kink locus”，但以 **离散转移** 替代连续斜率变化。若学校偏好使 MRS 在 $C=30,000$ 处趋近无限，将出现角点解（如学校恰好花 $30,000$ 以获赠款），验证上文“预算约束折叠偏好”的一般原理。  
  - **决策洞见**：当前支出 $C=20,000$ 低于临界点，学校若选择 $C \geq 30,000$（如 $C=30,000$）可获额外 $10,000$ X，**扭转载体效应**——非价格变化却改变可行集形状，类似上文外部温度冲击对预算轨迹的偏移。

- **隐含拓展：Plan C/D 与预算曲率**  
  （虽未在文本中详述，但问题提及）  
  - Plan C 使预算线变平（$X = 60,000 - 0.5C$，斜率 -0.5），类似上文“低成本调节区”（如12月右侧加热区斜率 -2）。匹配财政协同 **压缩相对价格差异**，提升计算机消费诱因。  
  - Plan D 引入上限，创建“二次转折点”，完善上文“多阶非线性约束”模型——例如当 $C>20,000$ 时，斜率回至 -1，形成两阶段 kink，**强化政策设计中约束复杂度对行为的影响**。

#### 知识连续性结论
- 本图片通过 **(e)/(f) 的 MRS 量化** 和 **5.10 的政策性预算重构**，验证上文三大机制：  
  1. **内点/角点解的判别**：基于 MRS 与预算斜率（上文 d）及 MRS 区间（扩展 f）的匹配。  
  2. **约束结构主导可行集**：Plan B 的跳跃式转折点与上文温度转折点同源，证明环境或政策造成的 **“非线性折叠”** 是普遍消费者选择框架。  
  3. **外部冲击的等效收入效应**：12月/8月天气差异 vs Plan A/B 收入变化，统一于“实际购买力”分析（上文“温度禀赋价值”延伸至政策禀赋）。  
- 此案例将维度从 **温度-食物** 拓展至 **支出组合-政策干预**，但核心逻辑一致：**预算约束的几何特征（折点、斜率、跳跃）始终是推导需求均衡的首要决定因素**，为宏观政策设计（如匹配赠款）提供微观基础。

---
### Page/Slide 14



### 当前图片解析

#### 1. 提取文字与公式
**文字内容：**
- 页眉：`62 CHOICE (Ch. 5)`
- (d)：*If plan C is adopted and Central High School spends $C$ dollars on computers, then it will have $X = 60,000 - 0.5C$ dollars left to spend on other things. Therefore its budget line has the equation $0.5C + X = 60,000$. Use blue ink to draw this budget line.*
- (e)：*If plan D is adopted, the school district’s budget consists of two line segments that intersect at the point where expenditure on computers is $20,000$ and expenditure on other instructional materials is $50,000$.*
- (f)：*The slope of the flatter line segment is $-0.5$. The slope of the steeper segment is $-1$. Use pencil to draw this budget line.*
- 图表坐标轴：  
  - `Thousands of dollars worth of computers` (横轴，0–60)  
  - `Thousands of dollars worth of other things` (纵轴，0–60)  
- 图注：  
  - `Black budget line (plan A)`  
  - `Blue budget line (plan C)`  
  - `Pencil budget line (plan D)`  
  - `Red budget line (plan B)`  
- 底部文字：`5.11 (0) Suppose that Central High School has preferences that can be represented by the utility function $U(C,X) = CX^2$. Let us try to determine how the various plans described in the last problem will affect the amount that C.H.S. spends on computers.`

**公式：**
- Plan C 预算方程：$0.5C + X = 60,000$ 或等价形式 $X = 60,000 - 0.5C$  
- Plan D 关键参数：  
  - 转折点坐标：$(C, X) = (20,000,\ 50,000)$（即图中 $(20, 50)$ 位）  
  - 较平缓段斜率：$-0.5$  
  - 较陡峭段斜率：$-1$  

---

#### 2. 图表分析（结合上文知识点总结）
上文已系统化归纳预算约束的几何特征对均衡选择的影响，本图片通过 **Plan C 与 Plan D 的预算线显式对比**，深化了对“非线性约束如何扭曲可行集”的验证。以下聚焦图片中**新增可量化信息**（Plan C 和 Plan D 的具体结构），避免重复上文对 Plan A/B 的结论。

##### **Plan C 预算线（蓝线）：相对价格压缩与消费诱因**
- **几何特征**：  
  方程 $0.5C + X = 60,000$ 对应斜率 $-0.5$，比基准线（Plan A，斜率 $-1$）更平缓。当 $C=0$ 时 $X=60,000$；$C=60,000$ 时 $X=30,000$（图中纵轴截距为 60，横轴 60 处纵坐标为 30）。  
- **经济含义**：  
  - 斜率 $-0.5$ 体现 **计算机相对价格下降**（原每单位计算机需放弃 1 单位其他支出，现仅放弃 0.5 单位），直接匹配上文隐含拓展中“财政协同压缩相对价格差异”的机制。  
  - 与上文温度-食物模型类比：此结构等价于 **12 月右侧加热区斜率 $-2$ 的简化版**（上文 d 部分），即政策主动 **降低特定商品隐含成本**，通过扭曲价格信号显著提升计算机消费占比。  
  - *关键延续*：若学校偏好对计算机边际替代率（MRS）在 $-0.5$ 附近，内点解将向 **计算机消费增益** 移动——呼应上文“预算约束几何特性决定需求均衡”的核心逻辑。

##### **Plan D 预算线（铅笔线）：二次转折点与政策上限效应**
- **几何特征**：  
  - 由两段组成，**转折点严格锁定于 $(20, 50)$**（对应 $C=20,000$, $X=50,000$）。  
  - 低支出段（$C < 20,000$）：斜率 $-0.5$（图中左侧较平缓段），从 $(0,60)$ 延伸至 $(20,50)$。  
  - 高支出段（$C \geq 20,000$）：斜率 $-1$（图中右侧较陡峭段），从 $(20,50)$ 延伸至 $(60,10)$。  
- **经济含义**：  
  - **二次转折点的突变逻辑**：  
    - 低支出段斜率 $-0.5$ 体现政策 **对初期计算机消费的补贴**（类似 Plan C 机制），但当支出突破 $C=20,000$ 时，相对价格回弹至 $-1$，形成 **政策上限的硬约束**。  
    - 这验证了上文“多阶非线性约束”模型（Plan D 隐含拓展）：预算边界在临界点处发生 **斜率突变而非跳跃**，与 Plan B 的垂直跳跃（上文 5.10 部分）形成对比，但同属 **预算线折叠偏好的一般化表现**。  
  - **决策影响**：  
    - 若学校无差异曲线在 $C=20,000$ 处 MRS 落在 $[-1, -0.5]$ 区间，将出现 **角点解**（上文 f 部分 MRS 量化逻辑），引致对计算机支出的“挤出效应”——在 $C \geq 20,000$ 时，额外支出将面临更高机会成本。  
    - 与上文温度模型深度呼应：此结构类比 **季节变换触发的双阶段约束调整**（如 9 月降温后斜率突变），但此处由 **政策阈值驱动**，强化“外部规则可主动构造消费瓶颈”的结论。

##### **整体图表的关键验证作用**
- **与上文知识链衔接**：  
  图片通过精确坐标和斜率标注，将 **上文抽象理论转化为可操作图形**：  
  - Plan C 的斜率 $-0.5$ → 量化“低成本调节区”的有效强度；  
  - Plan D 的 $(20,50)$ 转折点 → 完整映射“政策上限”如何拆分约束，替代上文仅限于 $C=30,000$ 的单一跳跃（Plan B）。  
- **对均衡分析的启示**：  
  结合底部效用函数 $U(C,X)=CX^2$，预算线的**凸性畸变**（Plan D 的分段斜率）将直接改变最优解位置：  
  - 若 MRS 在 $C<20,000$ 时 $|MRS| > 0.5$，则沿平缓段解出内点；  
  - 若 MRS 跳跃至 $C \geq 20,000$ 时 $|MRS| < 1$，则触发角点解（$C=20,000$）。  
  这完备印证了上文“约束结构主导可行集”的原理——政策设计中，**预算线拐点数量及斜率梯度** 比名义收入变化更能精准操控需求分布。

> 注：Plan B（红虚线）在图中仅示意性展示，其细节（$C=30,000$ 处垂直跳跃）已全面纳入上文 5.10 分析，故此处不重复；Plan A 作为基准线亦无需赘述。本图核心价值在于 **将 Plan C/D 的微观约束参数显式化**，为后续效用计算提供精确几何依据。

---
### Page/Slide 15



### 1. 图片文字与公式提取  
#### **问题与答案**  
- **(a)** If the state adopts none of the new plans, find the expenditure on computers that maximizes the district’s utility subject to its budget constraint.  
  **$20,000$**  
- **(b)** If plan A is adopted, find the expenditure on computers that maximizes the district’s utility subject to its budget constraint.  
  **$23,333$**  
- **(c)** On your graph, sketch the indifference curve that passes through the point $(30,000, 40,000)$ if plan B is adopted. At this point, which is steeper, the indifference curve or the budget line?  
  **The budget line**  
- **(d)** If plan B is adopted, find the expenditure on computers that maximizes the district’s utility subject to its budget constraint. (Hint: Look at your graph.)  
  **$30,000$**  
- **(e)** If plan C is adopted, find the expenditure on computers that maximizes the district’s utility subject to its budget constraint.  
  **$40,000$**  
- **(f)** If plan D is adopted, find the expenditure on computers that maximizes the district’s utility subject to its budget constraint.  
  **$23,333$**  

#### **附加题目（5.12）**  
- **(0)** The telephone company allows one to choose between two different pricing plans:  
  - **Plan 1:** \$12/month fixed fee + unlimited local calls.  
  - **Plan 2:** \$8/month fixed fee + \$0.05 per call. Total budget = \$20/month.  
- **(a)** Budget lines for both plans cross at **$(80, 8)$**.  

---

### 2. 关键数据与上文知识点的衔接  
#### **(e) Plan C 的 40,000：相对价格压缩的量化验证**  
- **与上文的衔接**：  
  - 上文指出 Plan C 的预算线斜率 $-0.5$ 对应 **计算机相对价格压缩**（放弃 0.5 单位其他支出即可获得 1 单位计算机）。  
  - 本题答案 $C=40,000$ 直接验证了这一机制：在效用函数 $U=CX^2$ 下，边际替代率 $MRS = \frac{X}{2C}$ 需等于相对价格 $0.5$（即 $MRS = 0.5$）。  
  - 代入预算约束 $0.5C + X = 60,000$，解得 $C=40,000$，表明 **价格信号扭曲显著提升了计算机消费**（较基准 Plan A 的 $23,333$ 增加 71%）。  
  - *延续性*：印证上文结论——当 $MRS$ 接近预算线斜率时，内点解向高计算机消费移动。  

#### **(f) Plan D 的 23,333：政策上限效应的动态均衡**  
- **与上文的衔接**：  
  - 上文强调 Plan D 在 $C=20,000$ 处存在 **斜率突变**（低支出段 $-0.5$ → 高支出段 $-1$），构成 **政策上限硬约束**。  
  - 本题答案 $C=23,333$ 位于 **高支出段**（$C > 20,000$），说明：  
    - 尽管低支出段提供补贴（斜率 $-0.5$），但效用函数 $U=CX^2$ 导致 $MRS$ 在高支出段仍满足最优条件（$MRS = 1$，即 $X=2C$）。  
    - 代入高支出段预算线 $C + X = 70,000$（由转折点 $(20,50)$ 推导），解得 $C=23,333$，体现 **补贴失效后的均衡回弹**。  
  - *延续性*：验证上文“**斜率梯度比名义收入更能操控需求分布**”——政策阈值虽设在 $C=20,000$，但最优解仍突破该点，反映补贴强度不足以维持低机会成本优势。  

#### **(c) 与 (d) 的补充链接**  
- **(c)** 的答案“**预算线更陡峭**”对应上文 Plan B 的 **垂直跳跃约束**（$C=30,000$ 处），表明不可行集导致无差异曲线无法在该点相切。  
- **(d)** 的 $C=30,000$ 为 Plan B 的角点解，进一步佐证上文“**单一跳跃约束将消费锁定在临界值**”的结论。  

---

### 3. 对效用函数与政策设计的深化启示  
- **效用函数 $U=CX^2$ 的关键作用**：  
  - 该函数确保 $MRS$ 随 $C$ 增加而下降（$MRS = X/(2C)$），使 Plan D 的 **高支出段内点解成为可能**（若 $MRS$ 递减速度过快，则可能在 $C=20,000$ 触发角点解）。  
- **政策设计验证**：  
  - Plan C 的 $40,000$ 与 Plan D 的 $23,333$ 对比，直观体现 **非线性约束的差异化效果**：  
    - 单一斜率压缩（Plan C）可最大化刺激消费；  
    - 阈值补贴（Plan D）若强度不足，则补贴区的局部优势会被高成本区覆盖。  
  - 与上文温度-食物模型呼应：**政策参数需匹配效用函数形态**，否则临界点可能失效（如 Plan D 的转折点未成为实际约束点）。  

> 注：本图片为文字性习题答案，无新增图表。解析聚焦 **(e)(f)** 核心数据与上文逻辑链的实证衔接，避免重复 Plan A/B 已知结论。

---
### Page/Slide 16



### 提取内容  
- **文字**:  
  - "64 CHOICE (Ch. 5)"  
  - "Other goods"（Y轴标签）  
  - "Local phone calls"（X轴标签）  
  - "Pencil curve", "Red line", "Black line", "Blue curve"（图表标注）  
  - "(b) On the graph above, use pencil to draw indifference curves for someone who prefers the second plan to the first. Use blue ink to draw an indifference curve for someone who prefers the first plan to the second."  
- **隐含公式与坐标**:  
  - Black line: 水平线 $y = 8$（Plan 1 预算约束）  
  - Red line: 虚线 $y = 12 - 0.05x$（Plan 2 预算约束）  
  - 交点：$(80, 8)$（由上文知识点总结已确认）  

---

### 图表解析  
#### **1. Black line（水平线 $y = 8$）**  
- **代表 Plan 1**（\$12 固定费用 + 无限通话）：支付固定费用后，全部剩余预算 \$8 用于其他商品，通话量不受限。  
- **核心含义**：  
  - 通话的边际机会成本为 **0**（放弃 0 单位其他商品可获得无限通话），与上文 **Plan B 垂直跳跃约束** 形成对比：此处无斜率突变，但 **消费锁定效应** 依赖偏好分布。  
  - 若消费者通话需求低（如 $x < 80$），该计划占优（避免 Plan 2 的通话附加费）；但上文结论 **"政策阈值需匹配效用函数形态"** 在此处体现为：若效用函数 $U$ 对通话的边际效用低（如 $MRS \approx 0$），水平约束可能触发 **角点解**（$x=0$），但本题中 Plan 1 的可行性边界仅通过预算线位置体现，未涉及临界点跳跃（区别于 Plan D 的硬约束）。  

#### **2. Red line（虚线 $y = 12 - 0.05x$）**  
- **代表 Plan 2**（\$8 固定费用 + \$0.05/通）：每单位通话机会成本固定为 **\$0.05**，预算线斜率 $-0.05$。  
- **核心含义**：  
  - 斜率直接对应 **通话相对价格压缩程度**：每增加 1 次通话需放弃 0.05 单位其他商品，与上文 **Plan C 斜率 $-0.5$** 逻辑同源（均为线性价格机制）。  
  - **印证上文机制**：当边际替代率 $MRS = \text{相对价格}$ 时达内点解（例如，若 $U = \text{calls} \times (\text{other goods})^2$，则 $MRS = \frac{\text{other goods}}{2 \times \text{calls}} = 0.05$）。此处斜率恒定，消费平滑变化，区别于 Plan D 的分段斜率突变。  

#### **3. 关键交点 $(80, 8)$**  
- **验证上文数据**：代入 Plan 2 约束 $8 = 12 - 0.05 \times 80$，确认最小成本分化点。  
- **政策含义**：  
  - $x < 80$ 时：Plan 1 剩余预算更高（因 Plan 2 额外支出通话费），体现 **固定费用优势**；  
  - $x > 80$ 时：Plan 2 边际成本更低，驱动高通话需求。  
  - **与计算机案例对应**：类似 Plan C 的 **相对价格信号**（斜率 $-0.5$ 鼓励 $C$ 增至 40,000），此处斜率 $-0.05$ 引导通话量向 80 以上移动，但因二元计划选择（非单计划内分段），**需求调节无政策阈值失灵风险**（对比 Plan D 的转折点失效）。  

#### **4. 无差异曲线绘制意图（Pencil curve / Blue curve）**  
- **Pencil curve（偏好 Plan 2）**：  
  - 应绘于 Red line 切点处（如 $x > 80$），**验证上文 "斜率匹配主导内点解"**：当 $MRS = 0.05$（接近 Plan 2 斜率），高通话量成为均衡选择，体现 **补贴强度通过斜率传递至消费决策**（类比 Plan C 的价格扭曲效应）。  
- **Blue curve（偏好 Plan 1）**：  
  - 应绘于 Black line 附近（如 $x < 80$ 时 $y \approx 8$），**凸显 "名义收入非关键"**：虽 Plan 1 剩余预算 \$8 低于 Plan 2 的 \$12，但零通话成本使效用更高，反映 **相对价格对替代效应的支配性**（呼应上文 "斜率梯度比名义收入更能操控需求分布"）。  

> **知识连续性**：本图将上文抽象模型具象化，证明 **预算线斜率是需求分布的直接调控杠杆**（Plan 2 低斜率刺激高通话量，同 Plan C 刺激计算机消费）。但区别在于：电话计划为 **离散选择**（二元预算集），而计算机案例为 **连续分段约束**（Plan D 转折点）；两者共性是 **MRS 与预算线斜率的均衡条件决定消费分布**，深化上文 "政策参数需匹配效用函数形态" 的核心结论。

---
### Page/Slide 17



### 提取内容  
- **坐标轴**：  
  - 横轴：`Eggs`（范围 0–4）  
  - 纵轴：`Other goods`（范围 0–8）  
- **关键点**：  
  - `a`：(0, 8)  
  - `b`：(1, 2.5)  
  - `c`：(2, 6)  
- **曲线**：U 型无差异曲线（通过 a、b、c 三点）  

---

### 图表解析  
#### **1. U 型无差异曲线的结构特征**  
- **形状含义**：曲线在 **b (1, 2.5)** 处达到最低点，表明 **效用峰值约束**：  
  - 消费组合在 `Eggs=1` 时，达到当前效用水平所需的 `Other goods` 消耗量最小（资源效率最优）。  
  - 隐含效用函数形式：$ U = \text{Other goods} - k(\text{Eggs} - 1)^2 \ (k>0) $，在 $\text{Eggs}=1$ 时边际效用为 0。  
- **与上文连续性**：呼应上文 **"效用函数形态决定需求分布"**，此处 **内部效用峰值**（$\text{Eggs}=1$）直接限定消费边界，强化 **"MRS 非单调性触发角点解"** 的普适逻辑。  

#### **2. 边际替代率（MRS）的动态变化**  
- **b 点左侧（$\text{Eggs} < 1$）**：  
  - 例如 $ a \to b $：$\Delta \text{Eggs}=+1$，$\Delta \text{Other goods}=-5.5$，**MRS ≈ 5.5 > 0**。  
  - **核心含义**：消费者愿以高机会成本获取鸡蛋，反映 **边际效用递减前段**（鸡蛋为好品）。  
- **b 点（$\text{Eggs} = 1$）**：  
  - 曲线斜率为 0 → **MRS = 0**，即无需放弃 `Other goods` 即可增加 1 单位鸡蛋。  
  - **与上文关联**：印证上文 **"MRS ≈ 0 时需求锁定在阈值点"**，若预算线斜率匹配此特征（如 Plan 1 的零机会成本），消费者将固定消费 **$\text{Eggs}=1$**。  
- **b 点右侧（$\text{Eggs} > 1$）**：  
  - 例如 $ b \to c $：$\Delta \text{Eggs}=+1$，$\Delta \text{Other goods}=+3.5$，**MRS < 0**。  
  - **核心含义**：鸡蛋转为 **坏品**（边际效用为负），需额外补偿 `Other goods` 才愿增购。  

#### **3. 政策设计的隐喻与延展**  
- **预算约束适配逻辑**：  
  - 若预算线为 $ \text{Other goods} = B - p \cdot \text{Eggs} $，则：  
    - 当 $ p > 0 $（鸡蛋付费），若 $ p $ 远大于 0，消费收缩至 $ \text{Eggs} < 1 $；  
    - 当 $ p = 0 $（鸡蛋免费），消费将移向 $ \text{Eggs} > 1 $，但需 $ \text{Other goods} $ 递增补偿（如 $ c $ 点）。  
  - **与上文连续性**：类比 Plan 2 的 **斜率 $-0.05$ 引导通话量向 80 以上移动**，此处 **$ p $ 需围绕饱和点 $\text{Eggs}=1$ 设计**——若政策目标为自然消费量，预算线应在 $ b $ 点与曲线相切（$ p = 0 $），避免过度消费引发效用损失。  
- **核心结论**：  
  > 无差异曲线的 **U 型拐点（b 点）** 是效用函数形态的直观体现，政策参数必须与 **饱和点位置** 精确匹配，否则将导致 **资源错配**（如补贴过度使 $\text{Eggs}>1$）。此逻辑深化上文 **"政策阈值依赖效用函数形态"** 的核心论断，且适用于任意具有 **内部效用峰值** 的消费场景。

---
### Page/Slide 18



### 提取内容  
- **文字**：  
  `66 CHOICE (Ch. 5)`  

---

### 知识连续性说明  
1. **章节定位意义**：  
   - 该标题表明当前内容属于**消费者选择理论（Ch. 5）**，直接承接上文对 **预算线斜率与需求分布关系** 的实证分析（如电话计划离散选择、计算机消费连续分段约束案例）。  
   - **隐性逻辑关联**：  
     - 上文结论强调 **"政策参数需匹配效用函数形态"**，而消费者选择理论的核心即通过 **MRS = 预算线斜率** 的均衡条件推导最优消费组合。  
     - 当前章节标题暗示后续内容将系统化阐释 **"如何通过约束条件设计（如价格补贴、配额）引导需求向效用峰值收敛"**，与上文 **"内部效用峰值决定政策阈值"** 的结论形成理论闭环。  

2. **与上文关键结论的衔接**：  
   - 上文以 **U型无差异曲线拐点（如图中b点）** 证明 **"MRS非单调性触发角点解"**，本章将扩展为 **一般性消费者优化框架**，严格证明：  
     - 当效用函数存在内部极值（如 $ U = \text{Other goods} - k(\text{Eggs} - 1)^2 $）时，**预算线斜率必须等于MRS在拐点处的值（此处为0）**，才能实现资源无浪费配置。  
     - 直接验证上文 **"斜率梯度比名义收入更能操控需求分布"** 的数学基础。  

> **注**：由于当前图片仅含章节标题，无实质性图表/公式，此处通过定位其在知识体系中的角色，延续上文 **"政策设计需适配效用函数形态"** 的核心逻辑链。后续章节将具体展开类似上文电话计划案例的优化模型。
