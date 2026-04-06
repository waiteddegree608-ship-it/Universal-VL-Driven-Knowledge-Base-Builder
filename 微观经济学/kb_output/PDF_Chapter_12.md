# PDF_Chapter_12

### Page/Slide 1



### 1. 文字与公式提取  
**标题与章节**  
- Chapter 12  
- Uncertainty  

**核心概念与公式**  
- **或有商品（Contingent Commodities）**：将不同事件状态下的消费定义为独立商品。例如，事件 $ A $ 或 $ B $ 发生时的消费分别记为 "consumption if $ A $ happens" 和 "consumption if $ B $ happens"。  
- **冯·诺依曼-摩根斯坦效用（von Neumann-Morgenstern Utility）**：  
  $$
  U(c_1, c_2) = \pi_1 u(c_1) + \pi_2 u(c_2)
  $$  
  其中 $ c_1, c_2 $ 为两种状态下的消费，$ \pi_1, \pi_2 $ 为对应概率。  
- **预期效用假设（Expected Utility Hypothesis）**：消费者通过最大化此类效用函数进行决策。  
- **实例中的效用函数**（红人队赌博案例）：  
  $$
  \pi_1 \sqrt{c_1} + \pi_2 \sqrt{c_2}
  $$  
  其中 $ \pi = 0.2 $ 为红人队进入世界大赛的概率，$ c_W $ 和 $ c_{NW} $ 分别表示成功或失败状态下的消费。  

**关键定义**  
- 预算约束：通过或有商品的定价和概率设定，确定消费者可负担的消费束集合。  
- 决策逻辑：赌博结果通过状态依存消费 $ c_W = 1,000 + 10x $ 和 $ c_{NW} = 1,000 - x $ 显式关联到初始财富与投注金额 $ x $。  

---

### 2. 图表分析与上文关联  
**图片中无显式图表**，但文字内容延续了第 11 章跨期选择的分析框架：  
- **类比逻辑**：将时间维度（第 11 章）替换为状态维度（本章），通过“或有商品”将不确定性问题转化为商品空间选择问题。  
- **效用函数动态**：冯·诺依曼-摩根斯坦效用形式 $ \pi_1 u(c_1) + \pi_2 u(c_2) $ 承接了跨期效用的加权逻辑，但权重由时间贴现率转为事件概率。  
- **实例隐含结构**：红人队案例中的 $ c_W $ 与 $ c_{NW} $ 构成二维状态空间，其预算约束线斜率由赔率（10:1）和概率（0.2）共同决定，与上文跨期预算约束的斜率逻辑一致。  

**知识连续性**：本章通过“或有商品”将风险问题嵌入标准消费者理论，延续了第 11 章“将新问题映射到已有框架”的核心方法论，但将时间偏好替换为风险偏好分析。

---
### Page/Slide 2



### 1. 文字与公式提取  
**正文内容**  
- 预算约束推导：  
  $$
  \text{若投注 } x \text{ 美元：} \quad c_W = 1,000 + 10x, \quad c_{NW} = 1,000 - x
  $$  
  由 $ x = 1,000 - c_{NW} $ 代入 $ c_W $ 得：  
  $$
  c_W + 10c_{NW} = 11,000 \quad \text{或等价形式} \quad 0.1c_W + c_{NW} = 1,100
  $$  
- 效用最大化目标：  
  $$
  U(c_W, c_{NW}) = 0.2\sqrt{c_W} + 0.8\sqrt{c_{NW}} \quad \text{约束于} \quad 0.1c_W + c_{NW} = 1,100
  $$  
  通过 MRS = 价格比率求解得：  
  $$
  c_{NW} = 0.16c_W, \quad c_W = \$4,230.77, \quad c_{NW} = \$676.92 \quad (\text{投注 } \$323.08)
  $$  

**习题 12.1 (a) 内容**  
- 状态定义：  
  $ c_A $（系统通过时的消费），$ c_{NA} $（系统未通过时的消费）  
- 消费关系（购买 $ x $ 股）：  
  $$
  c_A = 50,000 + 5x, \quad c_{NA} = 50,000 - 5x
  $$  
- 效用函数：  
  $$
  U(c_A, c_{NA}) = 0.75 \ln c_A + 0.25 \ln c_{NA}
  $$  

---

### 2. 内容解析与上文知识关联  
#### 预算约束的显式推导  
上文仅提及红人队案例中 $ c_W $ 与 $ c_{NW} $ 通过投注金额 $ x $ 关联，但未展示具体代数过程。本页揭示其**约束条件的构造逻辑**：  
- 将状态消费 $ c_W, c_{NW} $ 转化为关于 $ x $ 的线性方程，通过消去内生变量 $ x $ 得到**或有商品的线性预算线**。  
- 系数 $ 0.1 $ 源于赔率（$ 10:1 $），体现"成功状态消费的隐含价格是失败状态的 $ 0.1 $ 倍"，延续上文"预算约束斜率由赔率与概率共同决定"的结论。  

#### 效用最大化求解路径  
- **MRS 条件的应用**：  
  利用 $ \text{MRS} = \frac{0.2 / (2\sqrt{c_W})}{0.8 / (2\sqrt{c_{NW}})} = \frac{0.25 \sqrt{c_{NW}}}{\sqrt{c_W}} $ 等于价格比率 $ 0.1 $，将上文所述"边际替代率等于价格比率"原则具体化。  
- **数值解的经济含义**：  
  $ c_{NW} = 0.16c_W $ 表明消费者在低概率事件（红人队成功，概率 $ 0.2 $）下分配更多消费，反映**风险偏好**（因效用函数为凹函数，隐含风险厌恶，但结果仍受赔率影响）。  

#### 习题 12.1 的方法论延续  
- **状态依存消费的构建**：  
  将"武器系统是否通过"作为状态变量，直接映射到上文的"或有商品"框架（$ c_A $ 和 $ c_{NA} $ 等价于 $ c_1, c_2 $）。  
- **线性化消费关系**：  
  $ c_A = 50,000 + 5x $ 与 $ c_{NW} = 1,000 + 10x $ 结构一致，体现**同一建模逻辑**：通过内生变量（$ x $）连接不同状态的消费。  
- **效用函数的拓展**：  
  从平方根效用 $ \sqrt{c} $ 转为对数效用 $ \ln c $，说明冯·诺依曼-摩根斯坦形式的**灵活性**（可容纳不同风险偏好参数化）。  

#### 知识连续性说明  
- 延续第 11 章"跨期选择"的**代数求解范式**（预算约束 + 效用最大化），但将时间变量替换为状态变量。  
- 通过显式推导 $ x $ 如何嵌入预算约束，深化上文"赌博结果通过状态依存消费显式关联"的抽象表述，体现**风险理论操作化**的全过程。

---
### Page/Slide 3



### 1. 文字与公式提取  
**Condor 案例（习题延续）**  
- 消费关系（购买 $ x $ 股）：  
  $$
  c_{NA} = 50,000 - 5x
  $$  
- 预算约束推导（消除 $ x $）：  
  $$
  0.5 c_A + 0.5 c_{NA} = 50,000
  $$  
- 效用最大化条件（MRS = 价格比率）：  
  $$
  \frac{c_A}{c_{NA}} = 3
  $$  
- 最优状态消费 bundle：  
  $$
  (c_A, c_{NA}) = (75,000, 25,000)
  $$  
  对应股票购买量：$ 5,000 $ 股  

**Willy 案例（习题 12.2）**  
- 状态定义：  
  $ c_F $（洪水发生时的消费），$ c_{NF} $（无洪水时的消费）  
- 初始资产：  
  无保险时，$ (c_F, c_{NF}) = (50,000, 500,000) $  
- 保险机制：  
  覆盖额 $ x $ 美元，保费 $ 0.1x $ 美元（无论是否洪水）  
- 投保后消费关系：  
  $$
  c_F = 50,000 + 0.9x, \quad c_{NF} = 500,000 - 0.1x
  $$  
- 效用函数（冯·诺依曼-摩根斯坦）：  
  $$
  U(c_F, c_{NF}) = 0.1 \sqrt{c_F} + 0.9 \sqrt{c_{NF}}
  $$  
- 洪水概率：  
  $ \frac{1}{10} $（即 $ 0.1 $）  

---

### 2. 内容解析与上文知识关联  
#### 预算约束的经济逻辑深化  
上文仅说明预算约束斜率由赔率与概率共同决定，但未明确**市场定价机制**如何嵌入。本页通过 Condor 案例揭示：  
- 预算约束 $ 0.5 c_A + 0.5 c_{NA} = 50,000 $ 的系数**相等**（0.5），表明市场对两种状态的**定价对称**（相对价格比 $ p_A / p_{NA} = 1 $）。  
- 这与上文“赔率影响斜率”一致：当 $ c_A = 50,000 + 5x $, $ c_{NA} = 50,000 - 5x $ 时，消除内生变量 $ x $ 后，约束本质反映**单位状态消费的隐含成本**。此处对称定价暗示：  
  - 金融工具（如股票）的交易机制可能隐含**公平市场假设**（价格不反映真实概率差异）。  
  - 与红人队案例关键区别：红人队赔率 10:1 导致 $ p_W / p_{NW} = 0.1 $（非对称），而本例对称定价考验**风险偏好与市场定价的互动**。  

#### 效用最大化的核心条件验证  
上文提及 MRS = 价格比率，但未展示参数化应用。本页：  
- Condor 案例中 $ \frac{c_A}{c_{NA}} = 3 $ 直接源自：  
  $$
  \text{MRS} = \frac{MU_A}{MU_{NA}} = \frac{0.75 / c_A}{0.25 / c_{NA}} = 3 \frac{c_{NA}}{c_A} \quad \text{设等于} \quad \frac{p_A}{p_{NA}} = 1
  $$  
  体现**概率权重在边际替代率中的显式作用**：效用函数权重（0.75, 0.25）驱动最优消费分配，但**受市场价格约束**。  
- 与红人队案例对比：  
  | **维度**         | 红人队案例                     | Condor 案例                  |  
  |------------------|-------------------------------|-----------------------------|  
  | 价格比率         | $ p_W / p_{NW} = 0.1 $      | $ p_A / p_{NA} = 1 $      |  
  | 概率权重         | 0.2 (win), 0.8 (lose)        | 0.75 (A), 0.25 (NA)        |  
  | 最优消费关系     | $ c_{NW} = 0.16 c_W $       | $ c_A = 3 c_{NA} $        |  
  说明**相同理论框架（或有商品）适应不同市场环境**：价格比率由外部机制给定，效用权重决定消费偏向。  

#### Willy 案例的风险管理深化  
上文强调风险偏好替换时间偏好，Willy 案例提供**保险市场的具体操作化**：  
- 预算约束隐含形式 $ 0.1 c_F + 0.9 c_{NF} = 455,000 $，其系数**严格匹配客观概率**（洪水概率 0.1）。  
- 原因：保费 $0.10/$1 覆盖 = $0.1 \times$ 保额，构成**公平保险市场**（fair odds）。  
- 关键推论：  
  - 若效用函数为凹函数（如 $\sqrt{c}$），风险厌恶消费者将追求**消费平滑**（$ c_F = c_{NF} $）。  
  - 本案例延续上文“风险理论操作化”，展示：  
    - 如何将自然灾害等风险事件转化为状态依存消费；  
    - 保险成本如何通过内生变量 $ x $ 嵌入预算约束（类比投注金额 $ x $）。  

#### 知识连续性总结  
本页案例体现第三层次知识演进：  
1. **框架一致性**：  
   - 消除决策变量 $ x $ 的代数过程（Condor 投资、Willy 保险）与上文红人队投注逻辑同构，均将**风险决策映射到二维状态空间**。  
2. **风险偏好的参数化**：  
   - 红人队（平方根效用）、Condor（对数效用）、Willy（平方根效用）展示效用函数形式的灵活性，但核心均为 $ U = \pi \cdot u(c_{\text{state1}}) + (1-\pi) \cdot u(c_{\text{state2}}) $。  
3. **市场失灵的预演**：  
   - Condor 对称定价但效用权重不对称（0.75 vs 0.25），导致最优 bundle 偏离概率比例，为后续**市场不完备性分析**埋下伏笔（未展开但方法论已体现）。  

> 注：本页无图表，分析聚焦公式经济解释。所有推导均延续上文“将新问题嵌入标准消费者理论”范式，仅替换决策变量与定价机制。

---
### Page/Slide 4



## 当前图片内容解析

### 1. 文字与公式提取
#### 文字内容
- (c) You can eliminate \(x\) from the two equations for \(c_F\) and \(c_{NF}\) that you found above. This gives you a budget equation for Willy. Of course there are many equivalent ways of writing the same budget equation, since multiplying both sides of a budget equation by a positive constant yields an equivalent budget equation. The form of the budget equation in which the “price” of \(c_{NF}\) is 1 can be written as \(.9 c_{NF} + .1 c_F = 455,000\).
- (d) Willy’s marginal rate of substitution between the two contingent commodities, dollars *if there is no flood* and dollars *if there is a flood*, is \(MRS(c_{NF}, c_F) = -\frac{.9 \sqrt{c_F}}{.1 \sqrt{c_{NF}}}\). To find his optimal bundle of contingent commodities, you must set this marginal rate of substitution equal to the number \( = -9\). Solving this equation, you find that Willy will choose to consume the two contingent commodities in the ratio \(c_{NF} / c_F = 1\).
- (e) Since you know the ratio in which he will consume \(c_{NF}\) and \(c_F\), and you know his budget equation, you can solve for his optimal consumption bundle, which is \((c_{NF}, c_F) = (455,000, 455,000)\). Willy will buy an insurance policy that will pay him \(\$450,000\) if there is a flood. The amount of insurance premium that he will have to pay is \(\$45,000\).
- 12.3 (0) Clarence Bunsen is an expected utility maximizer. His preferences among contingent commodity bundles are represented by the expected utility function \(u(c_1, c_2, \pi_1, \pi_2) = \pi_1 \sqrt{c_1} + \pi_2 \sqrt{c_2}\).  
  Clarence’s friend, Hjalmar Inggvist, has offered to bet him \(\$1,000\) on the outcome of the toss of a coin. That is, if the coin comes up heads, Clarence must pay Hjalmar \(\$1,000\) and if the coin comes up tails, Hjalmar must pay Clarence \(\$1,000\). The coin is a fair coin, so that the probability of heads and the probability of tails are both \(1/2\). If he doesn’t accept the bet, Clarence will have \(\$10,000\) with certainty. In the privacy of his car dealership office over at Bunsen Motors, Clarence is making his decision. (Clarence uses the pocket calculator that his son, Elmer, gave him last Christmas. You will find that it will be helpful for you to use a calculator too.) Let Event 1 be “coin comes up heads” and let Event 2 be “coin comes up tails.”

#### 公式内容
- Budget constraint: \(.9 c_{NF} + .1 c_F = 455,000\)
- Marginal rate of substitution: \(MRS(c_{NF}, c_F) = -\dfrac{.9 \sqrt{c_F}}{.1 \sqrt{c_{NF}}}\)
- Optimal consumption ratio: \(c_{NF} / c_F = 1\)
- Optimal bundle: \((c_{NF}, c_F) = (455,000, 455,000)\)
- Insurance payout: \(\$450,000\) (if flood occurs)
- Insurance premium: \(\$45,000\)
- Expected utility function: \(u(c_1, c_2, \pi_1, \pi_2) = \pi_1 \sqrt{c_1} + \pi_2 \sqrt{c_2}\)

---

### 2. 详细解析（基于上文知识点总结）

#### Willy 案例解析
- **预算约束的定价机制**：  
  公式 \(.9 c_{NF} + .1 c_F = 455,000\) 中，系数 \(0.9\)（无洪水状态）和 \(0.1\)（洪水状态）严格匹配客观概率（洪水概率 \(0.1\)，无洪水概率 \(0.9\)），延续了**公平保险市场**的核心设定。这与上文总结中“Willy 案例的预算约束系数匹配客观概率”一致，隐含保费计算规则为 \(0.10/\$1\) 覆盖，即单位保额的保费等于状态发生概率。
  
- **MRS 与最优消费的推导逻辑**：  
  - MRS 表达式 \(MRS(c_{NF}, c_F) = -\dfrac{.9 \sqrt{c_F}}{.1 \sqrt{c_{NF}}}\) 体现了**概率权重在边际替代率中的显式作用**：分子 \(0.9\) 和分母 \(0.1\) 直接反映状态概率，而 \(\sqrt{c}\) 项源自平方根效用函数（凹函数形式，体现风险厌恶）。  
  - 设 MRS 等于价格比率 \(-9\)（即 \(p_{NF}/p_F = 0.9 / 0.1 = 9\)），解得最优消费比 \(c_{NF}/c_F = 1\)。这验证了上文总结中“风险厌恶消费者追求消费平滑”的结论：因效用函数凹性，Willy 通过保险完全消除消费差异，实现 \(c_{NF} = c_F\)。  
  - 经济含义：保费 \(\$45,000\) 是初始财富（隐含 \(455,000 + 45,000 = 500,000\)）按洪水概率 \(0.1\) 计算的结果，赔付额 \(\$450,000\) 确保洪水状态消费不降（\(500,000 - 45,000 = 455,000\)），未重复上文已明确的“保险成本嵌入内生变量”逻辑。

#### Clarence 案例解析（知识连续性深化）
- **与上文框架的同构性**：  
  - 效用函数 \(u = \pi_1 \sqrt{c_1} + \pi_2 \sqrt{c_2}\) 延续了上文总结中“期望效用函数的通用形式 \(U = \pi u(c_{\text{state1}}) + (1-\pi) u(c_{\text{state2}})\)”。平方根形式（凹函数）与 Willy 案例一致，直接体现**风险厌恶偏好**，作为第三层次知识中“效用函数形式灵活性”的新例证。  
  - 赌注机制（公平硬币，\(\pi_1 = \pi_2 = 0.5\)）与 Condor 案例的对称定价（\(p_A / p_{NA} = 1\)）形成对照：此处市场机制隐含**对称定价**（赔率 1:1），但消费者效用权重 \(\pi_1 = \pi_2 = 0.5\) 与之匹配，故最优决策可能不扭曲消费分配。

- **风险决策的操作化**：  
  - 初始确定财富 \(\$10,000\) 可视为无赌注状态，接受赌注后状态收入为：  
    - Event 1 (heads): \(c_1 = 10,000 - 1,000 = 9,000\)  
    - Event 2 (tails): \(c_2 = 10,000 + 1,000 = 11,000\)  
  - 是否接受赌注取决于期望效用比较：  
    - 无赌注：\(U_{\text{no bet}} = \sqrt{10,000} = 100\)  
    - 有赌注：\(U_{\text{bet}} = 0.5 \sqrt{9,000} + 0.5 \sqrt{11,000} \approx 99.86 < 100\)  
    风险厌恶导致拒绝赌注，**延续了“将新风险事件转化为状态依存消费”的范式**，并预演市场完备性——此处公平赌注因风险厌恶未被接受，凸显消费者偏好对定价对称性的修正作用（上文总结中“市场不完备性分析”的方法论雏形）。

- **与红人队/Condor 案例的演进关系**：  
  - 本案例以更简形式（二元等概率）展示**定价对称下风险偏好如何主导决策**：对比 Condor（效用权重 0.75 vs 0.25 导致消费偏差），Clarence 的权重匹配概率，故无赌注决策不偏离确定等价，但风险厌恶仍使其选择避免波动。这强化了上文总结中“相同理论框架适应不同市场环境”的结论，同时为后续分析非对称定价（如红人队案例）提供基准参照。

---
### Page/Slide 5



### 提取内容：当前图片文字与公式

#### 文字内容：
- **(a)** 若Clarence接受赌注，则在事件1中，他将拥有9,000美元；在事件2中，他将拥有11,000美元。
- **(b)** 由于各事件概率均为1/2，Clarence在事件1获得$c_1$、事件2获得$c_2$的赌注期望效用公式为$\frac{1}{2} \sqrt{c_1} + \frac{1}{2} \sqrt{c_2}$。因此，若他接受Hjalmer的赌注，期望效用为99.8746。
- **(c)** 若Clarence不接受赌注，则在事件1和事件2中，他均拥有10,000美元。因此，其期望效用为100。
- **(d)** 通过比较接受与不接受赌注的期望效用，Clarence据此决策。他接受该赌注吗？**不**。
- **12.4 (0)** Bunsen Motors的闲暇日，Clarence Bunsen（其风险偏好已在上题描述）决定深入研究期望效用函数：
  - **(a)** 他考虑全押$10,000的高风险赌注：若抛硬币为正面则失去全部财富（0美元），反面则获得$20,000。接受赌注的期望效用为70.71，不接受则为100，故他拒绝该赌注。
  - **(b)** 他进一步思考：若抛正面损失$10,000（财富为0），反面则赢得$50,000（财富为$60,000）。接受赌注的期望效用为122.5，不接受为100，故他应**接受**该赌注。

#### 公式与数值：
- 期望效用函数：$\frac{1}{2} \sqrt{c_1} + \frac{1}{2} \sqrt{c_2}$
- 关键数值：
  - 小赌注（±$1,000）接受效用：99.8746  
  - 小赌注不接受效用：100  
  - 全押赌注接受效用：70.71  
  - 全押赌注不接受效用：100  
  - 有利赌注接受效用：122.5  
  - 有利赌注不接受效用：100  

---

### 解析（知识连续性深化）

#### 1. **风险偏好对决策边界的动态影响**  
上文已阐明，Clarence的平方根效用函数（$u = \pi_1 \sqrt{c_1} + \pi_2 \sqrt{c_2}$）体现严格风险厌恶，导致其在**公平对称赌注**（如±$1,000）中拒绝参与（$U_{\text{bet}} \approx 99.87 < U_{\text{no bet}} = 100$）。当前图片通过两个扩展场景揭示风险厌恶并非绝对排斥所有赌注，而是依赖**效用函数曲率与赌注结构的互动**：  
- **全押赌注（12.4(a)）**：  
  - 尽管仍是公平定价（概率对称），但赌注幅度过大导致$c_1 = 0$，平方根效用的凹性（$u''<0$）在此处产生**强边际效用递减**：$c_1=0$时$\sqrt{c_1}=0$，而$c_2=20,000$时$\sqrt{c_2} \approx 141.42$。  
  - 期望效用降至70.71（远低于确定性等价100），验证了上文“风险厌恶程度随财富波动幅度非线性放大”的结论。此情形凸显**破产风险对效用的毁灭性影响**，本质上拓展了上文“市场不完备性分析”的方法论——即使定价公平，极端风险可能使效用降至不可接受水平。  
- **有利赌注（12.4(b)）**：  
  - 赌注不对称：$c_1=0$（财富归零），$c_2=60,000$（财富增至原6倍）。  
  - 关键经济含义：**期望货币价值（EMV）为正**（$0.5 \times 0 + 0.5 \times 60,000 = 30,000 > 10,000$），部分抵消了风险厌恶。  
  - 效用增益源于**高财富端边际效用降幅弱化**：$\sqrt{60,000} \approx 244.95$，其加权贡献（$0.5 \times 244.95 = 122.475$）显著超越确定性等价100。  
  - 这直接回应了上文“相同理论框架适应不同市场环境”的结论：当**赌注斜率足够陡峭**（如赢面大幅优于损失面），风险厌恶个体可能逆转决策。对比红人队案例，此处显示**消费者偏好可被极端有利条件修正定价对称性的局限性**。

#### 2. **风险决策范式的拓展**  
- 上文通过Clarence小赌注案例建立“状态依存消费转化”范式（将赌注转化为$c_1, c_2$比较）。当前图片通过**极端风险场景**（全押与高收益赌注）深化此范式：  
  - 全押案例（12.4(a)）展示**破产效应**：$c_1=0$使效用函数在该点失去定义域连续性（$\sqrt{0}=0$），强化了上文“保险需求源于极端损失厌恶”的隐含逻辑。  
  - 有利赌注案例（12.4(b)）揭示**风险承受阈值**：当赌注隐含**风险溢价**（EMV与确定财富差额$20,000$）超过风险厌恶程度，决策从拒绝转向接受。这预演了后续“风险溢价计算”的核心问题，且与Willy案例的**公平保险机制**形成映照——保险消除风险（$c_{NF}=c_F$），而此处高期望回报补偿风险。  
- 动态变化含义：  
  | 赌注类型       | 期望效用 | 相比上文进展                              |  
  |----------------|----------|------------------------------------------|  
  | 小赌注（公平） | 99.87    | 验证基础风险厌恶（上文已覆盖）           |  
  | 全押（公平）   | 70.71    | 揭示风险厌恶在破产风险下的非线性放大     |  
  | 有利赌注       | 122.5    | 证明正EMV赌注可突破风险厌恶阈值          |  

> **关键延续**：所有场景均基于$\sqrt{c}$效用函数的凹性，但当前图片通过**财富分布极化**量化了上文“风险厌恶影响程度取决于财富波动范围”的结论，为后续研究保险需求和资产定价奠定操作化基础。

---
### Page/Slide 6



### 当前图片内容提取

#### 1. 文字与公式提取
- **文字内容**：
  - (c) Clarence later asks himself, “If I make a bet where I lose my $10,000 if the coin comes up heads, what is the smallest amount that I would have to win in the event of tails in order to make the bet a good one for me to take?” After some trial and error, Clarence found the answer. You, too, might want to find the answer by trial and error, but it is easier to find the answer by solving an equation. On the left side of your equation, you would write down Clarence’s utility if he doesn’t bet. On the right side of the equation, you write down an expression for Clarence’s utility if he makes a bet such that he is left with zero consumption in Event 1 and \(x\) in Event 2. Solve this equation for \(x\). The answer to Clarence’s question is where \(x = 10,000\). The equation that you should write is \(100 = \frac{1}{2} \sqrt{x}\). The solution is \(x = 40,000\).
  - (d) Your answer to the last part gives you two points on Clarence’s indifference curve between the contingent commodities, money in Event 1 and money in Event 2. (Poor Clarence has never heard of indifference curves or contingent commodities, so you will have to work this part for him, while he heads over to the Chatterbox Cafe for morning coffee.) One of these points is where money in both events is $10,000. On the graph below, label this point \(A\). The other is where money in Event 1 is zero and money in Event 2 is 40,000. On the graph below, label this point \(B\).
  - (e) You can quickly find a third point on this indifference curve. The coin is a fair coin, and Clarence cares whether heads or tails turn up only because that determines his prize. Therefore Clarence will be indifferent between two gambles that are the same except that the assignment of prizes to outcomes are reversed. In this example, Clarence will be indifferent between point B on the graph and a point in which he gets zero if Event 2 happens and 40,000 if Event 1 happens. Find this point on the Figure above and label it \(C\).

- **公式**：
  - 无差异条件方程：\(100 = \frac{1}{2} \sqrt{x}\)
  - 解：\(x = 40,000\)

#### 2. 图表描述
- **图表类型**：二维坐标系中的无差异曲线图。
- **坐标轴**：
  - 横轴：Money in Event 1 (x 1,000)，刻度范围 0–40（单位：千美元）。
  - 纵轴：Money in Event 2 (x 1,000)，刻度范围 0–40（单位：千美元）。
- **曲线特征**：
  - 一条向下凸向原点的平滑曲线（凸性源于平方根效用的凹性），标记点包括：
    - 点 \(A\)：坐标 \((10, 10)\)，对应 \(c_1 = 10,000\), \(c_2 = 10,000\)
    - 点 \(B\)：坐标 \((0, 40)\)，对应 \(c_1 = 0\), \(c_2 = 40,000\)
    - 点 \(C\)：坐标 \((40, 0)\)，对应 \(c_1 = 40,000\), \(c_2 = 0\)
  - 曲线上另有点 \(d\)（位于曲线中段，低于点 \(A\)）。

---

### 图表解析：变化的含义与知识连续性深化

#### 边际替代率非线性与风险厌恶量化
图表中的无差异曲线（\(U = 100\)）由期望效用函数 \(\frac{1}{2} \sqrt{c_1} + \frac{1}{2} \sqrt{c_2} = 100\) 定义，直接延续上文对**状态依存消费决策**的分析框架：
- **点 \(A\)（无风险点）**：\(c_1 = c_2 = 10,000\)，效用 \(U = 100\)。上文以"不接受赌注效用为100"为基准，此处定位了确定性等价点，作为风险偏好分析的原点。
- **点 \(B\) 与点 \(C\)（极端风险对称点）**：
  - \(B\)：\( (c_1 = 0, c_2 = 40,000) \)，效用 \( \frac{1}{2} \sqrt{0} + \frac{1}{2} \sqrt{40,000} = 100 \)
  - \(C\)：\( (c_1 = 40,000, c_2 = 0) \)，效用 \( \frac{1}{2} \sqrt{40,000} + \frac{1}{2} \sqrt{0} = 100 \)
  - **经济含义**：两点均满足无差异条件，但隐含上文"破产风险对效用的毁灭性影响"。当 \(c_1 \to 0\) 时，\(\sqrt{c_1}\) 的凸性导致边际效用急剧下降（\(u'' < 0\)），需 \(c_2\) 从 10,000 跃升至 40,000 才维持效用不变。这量化了上文结论——**财富波动幅度越大，风险厌恶程度非线性放大**（小赌注中 \(c_1\) 仅降至 9,000 时拒绝；此处 \(c_1 = 0\) 需 4 倍补偿）。
- **曲线凸性作用**：  
  曲线在端点 \(B\) 和 \(C\) 处陡峭（如从 \(B\) 到 \(A\)，\(c_1\) 增加 10（千美元）需 \(c_2\) 减少 30），在中部平缓（如从 \(A\) 到 \(C\)，\(c_1\) 增加 30 需 \(c_2\) 减少 10）。这印证上文"风险厌恶影响程度取决于财富波动范围"：  
  - 当逼近破产（\(c_1 \approx 0\)），轻微损失需巨额收益补偿（对应上文全押赌注接受效用 70.71 < 100 的机制）；  
  - 当财富充裕（\(c_1 > 10\)），风险承受力边际改善（为有利赌注决策埋下伏笔）。

#### 决策边界的动态拓展
图表通过无差异曲线深化上文"风险决策范式"：
- **无风险风险轴（45°线）**：点 \(A\) 位于该线上，代表无风险状态。任何偏离该线的点（如 \(B\)、\(C\)）均引入风险，与上文"公平对称赌注拒绝"一致；而曲线凸性表明，风险增加的边际成本递增。
- **有利赌注的阈值突破**：  
  上文有利赌注（\(c_1 = 0, c_2 = 60,000\)）效用 122.5 > 100，对应此图中 \(B\) 点（\(c_2 = 40,000\)）所在无差异曲线外一点。本图曲线（\(U = 100\)）标志着风险厌恶的**临界边界**：  
  - 当赌注组合（如 \(c_2 > 40,000\) 且 \(c_1 = 0\)) 位于曲线上方，期望回报足以覆盖风险厌恶（呼应上文有利赌注接受逻辑）；  
  - 当组合位于曲线下方（如全押赌注 \(c_2 = 20,000\)），即使公平定价（EMV 对称）仍被拒。  
  这操作化了上文"赌注斜率足够陡峭可逆转决策"的核心：曲线形状定义了风险溢价（Risk Premium）的度量方式——从点 \(A\) 到曲线的垂直距离反映需多少期望回报补偿风险。

> **关键延续**：无差异曲线将上文离散赌注分析（小赌注、全押、有利赌注）整合为连续理论框架。曲线端点陡峭段对应"保险需求机制"（破产风险强烈驱动保险购买），中段平缓区则隐含"风险资产配置阈值"，直接衔接后续资产定价章节。点 \(B\) 与 \(C\) 的对称性进一步验证上文结论——风险厌恶程度与具体状态路径无关，仅取决于财富分布，为"状态依存偏好"理论提供微观可视化基础。

---
### Page/Slide 7



### 提取的文字与公式

#### 文字内容
- **页眉**: `NAME ________________ 167`
- **(f) 部分**:  
  "Another gamble that is on the same indifference curve for Clarence as not gambling at all is the gamble where he loses $5,000 if heads turn up and where he wins 6,715.73 dollars if tails turn up. (Hint: To solve this problem, put the utility of not betting on the left side of an equation and on the right side of the equation, put the utility of having $10,000 - $5,000 in Event 1 and $10,000 + x in Event 2. Then solve the resulting equation for x.) On the axes above, plot this point and label it D. Now sketch in the entire indifference curve through the points that you have labeled."
- **12.5 (0) 部分开头**:  
  "Hjalmer Inggvist’s son-in-law, Earl, has not worked out very well. It turns out that Earl likes to gamble. His preferences over contingent commodity bundles are represented by the expected utility function"
- **(a) 部分**:  
  "Just the other day, some of the boys were down at Skoog’s tavern when Earl stopped in. They got to talking about just how bad a bet they could get him to take. At the time, Earl had $100. Kenny Olson shuffled a deck of cards and offered to bet Earl $20 that Earl would not cut a spade from the deck. Assuming that Earl believed that Kenny wouldn’t cheat, the probability that Earl would win the bet was 1/4 and the probability that Earl would lose the bet was 3/4. If he won the bet, Earl would have 120 dollars and if he lost the bet, he would have 80 dollars. Earl’s expected utility if he took the bet would be 8,400, and his expected utility if he did not take the bet would be 10,000. Therefore he refused the bet."
- **(b) 部分**:  
  "Just when they started to think Earl might have changed his ways, Kenny offered to make the same bet with Earl except that they would bet $100 instead of $20. What is Earl’s expected utility if he takes that bet? 10,000. Would Earl be willing to take this bet? He is just indifferent about taking it or not."
- **(c) 部分**:  
  "Let Event 1 be the event that a card drawn from a fair deck of cards is a spade. Let Event 2 be the event that the card is not a spade. Earl’s preferences between income contingent on Event 1, \( c_1 \), and income contingent on Event 2, \( c_2 \), can be represented by the equation \( u = \frac{1}{4} c_1^2 + \frac{3}{4} c_2^2 \). Use blue ink on the graph below to sketch Earl’s indifference curve passing through the point (100,100)."

#### 公式
- 预期效用函数通用形式: \( u(c_1, c_2, \pi_1, \pi_2) = \pi_1 c_1^2 + \pi_2 c_2^2 \)
- (c) 部分特定形式: \( u = \frac{1}{4} c_1^2 + \frac{3}{4} c_2^2 \)

---

### 图表与内容解析

当前图片未提供实际图表，但 (c) 部分提及“graph below”，要求基于效用函数 \( u = \frac{1}{4} c_1^2 + \frac{3}{4} c_2^2 \) 绘制通过点 \((100, 100)\) 的无差异曲线。结合上文知识点总结（凹效用、风险厌恶框架），此处解析聚焦以下连续性深化：

#### 1. **无差异曲线的形状与风险偏好类型对比**
   - **当前效用函数特性**:  
     \( u = \frac{1}{4} c_1^2 + \frac{3}{4} c_2^2 \) 中， \( v(c) = c^2 \) 为**凸函数**（二阶导 \( v''(c) = 2 > 0 \)), 这直接定义了**风险爱好**偏好。通过点 \((c_1, c_2) = (100, 100)\) 的无差异曲线满足:
     $$
     \frac{1}{4} c_1^2 + \frac{3}{4} c_2^2 = 10,000
     $$
     无差异曲线**凹向原点**（以原点为凹侧），**边际替代率递增**（曲线斜率随 \( c_1 \) 增加而变陡）。
   - **与上文连续性**:  
     上文知识点总结中，凹效用函数 \( \frac{1}{2} \sqrt{c_1} + \frac{1}{2} \sqrt{c_2} = 100 \) 导致**凸向原点**的无差异曲线（风险厌恶）。本例的凸效用函数首次在材料中**系统性对比风险爱好**案例，揭示：
     - **风险偏好本质**：上文强调“财富波动放大厌恶”，此处则证明波动可被偏好**放大接受**（点 \( B/C \) 的极端风险从厌恶转为吸引）。
     - **决策机制反转**：上文风险厌恶拒绝公平赌注，此处风险爱好者（Earl）在 (b) 中对期望财富 \( 50 < 100 \) 的赌注（ \( c_1=200, c_2=0 \) ）达到效用无差异，体现 **“凸效用覆盖期望损失”** ——曲线凹性使高财富边际效用递增，补偿了极端损失风险。

#### 2. **极端风险下的决策边界变化**
   - **(a) 和 (b) 的量化含义**:  
     - (a) 中，赌注期望财富 \( 0.25 \times 120 + 0.75 \times 80 = 90 < 100 \)（不公平），且 \( \text{EU}_{\text{gamble}} = 8,400 < 10,000 = \text{EU}_{\text{no bet}} \)，拒绝。  
       → **上文连续性**：印证“风险厌恶需明确盈亏不对称”结论，但本例因效用凸性，**小额损失拒绝源于期望财富不足而非风险本身**（上文风险厌恶者拒绝源于波动成本）。
     - (b) 中，赌注期望财富 \( 0.25 \times 200 + 0.75 \times 0 = 50 \ll 100 \)，但 \( \text{EU}_{\text{gamble}} = 10,000 = \text{EU}_{\text{no bet}} \)。  
       → **核心深化**：上文风险厌恶的“风险溢价”为正（需补偿），而此处风险溢价为**负**——风险本身具有正价值。点 \( (c_1=200, c_2=0) \) 位于无差异曲线**内部**，与上文点 \( B/C \)（在上文曲线外部才接受）完全相反，直接操作化 **“风险态度决定风险价值符号”** 及其对无差异曲线位置的决定性影响。
   - **与上文知识连续性**:  
     上文点 \( D \)（来自 (f) 部分）计算赢面 \( x=6,715.73 \) 依赖凹效用，本例 (f) 隐含的相同无差异曲线计算 **\( \frac{1}{2}\sqrt{5,000} + \frac{1}{2}\sqrt{10,000 + x} = 100 \)** 与 (c) 的凸效用曲线形成**正交对照**：  
     - 凹效用需高补偿（\( x=6,715 \)）覆盖低财富风险；  
     - 凸效用则低补偿即可（如 (b) 中 \( c_2=0 \) 仍达效用无差异）。

#### 3. **边际替代率动态与理论拓展**
   - **曲线斜率含义**:  
     由 \( u = \frac{1}{4} c_1^2 + \frac{3}{4} c_2^2 = \text{const} \)，隐函数求导得边际替代率 \( \text{MRS} = -\frac{dc_2}{dc_1} = \frac{\pi_1 c_1}{\pi_2 c_2} \)。  
     - 在 \((100,100)\) 处，\( \text{MRS} = \frac{(1/4) \times 100}{(3/4) \times 100} = \frac{1}{3} \)（平缓段）；  
     - 接近轴点（如 \( c_2 \to 0 \)），MRS 趋向无穷（陡峭段）。  
     **关键区别**：上文凹效用的 MRS 递减（曲线凸），而本例 MRS 递增（曲线凹），证明 **“风险偏好类型决定 MRS 变动方向”**。
   - **理论连续性结论**:  
     上文曲线端点陡峭段驱动“保险需求”，本例端点陡峭段则导向 **“风险追逐”** ——如 (b) 中 \( c_2=0 \) 可被接受，预示极端事态下风险爱好者会主动追求破产边缘机会。这为后续章节的**资产定价与市场均衡**提供微观基础：风险厌恶者构成保险市场，风险爱好者提供风险资本，共同校准均衡风险溢价。  
     > **核心延续**：无差异曲线凹凸性差异量化了风险偏好的**双重性**（厌恶 vs. 爱好），并将上文离散赌注分析拓展至连续偏好谱系，验证“效用函数二阶特性是风险决策单一决定因素”这一公理化核心。

---
### Page/Slide 8



### 图片解析

#### 1. 提取文字与公式
**文字内容：**  
- 图表标题：  
  `Money in Event 2`（纵轴）、`Money in Event 1`（横轴）  
- 图例标注：  
  `Blue curve`（蓝色曲线）、`Red curves`（红色曲线）  
- 问题描述：  
  `(d) On the same graph... Earl’s preferences... represented by the formula $ u = \frac{1}{2}c_1^2 + \frac{1}{2}c_2^2 $.`  

**公式：**  
$$
u = \frac{1}{2}c_1^2 + \frac{1}{2}c_2^2
$$

---

#### 2. 图表解析（结合上文知识点）

##### **曲线形态与风险偏好类型**
- **红色曲线（Earl的无差异曲线）**：  
  - **形状**：**凹向原点**（Concave to the origin），与凸效用函数 $ u = \frac{1}{2}c_1^2 + \frac{1}{2}c_2^2 $ 一致。  
  - **经济含义**：  
    - 凸效用函数对应**风险爱好**（Risk-loving），高财富的边际效用递增（$ u''(c) > 0 $）。  
    - 与上文知识点一致：风险爱好者愿意接受期望财富远低于确定性财富的赌注（如上文(b)中 $ c_1=200, c_2=0 $ 时效用仍达无差异）。  
  - **MRS动态**：  
    $$
    \text{MRS} = \frac{c_1}{c_2} \quad \text{（递增）}
    $$  
    - 当 $ c_2 \to 0 $ 时，MRS 趋向无穷（曲线陡峭），证明**极端损失风险可被接受**（如上文(b)中 $ c_2=0 $ 仍达效用无差异）。  
    - 与上文风险厌恶（凹效用）的**MRS递减**形成正交对照。  

- **蓝色曲线**：  
  - **隐含假设**：来自上文风险厌恶案例的无差异曲线（$ u = \frac{1}{2}\sqrt{c_1} + \frac{1}{2}\sqrt{c_2} $）。  
  - **形状**：**凸向原点**（Convex to the origin），因凹效用函数导致风险厌恶。  
  - **对比意义**：  
    - 蓝色曲线在 $ (100,100) $ 附近斜率平缓，端点陡峭（MRS递减），体现**保险需求**；  
    - 红色曲线在 $ (100,100) $ 附近斜率较陡，端点更陡峭（MRS递增），体现**风险追逐**（如主动追求 $ c_1=200, c_2=0 $ 的极端构局）。  

##### **关键点 $ (100,100) $ 的决策含义**
- **红色曲线通过 $ (100,100) $ 的设定**：  
  - 与上文(a)中拒绝期望财富90的赌注（$ c_1=120, c_2=80 $）形成反差：  
    - 风险厌恶者因**期望财富不足 + 波动成本**拒绝（上文）；  
    - 风险爱好者因**高财富边际效用递增**接受更低期望财富的赌注（如上文(b)中期望财富50的赌注）。  
  - 印证上文结论：**风险溢价符号由偏好类型决定**——风险厌恶者要求正溢价，风险爱好者接受负溢价（风险本身有正价值）。  

---

#### 3. 理论延续性
- **与上文知识的关联**：  
  1. **无差异曲线凹凸性的双重性**：  
     - 蓝色凸曲线 → 风险厌恶（上文知识点）；  
     - 红色凹曲线 → 风险爱好（本图核心）。  
  2. **极端决策边界**：  
     - 蓝色曲线要求**高补偿**（如上文(f)部分 $ x=6,715 $）才能接受低财富风险；  
     - 红色曲线仅需**极低补偿**（如 $ c_2=0 $ 时仍达无差异），直接操作化“风险对爱好者的吸引力”。  
  3. **微观基础验证**：  
     - 本图将上文离散赌注分析拓展至连续偏好谱系，强化“效用函数二阶导数决定风险态度”的公理化结论。  

> **核心结论**：红色 curves 的凹性（凸效用）与蓝色 curves 的凸性（凹效用）通过图形化对比，具象化了风险偏好类型的本质差异——**边际效用变动方向决定个体对不确定性的真实价值判断**。

---
### Page/Slide 9



### 图片解析

#### 1. 提取文字与公式
**文字内容：**  
- 图表标注：  
  - 横轴：`Cs`（consumption if shines，晴天消费）  
  - 纵轴：`Cr`（consumption if rains，雨天消费）  
  - 线型：`Blue line`（蓝色线）、`Red line`（红色线）  
  - 点坐标：`a`、`e`  
- 文本部分：  
  - `(b) On the same graph, mark the combination of consumption contingent on rain and consumption contingent on sun that he could achieve by buying 10 rain coupons from the casino. Label it A.`  
  - `(c) On the same graph, use blue ink to draw the budget line representing all of the other patterns of consumption that Sam can achieve by buying rain coupons. (Assume that he can buy fractional coupons, but not negative amounts of them.) What is the slope of Sam’s budget line at points above and to the left of his initial endowment? The slope is −1.`  
  - `(d) Suppose that the casino also sells sunshine coupons. These tickets also cost $1. With these tickets, the casino gives you $2 if it doesn’t rain and nothing if it does. On the graph above, use red ink to sketch in the budget line of contingent consumption bundles that Sam can achieve by buying sunshine tickets.`  
  - `(e) If the price of a dollar’s worth of consumption when it rains is set equal to 1, what is the price of a dollar’s worth of consumption if it shines? The price is 1.`  
  - `12.7 (0) Sidewalk Sam, from the previous problem, has the utility function for consumption in the two states of nature`  
  - `where $c_s$ is the dollar value of his consumption if it shines, $c_r$ is the dollar value of his consumption if it rains, and $\pi$ is the probability that it will rain. The probability that it will rain is $\pi = .5$.`  

**公式：**  
$$
u(c_s, c_r, \pi) = c_s^{1-\pi} c_r^{\pi}
$$
$$
\pi = 0.5
$$

---

#### 2. 图表解析（结合上文知识点）

##### **预算线形态与市场完备性**
- **蓝线与红线的统一性**：  
  - 两线均为**斜率为 −1 的直线**（从图表左上 $(0,40)$ 延伸至右下 $(40,0)$），印证上文要点：费率公平性下，状态价格相等（$\pi_r = \pi_s = 1$）。  
  - 蓝线代表雨优惠券市场，红线代表阳光优惠券市场；但因优惠券定价满足无套利条件（雨优惠券公平价格 $\pi$，阳光优惠券公平价格 $1-\pi$，且 $\pi = 0.5$），**两条线实际重合**，表明市场完备——任意状态消费可通过交易完全对冲风险。  
  - **经济含义**：  
    - 横轴 $c_s$ 与纵轴 $c_r$ 均以货币衡量，预算约束为 $c_s + c_r = \text{constant}$。  
    - 点 $a$（约 $(20,20)$）为典型初始禀赋点；若初始消费不对称（如点 $e$ 约 $(30,10)$），Sam 可通过交易实现风险平滑。  
    - 与上文“离散赌注分析拓展至连续偏好”呼应：此处状态消费的连续性使风险决策可精确优化，而非仅依赖离散选项。

- **关键点 $a$ 与 $e$ 的决策示意**：  
  - 若点 $e$ 为初始禀赋（$(30,10)$），则期望消费 $E[c] = 20$，但各状态消费差异大；  
  - 点 $a$（$(20,20)$）代表**完全保险状态**，可作为交易终点。  
  - **风险平滑机制**：  
    - 比如购买雨优惠券（成本 $1，雨天收益 $1），若初始在 $e$，Sam 可转移至 $a$。  
    - 与上文“风险溢价符号由偏好类型决定”一致：此处无额外风险成本，因市场完全且定价公平。

##### **效用函数二阶特性驱动风险态度**
- **Sam 的风险厌恶本质**：  
  - 代入 $\pi = 0.5$，效用函数化为 $u = c_s^{0.5} c_r^{0.5} = \sqrt{c_s c_r}$。  
  - **二阶特性分析**：  
    - 无差异曲线满足 $c_r = k^2 / c_s$，其二阶导数 $\frac{d^2 c_r}{dc_s^2} = 2k^2 c_s^{-3} > 0$，故曲线**凸向原点**（convex to origin）。  
    - 边际替代率 $\text{MRS} = \frac{c_r}{c_s}$ 随 $c_s$ 增加而递减，与上文风险厌恶情形（凹效用）一致。  
  - **决策含义**：  
    - Sam 优先选择 $c_s = c_r$ 的点（如 $a$），以降低消费波动；若初始在 $e$，交易至 $a$ 可提升效用。  
    - 验证上文公理化核心：**效用函数凹性（此处 $u$ 拟凹且 $u''(c) < 0$ 单变量视角）直接决定风险厌恶**，无需依赖赌注规模。  
    - 与上文风险爱好案例正交：上文凸效用函数 $(u = \frac{1}{2}c_1^2 + \frac{1}{2}c_2^2)$ 导致凹无差异曲线，而此处凹效用引致凸无差异曲线，凸显“二阶特性”作为唯一决定因素。

---

#### 3. 理论延续性
- **对上文知识点的承接**：  
  1. **偏好谱系显性化**：  
     - 上文通过离散赌注验证“二阶特性”公理，本图以连续状态消费（$c_s, c_r$）直接展示其微观基础。  
     - 效用函数 $u = \sqrt{c_s c_r}$ 的恒定相对风险厌恶系数 1，将抽象风险态度转化为具体最优消费选择。  
  2. **市场机制与风险定价**：  
     - 预算线斜率 $-1$ 表明外部风险溢价为零，Sam 的交易行为完全由自身效用二阶特性驱动，强化“风险决策单一决定因素”结论。  
  3. **拓展意义**：  
     - 点 $e$ 到 $a$ 的潜在路径具象化上文“(b)中拒绝低期望财富赌注”的逻辑：此处 Sam 主动平滑消费，因风险厌恶使波动消耗效用；若为风险爱好者（上文凸效用），则会偏离至 $e$ 类点。

> **核心结论**：预算线与效用函数的几何交点（如 $a$）揭示风险厌恶者的最优决策——**在完备公平市场中，消费平滑是二阶特性驱动的必然结果，且唯一依赖于效用函数的凹凸性而非外部环境**。

---
### Page/Slide 10



### 当前图片内容提取

#### 文字与公式
- **页码及标题**：170 UNCERTAINTY (Ch. 12)  
- **问题 (a)**：How many units of consumption is it optimal for Sam to consume conditional on rain? **20 units.**  
- **问题 (b)**：How many rain coupons is it optimal for Sam to buy? **10.**  
- **习题 12.8 (0)**：  
  > Sidewalk Sam’s brother Morgan von Neumann is an expected utility maximizer. His von Neumann-Morgenstern utility function for wealth is $u(c) = \ln c$. Sam’s brother also sells sunglasses on another beach in Atlantic City and makes exactly the same income as Sam does. He can make exactly the same deal with the casino as Sam can.  
  - **(a)** If Morgan believes that there is a 50% chance of rain and a 50% chance of sun every day, what would his expected utility of consuming $(c_s, c_r)$ be?  
    **$ u = \frac{1}{2} \ln c_s + \frac{1}{2} \ln c_r $.**  
  - **(b)** How does Morgan’s utility function compare to Sam’s? Is one a monotonic transformation of the other?  
    **Morgan’s utility function is just the natural log of Sam’s, so the answer is yes.**  
  - **(c)** What will Morgan’s optimal pattern of consumption be? Answer: Morgan will consume **20** on the sunny days and **20** on the rainy days. How does this compare to Sam’s consumption?  
    **This is the same as Sam’s consumption.**  
- **习题 12.9 (0)**：  
  > Billy John Pigs of Mule Shoe, Texas, has a von Neumann-Morgenstern utility function of the form $u(c) = \sqrt{c}$. Billy John also weighs about 300 pounds and can outrun jackrabbits and pizza delivery trucks. Billy John is beginning his senior year of college football. If he is not seriously injured, he will receive a $1,000,000 contract for playing professional football. If an injury ends his football career, he will receive a $10,000 contract as a refuse removal facilitator in his home town. There is a 10% chance that Billy John will be injured badly enough to end his career.  
  - **(a)** What is Billy John’s expected utility?  
    **We calculate $ .1 \sqrt{10,000} + .9 \sqrt{1,000,000} = 910 $.**  

---

### 内容解析（结合上文知识点）
#### 1. Morgan von Neumann 的效用函数与风险态度
- **效用函数对比**：  
  - 上文知识点中，Sam 的效用函数在 $\pi = 0.5$ 下简化为 $u(c_s, c_r) = \sqrt{c_s c_r}$（即 $\sqrt{c_s c_r}$）。  
  - Morgan 的期望效用 $u = \frac{1}{2} \ln c_s + \frac{1}{2} \ln c_r = \ln(\sqrt{c_s c_r})$ 是 Sam 效用函数的**单调变换**（自然对数）。  
  - 这直接验证了上文核心结论：**效用函数的凹凸性（二阶特性）决定风险态度，而非具体形式**。单调变换不改变偏好序，因此 Morgan 与 Sam 的最优决策一致（均选择 $c_s = c_r = 20$），体现了风险厌恶行为的普适性。  
- **决策含义**：  
  - 两者均通过交易实现消费平滑（$c_s = c_r$），与上文图表中点 $a$（20,20）的完全保险状态一致。  
  - 这强化了上文观点：在完备公平市场中，风险厌恶者会消除消费波动；决策唯一依赖于效用函数的凹性（此处 $u''(c) < 0$），与预期财富无关。

#### 2. Billy John Pigs 的期望效用计算
- **效用函数特性**：  
  - Billy John 的效用函数 $u(c) = \sqrt{c}$ 是**凹函数**（$u''(c) = -\frac{1}{4}c^{-3/2} < 0$），与上文 Sam 的效用函数同属风险厌恶类（上文已论证 $\sqrt{c_s c_r}$ 的凹性）。  
  - 其计算 $0.1 \sqrt{10,000} + 0.9 \sqrt{1,000,000} = 910$ 展示了**期望效用的具体化**：低概率高损失（ injury）通过凹性放大效用损失，符合风险厌恶者的决策逻辑。  
- **与上文的延续性**：  
  - 本例延伸了上文“风险溢价符号由偏好类型决定”的结论：若 Billy John 面临赌注，其会选择避免风险（隐含正风险溢价），且优化路径与 Sam 一致（消费平滑优先）。  
  - 量化计算（910）具象化了上文“离散赌注分析拓展至连续偏好”的框架，确认效用凹性直接驱动行为，无需依赖市场完备性（此处仅单期决策）。  

> **关键衔接**：Morgan 和 Billy John 的案例共同验证了上文“效用函数二阶特性是风险态度的唯一决定因素”——无论效用形式（对数、根号或乘积），凹性均导致相同风险厌恶行为，且单调变换不改变最优选择。这进一步驳斥了风险态度依赖外部环境的误解（如预算线斜率），重申决策内生于偏好结构。

---
### Page/Slide 11



## 提取图片内容

### 文字与公式
- **(b)** If Billy John pays \$p for an insurance policy that would give him \$1,000,000 if he suffered a career-ending injury while in college, then he would be sure to have an income of \$1,000,000 - p no matter what happened to him. Write an equation that can be solved to find the largest price that Billy John would be willing to pay for such an insurance policy.  
  **The equation is** $ 910 = \sqrt{1,000,000 - p} $.

- **(c)** Solve this equation for $p$. $ p = 171,900 $.

- **12.10 (1)** You have \$200 and are thinking about betting on the Big Game next Saturday. Your team, the Golden Boars, are scheduled to play their traditional rivals the Robber Barons. It appears that the going odds are 2 to 1 against the Golden Boars. That is to say if you want to bet \$10 on the Boars, you can find someone who will agree to pay you \$20 if the Boars win in return for your promise to pay him \$10 if the Robber Barons win. Similarly if you want to bet \$10 on the Robber Barons, you can find someone who will pay you \$10 if the Robber Barons win, in return for your promise to pay him \$20 if the Robber Barons lose. Suppose that you are able to make as large a bet as you like, either on the Boars or on the Robber Barons so long as your gambling losses do not exceed \$200. (To avoid tedium, let us ignore the possibility of ties.)

- **(a)** If you do not bet at all, you will have \$200 whether or not the Boars win. If you bet \$50 on the Boars, then after all gambling obligations are settled, you will have a total of **300** dollars if the Boars win and **150** dollars if they lose. On the graph below, use blue ink to draw a line that represents all of the combinations of “money if the Boars win” and “money if the Robber Barons win” that you could have by betting from your initial \$200 at these odds.

---

## 内容解析

### Billy John 保险问题（习题 12.9(b)(c)）  
- **方程含义与风险厌恶的延续**  
  方程 $ 910 = \sqrt{1,000,000 - p} $ 直接源于上文**风险厌恶者追求确定性等价**的核心逻辑：  
  - 左侧 $910$ 是 Billy John 无保险时的**预期效用**（上文已计算：$0.9 \sqrt{1,000,000} + 0.1 \sqrt{10,000} = 910$），代表其对风险态度的真实偏好。  
  - 右侧 $\sqrt{1,000,000 - p}$ 表示购买保险后**确定性收入**的效用（收入恒为 $1,000,000 - p$），因效用函数 $u(c) = \sqrt{c}$ 严格凹（$u''(c) < 0$），其凸性确保风险厌恶者会接受此方程作为**最大支付价格的决策条件**——支付 $p$ 后效用不低于预期效用时，方为最优。  
  - 此方程不依赖外部环境（如保费模式），仅由**效用函数的凹性**驱动，延续了上文“风险态度内生于偏好二阶特性”的结论（单调变换不影响决策，但凹性严格决定保险需求）。

- **$p = 171,900$ 的隐含经济含义**  
  - 求解结果 $p = 171,900$ 量化了**确定性等价收入**的实现路径：  
    - 无保险时预期财富为 $0.1 \times 10,000 + 0.9 \times 1,000,000 = 901,000$，但因效用凹性，等效确定性收入仅 $910^2 = 828,100$。  
    - $p$ 使支付后确定性收入 $1,000,000 - p = 828,100$，恰好等于确定性等价收入，隐含**风险溢价** $901,000 - 828,100 = 72,900$（无重复上文，仅点明此溢价由偏好内生）。  
  - 与上文 Sam 和 Morgan 案例一致，此结果验证**完备公平市场中风险厌恶者必然消除消费波动**：Billy John 以 $p$ 交换后， Consumption 在所有状态下相等（$c_s = c_r = 828,100$），对应上文图表中完全保险的均衡点 $a$。

### 赌注问题简介（习题 12.10(a)）  
- **预算线构造与风险偏好关联**  
  - 文字描述的赌注场景（初始财富 \$200，2:1 逆赔率）定义了**状态空间预算约束**：  
    - 设 $c_s$ = “Boars 赢时财富”， $c_r$ = “Robber Barons 赢时财富”。  
    - 比例 2:1 暗示市场定价隐含概率（Boars 获胜概率 $1/3$），但更关键的是**公平赌注特性**：  
      $$ c_s = 600 - 2c_r \quad \text{（由赌注规则推导）} $$  
      此线性约束的斜率为 $-2$，对应上文“公平保险市场”的预算线（斜率 $-\pi/(1-\pi)$），此处 $\pi = 1/3$ 使 $-\pi/(1-\pi) = -0.5$，但因赔率结构不同，实际几何意义一致——**无套利条件下，预算线斜率反映状态间相对价格**。  
  - 与上文知识的连续性：  
    - 该预算线是上文“离散赌注分析”向**连续决策环境**的自然延伸，但强调**初始财富与赌注限额**（损失不超过 \$200）对可行集的限制（如 $c_r \geq 0$, $c_s \geq 0$），为后续效用最大化提供约束基础。  
    - 风险厌恶者（如 $u(c) = \sqrt{c}$）将在该预算线上选择平滑消费点（$c_s = c_r$），重现上文“消费平滑是风险厌恶最优解”的核心结论。

---
### Page/Slide 12



### 当前图片解析

#### 1. 提取文字与公式
- **图表标题与轴标签**：
  - X-axis: "Money if the Boars win"（$\text{Boars 获胜时的货币}$）
  - Y-axis: "Money if the Boars lose"（$\text{Boars 失利时的货币}$）
- **图例与点标记**：
  - "Red line"（红线）
  - "Blue line"（蓝线）
  - 点：e, d, c
- **正文文字**：
  - (b) Label the point on this graph where you would be if you did not bet at all with an E.
  - (c) After careful thought you decide to bet \$50 on the Boars. Label the point you have chosen on the graph with a C. Suppose that after you have made this bet, it is announced that the star Robber Baron quarterback suffered a sprained thumb during a tough economics midterm examination and will miss the game. The market odds shift from 2 to 1 against the Boars to “even money” or 1 to 1. That is, you can now bet on either team and the amount you would win if you bet on the winning team is the same as the amount that you would lose if you bet on the losing team. You cannot cancel your original bet, but you can make new bets at the new odds. Suppose that you keep your first bet, but you now also bet \$50 on the Robber Barons at the new odds. If the Boars win, then after you collect your winnings from one bet and your losses from the other, how much money will you have left? **\$250**. If the Robber Barons win, how much money will you have left after collecting your winnings and paying off your losses? **\$200**.
  - (d) Use red ink to draw a line on the diagram you made above, showing the combinations of “money if the Boars win” and “money if the Robber Barons win” that you could arrange for yourself by adding possible bets at the new odds to the bet you made before the news of the quarterback’s misfortune. On this graph, label the point D that you reached by making the two bets discussed above.
  - 12.11 (2) The certainty equivalent of a lottery is the amount of money you would have to be given with certainty to be just as well-off with that lottery. Suppose that your von Neumann-Morgenstern utility function

#### 2. 图表解析（结合上文知识点）

##### 关键方程与预算线
- **蓝线（原始预算约束）**：  
  基于上文知识点总结中“比例 2:1 暗示市场定价隐含概率”和推导的方程 $ c_s = 600 - 2c_r $，其中：
  - $ c_s $：Boars 获胜时的财富（X-axis）
  - $ c_r $：Boars 失利时的财富（Y-axis）  
  斜率 $-2$ 源于 2:1 逆赔率，体现无套利条件下**状态间相对价格**（对应上文“预算线斜率反映状态间相对价格”）。初始财富 \$200 定义了可行集边界：
  - 点 E（无赌注）：$ (c_s, c_r) = (200, 200) $（需手动标注）
  - 点 C（赌 \$50）：$ (c_s, c_r) = (300, 150) $，与上文“赌注规则推导”的终点一致。

- **红线（新预算约束）**：  
  赔率变为 1:1 后，新增赌注的预算线斜率因状态概率调整而变化。结合点 C 的初始位置（$ c_s = 300 $, $ c_r = 150 $），新约束方程为：  
  $$
  c_s + c_r = 450
  $$  
  斜率 $-1$ 源于 1:1 赔率的**公平定价特性**（隐含状态等概率，与上文“公平保险市场预算线”逻辑同源）。此线表示在保留首次赌注前提下，通过新赌注可实现的财富组合集。

##### 点与动态含义
- **点 C（300, 150）**：  
  首次赌 \$50 的结果，体现上文“初始财富与赌注限额对可行集的限制”。财富高度分散（\$300 vs \$150），验证了未平滑消费对风险厌恶者的不利性（若效用函数 $ u(c) = \sqrt{c} $，此点劣于平滑点）。

- **点 D（250, 200）**：  
  新增 \$50 赌注 Robber Barons 的结果（$ c_s = 250 $, $ c_r = 200 $），落于红线。与点 C 相比：
  - 财富离散度从 150 降至 50（\$300→\$250 vs \$150→\$200）
  - 更接近 $ c_s = c_r $ 的平滑消费点（此处 \$225），体现**新信息（四分卫受伤）导致状态价格变动能诱导风险厌恶者主动对冲**（hedge），直接呼应上文“风险厌恶者通过保险需求消除消费波动”的核心结论。

- **点 E（200, 200）**：  
  无赌注点，代表确定性等价点（certainty equivalent）。在蓝线上，它是风险厌恶者可能选择的基准；若效用函数严格凹（$ u''(c) < 0 $），初始预算线均优于此点（因赌注允许正期望收益），但分散风险后点 D 更贴近 E 的平滑性。

##### 图表动态的经济意义
- **蓝线到红线的旋转**：  
  赔率变动（2:1 → 1:1）**改变状态价格比**，使预算线从斜率 -2 转为 -1。这类似上文保险市场中保费变化的均衡调整，但此处由**外生信息冲击**驱动（四分卫受伤降低 Boars 获胜概率），体现“市场定价反映新信息”原则。
  
- **风险偏好验证**：  
  点 D 的 $ c_s \approx c_r $ 选择与上文 Billy John 案例一致——**风险厌恶者在新约束下追求消费平滑**。点 D 的效用 $ \sqrt{250} $ 和 $ \sqrt{200} $ 更接近，隐含风险溢价减少，呼应了上文“确定性等价收入”的量化逻辑（无重复计算，仅强调行为一致性）。  
  若效用最大化，风险厌恶者会沿红线选择 $ c_s = c_r = 225 $ 点，完全消除波动，重现上文“消费平滑是风险厌恶最优解”结论。

综上，该图通过**状态空间预算约束的动态变化**，直观展示了信息更新如何重塑风险决策可行集，为后续效用最大化分析提供几何框架，无缝衔接上文状态偏好理论的核心逻辑。

---
### Page/Slide 13



### 提取内容  
**文字与公式摘要**（基于图片第173页）：  

- **效用函数定义**：  
  $ U(x,y,\pi) = \pi \sqrt{x} + (1-\pi) \sqrt{y} $  
  其中，$ \pi $ 是事件1发生的概率，$ 1-\pi $ 是事件1不发生的概率。  

- **问题 (a)**：  
  > If $ \pi = .5 $, calculate the utility of a lottery that gives you \$10,000 if Event 1 happens and \$100 if Event 1 does not happen.  
  **答案**： $ 55 = .5 \times 100 + .5 \times 10 $  
  *注：隐含计算为 $ .5 \times \sqrt{10,000} + .5 \times \sqrt{100} = .5 \times 100 + .5 \times 10 $.*  

- **问题 (b)**：  
  > If you were sure to receive \$4,900, what would your utility be?  
  **答案**： $ 70 $  
  *注：$ \sqrt{4,900} = 70 $，因确定性收入对应 $ x = y = 4,900 $。*  

- **问题 (c)**：  
  > Given this utility function and $ \pi = .5 $, write a general formula for the certainty equivalent of a lottery that gives you \$x if Event 1 happens and \$y if Event 1 does not happen.  
  **答案**： $ (.5 x^{1/2} + .5 y^{1/2})^2 $  

- **问题 (d)**：  
  > Calculate the certainty equivalent of receiving \$10,000 if Event 1 happens and \$100 if Event 1 does not happen.  
  **答案**： \$3,025  
  *注：代入 (c) 得 $ (.5 \times 100 + .5 \times 10)^2 = 55^2 = 3,025 $。*  

- **问题 12.12 (0)**：  
  > Dan Partridge is a risk averter who tries to maximize the expected value of $ \sqrt{c} $, where $ c $ is his wealth. Dan has \$50,000 in safe assets and he also owns a house that is located in an area where there are lots of forest fires. If his house burns down, the remains of his house and the lot it is built on would be worth only \$40,000, giving him a total wealth of \$90,000. If his home doesn’t burn, it will be worth \$200,000 and his total wealth will be \$250,000. The probability that his home will burn down is .01.  
  **(a) Expected utility without insurance**： \$498  
  **(b) Certainty equivalent without insurance**： \$248,004  
  **(c) Fully insured wealth**：  
  > If Dan buys \$160,000 worth of insurance, he will be fully insured in the sense that no matter what happens his after-tax wealth will be \$248,400.  

---

### 解析  
当前图片内容与【上文知识点总结】形成紧密的连续性，**无需重复确定性等价收入（certainty equivalent）的定义**，但通过具体计算验证了其核心逻辑：  

1. **效用函数风险厌恶属性的直接体现**：  
   - 公式 $ U = \pi \sqrt{x} + (1-\pi) \sqrt{y} $ 中，$ \sqrt{c} $ 的凹性（$ u''(c) < 0 $）呼应上文“风险厌恶者偏好消费平滑”的结论。  
   - 问题 (a) 的效用计算（$ 55 $）与 (b) 的确定性收入效用（$ 70 $）对比，直观展示风险厌恶：**彩票期望效用（$ 55 $）低于确定性等价收入效用（$ 70 $)**，印证上文“风险厌恶者为规避风险愿接受低于期望值的确定收入”。  

2. **确定性等价收入的量化验证**：  
   - 问题 (c) 和 (d) 的公式 $ (.5 x^{1/2} + .5 y^{1/2})^2 $ 及结果 \$3,025，是上文“certainty equivalent”概念的**数学实现**：  
     - 它严格推导自 $ U(\text{CE}) = E[U] $，即 $ \sqrt{\text{CE}} = \pi \sqrt{x} + (1-\pi) \sqrt{y} $。  
     - 与上文 Billy John 案例逻辑一致——**风险溢价 = 期望财富 - CE**（此处 \$5,050 - \$3,025 = \$2,025），量化了风险厌恶的成本。  
   - 12.12(b) 的 \$248,004 深化此点：  
     - 期望财富 = $ .01 \times 90,000 + .99 \times 250,000 = 248,400 $，  
     - **CE (\$248,004) < 期望财富 (\$248,400)**，直接体现“风险厌恶者接受财富减少以换取确定性”，与上文点 D 逼近 $ c_s = c_r $ 的平滑消费目标同源。  

3. **与上文图表逻辑的隐性衔接**：  
   - 虽无显式图表，但 12.12(c) 的“完全保险后财富固定为 \$248,400”隐含**状态空间预算线旋转**：  
     - 保险市场以 “1 美元保费对应 100 美元赔付” 定价，**隐含状态价格比趋近 1:1**（类比上文红线预算线），使风险厌恶者实现消费平滑（$ c_s = c_r $）。  
   - 此现象是上文“赔率变动驱动风险对冲”（如点 D 的生成）的**直接拓展**——外生风险（火灾概率 .01）通过保险机制被内生化，最终效用逼近上文确定性点 E。  

综上，本页通过**数值实例强化了上文理论框架**：风险厌恶者的核心行为逻辑（期望效用最大化导向消费平滑）在计算中被严格复现，且保险案例无缝承接了预算线动态调整的微观机制，为后续政策分析（如保险需求）提供可操作化基础。

---
### Page/Slide 14



### 提取内容  
**文字与公式：**  
- `(d) Therefore if he buys full insurance, the certainty equivalent of his wealth is $248,400, and his expected utility is $\sqrt{248,800}$.`  
- `12.13 (0) Portia has been waiting a long time for her ship to come in and has concluded that there is a 25% chance that it will arrive today. If it does come in today, she will receive $1,600. If it does not come in today, it will never come and her wealth will be zero. Portia has a von Neumann-Morgenstern utility such that she wants to maximize the expected value of $\sqrt{c}$, where $c$ is total income. What is the minimum price at which she will sell the rights to her ship? $100$.`  

---

### 解析  
#### (1) Dan 全保险案例延续（对应图片 (d)）  
- **数值逻辑衔接上文**：  
  上文已明确全保险时财富固定为 $\$248,400$（通过 $160,000$ 美元保险对冲风险）。因此，**确定性等价**（certainty equivalent）应等于实际财富 $\$248,400$（因无风险），期望效用为 $u(248,400) = \sqrt{248,400}$。图片中写为 $\sqrt{248,800}$，属印刷误差（实际计算：$\sqrt{248,400} \approx 498.4$，而无保险期望效用为 $498$，符合“全保险劣后于确定性财富但优于风险状态”的逻辑）。  
- **核心机制验证**：  
  此结果强化上文“保险实现消费平滑”结论：  
  - 固定财富 $c_s = c_r = 248,400$（状态空间预算线退化为点），消除了火灾风险。  
  - 期望效用 $\sqrt{248,400} > 498$（无保险时），印证上文“风险溢价成本被保险覆盖”，直接对应点 **D** 的效用提升路径。  

#### (2) Portia 案例（12.13）  
- **与上文理论的连续性**：  
  Portia 的效用函数 $u(c) = \sqrt{c}$ 与 Dan 相同（风险厌恶，$u''(c) < 0$），延续**确定性等价收入**的量化逻辑：  
  - 期望财富：$E[c] = 0.25 \times 1600 + 0.75 \times 0 = \$400$。  
  - 期望效用：$E[U] = 0.25 \times \sqrt{1600} + 0.75 \times \sqrt{0} = 10$。  
  - **确定性等价**：$CE$ 满足 $\sqrt{CE} = E[U] = 10$，故 $CE = 100$。  
- **行为经济学含义**：  
  - 最低出售价 $\$100$ 严格等于 $CE$，体现“风险厌恶者为消除不确定性，愿牺牲部分期望财富”（风险溢价 $= E[c] - CE = 300$）。  
  - 与上文 Billy John 案例同源：**$CE$ 是效用等价的确定收入阈值**，直接延伸了“风险成本内生化”框架（此处通过资产出售实现风险转移）。  

#### (3) 整体知识衔接  
- 本页无独立图表，但 Dan 的 $(d)$ 和 Portia 问题共同**实证化上文风险对冲机制**：  
  - 全保险使 Dan 达到 $c_s = c_r$（效用最大化点 **E** 的逼近），Portia 通过出售权将风险转移至外部，均体现“风险厌恶者通过市场工具将随机财富转化为确定等价”。  
  - 12.13 的 $\$100$ 解是上文确定性等价定义在离散二元状态下的直接应用，为后续保险需求分析提供微观基础（如保费与风险溢价关系）。
