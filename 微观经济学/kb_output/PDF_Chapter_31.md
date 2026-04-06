# PDF_Chapter_31

### Page/Slide 1



### 1. 文字与公式提取  
#### 文字内容  
- **标题**：Chapter 31 Welfare  
- **Introduction**：讨论社会偏好（social preferences）的确定方法，检验Arrow公理在社会福利关系中的适用性；通过社会福利函数求解最优配置，方法类比消费者效用最大化问题（预算约束下的最优选择）。  
- **Example**：社会计划者需在两人间分配固定总收入 $ W $，目标函数为 $ \sqrt{Y_1} + \sqrt{Y_2} $，约束条件 $ Y_1 + Y_2 = W $。若存在不对称成本（如 $ 2Y_1 + Y_2 = W $），则需调整边际替代率（MRS）与“价格比例”匹配。  
- **31.1 (2)**：介绍 **Borda count**（排序投票法），通过加总个体排名得分确定社会偏好，满足完全性、传递性假设。  

#### 公式  
1. 社会福利函数：  
   $$
   \sqrt{Y_1} + \sqrt{Y_2}
   $$  
2. 对称约束条件：  
   $$
   Y_1 + Y_2 = W
   $$  
3. 非对称约束条件：  
   $$
   2Y_1 + Y_2 = W
   $$  
4. 边际替代率（MRS）与价格比例相等：  
   $$
   \frac{\sqrt{Y_2}}{\sqrt{Y_1}} = 2 \quad \Rightarrow \quad Y_2 = 4Y_1
   $$  
5. 非对称分配结果：  
   $$
   Y_1 = \frac{W}{5}, \quad Y_2 = \frac{4W}{5}
   $$  

---

### 2. 关键内容解析  
#### (1) 社会福利函数的优化逻辑  
- **类比消费者理论**：社会计划者的优化问题与消费者效用最大化同构——  
  - **社会福利函数** $ \sqrt{Y_1} + \sqrt{Y_2} $ 相当于消费者效用函数；  
  - **收入分配约束**（如 $ Y_1 + Y_2 = W $）对应预算约束，其中“价格”隐含为边际分配成本（对称情况下均为1）。  
- **对称分配结果**：当约束为 $ Y_1 + Y_2 = W $ 时，**MRS = 1**（因对称权重），解得 $ Y_1 = Y_2 = W/2 $，体现平等分配原则。  
- **非对称调整机制**：当分配成本不对称（如 $ 2Y_1 + Y_2 = W $），需通过 **MRS = 价格比** 确定最优解：  
  $$
  \text{MRS} = \frac{\partial U / \partial Y_1}{\partial U / \partial Y_2} = \frac{\sqrt{Y_2}}{\sqrt{Y_1}} = 2 \quad \text{(价格比)}
  $$  
  解得 $ Y_2 = 4Y_1 $，结合约束条件得 $ Y_1 = W/5 $，$ Y_2 = 4W/5 $。这表明：  
  - 边际成本更高的个体（Person 1）获得更少收入；  
  - 社会福利最大化需平衡**分配效率**与**成本差异**。  

#### (2) Borda Count 的社会偏好构建  
- **核心机制**：个体对所有备选方案排序，分数按名次累加（如第1名得10分，第2名得9分…）。总分（Borda count）高的方案被社会视为更优。  
- **与Arrow公理的关联**：  
  - 该方法通过显式计分规避了**偏好传递性矛盾**（如Condorcet悖论），但需假设个体偏好严格完全且无无差异；  
  - 其隐含的社会偏好关系满足**社会至少一样好**的判定（Borda count较小者优先）。  

#### (3) 知识连续性说明  
- 本章节将**个体偏好聚合**（Arrow公理）与**社会最优配置**（福利经济学第二定理延伸）结合，通过数学优化框架揭示：  
  - 社会福利函数形式决定了公平性标准（如对称分配对应功利主义）；  
  - 约束条件的“价格”结构直接影响资源再分配比例，呼应Edgeworth Box中Pareto最优的**MRS相等条件**。

---
### Page/Slide 2



### 1. 文字与公式提取  
#### 文字内容  
- **页眉**：384 WELFARE (Ch. 31)  
- **(a)** 问题：社会偏好序是否满足完全性？**Yes**。自反性？**Yes**。传递性？**Yes**。  
- **(b)** 问题：若所有人偏好 $ x $ 超过 $ y $，Borda 计分是否也会将 $ x $ 列为社会更优？**Yes**。解释：所有人将 $ x $ 排在 $ y $ 前时，$ x $ 的总得分必高于 $ y $。  
- **(c)** 问题：两人三候选 $ x,y,z $ 的 Borda 计分  
  - 初始情形：Voter 1 为 $ x > z > y $，Voter 2 为 $ y > x > z $ → $ x: 3 $，$ y: 4 $，$ z: 5 $。  
  - 修改后：Voter 1 改为 $ x > y > z $，Voter 2 改为 $ y > z > x $ → $ x: 4 $，$ y: 3 $，$ z: 5 $。  
- **(d)** 问题：社会偏好是否仅依赖 $ x $ 与 $ y $ 的相对排名？**No**。解释：$ z $ 的排名变化导致 $ x,y $ 的社会偏好逆转，但个体对 $ x,y $ 的偏好未变。  
- **31.2 (2)** 问题：给定效用可能性边界 $ U_A + 2U_B = 200 $，要求绘制该边界图。  

---

### 2. 关键内容解析  
#### (1) 社会偏好属性验证（呼应上文 Arrow 公理）  
- **(a) 的逻辑延伸**：  
  上文指出 Borda 计分法通过显式计分满足**完全性**（所有方案可排序）和**传递性**（总分高低明确社会偏好序），此处答案 **Yes** 直接验证了 Borda 方法对 Arrow 公理中**完备性**和**传递性**的满足。  
- **(b) 的核心逻辑**：  
  个体一致偏好 $ x > y $ 时，Borda 计分通过**个体排名累加**（如 $ x $ 的总分严格高于 $ y $）强制社会偏好与个体一致。这与上文所述“Borda 计分规避 Condorcet 悖论”逻辑一致——**显式评分机制确保社会偏好与多数一致情形兼容**。  

#### (2) Borda 计分独立性缺陷（深化 Arrow 公理讨论）  
- **(c)-(d) 的联动意义**：  
  - 初始情形：$ x $ 总分 3（优于 $ y $），源于 $ z $ 作为“中间选项”被 voter 1 排在 $ x $ 后、voter 2 排在 $ x $ 前，其排名间接影响 $ x $ 与 $ y $ 的社会排序。  
  - 修改后：$ z $ 未被移除，仅改变其与 $ x,y $ 的相对位置，但 **$ x $ 与 $ y $ 的社会偏好由 $ x > y $ 变为 $ y > x $**（尽管个体始终未改变 $ x $ 与 $ y $ 的直接比较）。  
  - **关键结论**：Borda 计分违反 Arrow 的**独立无关备选方案公理（IIA）**。上文强调 Arrow 公理中 IIA 要求“社会偏好仅取决于 $ x,y $ 的个体排序”，而本例证明：**无关选项 $ z $ 的排名变动足以颠覆 $ x,y $ 的社会偏好**，揭示 Borda 方法在公理化框架下的逻辑漏洞。  

#### (3) 效用可能性边界的隐含逻辑（衔接社会福利优化）  
- **31.2 (2) 的扩展意义**：  
  边界 $ U_A + 2U_B = 200 $ 本质是变形的 **社会福利约束**，类比上文“收入分配约束”：  
  - **斜率意义**：$ \text{Slope} = -1/2 $，反映个体 B 生产效用的边际成本是 A 的 2 倍（类似上文 $ 2Y_1 + Y_2 = W $ 中 Person 1 的分配成本更高）。  
  - **优化方向**：社会福利最大化需使 MRS（效用边际替代率）等于该斜率（即 $ \frac{\partial U_A}{\partial U_B} = 1/2 $），与上文“MRS = 价格比例”逻辑严格一致，进一步印证**福利最大化是资源分配效率与成本权重的平衡**。  

#### 知识连续性要点  
- 本页问题以**案例化方式**实证了上文理论：  
  1. Borda 计分的**操作规则**（(c)）直接应用上文“按名次累加”机制；  
  2. **IIA 违反示例**（(d)）补充说明上文隐含前提——Borda 有效但依赖其他选项的排名；  
  3. 效用边界方程呼应社会福利函数的**约束形式**，强化“福利优化 = 规则化消费者问题”的类比框架。

---
### Page/Slide 3



# 社会福利函数优化：效用可能性边界上的极值点分析

## 1. 图片内容提取

### 文字与公式
- **图表标识**：
  - 横轴：UA（0-200）
  - 纵轴：UB（0-200）
  - 曲线：Utility frontier（效用可能性边界）、Black line、Red line、Blue line

- **社会福利函数**：
  | 社会福利类型 | 函数表达式 | 最优分配点 |
  |--------------|------------|------------|
  | Nitzschean | $W(U_A,U_B) = \max\{U_A,U_B\}$ | $U_A = 200$, $U_B = 0$ |
  | Rawlsian | $W(U_A,U_B) = \min\{U_A,U_B\}$ | $U_A = 66.66$, $U_B = 66.66$ |
  | Cobb-Douglas | $W(U_A,U_B) = U_A^{1/2}U_B^{1/2}$ | $U_A = 100$, $U_B = 50$ |

- **作图说明**：
  - 黑线：Nitzschean 等社会福利线
  - 红线：Rawlsian 等社会福利线
  - 蓝线：Cobb-Douglas 等社会福利线

## 2. 图表解析与上文衔接

### (a) Nitzschean 社会福利优化
- **位置**：在效用边界最右端点 (200,0)
- **含义延伸**：该点选择体现"最大化最大值"原则，与上文**社会偏好传递性**形成对比——当社会偏好仅关注单一主体效用最大化时，背离了 Arrow 公理隐含的**群体一致性**要求
- **经济逻辑**：对应于上文提及的 MRS（边际替代率）分析框架，该点 MRS 趋近于 0，意味着社会完全放弃对 B 的效用关注

### (b) Rawlsian 社会福利优化
- **位置**：效用交叉点 (66.66, 66.66)
- **含义延伸**：该点验证上文"福利最大化 = 规则化消费者问题"框架——当社会偏好严格遵循**最小化原则**时，等社会福利线（红线）呈现直角特性
- **对比价值**：与上文 Borda 计分法形成呼应，Rawlsian 准则具有**独立无关备选方案公理（IIA）** 意义的纯粹性，因为其决策仅基于 U_A 和 U_B 的相对更低值

### (c) Cobb-Douglas 社会福利优化
- **位置**：边界点 (100,50)
- **深层联系**：该点的 $U_A = 2U_B$ 比例严格符合上文 $U_A + 2U_B = 200$ 边界斜率要求，印证了**社会福利最大化需满足 MRS = 边界斜率**的核心命题
- **方法论意义**：作为上文"效用可能性边界"理论的典型案例，证明了社会福利函数优化与**消费者效用最大化问题**的数学同构性——如同 Cobb-Douglas 效用函数的 50-50 支出规律，此处 $U_A$ 权重表现为 $U_B$ 的 2 倍

### (d) 三种等福利线的经济含义
- **Black line (Nitzschean)**：呈现"角点解"特征，与上文 Arrow 公理不符（缺乏群体偏好一致性）
- **Red line (Rawlsian)**：L 形等社会福利线，体现**效用平等压缩效应**——系统性向最小效用者倾斜，但与上文 Borda 计分法一样不满足 Arrow IIA 公理
- **Blue line (Cobb-Douglas)**：凸曲线与效用边界相切点，直接对应上文**社会福利约束的拉格朗日最优化条件**，验证了 $MRS = \frac{1}{2}$ 时的最优分配

## 3. 知识连续性说明

本页通过三种典型社会福利函数的**几何可视化**，将上文抽象的：
- 社会偏好序理论（31.1 部分）转化为可量化的效用分配问题
- 效用边界约束方程（31.2）具象化为最优分配点定位
- Arrow 公理分析（IIA 违反等）延伸至不同社会准则的实践差异

尤其凸显了**边界斜率与 MRS 的匹配原则**——这正是衔接上文"福利最大化 = 规则化消费者问题"类比框架的关键支点，进一步确立了微观福利经济学的统一分析范式。

---
### Page/Slide 4



# 社会福利函数优化案例解析

## 1. 图片内容提取

### 文字与公式
- **核心设定**：
  - 预算约束：`a + b = $1,000`（初始案例）
  - 扩展约束：`a + 2b = 1,000`（31.4(2)部分，A消费效率是B的2倍）

- **效用函数案例**：
  | 子问题 | 效用函数 | 分配结果 | 经济特征 |
  |--------|------------|------------|------------|
  | (a) | $U(a,b) = \sqrt{a} + \sqrt{b}$ | $a = b = \$500$ | 边际效用递减 |
  | (b) | $U(a,b) = -\frac{1}{a} - \frac{1}{b}$ | $a = b = \$500$ | 特殊凸性 |
  | (c) | $U(a,b) = \log a + \log b$ | $a = b = \$500$ | Cobb-Douglas形式 |
  | (d) | $U(a,b) = \min\{a,b\}$ | $a = b = \$500$ | Rawlsian准则 |
  | (e) | $U(a,b) = \max\{a,b\}$ | $a = \$1,000, b = 0$ or vice versa | 极端分配 |
  | (f) | $U(a,b) = a^2 + b^2$ | 全部给一个孩子 | 非凸偏好 |
  | 31.4(2)(a) | $U(a,b) = a + b$ | A获得更多金钱和商品 | 效率差异 |

- **关键结论**：
  - 所有案例中，`a = b = $500`的解均源于MRS=1（初始约束条件下）
  - (f)部分强调：**"She gives everything to one child. Her preferences are not convex, indifference curves are quarter circles."**

## 2. 案例解析与上文衔接

### (c) Cobb-Douglas 效用函数的实证价值
- 该案例 `U = log a + log b` 直接验证上文"福利优化 = 规则化消费者问题"框架：
  - 数学上等价于 $U = a^{1/2}b^{1/2}$（对数单调变换）
  - 均等分配结果反映**边际替代率相等原则**（`MRS = 1`），与上文图表中蓝线切点逻辑完全一致
  - 印证上文"**效用边界斜率与MRS需匹配**"核心命题

### (d) Rawlsian 准则的IIA违反内涵
- $\min\{a,b\}$ 效用函数导致 $a=b$ 的强制均等分配：
  - **隐含验证**：该规则**违反IIA公理**——当存在第三选项时（如效率异质案例31.4(2)），分配结果将突变
  - 与上文知识点2呼应：此准则**依赖相对位置**而非绝对值（即使b增加但仍是较小值，分配不变）
  - 凸现Borda计分隐含前提：社会偏好需考虑**所有选项的相对排名**

### (e)+(f) 对边界解的双重验证
- **max{a,b}案例**：
  - 产生极端分配$(1000,0)$，直接体现Nitzschean准则的"角点解"特性
  - 与上文图表中黑线位置完全对应：**最大化单一主体效用时，社会福利函数退化为个体偏好**
  
- **a²+b²案例**：
  - 证明"非凸偏好导致边界解"——与上文知识点3中"效用边界约束"形成闭环
  - **关键补充**：明确指出"indifference curves are quarter circles"，解释为何产生极端解（曲率方向导致边界点最优）

### 31.4(2) 对效用边界的强化论证
- `a + 2b = 1,000` 约束下：
  - 消费效率差异创造**隐性质价比**（A的1单位=2单位B消费）
  - $U=a+b$ 时A获得全部资源，**量化验证**：
    - 边界斜率 $\frac{da}{db} = -2$ 
    - MRS=1 与 边界斜率不匹配 → 退化为边界解
  - 完美呼应上文"**MRS=边界斜率**是内部解必要条件"的理论

## 3. 知识连续性说明

本页案例将上文抽象理论**操作化为可计算模型**：
- (d)和(e)案例实证"上文知识点总结"第2点：Borda有效性**依赖选项间相对位置**（min/max函数不满足 Arrow IIA）
- (c)和31.4(2)案例验证第3点：效用边界约束方程**决定优化路径**（当预算约束斜率变化时，内部解消失）
- 所有案例均符合第1点隐含逻辑：**社会福利最大化本质是消费者问题的扩展**（100%问题符合提示中的"类似消费者问题"框架）

特别凸显**约束条件对解结构的决定作用**——当约束斜率（31.4(2)中-2）与MRS不匹配时，必然产生边界解，这正是衔接上文"福利边界斜率与MRS匹配"原则的核心操作机制。

---
### Page/Slide 5



### 提取当前图片内容

#### 文字与公式
- **标题与页码**: `NAME ________ 387`
- **子问题 (b)**:
  - 效用函数: $U(a,b) = a \times b$
  - 问题: *Which child will get more money?*  
    答案: *They get the same amount of money.*
  - 问题: *Which child will get to consume more?*  
    答案: *A consumes more.*
- **子问题 (c)**:
  - 效用函数: $U(a,b) = -\frac{1}{a} - \frac{1}{b}$
  - 问题: *Which child will get more money?*  
    答案: *B gets more money.*
  - 问题: *Which child will get to consume more?*  
    答案: *They consume the same amount.*
- **子问题 (d)**:
  - 效用函数: $U(a,b) = \max\{a, b\}$
  - 问题: *Which child will get more money?*  
    答案: *A.*
  - 问题: *Which child will get to consume more?*  
    答案: *A.*
- **子问题 (e)**:
  - 效用函数: $U(a,b) = \min\{a, b\}$
  - 问题: *Which child will get more money?*  
    答案: *B.*
  - 问题: *Which child will get to consume more?*  
    答案: *They consume the same amount.*
- **Calculus 31.5 (1)**:
  - 背景: *Norton and Ralph have a utility possibility frontier given by $U_R + U_N^2 = 100$ (where $R$ and $N$ signify Ralph and Norton).*
  - (a) *If Norton’s utility = 0, Ralph’s highest utility:* **100**.  
    *If Ralph’s utility = 0, Norton’s best:* **10**.
  - (b) *Plot the utility possibility frontier on the graph below.*
- **图表标题**: 
  - y-axis: *Ralph's utility* (range 0–100)
  - x-axis: *Norton's utility* (range 0–20)
- **图表曲线**: 通过点 (0, 100) 和 (10, 0) 的单调递减曲线，凸向原点（concave to the origin）。

---

### 图表详细解析

#### 图表核心信息
- **效用可能性边界 (Utility Possibility Frontier, UPF) 方程**: $U_R = 100 - U_N^2$。  
  该方程定义了所有帕累托有效效用组合（Ralph 和 Norton 效用的可行集），源于资源约束与个体偏好互动。
- **关键点**:
  - 当 $U_N = 0$（Norton 效用为 0），$U_R = 100$（Ralph 效用最大化）。
  - 当 $U_R = 0$（Ralph 效用为 0），$U_N = 10$（Norton 效用为 10，因 $U_N^2 = 100$）。
- **曲线形状**: 
  - **一阶导数**: $\frac{dU_R}{dU_N} = -2U_N$，表示边际转换率（MRT）的绝对值随 $U_N$ 增加而增大。
  - **二阶导数**: $\frac{d^2U_R}{dU_N^2} = -2 < 0$，确认曲线**凸向原点**（concave to the origin），反映边际转换率递增的特性。

#### 结合上文知识的连续性解释
1. **UPF 形状与效用边界约束的关联**:
   - 上文已强调 "效用边界约束方程决定优化路径"（如 31.4(2) 中 $a + 2b = 1,000$ 约束导致边界解）。此处 $U_R + U_N^2 = 100$ 是具体化实例，**曲线凸性直接体现资源分配的边际成本递增**：
     - 低 $U_N$ 区域（如 $U_N \approx 0$）：MRT 绝对值小（$\left| \frac{dU_R}{dU_N} \right| \approx 0$），增加 Norton 效用需牺牲的 Ralph 效用少 → 边界平坦（匹配上文图表中蓝线初始段）。
     - 高 $U_N$ 区域（如 $U_N \approx 10$）：MRT 绝对值大（$\left| \frac{dU_R}{dU_N} \right| = 20$），增加 Norton 效用需牺牲显著 Ralph 效用 → 边界陡峭（解释为何经济学中 UPF 通常凸向原点）。
   - 此特性**强化上文关键结论**：当 MRS（社会福利函数的边际替代率）与 UPF 斜率不匹配时，内部解消失。例如，若社会福利函数为 $W = U_R + U_N$，则最优解要求 MRS = 1，但 UPF 斜率 $-2U_N$ 仅在 $U_N = 0.5$ 时等于 -1，否则退化至边界（如 $U_N = 0$ 或 $U_N = 10$）。

2. **与 (e) 和 (f) 案例的隐含联系**:
   - 子问题 (e) 中 ($U = \min\{a, b\}$) 强制均等分配，但此处 UPF **非直线**（与上文 Rawlsian 准则的线性 UPF 区分），凸显当个体偏好差异导致 UPF 曲率时，**均等分配不一定帕累托有效**。例如：
     - 若社会采用 Rawlsian 准则（最大化最小效用），此处最优解将偏离 $U_R = U_N$（因曲线凸性，等效用点非切点）。
   - 这**深化上文 "非凸偏好导致边界解"** 的论点：$U_N^2$ 项暗示 Norton 偏好的隐含凸性（类似上文 (f) 的 $a^2 + b^2$），若社会福利函数非凸，解极易退化至端点（如 (a) 所示 $U_N = 10$ 或 $U_R = 100$）。

3. **定量验证上文理论**:
   - 上文指出 "边界斜率与 MRS 匹配是内部解必要条件"。此处 UPF 斜率 $-2U_N$ 随 $U_N$ 动态变化，**量化说明为何分配结果敏感于初始约束**：
     - 例如，若社会福利函数为 Cobb-Douglas 型 $W = U_R^{1/2} U_N^{1/2}$，内部解要求 $\frac{MRS}{\text{UPF slope}} = 1$，但此处 $\frac{U_R}{U_N} = 2U_N$ → $U_R = 2U_N^2$。代入 UPF 得 $2U_N^2 + U_N^2 = 100$，解 $U_N = \sqrt{100/3} \approx 5.77$，$U_R \approx 66.7$（内部解存在）。
     - 若社会福利函数改为 $W = \max\{U_R, U_N\}$（Nitzschean 准则），则必退化边界解（如 UPF 段 $U_R = 100$ 当 $U_N = 0$），直接**呼应上文 (e) 的角点解特性**。

#### 知识扩展
- **图表未显式绘制的含义**：曲线凸性表明 Norton 效用提升的边际成本递增，隐含**Norton 可能面临递减边际生产率**（如上文 31.4(2) 中消费效率差异）。这解释了为何在实证中，UPF 通常非线性：当一方提升效用时，社会需投入更多资源（类似 "隐性质价比" 概念）。
- **与子问题 (b)–(e) 的衔接**：子问题中 "B gets more money" 等非对称答案，反映该 UPF 分析框架中**分配结果取决于效用函数对称性**。例如 (c) 中 $U = -\frac{1}{a} - \frac{1}{b}$ 本应均等分配，但答案指定 "B gets more"，暗示实际模型存在未声明的偏好不对称（如 $a$、$b$ 非对称定义），这进一步佐证上文观点：**IIA 公理失效时分配结果可能突变**（尤其涉及相对效用排序）。

---
### Page/Slide 6



### 提取当前图片内容  
#### 文字  
- **页眉**: `388 WELFARE (Ch. 31)`  
- **问题 (c)**:  
  > Derive an equation for the slope of the above utility possibility curve.  
- **问题 (d)**:  
  > Both Ralph and Norton believe that the ideal allocation is given by maximizing an appropriate social welfare function. Ralph thinks that $U_R = 75$, $U_N = 5$ is the best distribution of welfare, and presents the maximization solution to a weighted-sum-of-the-utilities social welfare function that confirms this observation. What was Ralph’s social welfare function? (Hint: What is the slope of Ralph’s social welfare function?)  
- **问题 (e)**:  
  > Norton, on the other hand, believes that $U_R = 19$, $U_N = 9$ is the best distribution. What is the social welfare function Norton presents?  
- **问题 31.6 (2)**:  
  > Roger and Gordon have identical utility functions, $U(x, y) = x^2 + y^2$. There are 10 units of $x$ and 10 units of $y$ to be divided between them. Roger has blue indifference curves. Gordon has red ones.  
- **问题 (a)**:  
  > Draw an Edgeworth box showing some of their indifference curves and mark the Pareto optimal allocations with black ink. (Hint: Notice that the indifference curves are nonconvex.)  
- **问题 (b)**:  
  > What are the fair allocations in this case? See diagram.  
- **问题 31.7 (2)**:  
  > Paul and David consume apples and oranges. Paul’s utility function is $U_P(A_P, O_P) = 2A_P + O_P$ and David’s utility function is  

#### 公式  
- $\frac{dU_R}{dU_N} = -2U_N$  
- $W = U_R + 10U_N$  
- $W = U_R + 18U_N$  
- $U(x, y) = x^2 + y^2$  
- $U_P(A_P, O_P) = 2A_P + O_P$  

#### 图表描述  
- **类型**: Edgeworth box for Roger (bottom-left origin) and Gordon (top-right origin).  
- **坐标轴**: Horizontal ($x$) from 0 to 10; Vertical ($y$) from 0 to 10.  
- **曲线**:  
  - Blue dashed lines: Roger’s indifference curves.  
  - Red solid lines: Gordon’s indifference curves.  
  - Black lines: Pareto optimal allocations (labeled with arrows).  
- **Key labels**: "Fair" at (0,10) and (10,0); "Blue curves", "Red curves", "Black lines" annotated in the box.  

---

### 图表解析（结合上文知识点）  
#### **核心含义：非凸偏好如何导致帕累托最优集不连续**  
- **图形特征**:  
  - 无差异曲线（红/蓝线）**凹向原点**（concave to the origin），源于效用函数 $U(x, y) = x^2 + y^2$。  
    - 推导：$MRS = -\frac{MU_x}{MU_y} = -\frac{x}{y}$，当沿曲线移动时，$|MRS|$ 随 $x$ 增加而**递增**（边际替代率递增），与上文 $\frac{dU_R}{dU_N} = -2U_N$ 的 **MRT 递增特性一致**（此处 MRS 递增对应生产端的 MRT 递增）。  
  - "Black lines"（帕累托最优集）呈现**分段不连续**特征：  
    - 在非凸偏好下，切点（MRS 相等）仅存在于局部区域，导致帕累托前沿**并非完整连续曲线**（对比上文 UPF 的凸性，此处因消费端非凸，帕累托集出现断裂）。  

- **与上文知识的连续性**:  
  - **边界解特性强化**：上文指出 "非凸偏好导致边界解"（如子问题 (e) 中 Rawlsian 准则的退化解）。此图直接验证：  
    - 由于无差异曲线凹向原点（类似上文 Norton 偏好中 $U_N^2$ 项的隐含凸性），MRS 递增特性使 **a) 帕累托最优集仅存在于高/低消费区域端点**（如图中黑线靠近 "Fair" 点），**b) 内部解可能消失**（如图中黑线中间段缺失）。  
    - 例如，当两人 $x$ 消费趋近均可分点时，MRS 无法匹配，导致图中帕累托集在中间区域断裂——**呼应上文 "MRS 与 UPF 斜率不匹配时内部解消失"**。  
  - **再分配敏感性**：  
    - 问题 (d)-(e) 中，Ralph 与 Norton 的社会福利函数 $W = U_R + 10U_N$ 与 $W = U_R + 18U_N$ 的权重差异，直接源于 UPF 斜率 $-2U_N$ 的动态变化（上文定量验证部分）。  
    - 图中 "Fair" 标注暗示：在非凸偏好下，"公平分配"（如 $x$ 均分）**必非帕累托有效**（因效用边界无法触及等效用点），这**深化子问题 (e) 的均等分配失效结论**（上文强调 "均等分配不一定帕累托有效"）。  

#### **关键推论**  
- 此 Edgeworth box 是上文 UPF 分析的**消费端实例**：  
  - 无差异曲线的凹性产生与上文 $U_R + U_N^2 = 100$ 类似的 **MRT 递增效应**（但方向相反：生产端 MRT 递增 vs. 消费端 MRS 递增），共同导致分配结果对初始约束高度敏感。  
  - "Black lines" 的断裂特征量化说明：**当 $U(x,y) = x^2 + y^2$ 时，社会福利函数若为线性加权（如 $W = U_R + \alpha U_N$），内部解仅存在于特定 $\alpha$（如 Ralph 的 10，Norton 的 18）**，否则退化至边界点（匹配上文 "权重失配→角点解" 逻辑）。  
- **政策含义**：与上文一致，此类模型解释为何现实中福利分配常依赖**制度设计**（如税收再分配）以匹配 MRS 与 MRT，否则市场解易陷入低效边界（如图中黑线集中于角落）。

---
### Page/Slide 7



### Current Image Text and Formula Extraction

#### Text Content
- **Utility Function & Setup**:  
  `U_D(A_D, O_D) = A_D + 2O_D, where A_P and A_D are apple consumptions for Paul and David, and O_P and O_D are orange consumptions for Paul and David. There are a total of 12 apples and 12 oranges to divide between Paul and David. Paul has blue indifference curves. David has red ones. Draw an Edgeworth box showing some of their indifference curves. Mark the Pareto optimal allocations on your graph.`

- **Diagram Labels**:  
  `Blue curves`, `Red curves`, `Pareto optimal`, `Fair`, `Blue shading`, `Red shading`

- **Question (a)**:  
  `Write one inequality that says that Paul likes his own bundle as well as he likes David’s and write another inequality that says that David likes his own bundle as well as he likes Paul’s. \( 2A_P + O_P \geq 2A_D + O_D \) and \( A_D + 2O_D \geq A_P + 2O_P \).`

- **Question (b)**:  
  `Use the fact that at feasible allocations, \( A_P + A_D = 12 \) and \( O_P + O_D = 12 \) to eliminate \( A_D \) and \( O_D \) from the first of these equations. Write the resulting inequality involving only the variables \( A_P \) and \( O_P \). Now in your Edgeworth box, use blue ink to shade in all of the allocations such that Paul prefers his own allocation to David’s. \( 2A_P + O_P \geq 18 \).`

- **Question (c)**:  
  `Use a procedure similar to that you used above to find the allocations where David prefers his own bundle to Paul’s. Describe these points with an inequality and shade them in on your diagram with red ink. \( A_D + 2O_D \geq 18 \).`

- **Question (d)**:  
  `On your Edgeworth box, mark the fair allocations.`

#### Formula Summary
- Utility function (David):  
  \( U_D(A_D, O_D) = A_D + 2O_D \)
- Envy conditions:  
  \( 2A_P + O_P \geq 2A_D + O_D \) (Paul)  
  \( A_D + 2O_D \geq A_P + 2O_P \) (David)
- Resource constraints:  
  \( A_P + A_D = 12 \)  
  \( O_P + O_D = 12 \)
- Simplified no-envy for Paul (substituted):  
  \( 2A_P + O_P \geq 18 \)
- Simplified no-envy for David (substituted):  
  \( A_D + 2O_D \geq 18 \) (or equivalently, \( A_P + 2O_P \leq 18 \))
- Diagram-specific:  
  Frank label at (x=12, y=0) in Paul's coordinates.

---

### Chart Analysis with Context from Prior Knowledge

#### Graphical Features and Pareto Optimality
The Edgeworth box (12×12 grid, apples on x-axis, oranges on y-axis) contrasts with the previous Roger/Gordon example by using **linear utilities** instead of non-convex ones:
- **Paul’s utility**: \( U_P = 2A_P + O_P \), so blue indifference curves are straight lines with slope **−2** (MRS constant at −2).  
- **David’s utility**: \( U_D = A_D + 2O_D \), so red indifference curves are straight lines with slope **−1/2** (MRS constant at −1/2).  

Unlike the earlier non-convex case where \( U(x,y) = x^2 + y^2 \) caused **MRS to increase** along indifference curves (leading to non-continuous Pareto sets), here **MRS is constant but unequal** (\( |MRS_P| = 2 > |MRS_D| = 0.5 \)). This results in:
- **No interior Pareto optimal points**: Tangency (MRS equality) is impossible since −2 ≠ −0.5.  
- **Pareto optimal set confined to edges**:  
  - **Bottom edge** (\( O_P = 0 \)): Paul consumes no oranges; David has all oranges. All apple allocations here are efficient (no mutually beneficial trade possible).  
  - **Right edge** (\( A_P = 12 \)): Paul consumes all apples; David has no apples. All orange allocations here are efficient.  
The "Pareto optimal" arrows in the diagram trace these boundaries, confirming that efficiency requires extreme specialization—unlike the non-convex case where internal discontinuities arose from preference non-convexity. Here, boundary solutions stem from **linear (weakly) convex preferences** failing to generate interior tangencies.

#### Envy Conditions and Fairness
- **Blue shading** (\( 2A_P + O_P \geq 18 \)):  
  Represents allocations where Paul prefers his own bundle to David’s, derived by substituting resource constraints into \( U_P(\text{own}) \geq U_P(\text{David's bundle}) \). This is analogous to the earlier UPF analysis where social welfare weights (\( W = U_R + \alpha U_N \)) determined interior vs. corner solutions. Here, **\(\alpha\)-like inequality constraints** (\( 2A_P + O_P \geq 18 \)) define the feasible region for Paul’s self-preference.  
- **Red shading** (\( A_D + 2O_D \geq 18 \) or \( A_P + 2O_P \leq 18 \)):  
  Similarly, David’s preference for his own bundle. The **overlap of blue and red regions** (where \( 18 \leq 2A_P + O_P \) and \( A_P + 2O_P \leq 18 \)) forms the *no-envy set*, which is non-empty but disjoint from the Pareto frontier (e.g., at (6,6), equality holds but efficiency fails).  
- **"Fair" label**:  
  Likely marks equal division (\( A_P = 6, O_P = 6 \)), where both are indifferent to swapping bundles (\( U_P(\text{own}) = 18 = U_P(\text{David}) \)). However, this point **lies outside the Pareto set**—reinforcing the prior conclusion that **equal resource division need not be efficient**, as MRS mismatch prevents optimal trade. This echoes subproblem (e) in the summary, where "uniformity does not guarantee Pareto efficiency."

#### Continuity with Prior Concepts
- **MRS dynamics contrast**: While the previous \( U(x,y) = x^2 + y^2 \) case featured **increasing MRS** (causing internal Pareto set gaps), this linear example exhibits **constant MRS with a fixed mismatch**, eliminating interior optima altogether. Both cases demonstrate how preference structure dictates whether efficiency requires boundary or interior solutions, but for distinct theoretical reasons (non-convexity vs. weak convexity).  
- **Policy implication continuity**: The exactly replicated failure of "fair" allocations to achieve efficiency—now in a convex setting—confirms the universality of the principle that **redistribution must align MRS with resource constraints** (as in the UPF slope \( -2U_N \)) to avoid boundary inefficiencies. The inequality shading quantifies this by showing how initial endowments (e.g., 12 apples/oranges) interact with utility weights to define the successful "bargaining space," much like the role of \( \alpha \) in \( W = U_R + \alpha U_N \) for social welfare optimization.

---
### Page/Slide 8



### 当前图片核心内容提取与解析  

#### 1. 文字与公式提取  
- **页码与章节**：390, WELFARE (Ch. 31)  
- **效用函数**：  
  - Romeo: $ U_R(S_R, S_J) = S_R^a S_J^{1-a} $  
  - Juliet: $ U_J(S_J, S_R) = S_J^a S_R^{1-a} $  
  - 约束条件：$ S_R + S_J = 24 $（总量固定）  
- **关键问题与答案**：  
  - **(a)** Romeo分配：给自己 $ 16 $，给Juliet $ 8 $（$ a = 2/3 $）  
  - **(b)** Juliet分配：给自己 $ 16 $，给Romeo $ 8 $  
  - **(c)** Pareto最优分配：**每人至少 $ 8 $ 单位**（即 $ S_R \geq 8 $ 且 $ S_J \geq 8 $）  
  - **(d)(e)** Edgeworth线分析（横向表示Romeo的分配量，纵向隐含Juliet的剩余量）  

---

#### 2. 关键知识点与上文连续性分析  

##### **(1) Cobb-Douglas效用与预算约束的类比**  
- **公式逻辑**：  
  Romeo最大化 $ U_R = S_R^a (24 - S_R)^{1-a} $，解得 $ S_R = a \cdot 24 = 16 $（$ a = 2/3 $）。  
  **与上文联系**：上文知识点提及“问题形式同消费者在预算约束下选择”，此处预算线即总量约束 $ S_R + S_J = 24 $，而 $ a $ 相当于Cobb-Douglas效用中的权重参数（类似价格-收入关系）。  
- **政策启示**：与上文“重分配需匹配MRS与资源约束”呼应。此处 $ a $ 直接决定个体对自身/他人消费的偏好强度，**分配结果由效用权重主导**，而非简单均分。

##### **(2) Pareto最优的区间特征**  
- **公式推导**：  
  - MRS（Romeo）：$ \frac{a}{1-a} \cdot \frac{S_J}{S_R} $，MRS（Juliet）：$ \frac{a}{1-a} \cdot \frac{S_R}{S_J} $。  
  - 若 $ S_R, S_J < 8 $，存在调整空间使双方效用同步上升（如 $ S_R=7 \to 8 $，$ S_J=17 \to 16 $）。  
  - **当 $ S_R \geq 8 $ 且 $ S_J \geq 8 $**，任何重新分配必然牺牲一方效用，形成**Pareto边界区间**（而非单点）。  
- **与上文对比**：  
  - 上文“线性偏好案例”因MRS固定不匹配导致**无内部Pareto解**，而此处因**利他偏好结构**（效用依赖对方消费）使Pareto集扩展为区间。  
  - 但核心结论延续：**均分（如 $ S_R = S_J = 12 $）并非唯一最优解**，且“公平”标签（均分）未体现效率边界——与上文“公平≠效率”一致。

##### **(3) Edgeworth线的隐含含义**  
- **图形逻辑**：  
  - 横轴：Romeo的 $ S_R $（左→右递增），Juliet的 $ S_J = 24 - S_R $（右→左递增）。  
  - **Romeo最优点**（$ S_R = 16 $）与 **Juliet最优点**（$ S_R = 8 $）分踞两端，反映双方**偏好冲突**。  
- **与上文“边界效率”关联**：  
  - 上文总结强调“效率需边界对齐”，此处Edgeworth线仅存**两端偏好极值点**，而Pareto集居于中间区间，印证**线性/凸偏好下效率解可能分布于区间内部**（与上文“非凸偏好导致边界解”形成对比）。

---

#### 3. 理论延伸：从个体分配到社会福利  
- **问题 (c) 的深层意义**：  
  Pareto最优区间 $ [8,16] $（对Romeo而言）表明，**社会最优无需唯一解**，而是需满足“最低个体效用门槛”。这与上文“重分配需匹配MRS”逻辑一致——当个体效用依赖他人消费时，**资源余量需覆盖利他需求的阈值**（此处 $ 8 $ 单位即临界值）。  
- **对UPF的启示**：  
  上文UPF斜率 $ -2U_N $ 量化效率边界，此处Pareto集的区间形态说明：**单一商品分配下，UPF退化为线段边界**，而“无嫉妒集”转化为“最低消费保障区间”，延续了“约束条件定义可行效率域”的核心逻辑。

---
### Page/Slide 9



### 当前图片核心内容提取与解析  

#### 1. 文字与公式提取  
- **页码与章节**：391, Continuation of WELFARE (Ch. 31)  
- **问题 (f)**：  
  - "Suppose that $ a = 1/3 $. If Romeo got to allocate the spaghetti, how much would he choose for himself? **8**."  
  - "If Juliet got to allocate the spaghetti, how much would she choose for herself? **8**."  
  - "Label the Edgeworth line below, showing the two people’s favorite points and the locus of Pareto optimal points."  
- **问题 (g)**：  
  - "When $ a = 1/3 $, at the Pareto optimal allocations what do Romeo and Juliet disagree about? **Romeo wants to give spaghetti to Juliet, but she doesn’t want to take it. Juliet wants to give spaghetti to Romeo, but he doesn’t want to take it. Both like spaghetti for themselves, but would rather the other had it.**"  
- **31.9 (2) Hatfield and McCoy problem**：  
  - Utility functions:  
    - Hatfield: $ U_H(W_H, W_M) = W_H - W_M^2 $  
    - McCoy: $ U_M(W_M, W_H) = W_M - W_H^2 $  
  - Constraint: $ W_H + W_M = 4 $ (4 quarts of whiskey to be allocated).  
  - **(a)**  
    - "If McCoy got to allocate all of the whiskey, how would he allocate it? **All for himself.**"  
    - "If Hatfield got to allocate all of the whiskey, how would he allocate it? **All for himself.**"  
  - **(b)**  
    - "If each of them gets 2 quarts of whiskey, what will the utility of each of them be? **$-2$**."  
    - "If a bear spilled 2 quarts of their whiskey and they divided the remaining 2 quarts equally between them, what would the utility of each of them be? **0**."  
    - "If it is possible to throw away some of the whiskey, is it Pareto optimal for them each to consume 2 quarts of whiskey? **No.**"  

---

#### 2. 关键知识点与理论延伸  
##### **(1) 参数 $ a $ 变化对分配结果的影响**  
- **公式推导**：  
  - Romeo 的效用最大化：$ U_R = S_R^{1/3} S_J^{2/3} $，约束 $ S_R + S_J = 24 $。  
    - 一阶条件解得 $ S_R = a \cdot 24 = (1/3) \times 24 = 8 $（此前 $ a = 2/3 $ 时 $ S_R = 16 $）。  
  - Juliet 的对称结果同理。  
- **连续性分析**：  
  - 与上文（Romeo-Juliet 模型）逻辑一致：$ a $ 代表个体对自身消费的偏好权重，$ a $ 减小使分配点**向均分移动**（$ a = 1/3 < 1/2 $ 时，自利偏好弱于利他，导致分配更均衡）。  
  - **Pareto 最优区间变化**：此前 $ a = 2/3 $ 时，Pareto 集为 $ [8, 16] $（对 Romeo）；当 $ a = 1/3 $ 时，对称性使最优区间收缩至 $ [8, 8] $（单点），因双方偏好均匀，均分 $ (S_R = S_J = 12) $ 失效（解释见 (g)）。  
- **Edgeworth 线隐含含义**：  
  - 问题 (f) 要求标定 Edgeworth 线：Romeo 最优点 $ (S_R = 8, S_J = 16) $ 与 Juliet 最优点 $ (S_R = 16, S_J = 8) $ 仍分踞两端，但 $ a = 1/3 $ 时两者重合于 **$ (S_R = 8, S_J = 16) $** 和 **$ (S_R = 16, S_J = 8) $**，反映偏好权重反转后分配极值点互换。  
  - Pareto 最优轨迹退化为水平/垂直线段，印证 **偏好对称性导致效率解边界简化**（对比上文非对称 $ a $ 时的区间解）。  

##### **(2) 敌对偏好下的福利困境 (Hatfield and McCoy)**  
- **效用函数特性**：  
  - 负外部性体现：$ U_H $ 含 $ -W_M^2 $，$ U_M $ 含 $ -W_H^2 $，表明个体效用随对方消费增加而**平方级递减**（比线性外部性更极端）。  
  - 约束 $ W_H + W_M = 4 $ 下，个体分配行为：  
    - 问题 (a) 中“all for himself”源于 **最大化自利效用需最小化对方消费**（例如 McCoy 令 $ W_M = 4, W_H = 0 $，则 $ U_M = 4 - 0 = 4 $，优于共享）。  
- **Pareto 最优条件反转**：  
  - 问题 (b) 中：  
    - 均分 $ (W_H = W_M = 2) $：$ U_H = 2 - 2^2 = -2 $（同 McCoy），**非 Pareto 有效**，因存在改进空间（如减少总消费）。  
    - 消费 1 夸脱：$ U_H = 1 - 1^2 = 0 > -2 $，符合 **“扔掉资源可提升效用”** 的特殊情形——因负外部性，资源稀缺性被**反向利用**，直接印证“Pareto 最优未必要求资源耗尽”。  
  - 与上文对比：上文“利他偏好”需保障最低消费（如 8 单位），而此处 **敌对偏好使效用最大化的最小消费点低于约束边界**，社会最优依赖**约束放松**（如销毁部分资源），体现外部性类型对制度设计的根本影响。  

##### **(3) 福利争议的本质 (问题 g 的深层逻辑)**  
- **分歧根源**：  
  - Romeo 欲赠与 Juliet 但被拒，反之亦然，表面矛盾实则源于 **利他偏好与感知利己的错位**：  
    - $ a = 1/3 $ 时，Romeo 的 MRS $ = \frac{(1/3)}{(2/3)} \cdot \frac{S_J}{S_R} = \frac{1}{2} \frac{S_J}{S_R} $，Juliet 的 MRS 需对称匹配，但感知差异导致一方认为“赠与增效”而对方认定“接收减效”。  
  - 此现象延伸上文结论：**Pareto 最优仅界定约束边界，不解决分配公平**（均分点 $ S_R = S_J = 12 $ 在此参数下非最优，与上文 $ a = 2/3 $ 时一致）。  
- **理论一致性**：  
  - 与 Edgeworth 线分析吻合：偏好点分离使双方“自主最优”与“共同最优”冲突，凸显 **机制设计需校准 MRS 差异**（如通过税制内化 externality），呼应上文“重分配必须匹配边际替代率”。

---
### Page/Slide 10



# 当前图片解析

## 文字与公式提取

- **页面信息**: 392 WELFARE (Ch. 31)  
- **问题内容**:  
  > (c) If it is possible to throw away some whiskey and they must consume equal amounts of whiskey, how much should they throw away?  
  > **3 quarts.**  

- **隐含公式与约束**（基于上文敌对偏好模型）:  
  - 总资源约束: \( W_H + W_M \leq 4 \)  
  - 制度约束: \( W_H = W_M = C \)（必须等量消费）  
  - 效用函数: \( U_H = C - C^2 \), \( U_M = C - C^2 \)  
  - 最优化条件: \( \max_C U(C) \implies C^* = \max \left\{ C - C^2 \right\} \)  
  - 抛弃量: \( T = 4 - 2C^* \)  

---

## 知识连贯性解释

上文已论证**敌对偏好下负外部性的极端性**（效用随对手消费平方递减）导致Pareto最优无需耗尽资源。本问题进一步在**强制等消费制度**下量化效率路径：  

1. **优化逻辑**：  
   - 代入等消费约束 \( W_H = W_M = C \) 后，效用函数简化为 \( U(C) = C - C^2 \)。  
   - 一阶条件 \( \frac{dU}{dC} = 1 - 2C = 0 \) 直接解得 \( C^* = 0.5 \)（每人最优消费量）。  
   - 总消费量 \( 2C^* = 1 \) 夸脱，因此需抛弃 \( T = 4 - 1 = 3 \) 夸脱——**直接验证上文"销毁资源可提升效用"的机制**。  

2. **与上文结论的衔接**：  
   - 此结果深化了问题 (b) 的发现：当 \( C = 1 \)（消费 1 夸脱）时 \( U = 0 \)，但此处进一步提升至 \( U = 0.25 \)（\( C^* = 0.5 \)），**体现外部性模型中"减量增效"的非单调性**。  
   - 对比Hatfield-McCoy 模型的其他情形：  
     - (a) 部分"全归己方"源于最大化自利需最小化对方消费；  
     - 本问题则通过**制度强制等消费**，使负外部性最小化路径转向**总消费压缩**，印证**制度设计必须适配外部性类型**的核心论断。  

3. **理论延伸**：  
   - **3 夸脱** 的精确值凸显**偏好结构（平方负外部性）与约束条件（等消费）共同决定最优抛掷量**，呼应上文"敌对偏好下社会最优依赖约束放松"的结论。  
   - 与Romeo-Juliet模型分野：利他偏好需保障最低消费（如8单位），而此处**敌对偏好使效用峰值点低于资源约束边界**（\( C^* = 0.5 < 2 \)），揭示外部性方向对制度设计的颠覆性影响。
