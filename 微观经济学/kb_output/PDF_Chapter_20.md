# PDF_Chapter_20

### Page/Slide 1



# 当前图片内容解析

## 1. 文字与公式提取

### 章节信息
- Chapter 20
- Cost Minimization

### 核心概念文本
> In the chapter on consumer choice, you studied a consumer who tries to maximize his utility subject to the constraint that he has a fixed amount of money to spend. In this chapter you study the behavior of a firm that is trying to produce a fixed amount of output in the cheapest possible way. In both theories, you look for a point of tangency between a curved line and a straight line. In consumer theory, there is an "indifference curve" and a "budget line." In producer theory, there is a "production isoquant" and an "isocost line." As you recall, in consumer theory, finding a tangency gives you only one of the two equations you need to locate the consumer’s chosen point. The second equation you used was the budget equation. In cost-minimization theory, again the tangency condition gives you one equation. This time you don’t know in advance how much the producer is spending; instead you are told how much output he wants to produce and must find the cheapest way to produce it. So your second equation is the equation that tells you that the desired amount is being produced.

### 例题文本
> A firm has the production function $f(x_1, x_2) = (\sqrt{x_1} + 3\sqrt{x_2})^2$. The price of factor 1 is $w_1 = 1$ and the price of factor 2 is $w_2 = 1$. Let us find the cheapest way to produce 16 units of output. We will be looking for a point where the technical rate of substitution equals $-w_1/w_2$. If you calculate the technical rate of substitution (or look it up from the warm up exercise in Chapter 18), you find $TRS(x_1, x_2) = -(1/3)(x_2/x_1)^{1/2}$. Therefore we must have $-(1/3)(x_2/x_1)^{1/2} = -w_1/w_2 = -1$. This equation can be simplified to $x_2 = 9x_1$. So we know that the combination of inputs chosen has to lie somewhere on the line $x_2 = 9x_1$. We are looking for the cheapest way to produce 16 units of output. So the point we are looking for must satisfy the equation $(\sqrt{x_1} + 3\sqrt{x_2})^2 = 16$, or equivalently $\sqrt{x_1} + 3\sqrt{x_2} = 4$. Since $x_2 = 9x_1$, we can substitute for $x_2$ in the previous equation to get $\sqrt{x_1} + 3\sqrt{9x_1} = 4$. This equation simplifies further to $10\sqrt{x_1} = 4$. Solving this for $x_1$, we have $x_1 = 16/100$. Then $x_2 = 9x_1 = 144/100$.

> The amounts $x_1$ and $x_2$ that we solved for in the previous paragraph are known as the conditional factor demands for factors 1 and 2, conditional on the wages $w_1 = 1$, $w_2 = 1$, and output $y = 16$. We express this by saying $x_1(1,1,16) = 16/100$ and $x_2(1,1,16) = 144/100$. Since we know the amount of each factor that will be used to produce 16 units of output and since we know the price of each factor, we can now calculate the cost of producing 16 units. This cost is $c(w_1,w_2,16) = w_1x_1(w_1,w_2,16) + w_2x_2(w_1,w_2,16)$. In this instance since $w_1 = w_2 = 1$, we have $c(1,1,16) = x_1(1,1,16) + x_2(1,1,16) = 160/100$.

### 关键公式
1. **生产函数**：$f(x_1, x_2) = (\sqrt{x_1} + 3\sqrt{x_2})^2$  
2. **技术替代率**：$\text{TRS}(x_1, x_2) = -\dfrac{1}{3}\left(\dfrac{x_2}{x_1}\right)^{1/2}$  
3. **切点条件**：$-\dfrac{1}{3}\left(\dfrac{x_2}{x_1}\right)^{1/2} = -\dfrac{w_1}{w_2}$  
4. **要素投入关系**：$x_2 = 9x_1$  
5. **产量约束**：$\sqrt{x_1} + 3\sqrt{x_2} = 4$  
6. **条件要素需求**：  
   - $x_1(1,1,16) = \dfrac{16}{100}$  
   - $x_2(1,1,16) = \dfrac{144}{100}$  
7. **成本函数**：$c(1,1,16) = \dfrac{160}{100}$  

---

## 2. 理论逻辑与推导要点

### 对偶关系强化
延续消费者理论中**无差异曲线-预算线切点**逻辑，此处**等产量线（$f(x_1,x_2)=y$）与等成本线（$w_1x_1+w_2x_2=c$）切点**满足：
- 生产理论：$\text{TRS} = -\dfrac{w_1}{w_2}$
- 消费理论：$\text{MRS} = -\dfrac{p_1}{p_2}$

### 例题推导的经济逻辑
1. **切点条件的经济学意义**：  
   $\text{TRS}$ 反映要素间技术替代能力，$w_1/w_2$ 体现要素市场相对价格。当二者相等时，厂商无法通过调整投入比例降低成本（即处于成本最小化状态）。

2. **约束方程的选择依据**：  
   消费者理论使用**预算约束**作为第二方程，此处因产量固定，使用**产量约束** $(\sqrt{x_1} + 3\sqrt{x_2})^2 = 16$ 作为第二方程，形成闭合解。

3. **条件要素需求的特性**：  
   $x_1(w_1,w_2,y), x_2(w_1,w_2,y)$ 本质是**生产侧的希克斯需求**：  
   - 仅依赖**要素价格**和**目标产量**（类比希克斯需求依赖价格和效用水平）  
   - 与一阶条件 $\text{TRS} = -w_1/w_2$ 联立求解，体现成本最小化的必要条件  

4. **成本计算的直接应用**：  
   通过 $c(w_1,w_2,y) = w_1x_1 + w_2x_2$ 将要素需求转化为**最小总成本**，此处 $c=1.6$ 表明：  
   - 当两要素同价时，成本由最优投入组合的加权和决定  
   - $x_2:x_1=9:1$ 体现要素替代弹性（由生产函数形式决定）  

### 理论延续性说明
本例具体化了前文**成本最小化的数学表述**：  
1. **切点条件**提供边际上要素替代的技术-市场匹配  
2. **产量约束**锁定可行解范围  
3. 二者共同导出**条件要素需求**，为后续推导**成本函数性质**（如规模报酬影响）奠定基础。  
（注：无图表，故无变化趋势分析）

---
### Page/Slide 2



### 1. 文字与公式提取  
#### 文字内容  
- **生产背景**：Nadine 的软件生产函数为 $ f(x_1, x_2) = x_1 + 2x_2 $，其中 $ x_1 $ 为非熟练劳动力，$ x_2 $ 为熟练劳动力。  
- **问题 (a)**：要求绘制产出 20 单位和 40 单位的等产量线。  
- **问题 (b)**：判断规模报酬性质 → **Constant**（常数）。  
- **问题 (c)**：仅用非熟练劳动力生产 $ y $ 单位输出 → 需 $ x_1 = y $。  
- **问题 (d)**：仅用熟练劳动力生产 $ y $ 单位输出 → 需 $ x_2 = \dfrac{y}{2} $。  
- **问题 (e)**：要素价格为 $ (1,1) $，生产 20 单位的最小成本解 → $ x_1 = 0 $，$ x_2 = 10 $。  

#### 公式  
- **生产函数**：$ f(x_1, x_2) = x_1 + 2x_2 $  
- **成本最小化解**：$ x_1 = 0,\ x_2 = 10 $（对应 $ y = 20 $，$ w_1 = w_2 = 1 $）  

---

### 2. 图表分析与理论延伸  
#### 图表关键特征  
- **类型**：等产量线（Isoquant）图。  
- **坐标轴**：横轴为非熟练劳动力 $ x_1 $，纵轴为熟练劳动力 $ x_2 $。  
- **等产量线**：  
  - $ y = 20 $：直线 $ x_2 = 10 - \dfrac{1}{2}x_1 $，斜率 $ -\dfrac{1}{2} $。  
  - $ y = 40 $：直线 $ x_2 = 20 - \dfrac{1}{2}x_1 $，斜率同上。  

#### 经济含义  
1. **完全替代技术特性**：  
   生产函数 $ f(x_1, x_2) = x_1 + 2x_2 $ 为**线性函数**，反映要素间**完全替代**关系。  
   - **边际技术替代率（TRS）** 为常数：  
     $$
     \text{TRS} = -\dfrac{MP_1}{MP_2} = -\dfrac{1}{2}
     $$  
   - 与上文非线性生产函数（如 $ (\sqrt{x_1} + 3\sqrt{x_2})^2 $）形成对比：  
     - 上文需满足切点条件 $ \text{TRS} = -w_1/w_2 $，得到**内部解**（正的要素需求）；  
     - 此处因 TRS 为常数，当 $ w_1/w_2 \neq |TRS| $ 时，**最优解位于边界**（角点解）。  

2. **问题 (e) 的边界解逻辑**：  
   - 要素价格比 $ w_1/w_2 = 1 $，而 $ |TRS| = \dfrac{1}{2} $，表明：  
     - 每单位成本下，使用 $ x_2 $ 的边际产出更高（$ \dfrac{MP_2}{w_2} = 2 > \dfrac{MP_1}{w_1} = 1 $）。  
   - **结论**：厂商仅使用 $ x_2 $ 生产，成本最低。  
     - 验证：$ f(0, 10) = 0 + 2 \times 10 = 20 $，总成本 $ c = 0 \times 1 + 10 \times 1 = 10 $。  
     - 若使用 $ x_1 $，需 $ f(20, 0) = 20 $，总成本为 20，效率更低。  

3. **与上文理论的衔接**：  
   - 上文强调**边界解（corner solution）** 的可能性（"kinks and boundary solutions"），此例具体化：  
     - 当生产技术允许完全替代时，要素价格比偏离 TRS 会导致单一要素投入。  
   - **规模报酬恒定**（问题 b）的根源：  
     $ f(tx_1, tx_2) = tx_1 + 2tx_2 = t \cdot f(x_1, x_2) $，与上文产量约束分析方法一致但技术特性不同。  

---

### 3. 核心结论  
- **线性生产函数的特殊性**：  
  TRS 恒定导致成本最小化方向为**极值解**（仅使用一种要素），而非上文通过联立方程求得的内点解。  
- **决策逻辑一致性**：  
  延续上文 "成本最小化 = 技术替代能力与要素价格匹配" 核心思想，但此处因技术限制，最优解被迫位于解集边界。  
- **实践启示**：  
  当要素间完全替代时，厂商会彻底淘汰低效要素（如本例中非熟练劳动力），直接反映要素效率与价格的主导作用。

---
### Page/Slide 3



### 当前图片内容解析

#### 1. 文字与公式提取
- **问题 (f)**:  
  If Nadine faces factor prices (1,3), what is the cheapest way for her to produce 20 units of output? $ x_1 = 20 $, $ x_2 = 0 $.  

- **问题 (g)**:  
  If Nadine faces factor prices $(w_1, w_2)$, what will be the minimal cost of producing 20 units of output?  
  $ c = \min\{20w_1, 10w_2\} = 10 \min\{2w_1, w_2\} $.  

- **问题 (h)**:  
  If Nadine faces factor prices $(w_1, w_2)$, what will be the minimal cost of producing $ y $ units of output?  
  $ c(w_1, w_2, y) = \min\{w_1, w_2/2\} y $.  

- **问题 20.2 (0)**:  
  The Ontario Brassworks produces brazen effronteries. Brass is an alloy of copper and zinc, used in fixed proportions. The production function is: $ f(x_1, x_2) = \min\{x_1, 2x_2\} $, where $ x_1 $ is copper and $ x_2 $ is zinc.  

- **子问题 (a)**:  
  Illustrate a typical isoquant for this production function in the graph below.  

- **子问题 (b)**:  
  Does this production function exhibit increasing, decreasing, or constant returns to scale? **Constant**.  

- **子问题 (c)**:  
  If the firm wanted to produce 10 effronteries, how much copper would it need? **10 units**. How much zinc would it need? **5 units**.  

---

#### 2. 图表分析与经济含义
**图表描述**（基于图片中的坐标网格）:  
- **坐标轴**: 横轴为铜 $ x_1 $（范围 0–40），纵轴为锌 $ x_2 $（范围 0–40）。  
- **等产量线特征**:  
  - 一条 L 形等产量线，水平段位于 $ x_2 = 10 $（$ x_1 \geq 10 $），垂直段位于 $ x_1 = 20 $（$ x_2 \geq 10 $），拐点在 $ (x_1, x_2) = (20, 10) $。  
  - 标注箭头指向对角线 $ x_2 = \frac{1}{2} x_1 $，表示所有拐点的连线路径。  
- **隐含产出水平**: 以拐点 $ (20, 10) $ 为例，代入生产函数 $ f(20, 10) = \min\{20, 2 \times 10\} = \min\{20, 20\} = 20 $，对应产出 20 单位。类似地，拐点 $ (x_1, x_2) = (y, y/2) $ 定义产出 $ y $ 的等产量线。  

**结合上文的含义解析**（延续技术替代与成本逻辑）:  
- **技术特性对比**:  
  - 上文线性生产函数 $ f(x_1, x_2) = x_1 + 2x_2 $ 体现**完全替代**（等产量线为直线，TRS 常数），最优解取决于要素价格比与 $ |\text{TRS}| = 1/2 $ 的匹配：  
    - 当 $ w_1/w_2 > |\text{TRS}| $（如问题 (f) 中 $ 1/3 < 1/2 $），厂商**仅用 $ x_1 $**（边界解 $ x_1 = 20, x_2 = 0 $）。  
  - 本图表的生产函数 $ f(x_1, x_2) = \min\{x_1, 2x_2\} $ 体现**完全互补**（固定比例技术）：  
    - 等产量线呈 L 形，**无替代弹性**。拐点轨迹 $ x_2 = \frac{1}{2} x_1 $ 表示效率前沿（$ x_1 = y $ 且 $ x_2 = y/2 $），任意偏离（如 $ x_2 > y/2 $ 但 $ x_1 < y $）均无法增产，仅造成浪费。  
    - 与上文线性案例形成核心差异：  
      | **技术类型** | **等产量线形状** | **最优解性质** | **成本最小化逻辑** |  
      |--------------|------------------|----------------|-------------------|  
      | 完全替代 (上文) | 直线 | 边界解（角点） | 比较 $ \text{MP}_1 / w_1 $ vs. $ \text{MP}_2 / w_2 $ |  
      | 完全互补 (本图表) | L 形 | 强制角点解 | 要素需严格按比例投入（$ x_1 / x_2 = 2 $） |  

- **规模报酬一致性**:  
  - 等产量线拐点位于 $ x_1 = y $, $ x_2 = y/2 $，满足 $ f(tx_1, tx_2) = t \cdot f(x_1, x_2) $，故规模报酬恒定（子问题 (b)）。这与上文问题 (b) 结论一致，但技术逻辑不同：  
    - 线性函数中，恒定规模报酬源于齐次性（$ f(tx_1, tx_2) = t f(x_1, x_2) $）；  
    - 固定比例函数中，源于要素不可拆分使用（增加 $ t $ 倍投入即得 $ t $ 倍产出）。  

- **实际应用延伸**:  
  - 子问题 (c) 中生产 10 单位需 $ x_1 = 10 $, $ x_2 = 5 $，直接验证拐点路径 $ x_2 = \frac{1}{2} x_1 $。  
  - 若要素价格变化（如 $ w_1 \ll w_2 $），厂商**无法转向单一要素**（因技术强制互补），成本最小化唯一解为 $ x_1 = y $, $ x_2 = y/2 $。这与上文线性函数的适应性边界解形成鲜明对比，凸显技术约束对要素需求的强决定作用。  

> **关键衔接**：上文强调“成本最小化 = 技术替代能力 × 要素价格”，本例则修正为“成本最小化 = 技术固定比例 × 价格压缩路径”——当替代弹性为零时，厂商失去调整自由，最优解严格绑定在拐点线上，凸显技术类型如何重塑决策框架。

---
### Page/Slide 4



### 当前图片文字与公式提取

#### 文字内容
- **标题**: 256 COST MINIMIZATION (Ch. 20)  
- **(d)** If the firm faces factor prices (1,1), what is the cheapest way for it to produce 10 effronteries? How much will this cost? It can only produce 10 units of output by using the bundle (10,5), so this is the cheapest way. It will cost $15.  
- **(e)** If the firm faces factor prices \((w_1, w_2)\), what is the cheapest cost to produce 10 effronteries? \(c(w_1, w_2, 10) = 10w_1 + 5w_2\).  
- **(f)** If the firm faces factor prices \((w_1, w_2)\), what will be the minimal cost of producing \(y\) effronteries? \((w_1 + w_2/2)y\).  
- **Calculus 20.3 (0)** A firm uses labor and machines to produce output according to the production function \(f(L, M) = 4L^{1/2}M^{1/2}\), where \(L\) is the number of units of labor used and \(M\) is the number of machines. The cost of labor is $40 per unit and the cost of using a machine is $10.  
- **(a)** On the graph below, draw an isocost line for this firm, showing combinations of machines and labor that cost $400 and another isocost line showing combinations that cost $200. What is the slope of these isocost lines? \(-4\).  
- **(b)** Suppose that the firm wants to produce its output in the cheapest possible way. Find the number of machines it would use per worker. (Hint: The firm will produce at a point where the slope of the production isoquant equals the slope of the isocost line.) \(4\).  
- **(c)** On the graph, sketch the production isoquant corresponding to an output of 40. Calculate the amount of labor \(5\) units and the number of machines \(20\) that are used to produce 40 units of output in the cheapest possible way, given the above factor prices. Calculate the cost of producing 40 units at these factor prices: \(c(40,20) = 400\).  
- **(d)** How many units of labor \(y/8\) and how many machines \(y/2\) would the firm use to produce \(y\) units in the cheapest possible way? How much would this cost? \(10y\). (Hint: Notice that there are constant returns to scale.)  

#### 公式
- 成本函数（固定比例技术）:  
  \[
  c(w_1, w_2, 10) = 10w_1 + 5w_2
  \]  
  \[
  \text{Minimal cost for } y \text{ units: } (w_1 + w_2/2)y
  \]  
- Cobb-Douglas 生产函数:  
  \[
  f(L, M) = 4L^{1/2}M^{1/2}
  \]  
- 等成本线斜率:  
  \[
  -4 \quad (\text{given } w_L = 40, \, w_M = 10)
  \]  
- 最优要素比例（机器/劳动）:  
  \[
  4
  \]  
- 成本最小化解:  
  \[
  L^* = \frac{y}{8}, \quad M^* = \frac{y}{2}, \quad \text{Cost} = 10y
  \]  
- 40 单位产出的具体数值:  
  \[
  L = 5, \quad M = 20, \quad c = 400
  \]  

---

### 经济含义解析（结合上文知识点总结）

#### 1. **固定比例技术（子部分 (d)-(f)）**  
- 当前图片中的子部分 (d)-(f) 延续了【上文知识点总结】中讨论的**完全互补技术**（固定比例），生产集满足 \(x_1 = y\) 且 \(x_2 = y/2\)（如上文拐点路径 \(x_2 = \frac{1}{2}x_1\)）。  
- **关键延续**:  
  - 成本函数 \(c = (w_1 + w_2/2)y\) 直接验证了上文结论：当替代弹性为零时，**最优解严格绑定于固定比例**，厂商无法通过价格变化调整要素组合（例如，即使 \(w_1 \ll w_2\)，仍必须使用 \(x_1 = y\) 与 \(x_2 = y/2\)）。  
  - 这与上文 "技术强制互补" 逻辑一致：最小成本路径仅取决于要素价格的线性加权，**无替代自由度**，凸显 "技术固定比例 × 价格压缩路径" 的成本最小化框架。  

#### 2. **Cobb-Douglas 技术（Calculus 20.3 部分）**  
- 当前图片中 Calculus 20.3 引入了**边际替代率递减技术**（生产函数 \(f(L, M) = 4L^{1/2}M^{1/2}\))，属于**常数替代弹性（\(\sigma = 1\)）** 案例，与上文两个极端案例形成对比：  
  | **技术类型**       | **上文案例**              | **当前 Calculus 20.3**         |  
  |--------------------|--------------------------|-------------------------------|  
  | **等产量线形状**   | L 形（完全互补）         | 凸向原点（平滑替代）           |  
  | **最优解性质**     | 强制角点解（无弹性）     | 内部切点解（弹性 > 0）        |  
  | **成本最小化逻辑** | 要素比例固定             | 比例随价格动态调整            |  

- **核心解析**:  
  - **等产量线与等成本线相切条件**: 在成本最小化时，\(\text{MRTS} = \left| \frac{w_L}{w_M} \right|\)（上文已建立的 "技术替代能力 × 要素价格" 框架）。  
    - 这里 \(\text{MRTS} = \left| \frac{MP_L}{MP_M} \right| = \frac{M}{L}\)（由生产函数导出），等成本线斜率 \(= w_L / w_M = 40/10 = 4\)。  
    - 解得最优比例 \(M/L = 4\)（问题 (b)），**直接体现价格对要素组合的调节作用**（与上文完全互补技术对比：价格变化不改变比例，此处价格驱动比例）。  
  - **规模报酬一致性**:  
    - 问题 (d) 中成本函数 \(c = 10y\) 基于常数规模报酬，满足 \(f(tL, tM) = t \cdot f(L, M)\)。  
    - 与上文规模报酬结论一致，但**技术逻辑差异显著**:  
      - 上文固定比例技术中，规模报酬恒定源于 "要素不可拆分”；  
      - 此处 Cobb-Douglas 的规模报酬恒定源于齐次性（\(\alpha + \beta = 1\)），且允许比例调整。  
  - **成本最小化路径**:  
    - 最优解 \(L^* = y/8\), \(M^* = y/2\)（问题 (d)）表明，**要素需求是价格的函数**（例如，若 \(w_M\) 下降，\(M/L\) 比例上升）。  
    - 这与上文 "边界解 vs. 角点解" 对比：此处内部解需满足 MRTS = 价格比，**替代弹性允许厂商优化组合**，区别于上文替代弹性为零时的僵化比例。  

#### 3. **知识框架整合**  
- 当前图片的 Calculus 20.3 部分**拓展了上文技术光谱**：  
  - 上文聚焦 \(\sigma = 0\)（完全互补）和 \(\sigma \to \infty\)（完全替代）的极端案例；  
  - 当前案例补充 \(\sigma = 1\) 的典型中间状态，验证 "成本最小化 = 替代弹性 × 价格信号" 的普适性：  
    - 当 \(\sigma > 0\)（如本例），厂商通过比例调整响应价格变化；  
    - 当 \(\sigma = 0\)（上文），价格仅影响成本水平，不改变比例。  
- **关键启示**: 技术参数（如替代弹性）决定了要素价格对生产决策的约束强度——本例中 MRTS 可变性使成本对价格更敏感，而上文固定比例技术则剥离了这种敏感性。

---
### Page/Slide 5



### 1. 提取当前图片内容  
#### 文字与公式  
- **题目标题与描述**  
  > `20.4 (0)` Earl sells lemonade in a competitive market on a busy street corner in Philadelphia. His production function is \( f(x_1, x_2) = x_1^{1/3} x_2^{1/3} \), where output is measured in gallons, \( x_1 \) is the number of pounds of lemons he uses, and \( x_2 \) is the number of labor-hours spent squeezing them.  

- **问题与答案**  
  (a) *Does Earl have constant returns to scale, decreasing returns to scale, or increasing returns to scale?* **Decreasing.**  
  (b) *Where \( w_1 \) is the cost of a pound of lemons and \( w_2 \) is the wage rate for lemon-squeezers, the cheapest way for Earl to produce lemonade is to use \( w_1 / w_2 \) hours of labor per pound of lemons.*  
  (c) *If he is going to produce \( y \) units in the cheapest way possible, then the number of pounds of lemons he will use is \( x_1(w_1, w_2, y) = w_2^{1/2} y^{3/2} / w_1^{1/2} \) and the number of hours of labor that he will use is \( x_2(w_1, w_2, y) = w_1^{1/2} y^{3/2} / w_2^{1/2} \).*  
  (d) *The cost to Earl of producing \( y \) units at factor prices \( w_1 \) and \( w_2 \) is \( c(w_1, w_2, y) = w_1 x_1(w_1, w_2, y) + w_2 x_2(w_1, w_2, y) = 2 w_1^{1/2} w_2^{1/2} y^{3/2} \).*  
  > `20.5 (0)` The prices of inputs \( (x_1, x_2, x_3, x_4) \) are \( (4, 1, 3, 2) \).  

- **图表信息**  
  - **坐标轴**：横轴为 Labour (0–40)，纵轴为 Machines (0–40)。  
  - **曲线**：  
    - $200 isocost line（等成本线）  
    - $400 isocost line（等成本线）  
    - 一条凸向原点的等产量线（isoquant），与两条等成本线相切。  

---

### 2. 图表解析（结合上文知识点）  
#### 关键延续：技术特性与成本最小化逻辑  
当前图表展示 **Cobb-Douglas 技术**（生产函数 \( f(x_1, x_2) = x_1^{1/3} x_2^{1/3} \)），**但与上文 Calculus 20.3 案例有本质差异**：  
- **上文 Cobb-Douglas 案例**（\( f(L, M) = 4L^{1/2}M^{1/2} \))：  
  - 规模报酬恒定（\(\alpha + \beta = 1\)），成本函数 \( c \propto y \)（线性）。  
  - 要素比例随价格动态调整，但单位成本不变。  
- **当前案例**：  
  - 规模报酬递减（\(\alpha + \beta = 2/3 < 1\)），问题 (a) 答案 "Decreasing" 直接验证此性质。  
  - 成本函数 \( c = 2 w_1^{1/2} w_2^{1/2} y^{3/2} \)（问题 (d)）表明：  
    - 成本随产量**非线性增长**（\( y^{3/2} \) 项），即边际成本递增（因 \( dc/dy \propto y^{1/2} \)）。  
    - 与上文常数规模报酬结论对比：**替代弹性仍为 1**（技术结构未变），但规模报酬下降使价格信号对成本的敏感性增强。  

#### 图表中等成本线与等产量线变化的含义  
| **要素**          | **解释**                                                                 | **与上文对比** |  
|-------------------|--------------------------------------------------------------------------|----------------|  
| **等产量线**      | 凸向原点，反映 **边际技术替代率递减**（\(\text{MRTS} = x_2 / x_1\)）。成本最小化要求 \(\text{MRTS} = w_1 / w_2\)（问题 (b) 推导）。 | 与上文 Cobb-Douglas 案例逻辑一致：技术替代能力未变，但**规模报酬差异导致成本路径不同**。 |  
| **$200 → $400 isocost 线** | 两条平行线表示成本加倍（因等成本线斜率恒定为 \( -w_1 / w_2 \))，但产量增幅 **小于 2 倍**（因 \( y \propto c^{2/3} \)）。 | 上文常数规模报酬下，$400 成本应产出 $200 成本的 2 倍产量；此处因规模报酬递减，**价格信号的调整效果被规模约束部分抵消**——厂商无法通过单一比例调整完全吸收成本变化。 |  
| **切点移动**      | $400 等成本线切点较 $200 点更远离原点，但 **产量增长速度下降**（等产量线间距随成本增加而扩大）。 | 与上文固定比例技术（\(\sigma = 0\)）对比：此处仍存在替代弹性，但**规模报酬特性抑制了价格对产出的调节范围**（上文 \(\sigma > 0\) 但常数规模报酬下，产量对成本响应为线性）。 |  

#### 核心经济含义  
- **技术参数主导约束强度**：  
  - 替代弹性 \(\sigma = 1\) 仍保证内部解（价格决定最优比例），但 **规模报酬参数**（\(\alpha + \beta\)）改写成本响应结构：  
    - 若 \(\alpha + \beta = 1\)（上文），价格信号完全映射为比例调整，成本扩张与产量同步。  
    - 若 \(\alpha + \beta < 1\)（当前），价格信号作用被规模不经济削弱，**成本最小化必须同时应对替代与规模约束**。  
- **对 "技术光谱" 的补全**：  
  本例填补上文 \(\sigma = 0\)（完全互补）与 \(\sigma = 1\)（常数规模报酬）之间的缺口——**替代弹性与规模报酬可解耦**：  
  - 同一替代弹性（\(\sigma = 1\)）下，规模报酬下降使生产决策对价格变化的敏感性降低（例如，\( w_2 \) 下降时，\( x_2 \) 增加幅度因规模不经济而受限）。  
  - 验证上文框架：成本最小化核心仍是 \(\text{MRTS} = \text{价格比}\)，但**长期成本曲线形状取决于规模报酬**（本例为凸函数）。  

> 本分析延续 "技术 × 价格" 双维框架，凸显规模报酬参数对生产决策的关键调制作用——当其与替代弹性叠加时，厂商优化路径从上文的 "纯替代驱动" 转向 "替代与规模的双重约束"。

---
### Page/Slide 6



### 提取当前图片内容  
#### 文字与公式  
**页码与标题**  
258 COST MINIMIZATION (Ch. 20)  

**问题 (a)-(d)**  
- (a) If the production function is given by \( f(x_1, x_2) = \min\{x_1, x_2\} \), what is the minimum cost of producing one unit of output? **\$5**.  
- (b) If the production function is given by \( f(x_3, x_4) = x_3 + x_4 \), what is the minimum cost of producing one unit of output? **\$2**.  
- (c) If the production function is given by \( f(x_1, x_2, x_3, x_4) = \min\{x_1 + x_2, x_3 + x_4\} \), what is the minimum cost of producing one unit of output? **\$3**.  
- (d) If the production function is given by \( f(x_1, x_2) = \min\{x_1, x_2\} + \min\{x_3, x_4\} \), what is the minimum cost of producing one unit of output? **\$5**.  

**20.6 (0) Joe Grow 问题**  
- 生产函数： \( h = \min\{l, 2w\} \) ，其中 \( h \) 为 happy plants 数量， \( l \) 为 light， \( w \) 为 water。  
- (a) Using 1 unit of light, least water for one happy plant: **1/2 unit of water**.  
- (b) Minimum inputs for 4 happy plants: **(4, 2)**.  
- (c) Conditional factor demand:  
  - Light: \( l(w_1, w_2, h) = h \)  
  - Water: \( w(w_1, w_2, h) = h/2 \)  
- (d) Cost function: \( c(w_1, w_2, h) = w_1 h + \frac{w_2}{2} h \)  

**20.7 (1) Flo Grow 问题**  
- 生产函数: \( h = t + 2f \) ，其中 \( f \) 为 fertilizer bags, \( t \) 为 talk hours.  
- Costs: Fertilizer \( w_f \) per bag, talk \( w_t \) per hour.  

---

### 解析：基于上文知识点的技术光谱补全  
当前图片未含图表，但通过解析 **固定比例（完全互补）** 与 **完全替代** 技术案例，可深化上文对技术光谱的讨论。上文已阐明：Cobb-Douglas 案例（\(\sigma = 1\)）中替代弹性与规模报酬的解耦机制，而本图片提供 \(\sigma = 0\) 和 \(\sigma = \infty\) 的极值案例，验证 **技术约束强度如何主导厂商对价格信号的响应**。  

#### 1. 完全互补技术（\(\sigma = 0\)）：固定比例生产  
- **案例**：问题 (a)、(c)、(d) 及 20.6 的 \( h = \min\{l, 2w\} \)。  
  - **技术结构**：要素必须按固定比例投入（如 Joe 例中 \( l/w = 2 \)），**替代弹性 \(\sigma = 0\)**，无替代空间。  
  - **成本含义**：  
    - 条件需求严格成比例（如 \( l(h) = h \), \( w(h) = h/2 \)），成本函数线性 \( c \propto h \)（例 20.6(d) 中 \( c = w_1 h + \frac{w_2}{2} h \))。  
    - **规模报酬恒定**（齐次度 1），边际成本恒定，与上文规模报酬递减案例 **关键差异**：  
      - 上文（规模报酬递减）：价格信号被规模不经济抑制，产量增幅 < 成本增幅（\( y \propto c^{2/3} \)）。  
      - 此处：价格变动仅改变成本水平，**不改变最优比例或产量增长路径**（因技术约束绝对垄断决策）。  
  - **对比上文**：上文指出 \(\sigma = 0\) 案例中 "无法通过单一比例调整完全吸收成本变化"，此处强化该结论——等产量线为直角折线，成本最小化切点无移动，价格信号仅影响 \( c \) 截距项。  

#### 2. 完全替代技术（\(\sigma = \infty\)）：价格驱动角点解  
- **案例**：问题 (b) 及 20.7 的 \( h = t + 2f \)。  
  - **技术结构**：要素可无成本替代，**替代弹性 \(\sigma = \infty\)**，MRTS 为常数（20.7 中 MRTS = 2）。  
  - **成本含义**：  
    - 成本最小化导致 **角点解**（e.g., 若 \( w_t / w_f < 1/2 \)，仅用 talk；否则仅用 fertilizer）。  
    - 成本函数 **分段线性**，价格小幅变动即引发要素需求突变（如 \( w_t \) 略升，需求从 talk 跳转至 fertilizer）。  
  - **对比上文**：上文强调 Cobb-Douglas 的内部解（\(\sigma = 1\)）使比例渐变，而此处验证：  
    - **替代弹性决定价格响应强度**：\(\sigma = \infty\) 时，厂商对价格敏感性最高（远超 \(\sigma = 1\) 案例），但仅限于切换要素组合，无法优化混合比例。  
    - 规模报酬恒定（线性函数齐次度 1）确保成本扩张路径为线性，**抵消了上文规模报酬递减的抑制作用**。  

#### 3. 复合技术案例：光谱连续性的实证  
- **问题 (c) \& (d)**：复合生产函数（如 \( f = \min\{x_1 + x_2, x_3 + x_4\} \))。  
  - **核心机制**：子技术组合（如互补组与互补组叠加）仍保留 **整体规模报酬恒定**（最小成本 \$3 和 \$5 均支持 \( c \propto y \)）。  
  - **经济意义**：验证上文论断——**技术光谱的本质是替代弹性分布**：  
    - 即使生产函数结构复杂（如 (d) 中双 min 函数），只要无内在规模不经济，厂商决策仍由价格信号主导替代（但此处替代仅限子系统内，因子组内 \(\sigma = 0\)）。  
    - 与上文规模报酬递减 Cobb-Douglas 对比：本复合案例 **无规模约束**，故价格变动对成本的影响更直接。  

#### 4. 对 "技术 × 价格" 框架的贡献  
- **统一逻辑**：成本最小化核心条件 \(\text{MRTS} = \text{价格比}\) 依然成立，但 **技术决定解的性质**：  
  | **技术类型**     | **MRTS 行为**      | **成本最小化解** | **价格敏感性** |  
  |------------------|---------------------|------------------|----------------|  
  | 完全互补 (\(\sigma = 0\)) | 未定义（角点）     | 固定比例         | 低（仅成本水平） |  
  | Cobb-Douglas (\(\sigma = 1\)) | 递减（上文）       | 内部解           | 中（比例渐变）  |  
  | 完全替代 (\(\sigma = \infty\)) | 常数               | 角点解           | 高（需求突变）  |  
- **光谱补全作用**：本图片的 \(\sigma = 0\) 和 \(\sigma = \infty\) 案例 **锚定技术光谱边界**，凸显上文核心结论：  
  - 当 \(\sigma = 0\)，技术约束完全压制价格信号（配合规模报酬恒定，产量对成本响应线性但僵化）；  
  - 当 \(\sigma = \infty\)，价格信号主导但效果极端（与上文规模报酬递减的 "双重约束" 形成反差）。  
- **延续性说明**：本图片直接支撑上文 "替代弹性与规模报酬可解耦" 的论点——此处所有案例规模报酬恒定，进一步确认：**规模报酬属性仅改写成本路径斜率，而替代弹性决定厂商能否及如何响应价格**。

---
### Page/Slide 7



### 1. Extracted Content from Current Image  
#### Text  
- **Title**: NAME ________ 259  
- **Problem (a)**:  
  > *If Flo uses no fertilizer, how many hours of talk must she devote if she wants one happy plant?* **1 hour**. *If she doesn’t talk to her plants at all, how many bags of fertilizer will she need for one happy plant?* **1/2 bag**.  
- **Problem (b)**:  
  > *If \( w_t < w_f / 2 \), would it be cheaper for Flo to use fertilizer or talk to raise one happy plant?* **It would be cheaper to talk**.  
- **Problem (c)**:  
  > Flo’s cost function is \( c(w_f, w_t, h) = \min\left\{ \frac{w_f}{2}, w_t \right\} h \).  
- **Problem (d)**:  
  > Her conditional factor demand for talk is \( t(w_f, w_t, h) = \begin{cases} h & \text{if } w_t < w_f / 2 \\ 0 & \text{if } w_t > w_f / 2 \end{cases} \).  
- **Problem 20.8 (0)**:  
  > Remember T-bone Pickens, the corporate raider? Now he’s concerned about his chicken farms, Pickens’s Chickens. He feeds his chickens on a mixture of soybeans and corn, depending on the prices of each. According to the data submitted by his managers, when the price of soybeans was $10 a bushel and the price of corn was $10 a bushel, they used 50 bushels of corn and 150 bushels of soybeans for each coop of chickens. When the price of soybeans was $20 a bushel and the price of corn was $10 a bushel, they used 300 bushels of corn and no soybeans per coop of chickens. When the price of corn was $20 a bushel and the price of soybeans was $10 a bushel, they used 250 bushels of soybeans and no corn for each coop of chickens.  
- **Problem 20.8 (a)**:  
  > Graph these three input combinations and isocost lines in the following diagram.  

#### Formulas  
- Cost function for Flo: \( c(w_f, w_t, h) = \min\left\{ \frac{w_f}{2}, w_t \right\} h \)  
- Conditional factor demand for talk:  
  \[
  t(w_f, w_t, h) = 
  \begin{cases} 
  h & \text{if } w_t < w_f / 2 \\ 
  0 & \text{if } w_t > w_f / 2 
  \end{cases}
  \]  

#### Chart Details (No Text Extracted)  
- **Axes**: Horizontal = Soybeans (0–400 bushels), Vertical = Corn (0–400 bushels).  
- **Key Points Plotted**:  
  - (0, 300): 0 soybeans, 300 corn (when \( p_{\text{soy}} = 20 \), \( p_{\text{corn}} = 10 \))  
  - (150, 50): 150 soybeans, 50 corn (when \( p_{\text{soy}} = p_{\text{corn}} = 10 \))  
  - (250, 0): 250 soybeans, 0 corn (when \( p_{\text{soy}} = 10 \), \( p_{\text{corn}} = 20 \))  
- **Isocost Lines**: Three lines with slopes corresponding to price ratios:  
  - Slope = \(-1\) (for \( p_{\text{soy}}/p_{\text{corn}} = 1 \)), passing through (150, 50)  
  - Slope = \(-2\) (for \( p_{\text{soy}}/p_{\text{corn}} = 2 \)), passing through (0, 300)  
  - Slope = \(-0.5\) (for \( p_{\text{soy}}/p_{\text{corn}} = 0.5 \)), passing through (250, 0)  

---

### 2. Chart Analysis with Context from Previous Knowledge  
The chart illustrates **cost-minimizing input choices under perfect substitution technology**, directly reflecting the \(\sigma = \infty\) case from the previous summary. Key insights:  

#### **Isoquant Shape and Implications**  
- The three input points lie on a **straight-line isoquant** for \(y = 1\) (one coop), confirming \(MRTS\) is constant (calculated as \(\Delta \text{corn} / \Delta \text{soybeans} = -300/250 = -6/5\), so \(|MRTS| = 1.2\)).  
- This aligns with the previous framework: a linear production function \(y = a \cdot s + b \cdot c\) (here, \(y = \frac{s}{250} + \frac{c}{300}\) though input levels imply minor empirical approximation) implies \(\sigma = \infty\), where technical feasibility allows cost-minimizing corner solutions.  

#### **Price-Driven Corner Solutions**  
- **When \(p_{\text{soy}}/p_{\text{corn}} = 0.5\) (less than \(|MRTS| = 1.2\))**:  
  Only soybeans is used (point (250, 0)). This matches the rule from the summary: if \(w_s / w_c < |MRTS|\), firms substitute entirely to the cheaper input (soybeans here), inducing a **corner solution**.  
- **When \(p_{\text{soy}}/p_{\text{corn}} = 2\) (greater than \(|MRTS| = 1.2\))**:  
  Only corn is used (point (0, 300)). Consistent with \(w_s / w_c > |MRTS|\), triggering a switch to corn.  
- **When \(p_{\text{soy}}/p_{\text{corn}} = 1\) (close to \(|MRTS| = 1.2\))**:  
  A mixed input combination (150 soybeans, 50 corn) is used. This occurs because the price ratio approaches the \(MRTS\), allowing a "quasi-interior" solution within the linear isoquant. However, as emphasized in the summary, any *minor* price change would cause an **abrupt jump** to a corner solution (e.g., if \(p_{\text{soy}}\) rose slightly above $12, only corn would be used), highlighting the extreme price sensitivity of \(\sigma = \infty\) technology.  

#### **Isocost Line Behavior**  
- Each isocost line is tangent only at the labeled point, confirming **no interior solution exists** when price ratios diverge from \(MRTS\). This reinforces the summary’s claim that cost minimization under perfect substitutes yields **discontinuous demand**:  
  - Isocost slopes \(\neq MRTS\) imply zero demand for one input (e.g., \(p_{\text{soy}}/p_{\text{corn}} = 2\) makes the isocost steeper than the isoquant, driving \(s = 0\)).  
  - The cost function remains **piecewise linear** (e.g., \(c = \min\{p_s / 250, p_c / 300\} \cdot y\)), so price changes below a threshold have no effect on input choice, while crosses trigger demand collapse to a single input.  

#### **Contrast with Previous Cases**  
- Unlike Cobb-Douglas (\(\sigma = 1\), scale variable), here **scale returns are constant** (linear production function), eliminating the "cost growth amplification" seen in scale-inefficient cases. This isolates the role of \(\sigma\):  
  - The Flo example (same \(\sigma = \infty\) type) shows \(c \propto h\), but **price changes cause binary switches** in input demand (e.g., \(t = h\) or \(0\)), not gradual adjustments.  
  - This chart exemplifies the "anchored boundary" of the \(\sigma\)-spectrum: price signals are fully decisive but generate fragile equilibria, as even small price shifts (e.g., \(\$1\) change) can induce extreme resource reallocations.  

This behavior directly extends the summary’s conclusion: substitution elasticity \(\sigma = \infty\) maximizes price responsiveness *only* in the form of all-or-nothing choices, with scale effects merely scaling costs proportionally (no output constraints).

---
### Page/Slide 8



# 经济学问题解析：成本最小化与规模报酬

## 1. 文字与公式提取

### 价格-成本关系数据
- **(b) 鸡舍成本计算**
  - 价格 (10,10)：\$2,000
  - 价格 (10,20)：\$2,500
  - 价格 (20,10)：\$3,000

- **(d) 特定投入组合成本**
  - 150玉米+50大豆组合：
    - 价格 $p_s=10, p_c=10$：\$2,000
    - 价格 $p_s=10, p_c=20$：\$3,500
    - 价格 $p_s=20, p_c=10$：\$2,500

- **(e) 成本最小化检验**
  - 价格 (20,10) 时，该束成本低于实际选择束

### 20.9 (0) 根公司案例
- 生产函数：$f(x) = \sqrt{x}$
- **(a) 规模报酬**：Decreasing
- **(b) 投入与成本**
  - 生产10单位产出：100 units
  - 成本函数：$100w$

### 关键理论表述
- "There is no such evidence, since the data satisfy WACM"
- "No. At prices (20,10), this bundle costs less than the bundle actually used at prices (20,10). If it produced as much as that bundle, the chosen bundle wouldn't have been chosen"

## 2. 经济学解析

### 价格变动与投入选择
图片中(b)和(d)部分展示了**价格比变动对成本最小化选择的敏感性**。当玉米与大豆价格比从(10,10)变为(20,10)时，企业迅速切换投入组合：从(d)可见150玉米+50大豆组合在高玉米价格下成本上升，但(b)显示实际支出反而降低，表明企业已转向更低成本组合——这与上文σ=∞技术特征一致：**价格达到临界阈值时产生投入组合的离散跳跃**。

价格(20,10)状态下，150玉米+50大豆组合成本(\$2,500)低于(b)中实际支出(\$3,000)，但(e)明确企业不会选择它，因为**该组合若能生产相同产量则不会被放弃**。这验证了WACM（弱公理成本最小化）成立：企业总是选择更低成本的可行组合。

### 规模报酬对比
20.9(0)中 $f(x) = \sqrt{x}$ 表明**递减规模报酬**（输出增长低于投入增长），与上文讨论的恒定规模报酬（线性生产函数）形成关键对比：
- 递减规模报酬导致**长期平均成本上升**（如10单位产出需100单位投入，成本$100w$）
- 与上文σ=∞技术中"scale effects merely scaling costs proportionally"不同，此处规模扩张本身会增加单位成本

### 成本函数的分段特性
价格变化下的成本响应呈现**非连续性**：
- (b)中价格从(10,10)→(10,20)时成本仅升至\$2,500（而非(d)中组合的\$3,500）
- 说明企业已切换到更低成本的单一投入组合，印证上文"price changes below a threshold have no effect"而跨阈值时"trigger demand collapse to a single input"

此案例深化了上文结论：当技术呈现低替代弹性（如本例未明确但可推断）时，**价格变动引发投入组合的阶梯式调整**，在σ=∞极端情形下则表现为更剧烈的二元选择。

---
### Page/Slide 9



# 经济学问题解析：生产函数与规模报酬（续）

## 1. 文字与公式提取

### 问题 20.10 (0) 大学食堂生产分析
- **生产函数**：$f(x) = x^2$（$x$ 为投入量，$f(x)$ 为产出量）
- **(a) 规模报酬类型**：`Increasing`（递增）
- **(b) 144 单位产出**：
  - 所需投入单位：`12`
  - 成本（单位投入成本 $w$）：`$12w$`
- **(c) 一般产出量 $y$**：
  - 所需投入单位：`$\sqrt{y}$`
  - 总成本：`$w \sqrt{y}$`
- **(d) 平均成本**：$AC(w,y) = w / \sqrt{y}$

### 问题 20.11 (0) Irma 手工艺品生产分析
- **生产函数**：$f(x_1,x_2) = (\min\{x_1, 2x_2\})^{1/2}$（$x_1$ 为塑料，$x_2$ 为劳动力）
- **(a) 等产量线要求**：
  - 绘制生产 4 只鹿的等产量线
  - 绘制生产 5 只鹿的等产量线

### 前置问题片段（部分上下文）
- **(c) 一般产出成本**：
  - 所需投入单位：`$y^2$`
  - 总成本：`$y^2 w$`
- **(d) 平均成本**：$AC(w,y) = y w$

---

## 2. 经济学解析

### 递增规模报酬的成本影响（20.10）
- 生产函数 $f(x) = x^2$ 表明**递增规模报酬**（产出增长快于投入增长），直接导致平均成本 $AC(w,y) = w / \sqrt{y}$ 随产出 $y$ 增加而**严格递减**。这与上文 $\sigma = \infty$ 技术（成本与规模成比例）形成鲜明对比：此处规模扩张本身压低单位成本，而上文中“scale effects merely scaling costs proportionally”仅适用于恒定规模报酬。因此，当价格变动时，企业更可能扩大生产以利用成本优势，而非切换投入组合。

### 固定比例生产与替代弹性（20.11）
- 生产函数 $f(x_1,x_2) = (\min\{x_1, 2x_2\})^{1/2}$ 暗示**完全互补技术**（替代弹性 $\sigma = 0$），等产量线呈直角。这与上文 $\sigma = \infty$ 极端情形**形成根本性对立**：
  - $\sigma = 0$：价格变动无法触发“all-or-nothing choices”，投入比例严格绑定（需满足 $x_1 = 2x_2$），成本最小化选择不受边际价格波动影响，均衡高度稳定。
  - $\sigma = \infty$（上文）：即使微小价格变化（如 \$1 波动）可引发资源“extreme reallocations”，导致脆弱均衡。
- 例如，生产 4 只鹿时 $\min\{x_1, 2x_2\} = 16$，要求 $x_1 = 16$ 且 $x_2 = 8$；若价格变化但 $x_1/p_1 \neq x_2/p_2$，企业仍坚持此比例，避免上文所述的“fragile equilibria”。

### 知识连续性与扩展
- 上文强调 $\sigma = \infty$ 时价格信号的**二元选择特性**（all-or-nothing），而本图 20.11 中的固定比例技术**消除了价格变动的影响**，揭示替代弹性谱系（$\sigma$-spectrum）的核心逻辑：低 $\sigma$ 抑制资源重置，高 $\sigma$ 放大价格敏感性。
- 20.10 中的递增规模报酬进一步说明：**规模效应可独立于替代弹性**塑造成本结构，当 $AC$ 递减时，企业倾向于规模化生产，部分抵消价格波动的破坏性——这补充了上文“scale effects merely scaling costs”的限定性（仅适用于恒定规模报酬情形）。

---
### Page/Slide 10



## 3. 当前图片解析（20.11 续）

### 1. 文字与公式提取  
- **图表要素**：  
  - 横轴 $x_1$（0–40），纵轴 $x_2$（0–40）  
  - 等产量线：  
    - "Output of 4 deer"：垂直线位于 $x_1 = 16$（$x_2 \geq 8$），水平线位于 $x_2 = 8$（$x_1 \geq 16$）  
    - "Output of 5 deer"：垂直线位于 $x_1 = 25$（$x_2 \geq 12.5$），水平线位于 $x_2 = 12.5$（$x_1 \geq 25$）  
  - 比例线：$x_2 = \frac{1}{2} x_1$（技术约束线）  
- **问题文本**：  
  - (b) "Does this production function exhibit increasing, decreasing, or constant returns to scale? **Decreasing returns to scale.**"  
  - (c) "If Irma faces factor prices (1,1), what is the cheapest way for her to produce 4 deer? **Use (16,8).** How much does this cost? **\$24.**"  
  - (d) "At the factor prices (1,1), what is the cheapest way to produce 5 deer? **Use (25,12.5).** How much does this cost? **\$37.50.**"  
  - (e) "At the factor prices (1,1), the cost of producing $y$ deer with this technology is $c(1,1,y) = \frac{3y^2}{2}$."  
  - (f) "At the factor prices $(w_1, w_2)$, the cost of producing $y$ deer with this technology is $c(w_1, w_2, y) = \left(w_1 + \frac{w_2}{2}\right) y^2$."  
- **隐含公式**（图表推导）：  
  - 生产函数：$f(x_1, x_2) = (\min\{x_1, 2x_2\})^{1/2}$  
  - 成本最小化条件：$x_1 = 2x_2$（比例线 $x_2 = \frac{1}{2} x_1$）  

### 2. 图表与经济学解析  
- **图表动态含义**：  
  - L 形等产量线确证固定比例技术（$\sigma = 0$），产量扩张路径严格沿 $x_1 = 2x_2$ 射线移动（变形处为 $(y^2, \frac{y^2}{2})$）。此路径 **无替代空间**，与上文 $\sigma = \infty$ 情形形成**对立极点**：  
    - 价格变动（如 $(w_1, w_2)$ 从 (1,1) → (2,1)）仅提升总成本，但**不改变** $x_1/x_2 = 2$ 的投入比例（深化"price changes have no effect on input ratios"）。  
    - 上文指出 $\sigma = \infty$ 时价格波动会导致"all-or-nothing choices"，而此处即使 $w_2$ 翻倍，企业仍使用 $(25,12.5)$ 生产 5 只鹿（仅成本从 \$37.50 升至 \$62.50），体现**均衡稳定性**。  
  - 等产量线随产量扩张（$y=4 \to y=5$）向原点外移，但**间距递增**（$x_1$ 从 16→25 而非线性 20），直观揭示 **递减规模报酬（DRS）** 特性：单位成本 $AC = \frac{c}{y} = \left(w_1 + \frac{w_2}{2}\right) y$ 随 $y$ 严格递增，与上文 20.10 的递增规模报酬（IRS）形成对比。  

- **知识连续性深化**：  
  - **规模报酬与替代弹性解耦**：  
    - 本例 $\sigma = 0$ 但 DRS，而 20.10（$f(x)=x^2$）为 IRS 且含无限替代可能（因其单投入）。这证实：**技术刚性（$\sigma$）与规模效应是独立维度**。  
    - 上文强调"scale effects merely scaling costs proportionally"仅适用于恒定规模报酬（CRS），本例 DRS 使成本呈二次增长（$c \propto y^2$），而非上文 $\sigma = \infty$ 时的线性成本（$c = y \cdot \min\{w_1, w_2/2\}$）。  
  - **对价格响应的补充解释**：  
    - $\sigma = 0$ 抑制投入调整，使成本响应**连续平滑**（上文"price changes below a threshold have no effect"但 DRS 会放大规模成本）。  
    - 例如生产 5 只鹿成本 \$37.50（VS 4 只仅 \$24），增幅 \$13.50 高于线性推算 (\$6/\text{deer})，说明 DRS 迫使企业**对抗性定价**以避免亏损，与上文 $\sigma = \infty$ 时的"cost collapse"机制根本不同。  
  - **成本函数演变逻辑**：  
    | 问题 | 规模报酬 | 成本函数 | 核心机制 |  
    |---|---|---|---|  
    | 20.10 | IRS ($\uparrow$) | $c = w \sqrt{y}$ | 规模扩张压低单位成本 |  
    | **当前 20.11** | **DRS ($\downarrow$)** | $c \propto y^2$ | **规模扩张推高单位成本** |  
    本例揭示：**技术结构决定企业应对需求冲击的方式**——DRS 下企业需精确匹配产量以控成本，而 IRS 下可依赖规模效应缓冲价格波动，完善了上文"price changes trigger demand collapse"仅对高 $\sigma$ 成立的论断。

---
### Page/Slide 11



### Current Image Analysis: Problem 20.12 and 20.13 (0)

#### 1. Extracted Text and Formulas  
- **Header**: `NAME ________ 263`  
- **Question (a)**:  
  "In the graph below, draw a production isoquant representing input combinations that will produce 4 deer. Draw another production isoquant representing input combinations that will produce 6 deer."  
- **Graph** (coordinate system):  
  - Horizontal axis: `x1` (0 to 40)  
  - Vertical axis: `x2` (0 to 40)  
  - Annotations:  
    - "Output of 4 deer" (with arrow pointing to a point)  
    - "Output of 6 deer" (with arrow pointing to a point)  
- **Question (b)**:  
  "Does this production function exhibit increasing, decreasing, or constant returns to scale? **Decreasing returns to scale.**"  
- **Question (c)**:  
  "If Al faces factor prices (1,1), what is the cheapest way for him to produce 4 deer? **(8,0)**. How much does this cost? **$8**."  
- **Question (d)**:  
  "At the factor prices (1,1), what is the cheapest way to produce 6 deer? **(18,0)**. How much does this cost? **$18**."  
- **Question (e)**:  
  "At the factor prices (1,1), the cost of producing $y$ deer with this technology is $c(1,1,y) = \frac{y^2}{2}$."  
- **Question (f)**:  
  "At the factor prices (3,1), the cost of producing $y$ deer with this technology is $c(3,1,y) = y^2$."  
- **20.13 (0) Problem Setup**:  
  "Suppose that Al Deardwarf from the last problem cannot vary the amount of wood that he uses in the short run and is stuck with using 20 units of wood. Suppose that he can change the amount of plastic that he uses, even in the short run."  
  - **Subquestion (a)**:  
    "How much plastic would Al need in order to make 100 deer? **4,990 units**."  

#### 2. Chart Explanation: Isoquant Structure and Economic Meaning  
The graph contains two L-shaped isoquants for outputs $y=4$ and $y=6$, derived from the production function $f(x_1, x_2) = \max\left\{\sqrt{2} \cdot x_1^{1/2}, x_2^{1/2}\right\}$. Key characteristics and changes:  

- **Isoquant Geometry for $y=4$ and $y=6$**:  
  - The isoquant for $y=4$ consists of:  
    - A vertical segment at $x_1 = y^2/2 = 8$ (where $\sqrt{2 \cdot x_1} = 4$) for $x_2 \in [0, 16]$ (since $x_2 \leq y^2 = 16$).  
    - A horizontal segment at $x_2 = y^2 = 16$ (where $\sqrt{x_2} = 4$) for $x_1 \in [0, 8]$.  
  - The isoquant for $y=6$ consists of:  
    - A vertical segment at $x_1 = 18$ (where $\sqrt{2 \cdot x_1} = 6$) for $x_2 \in [0, 36]$.  
    - A horizontal segment at $x_2 = 36$ (where $\sqrt{x_2} = 6$) for $x_1 \in [0, 18]$.  
  - The corners are at $(8, 16)$ for $y=4$ and $(18, 36)$ for $y=6$, confirming disjoint input usage (no combination feasible at lower cost).  

- **Dynamic Changes and Economic Interpretation**:  
  - **Input Substitution and Factor Prices**:  
    - Unlike the fixed-proportion technology in Problem 20.11 (where $\sigma = 0$), this L-shape arises from **discontinuous substitutability** ($\sigma = \infty$ in the limit). Factor price changes trigger an "all-or-nothing" input switch:  
      - At $(w_1, w_2) = (1,1)$, $w_1 / w_2 = 1 < 2$, so input 1 is always strictly cheaper. The cost-minimizing point lies on the vertical isoquant segment near $x_2 = 0$ (e.g., $(8,0)$ for $y=4$), and the horizontal segment is irrelevant.  
      - At $(w_1, w_2) = (3,1)$, $w_1 / w_2 = 3 > 2$, so input 2 is cheaper. The cost-minimizing point shifts to $(0, y^2)$ (e.g., equivalent to **(0, 16) for $y=4$**, though unstated in the image).  
    - This contrasts with 20.11’s fixed-proportion case (where input ratios were invariant to price changes). Here, price changes cause immediate, discontinuous input substitution with **no adjustment along the expansion path**.  

  - **Output Expansion and Returns to Scale**:  
    - As output increases from $y=4$ to $y=6$, the isoquants shift outward non-proportionally:  
      - $x_1$-corner moves from 8 to 18 (225% increase), while $y$ rises 50%.  
      - $x_2$-corner moves from 16 to 36 (225% increase).  
    - The **increasing distance between isoquants** (e.g., $x_1$ spans 8–18 for $y=4$–6 vs. linear $y$ growth) visually confirms **decreasing returns to scale (DRS)**. This aligns with $c \propto y^2$ (e.g., $c(1,1,y) = y^2/2$), where average cost $AC = c/y = y/2$ rises with output. It differs from 20.11’s DRS case, where costs scaled with $y^2$ due to fixed proportions, whereas here DRS stems from **input-specific concavity** (e.g., $f \propto \sqrt{x}$ per input).  

  - **Scale vs. Substitutability Interaction**:  
    - DRS ($c \propto y^2$) and infinite substitutability ($\sigma = \infty$) coexist, reinforcing output-cost nonlinearity. For instance, short-run cost for $y=100$ (Problem 20.13) jumps to 4,990 units of plastic when constrained to $x_1 = 20$, as DRS amplifies marginal cost ($MC = y$, derived from $c = y^2/2$ at $(1,1)$). This contrasts with 20.11’s DRS, where costs rose quadratically but input ratios were rigid; here, cost responses combine DRS with abrupt substitution under price shocks.  

- **Key Continuity from Upper Summary**:  
  - While 20.11 (min-function) showed $\sigma = 0$ with DRS, this case (max-function) demonstrates $\sigma = \infty$ with DRS, validating the upper summary’s point that "scale effects and technology elasticity are independent dimensions." Both exhibit DRS but differ fundamentally in input flexibility: this context enables price-triggered input switching, absent in 20.11, and aligns with the "all-or-nothing choices" property for $\sigma = \infty$. The isoquant spacing’s convexity (vs. linearity) underscores how DRS forces steeper cost scaling than CRS, refining the upper summary’s note on "scale effects merely scaling costs proportionally" as applicable only to CRS.

---
### Page/Slide 12



### 提取内容  
**文字**：  
- 264 COST MINIMIZATION (Ch. 20)  
- *(b)* If the cost of plastic is \$1 per unit and the cost of wood is \$1 per unit, how much would it cost Al to make 100 deer? **\$5,010**.  
- *(c)* Write down Al’s short-run cost function at these factor prices.  

**公式**：  
$$
c(1,1,y) = 20 + \frac{y^2 - 20}{2}
$$

---

### 解析与知识衔接  
#### 1. **成本函数结构与规模报酬递减 (DRS) 的延续**  
- 上文指出 $ c \propto y^2 $ 是 DRS 的典型特征（如 $ c(1,1,y) = y^2/2 $），而当前短-run 成本函数可简化为：  
  $$
  c(1,1,y) = \frac{y^2}{2} + 10
  $$  
  **二次项 $ y^2/2 $** 直接延续了 DRS 的核心特征：边际成本 $ MC = y $ 随产出递增，平均成本 $ AC = y/2 + 10/y $ 最终上升。  
- **常数项 $ +10 $** 源于短期约束（如固定投入的初始成本），但不改变 DRS 的本质——**非线性增长仍由 $ y^2 $ 项主导**，与上文 "DRS 源于 input-specific concavity" 的结论一致。

#### 2. **数值结果 (\$5,010) 的经济学含义**  
- 代入 $ y = 100 $ 得：  
  $$
  c(1,1,100) = \frac{100^2}{2} + 10 = 5,\!010
  $$  
  - 该结果与上文 **Problem 20.13** 中 "short-run cost jumps to 4,990 when $ x_1 = 20 $" 存在数值差异，但**结构性逻辑一致**：  
    - 差异源于约束条件的具体参数（如固定投入水平或技术设定），但均体现 **DRS 与短期约束的叠加效应**：  
      - DRS 导致边际成本递增（$ MC = y $），  
      - 固定投入进一步放大成本增长（此处固定成本项 $ +10 $ 为次要影响）。  
  - 数值差异**不影响理论结论**，仅反映不同场景下的约束强度，强化了 "DRS 在短期约束下成本加速上升" 的普适性。

#### 3. **与规模报酬和替代弹性的理论关联**  
- 上文强调 "DRS 与无限替代弹性 ($ \sigma = \infty $) 可共存"，此处短-run 成本函数隐含：  
  - 长期中（无固定投入），成本函数应退化为 $ c = y^2/2 $（如上文 DRS 案例），  
  - 短期因固定投入引入常数项，但**产出-成本的非线性关系不变**，说明：  
    > DRS 是技术固有属性（由生产函数的凹性决定），而短期约束仅额外增加固定成本，不改变规模报酬方向。  

- 这与上文结论 **"scale effects and technology elasticity are independent dimensions"** 完全一致：  
  - DRS（规模效应）决定 $ y^2 $ 项的存在，  
  - 短期约束（替代弹性受限）仅新增常数项，二者作用相互独立。
