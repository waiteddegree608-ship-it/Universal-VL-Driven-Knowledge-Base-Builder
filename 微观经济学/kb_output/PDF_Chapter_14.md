# PDF_Chapter_14

### Page/Slide 1



### 提取内容

#### 文字
- **Chapter 14**  
  **Consumer’s Surplus**  
  **Introduction.** In this chapter you will study ways to measure a consumer’s valuation of a good given the consumer’s demand curve for it. The basic logic is as follows: The height of the demand curve measures how much the consumer is willing to pay for the last unit of the good purchased—the willingness to pay for the marginal unit. Therefore the sum of the willingnesses-to-pay for each unit gives us the total willingness to pay for the consumption of the good.  
  In geometric terms, the total willingness to pay to consume some amount of the good is just the area under the demand curve up to that amount. This area is called **gross consumer’s surplus** or **total benefit** of the consumption of the good. If the consumer has to pay some amount in order to purchase the good, then we must subtract this expenditure in order to calculate the **(net) consumer’s surplus**.  
  When the utility function takes the quasilinear form, $u(x) + m$, the area under the demand curve measures $u(x)$, and the area under the demand curve minus the expenditure on the other good measures $u(x) + m$. Thus in this case, consumer’s surplus serves as an exact measure of utility, and the change in consumer’s surplus is a monetary measure of a change in utility.  
  If the utility function has a different form, consumer’s surplus will not be an exact measure of utility, but it will often be a good approximation. However, if we want more exact measures, we can use the ideas of the **compensating variation** and the **equivalent variation**.  
  Recall that the compensating variation is the amount of extra income that the consumer would need at the *new* prices to be as well off as she was facing the old prices; the equivalent variation is the amount of money that it would be necessary to take away from the consumer at the old prices to make her as well off as she would be, facing the new prices. Although different in general, the change in consumer’s surplus and the compensating and equivalent variations will be the same if preferences are quasilinear.  
  In this chapter you will practice:  
  - Calculating consumer’s surplus and the change in consumer’s surplus  
  - Calculating compensating and equivalent variations  
  **Example:** Suppose that the inverse demand curve is given by $P(q) = 100 - 10q$ and that the consumer currently has 5 units of the good. How much money would you have to pay him to compensate him for reducing his consumption of the good to zero?  
  **Answer:** The inverse demand curve has a height of 100 when $q = 0$ and a height of 50 when $q = 5$. The area under the demand curve is a trapezoid with a base of 5 and heights of 100 and 50. We can calculate  

#### 公式
- $u(x) + m$（拟线性效用函数形式）
- $P(q) = 100 - 10q$（反需求曲线方程）

---

### 详细解析

#### 知识连续性说明
本章是消费者理论的自然延伸，承接了前文对需求曲线和效用度量的讨论（如前文应已建立需求曲线作为边际支付意愿的几何表示）。本章聚焦于量化消费者对商品的估值，核心逻辑延续了“边际支付意愿求和”的思想，并通过几何面积将抽象概念转化为可计算的指标，为后续福利分析（如政策评估或价格变动影响）奠定基础。

#### 关键概念解析
1. **总支付意愿与消费者剩余**  
   - 需求曲线高度直接表示**边际支付意愿**（消费者对最后一单位商品的支付上限）。  
   - 总支付意愿（即总收益）通过需求曲线下面积计算，定义为**总消费者剩余**（或总收益）。当消费者实际支出需被扣除时，差额即为**净消费者剩余**（$ \text{Net Consumer Surplus} = \text{Total Willingness to Pay} - \text{Expenditure} $）。  
   - *连续性要点*：此计算方法建立在前文“需求曲线推导自效用最大化”的基础上，但此处首次将效用显式转化为货币度量（如面积求和），弥补了效用不可直接观测的缺陷。

2. **拟线性效用函数的关键作用**  
   - 当效用函数为 $ u(x) + m $（$ m $ 为货币消费）时，消费者剩余成为效用的**精确测度**：  
     - 需求曲线下面积 = $ u(x) $  
     - 净消费者剩余 = $ u(x) + m $（即总效用）  
   - *连续性要点*：此结论依赖于前文对拟线性效用的假设（常见于商品消费分析），此时消费者剩余变化直接等价于效用变化（$ \Delta \text{Consumer Surplus} = \Delta \text{Utility} $），为福利计算提供简洁框架。

3. **补偿变异与等价变异的替代意义**  
   - 若效用函数非拟线性，消费者剩余仅为**近似测度**，需引入：  
     - **补偿变异 (CV)**：新价格下维持原效用水平所需额外收入。  
     - **等价变异 (EV)**：原价格下维持新效用水平需减少的收入。  
   - *核心关联*：当偏好拟线性时，$ \Delta \text{Consumer Surplus} = \text{CV} = \text{EV} $，但一般情形中三者仅近似相等。  
   - *连续性要点*：CV/EV 概念扩展了前文“收入效应”的分析维度，将离散价格变动转化为连续福利度量，解决非拟线性情形的效用计算难题。

4. **示例的实践意义**  
   - 反需求曲线 $ P(q) = 100 - 10q $ 的示例中：  
     - 消费 5 单位时，$ P(5) = 50 $，与截距 $ P(0) = 100 $ 构成梯形面积。  
     - 面积计算（补偿支付金额）= $ \frac{1}{2} \times (100 + 50) \times 5 = 375 $。  
   - *解析*：此计算直接验证了总支付意愿的几何定义，梯形面积作为离散单位（从 $ q=5 $ 到 $ q=0 $）的积分近似，体现“边际支付意愿求和”的操作化。其结果即消费者放弃所有消费所需的最低补偿，是后续变动分析（如需求弹性影响）的基准。

#### 知识拓展提示
本章方法为后续市场效率分析提供工具：当需求曲线给定时，消费者剩余变化可量化政策干预（如税收、补贴）的福利损失。但需注意，该框架隐含“支付意愿等于效用变化”的拟线性假设，实际应用中若偏好差异显著，需转向 CV/EV 计算以避免偏差。

---
### Page/Slide 2



# 当前图片内容解析

## 提取内容

### 文字
- the area of this trapezoid by applying the formula
- In this case we have A = 5 × 1/2(100 + 50) = $375.
- Example: Suppose now that the consumer is purchasing the 5 units at a price of $50 per unit. If you require him to reduce his purchases to zero, how much money would be necessary to compensate him?
- In this case, we saw above that his gross benefits decline by $375. On the other hand, he has to spend 5 × 50 = $250 less. The decline in net surplus is therefore $125.
- Example: Suppose that a consumer has a utility function u(x₁,x₂) = x₁ + x₂. Initially the consumer faces prices (1,2) and has income 10. If the prices change to (4,2), calculate the compensating and equivalent variations.
- Answer: Since the two goods are perfect substitutes, the consumer will initially consume the bundle (10,0) and get a utility of 10. After the prices change, she will consume the bundle (0,5) and get a utility of 5. After the price change she would need $20 to get a utility of 10; therefore the compensating variation is 20 − 10 = 10. Before the price change, she would need an income of 5 to get a utility of 5. Therefore the equivalent variation is 10 − 5 = 5.
- 14.1(0) Sir Plus consumes mead, and his demand function for tankards of mead is given by D(p) = 100 − p, where p is the price of mead in shillings.
  - (a) If the price of mead is 50 shillings per tankard, how many tankards of mead will he consume? 50.
  - (b) How much gross consumer’s surplus does he get from this consumption? 3,750.
  - (c) How much money does he spend on mead? 2,500.
  - (d) What is his net consumer’s surplus from mead consumption? 1,250.
- 14.2(0) Here is the table of reservation prices for apartments taken from Chapter 1:
  - Person = A B C D E F G H
  - Price = 40 25 30 35 10 18 15 5

### 公式
- Area of a trapezoid = base × (1/2)(height₁ + height₂)
- A = 5 × (1/2)(100 + 50) = $375
- D(p) = 100 − p

## 详细解析

### 梯形面积公式的应用逻辑
- 公式 `Area = base × (1/2)(height₁ + height₂)` 直接体现**总支付意愿的几何操作化**：以消费量为底，需求曲线在起点和终点的高度（即边际支付意愿）为梯形双高。这与上文"需求曲线下面积为总消费者剩余"的核心结论完全一致，将抽象边际支付意愿转化为精确数值计算。

### 补偿支付案例的实践验证
- 示例中，消费从5单位降至0：
  - **总收益损失 $375** = 需求曲线下梯形面积（`5 × (1/2)(100 + 50)`），反映总支付意愿的消失。
  - **支出节省 $250** = `5 × 50`（原消费支出），体现成本变化。
  - **净剩余损失 $125** = `375 - 250`，**直接验证上文"净消费者剩余 = 总支付意愿 - 支出"的定义**。  
- 此计算强化福利分析的关键原则：消费者补偿需考虑**总收益变动与支出变动的净效应**，而非单一维度。

### 非拟线性偏好下的CV/EV计算范例
- 效用函数 `u(x₁,x₂) = x₁ + x₂`（非拟线性，因无货币消费项 `m`）的分析：
  - **CV = $10**：新价格下维持原效用（10）需额外收入 `$20 - 原收入 $10`。
  - **EV = $5**：原价格下接受新效用（5）可接受的收入减少量 `$10 - 实现效用5所需收入 $5`。
- **关键关联上文**：此结果有力证明"当偏好非拟线性时，CV ≠ EV"（上文强调拟线性时三者相等）。本例中 `CV > EV` 体现价格变动福利影响的不对称性，凸显列**非拟线性情形必须用CV/EV替代消费者剩余**的结论。

### Sir Plus需求问题的结构化计算
- **需求函数 `D(p) = 100 - p` 与上文反需求曲线 `P(q) = 100 - 10q` 的逻辑统一**：  
  此处 `P(q) = 100 - q`（因 `q = 100 - p` ⇒ `p = 100 - q`），斜率差异仅因商品单位定义，但**方法论完全延续上文**：
  - **(a) 消费量 50**：`q = D(50) = 100 - 50`，复现需求函数求解均衡消费的标准流程。
  - **(b) 总消费者剩余 3,750** = `1/2 × 50 × (100 + 50)`，**精确应用上文"梯形面积 = 总支付意愿"规则**（消费量50替代前例的5）。
  - **(c) 支出 2,500** = `50 × 50`，作为总剩余的扣除项。
  - **(d) 净剩余 1,250** = `3,750 - 2,500`，**实证上文净剩余公式**，并为政策福利分析提供可操作基准（如税收影响计算）。

### 保留价格表的隐含逻辑
- 习题14.2的保留价格表（Person A-H对应价格40,25,...,5）**本质是离散化边际支付意愿数据**：  
  每个消费者的 reservation price 构成阶梯状需求曲线的转折点。此表**呼应上文"消费者剩余为边际支付意愿求和"的思想**，为后续离散情形下的剩余计算（类似对第10题梯形面积的离散近似）奠定基础，但本页未展开相关计算。

---
### Page/Slide 3



### 提取内容  
#### 文字与公式  
**公寓市场问题 (14.2 续)**  
- (a) 均衡租金 $20 时，获得公寓的消费者：**A, B, C, D**  
- (b) 消费者 A 的净剩余：**20**；消费者 B 的净剩余：**5**  
- (c) 总净消费者剩余：**50**  
- (d) 总gross消费者剩余：**130**  
- (e) 租金降至 $19 时，gross剩余增加：**0**  
- (f) 租金降至 $19 时，净剩余增加：**4**  

**Calculus 14.3 (0) 耳塞消费问题**  
- 效用函数：  
  $$
  u(x,y) = 100x - \frac{x^2}{2} + y
  $$  
- (a) 效用函数类型：**Quasilinear**（拟线性）  
- (b) 逆需求曲线：  
  $$
  p = 100 - x
  $$  
- (c) 价格 $50 时消费量：**50**  
- (d) 价格 $80 时消费量：**20**  
- (e) 收入 $4,000、价格 $50 时的总效用：**$5,250**  

---

### 详细解析  

#### 公寓市场的离散剩余计算（呼应上文 14.2 保留价格表）  
- **保留价格表的隐含应用**：上文给出的保留价格（A:40, B:25, C:30, D:35, E:10, F:18, G:15, H:5）构成阶梯状需求曲线。  
  - 均衡租金 $20 时，仅 A、B、C、D 消费（保留价格 > 20），**直接验证上文“离散消费者剩余 = 保留价格求和 - 总支出”**：  
    - **总gross剩余 (d)** = 保留价格之和 = 40 + 25 + 30 + 35 = **130**，即总支付意愿（与上文梯形面积逻辑一致，但离散化）。  
    - **净剩余 (b, c)** = gross剩余 - 总支出 = 130 - (20 × 4) = **50**；个体分解（如 A:40-20=20）复现上文净剩余定义。  
  - **价格变动效应 (e, f)**：租金降至 $19 时，  
    - **gross剩余不变 (e)**，因消费者集合未变（所有保留价格 > 19），无新支付意愿产生。  
    - **净剩余增加 4 (f)**，源于降价 × 消费量 = (20-19) × 4 = 4，**印证上文“净剩余变动仅取决于支出变化”**（因gross剩余未变）。  

#### 耳塞消费的拟线性偏好分析（强化上文 Sir Plus 案例）  
- **效用函数特性**：$u(x,y) = 100x - \frac{x^2}{2} + y$ 为**拟线性**（(a)），与上文 Sir Plus 需求同属一类：  
  - **需求函数完全一致**：逆需求 $p = 100 - x$（(b)）与上文 $D(p) = 100 - p$ 互为变形，**几何意义相同**——需求曲线斜率为 -1，截距 100。  
  - **关键延续**：拟线性下，消费者剩余 = CV = EV（上文强调），故剩余计算可直接用于福利分析。  
- **剩余与效用计算验证**：  
  - 价格 $50 时消费 50 单位（(c)），**总支付意愿 = 梯形面积 = $\frac{1}{2} \times 50 \times (100 + 50) = 3,750$**（复用上文公式），支出 = $50 \times 50 = 2,500$，净剩余 = 1,250（未显式列出，但隐含于效用计算）。  
  - **总效用 5,250 (e)** 的构成：  
    - 代入 $x=50$, $p=50$，支出 $50 \times 50 = 2,500$，故 $y = 4,000 - 2,500 = 1,500$。  
    - 效用 = $100 \times 50 - \frac{50^2}{2} + 1,500 = 5,000 - 1,250 + 1,500 = 5,250$。  
    - **此处 $y$ 直接代表货币效用，凸显拟线性偏好下“剩余 = 效用增量”**，与上文 Sir Plus 案例中“净剩余 = 效用增益”完全等价。  

#### 价格变动的连续 vs. 离散场景对比  
- **公寓市场（离散）**：租金微降（$20 → 19$）仅影响净剩余（+4），因无新边际消费者（e.g., E 保留价格 10 < 19）。  
- **耳塞市场（连续）**：价格变动（e.g., $50 → 80$）直接导致需求量变动（50 → 20），**验证需求函数 $D(p) = 100 - p$ 的连续敏感性**。  
- **核心统一**：两类场景均通过 **“保留价格与实际价格的差额”** 量化剩余，区别仅在离散/连续操作化——**紧接上文“保留价格表为阶梯需求基础”的论断**。

---
### Page/Slide 4



### 详细解析：14.4 节 Sarah Gamp 无差异曲线分析  

#### 1. 当前图片中的提取内容  
- **文字与答案**：  
  - (f) What is his total utility for earplugs and other things if the price of earplugs is $80? **$4,200**.  
  - (g) Utility decreases by **1,050** when the price changes from $50 to $80.  
  - (h) What is the change in (net) consumer’s surplus when the price changes from $50 to $80? **1,050**.  
  - 14.4 (2) In the graph below, you see a representation of Sarah Gamp’s indifference curves between cucumbers and other goods. Suppose that the reference price of cucumbers and the reference price of “other goods” are both 1.  
    - (a) What is the minimum amount of money that Sarah would need to purchase a bundle that is indifferent to A? **20**.  
    - (b) What is the minimum amount of money that Sarah would need to purchase a bundle that is indifferent to B? **30**.  
    - (c) Suppose that the reference price for cucumbers is 2 and the reference price for other goods is 1. How much money does she need to purchase a bundle that is indifferent to bundle A? **30**.  
    - (d) What is the minimum amount of money that Sarah would need to purchase a bundle that is indifferent to B using these new prices? **40**.  

- **图表描述**：  
  - 坐标系：X轴为 `Cucumbers`（范围 0–40），Y轴为 `Other goods`（范围 0–40），网格单位均匀。  
  - 关键点：  
    - 点 A 位于无差异曲线上（坐标约 (5, 35)）。  
    - 点 B 位于另一无差异曲线上（坐标约 (25, 10)）。  
  - 视觉特征：多条凸向原点的无差异曲线，反映边际替代率递减；点 A 和 B 标注在特定曲线上。  

> **注**：无显式公式，但隐含支出函数计算（最小支出 = \( p_x \cdot x + p_y \cdot y \) 于无差异曲线切点）。  

---

#### 2. 图表含义解析（结合上文知识点）  
本图表展示 **补偿变化（Compensating Variation, CV）** 的几何基础，直接延续上文“福利变动测量”的核心逻辑：  
- **上文关键延续**：  
  - 上文（Calculus 14.3）强调，**拟线性偏好下**，消费者剩余变动 \(\Delta CS = \Delta CV = \Delta EV\)，且剩余可直接从逆需求曲线的梯形面积推导（如价格 $50 \to 80$ 时，\(\Delta CS = 1,050\)，见 (g) 和 (h)）。  
  - 本节（14.4）**扩展至一般偏好**（无差异曲线非线性），需通过支出函数计算 CV，因拟线性假设不再成立（无差异曲线斜率变化，表明非线性效用）。  

- **图表动态解读**：  
  - **参考价格均为 1 时（(a), (b)）**：  
    - 最小支出值（A: 20, B: 30）对应 **预算线与无差异曲线的切点支出**。  
      - 例如，支出 20 时，预算线 \(x + y = 20\) 与 A 的无差异曲线相切，表示达到 A 效用水平的最小成本。  
      - **经济含义**：这量化了**保持效用不变的最低补偿收入**（CV 的基础），印证上文“福利变动需通过支出调整衡量”。  
    - 关键对比：B 的支出更高（30 > 20），表明 **B 点效用水平高于 A**（无差异曲线更远离原点），强化了上文“保留价格与效用正相关”的逻辑。  

  - **黄瓜价格升至 2 时（(c), (d)）**：  
    - 最小支出上升：A 从 20 → 30，B 从 30 → 40。  
      - 计算：新预算线 \(2x + y = \text{expenditure}\)，切点支出增加。  
      - **经济含义**：价格变动导致**补偿变化扩大**（如 A 情形，CV = 30 - 20 = 10）。此结果验证上文“非拟线性下，CV 需显式计算支出函数”：  
        - 上文公寓市场（离散）和耳塞市场（拟线性）仅通过价格差计算剩余变动，但此处需几何求解，凸显**一般偏好下福利分析的复杂性**。  
    - 与上文耳塞案例的**隐式对比**：  
      - 耳塞的拟线性偏好使 \(\Delta CS\) 与 \(\Delta \text{utility}\) 严格相等（如 (g) 和 (h) 皆为 1,050）。  
      - 本图无直接效用数值，但支出变动（如 A 从 20→30）**等价于效用不变时的收入补偿要求**，延续了上文“剩余即福利变动”的框架，但方法更普适。  

- **整体知识整合**：  
  - 本图表是 **上文“离散 vs. 连续剩余计算”的深层扩展**：  
    - 公寓市场（离散）依赖保留价格阶梯，耳塞市场（连续拟线性）依赖需求曲线积分。  
    - **此图引入一般偏好下的 CV 量化**：通过无差异曲线与预算线切点，直观展示“**最小支出 = 保持原效用的补偿成本**”，为后续福利分析奠定几何工具基础。  
  - **与上文 Sir Plus 案例的哲学呼应**：  
    - 尽管偏好类型不同，但核心逻辑一致——**消费者剩余本质是效用变动的货币度量**。本图中最小支出差（如 (c) - (a) = 10）即价格变动对福利的冲击，直接对应上文租金变动时的净剩余变化（如上文 (f) 净剩余增加 4）。

---
### Page/Slide 5



### 当前图片解析（基于上文知识点总结）

#### 1. 提取文字与公式  
**文字内容：**  
- `(e) No matter what prices Sarah faces, the amount of money she needs to purchase a bundle indifferent to A must be (higher, lower) than the amount she needs to purchase a bundle indifferent to B. lower.`  
- `14.5 (2) Bernice’s preferences can be represented by \( u(x, y) = \min\{x, y\} \), where \( x \) is pairs of earrings and \( y \) is dollars to spend on other things. She faces prices \( (p_x, p_y) = (2, 1) \) and her income is 12.`  
- `(a) Draw in pencil on the graph below some of Bernice’s indifference curves and her budget constraint. Her optimal bundle is 4 pairs of earrings and 4 dollars to spend on other things.`  
- `(b) The price of a pair of earrings rises to $3 and Bernice’s income stays the same. Using blue ink, draw her new budget constraint on the graph above. Her new optimal bundle is 3 pairs of earrings and 3 dollars to spend on other things.`  
- `(c) What bundle would Bernice choose if she faced the original prices and had just enough income to reach the new indifference curve? (3,3). Draw with red ink the budget line that passes through this bundle at the original prices. How much income would Bernice need at the original prices to have this (red) budget line? $9.`  

**公式：**  
- 效用函数： \( u(x, y) = \min\{x, y\} \)  
- 价格向量： \( (p_x, p_y) = (2, 1) \)（原始价格）；新价格 \( p_x = 3 \)  
- 支出计算：  
  - 原始最优支出： \( 2 \times 4 + 1 \times 4 = 12 \)  
  - 新最优支出： \( 3 \times 3 + 1 \times 3 = 12 \)  
  - 达到新效用水平的原始支出： \( 2 \times 3 + 1 \times 3 = 9 \)  

---

#### 2. 图表含义解析（结合上文知识点）  
**图表核心特征：**  
- **坐标系**：X轴为 `Pairs of earrings`（范围 0–16），Y轴为 `Dollars for other things`（范围 0–16）。  
- **关键线与点**：  
  - **黑线**：原始预算线（\( 2x + y = 12 \)），与L形无差异曲线交于最优 bundle (4,4)。  
  - **蓝线**：新预算线（\( 3x + y = 12 \)），与新无差异曲线交于最优 bundle (3,3)。  
  - **红线**：补偿预算线（\( 2x + y = 9 \)），通过 bundle (3,3) 且平行于黑线。  
  - **铅笔线**：L形无差异曲线（转角处 \( x = y \)），反映固定比例偏好（互补品）。  

**动态解读（衔接上文知识点）：**  
- **与上文福利分析框架的连续性**：  
  上文（知识点总结）核心为 **补偿变化（CV）** 的几何计算：通过最小支出 = \( p_x \cdot x + p_y \cdot y \) 在无差异曲线与预算线的接触点（切点或角点）求解。本例虽偏好结构不同（L形 vs. 凸形曲线），但 **CV 的本质逻辑完全一致**——均通过支出函数量化“保持效用不变的收入调整”。  
  - **关键区别**：上文基于边际替代率递减（凸曲线），CV 需精确计算切点支出（如 Sarah 案例中 A→B 的支出差 30−20=10）；本例因固定比例偏好，无差异曲线为 L 形，**最优解位于角点（\( x = y \))**，故最小支出直接在转角处计算，无需求导。  
    - 例：原始效用 \( u=4 \) 时，最小支出为 12（bundle (4,4)）；新效用 \( u=3 \) 时，最小支出为 9（bundle (3,3)）。  

- **图表变化的经济学含义**：  
  1. **原始状态（黑线）**：  
     - \( u=4 \) 的无差异曲线转角在 (4,4)，预算线 \( 2x + y =12 \) 于此点实现效用最大化。  
     - **呼应上文**：这验证了上文“最小支出 = 保持效用的收入水平”（如 Sarah 例中支出 20 对应效用 A）。此处支出 12 直接量化原效用水平，延续上文“福利由支出衡量”的逻辑。  

  2. **价格变动后（蓝线）**：  
     - 价格上涨（\( p_x \) 从 2→3），新预算线更陡，最优 bundle 移至 (3,3)，效用降至 \( u=3 \)。  
     - **隐含 CV 对比**：若要求 **保持原效用 \( u=4 \) 在新价格下**，需收入 \( 3 \times 4 + 1 \times 4 = 16 \)，故 CV = 16−12 = $4。虽未显式提问，但此计算逻辑同上文 Sarah 案例（支出差 30−20=10 即 CV）。  
     - **与上文关键差异**：上文拟线性偏好下 CV 可直接用需求曲线积分（如耳塞案例 \(\Delta CS = 1050\)），本例因一般偏好需显式求解支出函数，**凸显非拟线性偏好下福利分析的几何复杂性**。  

  3. **补偿情境（红线）**：  
     - 问题 (c) 要求：在原始价格下，达到新效用 \( u=3 \) 的最小收入（$9），对应红线 \( 2x + y =9 \)。  
     - **直接映射上文知识点**：  
       - 这等价于上文（d）部分逻辑：**“新价格下保持原效用的最小支出”** 的逆问题（即原始价格下达到新效用的最小支出）。  
       - 支出 $9 反映价格变动后的“福利损失货币化”——若收入从 $12 降至 $9，效用将降至新水平，与上文“补偿收入调整”概念一致。  
     - **图表作用**：红线直观展示 **CV 的预算成本**，为后续福利分析提供几何工具，深化上文“支出函数是 CV 核心”的论述。  

- **整体知识整合：偏好结构差异下的统一逻辑**  
  - 本例 **固定比例偏好**（L形曲线）与上文 **凸偏好** 形成关键对照：  
    - 凸偏好：CV 通过切点精确求解，支出差体现拟线性/一般偏好下的福利变动（如上文 \(\Delta CS = \Delta CV = 1050\) 或 10）。  
    - 固定比例偏好：CV 在角点计算（如本例 CV = $4），但 **支出的因果链条一致**——价格变动 → 效用变动 → 补偿性支出调整。  
  - **哲学延续**：无论偏好类型，消费者剩余本质是 **效用变动的货币度量**。上文 Sarah 案例中支出差（30−20=10）即福利冲击，本例支出差（12−9=3）则量化“价格上升导致的效用损失”，直接呼应（e）部分结论（Bundle A 无差异所需支出低于 B，因效用更低）。

---
### Page/Slide 6



### 提取当前图片内容  
**页码及章节**：186 | CONSUMER'S SURPLUS (Ch. 14)  

**Bernice 案例（文字与公式）**：  
- (d) The maximum amount that Bernice would pay to avoid the price increase is **\$3**. This is the (compensating, equivalent) variation in income. **Equivalent**.  
- (e) What bundle would Bernice choose if she faced the new prices and had just enough income to reach her original indifference curve? **(4, 4)**. Draw with black ink the budget line that passes through this bundle at the new prices. How much income would Bernice have with this budget? **\$16**.  
- (f) In order to be as well-off as she was with her original bundle, Bernice’s original income would have to rise by **\$4**. This is the (compensating, equivalent) variation in income. **Compensating**.  

**Ulrich 案例（文字与公式）**：  
- **Calculus 14.6 (0)**:  
  - Utility function: \( u(x, y) = \ln(x + 1) + y \), where \( x \) = number of video games, \( y \) = dollars spent on sausages, \( p_x \) = price of video game, \( m \) = income.  
  - (a) MRS = price ratio: \( \frac{1}{x + 1} = p_x \).  
  - (b) Demand functions (quasilinear preferences):  
    - Video games: \( x = \frac{1}{p_x} - 1 \).  
    - Sausages: \( y = m - 1 + p \) (note: \( p \) implies \( p_x \), per context).  
  - (c) At \( p_x = \$0.25 \), \( m = \$10 \):  
    - Demands: \( x = 3 \), \( y = 9.25 \).  
    - Utility: \( u = 10.64 \).  
  - (d) To be as well-off after removing all video games: requires \( y = \$10.64 \).  

---

### 经济学含义解析（衔接上文知识点）  
#### **Bernice 案例：补偿变化（CV）与等价变化（EV）的显式验证**  
- **(e) 与 (f) 的 CV 逻辑**：  
  - 本情景直接对应上文知识点中 **"CV 的计算框架"**：新价格下保持原效用（bundle (4,4)）的最小支出为 \$16，原始支出为 \$12（隐含，见上文知识点 CV = 16 - 12 = \$4），故 **CV = \$4**。  
  - (f) 中 "income rise by \$4" 明确标识 CV，**延续上文核心思想**：CV 量化 "新价格下维持原效用所需的补偿性收入调整"。  
  - **关键连续性**：上文 L 形偏好案例中，CV 在角点计算（如 bundle (3,3) 斯支出 \$9）；此处虽未指定偏好类型，但 **CV 本质一致**——均通过支出函数（新价格下原效用的最小成本）度量福利损失。  

- **(d) 的 EV 逻辑**：  
  - "\$3" 为 **EV（等价变化）**，即 **"原始价格下接受价格变动时，等效的效用损失货币化"**。  
  - **对比上文知识框架**：  
    - 上文知识点聚焦 CV（"新价格下保持原效用的支出"），而 EV 是其对偶概念（"原价格下效用降至新水平的收入减少"）。  
    - 本例中 EV = \$3 < CV = \$4，反映 **风险厌恶型偏好结构**（上文知识点中未显式讨论，但呼应一般性结论：当商品为正常品，EV ≤ CV）。  
  - **知识深化**：上文知识点强调 "消费者剩余本质是效用变动的货币度量"，此处 EV = \$3 直接体现为 "避免价格变动愿支付金额"，验证了福利分析的统一性。  

#### **Ulrich 案例：拟线性偏好下 CV 与 EV 的简化计算**  
- **(c) 与 (d) 的福利测量**：  
  - (d) 中 "\$10.64" 即 **EV（或 CV，因拟线性偏好）**：移除所有视频游戏后，需 \$10.64 在香肠上维持原效用（10.64）。  
  - **动态衔接上文知识点**：  
    - 上文知识点指出，**拟线性偏好下 CV 可直接用需求曲线积分求解**（如耳塞案例 \(\Delta CS = 1050\)）。  
    - 本例中，\( y \) 的线性项使效用损失完全转化为货币补偿（\( \Delta y = \text{utility drop} \)），故 **EV = CV = \$10.64 - \$9.25 = \$1.39 \)**（原香肠支出 \$9.25，新需求 \$10.64），**凸显上文所述 "非拟线性偏好福利分析更复杂" 的论点**。  
  - (a)-(b) 的需求函数 \( x = \frac{1}{p_x} - 1 \) 验证 **MRS = 价格比条件**，其独立于收入的特性（上文知识点称 "拟线性偏好简化福利计算"）使补偿性收入调整仅依赖效用函数参数。  

#### **整体知识整合**  
- **CV/EV 的统一逻辑延续**：  
  - Bernice 案例量化 **价格变动的福利冲击**（CV = \$4, EV = \$3），Ulrich 案例演示 **商品移除的补偿测量**（EV/CV = \$1.39），二者共同支撑上文结论：**无论偏好类型（L 形、凸形、拟线性），支出函数均为 CV/EV 的几何与代数核心**。  
- **关键差异点强化**：  
  - 上文 L 形偏好需显式求角点解（如 (4,4)），本页 Bernice 案例隐含凸偏好（需求连续变化），而 Ulrich 拟线性偏好进一步简化计算——**印证上文 "偏好结构决定几何计算复杂度，但因果链条（价格变动→效用变动→补偿调整）恒定" 的哲学**。  
- **教学递进**：  
  本页通过具体数值（\$16, \$4, \$10.64），将上文抽象的 "补偿预算线"（如红线 \( 2x + y =9 \)）转化为可操作计算，为后续福利政策评估（如税收、补贴设计）提供实证案例。

---
### Page/Slide 7



### 提取当前图片中的文字与公式  
#### 文字内容  
- (e) Now an amusement tax of $.25 is put on video games and is passed on in full to consumers. With the tax in place, Ulrich demands 1 video game and 9.5 dollars’ worth of sausages. His utility from this bundle is 10.19. (Round off to two decimal places.)  
- (f) Now if we took away all of Ulrich’s video games, how much money would he have to have to spend on sausages to be just as well-off as with the bundle he purchased after the tax was in place? $10.19.  
- (g) What is the change in Ulrich’s consumer surplus due to the tax? −.45. How much money did the government collect from Ulrich by means of the tax? $.25.  
- Calculus 14.7 (1) Lolita, an intelligent and charming Holstein cow, consumes only two goods, cow feed (made of ground corn and oats) and hay. Her preferences are represented by the utility function $U(x, y) = x - x^2/2 + y$, where $x$ is her consumption of cow feed and $y$ is her consumption of hay. Lolita has been instructed in the mysteries of budgets and optimization and always maximizes her utility subject to her budget constraint. Lolita has an income of $m$ that she is allowed to spend as she wishes on cow feed and hay. The price of hay is always $1$, and the price of cow feed will be denoted by $p$, where $0 < p \leq 1$.  
  - (a) Write Lolita’s inverse demand function for cow feed. Hint: Lolita’s utility function is quasilinear. When $y$ is the numeraire and the price of $x$ is $p$, the inverse demand function for someone with quasilinear utility $f(x) + y$ is found by simply setting $p = f'(x)$. $p = 1 - x$.  
  - (b) If the price of cow feed is $p$ and her income is $m$, how much hay does Lolita choose? Hint: The money that she doesn’t spend on feed is used to buy hay. $m - p(1 - p)$.  
  - (c) Plug these numbers into her utility function to find out the utility level that she enjoys at this price and this income. $u = m + (1 - p)^2 / 2$.  
  - (d) Suppose that Lolita’s daily income is $3 and that the price of feed is $.50. What bundle does she buy? $(1/2, 11/4)$. What bundle would she buy if the price of cow feed rose to $1? $(0, 3)$.  

#### 公式列表  
- $U(x, y) = x - x^2/2 + y$  
- $p = 1 - x$  
- $y = m - p(1 - p)$  
- $u = m + (1 - p)^2 / 2$  
- Bundles: $(1/2, 11/4)$, $(0, 3)$  

---

### 经济学解析  
#### **Ulrich 征税情景的福利分析（延续上文拟线性偏好逻辑）**  
- **(e) 与 (f) 的效用-补偿关联**：  
  - 税后效用 $u = 10.19$（对应新价格 bundle）直接决定 (f) 中等价补偿支出 $y = \$10.19$。这延续上文知识点中 **"拟线性偏好下，效用损失等于货币补偿"** 的核心原则（如 Ulrich 案例 (d) 中 $u = 10.64$ 对应补偿 $y = \$10.64$）。此处 $10.19$ 是 **等价变化（EV）的货币化表述**：移除视频游戏后需在香肠上花费 $10.19 才能维持税后效用水平，验证了上文 **"EV 量化原价格下效用损失的货币等价"** 论点。  
  - 对比上文知识点 (c) 税前状态（$p_x = 0.25$, $u = 10.64$）与本处税后状态（$u = 10.19$），效用下降 $0.45$，直观体现价格变动的福利冲击。  

- **(g) 消费者剩余与税收的量化关系**：  
  - 消费者剩余变化 $\Delta CS = -0.45$ 精确等于 **效用损失的货币值**，**印证上文知识点中 "拟线性偏好下，消费者剩余变动直接等价于 EV/CV"**（无需积分或支出函数修正）。  
  - 政府税收 $\$0.25$ 低于 $\Delta CS = 0.45$ 的绝对值，符合 **"税收导致无谓损失"** 的一般结论（本例中无谓损失 $= 0.45 - 0.25 = 0.20$）。上文知识点强调 **"非拟线性偏好需复杂计算，但拟线性偏好中 CS 变化是福利分析的简洁代理"**，此处 $\Delta CS = -0.45$ 直接作为福利损失的度量。  

#### **Lolita 拟线性偏好案例的验证（深化上文方法论）**  
- **效用函数 $U(x,y) = x - x^2/2 + y$ 的结构意义**：  
  - 该式是 **典型拟线性偏好**（$y$ 为线性项），完全复刻上文 Ulrich 案例的数学框架。上文知识点指出 **"拟线性偏好中，补偿性收入调整仅依赖效用函数参数，需求独立于收入"**，此处 (b) 中 $y = m - p(1-p)$ 证实 $x$ 的需求与 $m$ 无关（仅 $y$ 随收入变化），支撑上文 **"简化解支函数计算"** 的论断。  
  - (c) 的效用函数 $u = m + (1-p)^2/2$ 直接体现 **"效用水平由收入 $m$ 和价格 $p$ 线性决定"**，续接上文知识点 **"非拟线性偏好福利分析更复杂"** 的对比逻辑——此处无需角点解或预算约束迭代。  

- **(d) 价格变动的实证演示**：  
  - 价格 $p$ 从 $0.50$ 升至 $1$ 时，需求从 $(0.5, 2.75)$ 跳至 $(0,3)$，凸显 **"拟线性偏好下的需求突变特性"**（上文知识点未显式讨论，但隐含于福利简化范式）。  
  - 此处 $x$ 需求量归零（$p = 1$ 时 $x = 0$）**呼应上文 Bernice 案例的角点解逻辑**（如 L 形偏好中 bundle $(4,4)$），但因拟线性特性，补偿计算（如 (f) 中 $y$ 的补偿）可直接通过效用函数参数导出，无需支出最小化。  

#### **整体知识衔接**  
- **CV/EV 统一性强化**：  
  Ulrich (g) 的 $\Delta CS = -0.45$ 与 Lolita (d) 的 bundle 变化共同 **实证上文核心结论——"无论价格变动或商品移除，拟线性偏好下 CV 与 EV 可直接由效用函数差推导"**。例如，Lolita 价格上升时，EV 可通过 $u$ 公式计算（$p=0.5$ 时 $u=3 + (1-0.5)^2/2=3.125$；$p=1$ 时 $u=3$），与 Ulrich 税后效用下降 $0.45$ 的逻辑同源。  
- **政策启示延伸**：  
  政府税收 $\$0.25$ 与 $\Delta CS$ 的差值（无谓损失 $0.20$）**为上文 "福利分析服务于政策评估" 提供微观基础**，直接衔接税收/补贴设计中的效率权衡（上文知识点收尾提及）。

---
### Page/Slide 8



### 提取内容：当前图片文字与公式

#### 文字内容
- **Page Header**: `188 CONSUMER'S SURPLUS (Ch. 14)`
- **Problem (e)**:  
  `How much money would Lolita be willing to pay to avoid having the price of cow feed rise to $1? 1/8. This amount is known as the equivalent variation.`
- **Problem (f)**:  
  `Suppose that the price of cow feed rose to $1. How much extra money would you have to pay Lolita to make her as well-off as she was at the old prices? 1/8. This amount is known as the compensating variation. Which is bigger, the compensating or the equivalent variation, or are they the same? Same.`
- **Problem (g)**:  
  `At the price $.50 and income $3, how much (net) consumer’s surplus is Lolita getting? 1/8.`
- **Problem 14.8 (2)**:  
  `F. Flintstone has quasilinear preferences and his inverse demand function for Brontosaurus Burgers is $P(b) = 30 - 2b$. Mr. Flintstone is currently consuming 10 burgers at a price of 10 dollars.`  
  - **(a)**: `How much money would he be willing to pay to have this amount rather than no burgers at all? $200. What is his level of (net) consumer’s surplus? $100.`  
  - **(b)**: `The town of Bedrock, the only supplier of Brontosaurus Burgers, decides to raise the price from $10 a burger to $14 a burger. What is Mr. Flintstone’s change in consumer’s surplus? At price $10, consumer’s surplus is $100. At $14, he demands 8 burgers, for net consumer’s surplus of $\frac{1}{2}(16 \times 8) = 64$. The change in consumer’s surplus is $-$36.`  
- **Problem 14.9 (1)**:  
  `Karl Kapitalist is willing to produce $p/2 - 20$ chairs at every price, $p > 40$. At prices below 40, he will produce nothing. If the price of chairs is $100, Karl will produce 30 chairs. At this price, how much is his producer’s surplus? $\frac{1}{2}(60 \times 30) = 900$.`  
- **Problem 14.10 (2)**:  
  `Ms. Q. Moto loves to ring the church bells for up to 10 hours a day. Where $m$ is expenditure on other goods, and $x$ is hours of bell ringing, her utility is $u(m,x) = m + 3x$ for $x \leq 10$. If $x > 10$, she develops painful blisters and is worse off than if she didn’t ring the bells.`

#### 公式列表
- Inverse demand function: $P(b) = 30 - 2b$
- Consumer surplus calculation:  
  $\frac{1}{2}(16 \times 8) = 64$  
  $\Delta CS = -36$
- Supply function: $s = p/2 - 20$ for $p > 40$
- Producer surplus calculation:  
  $\frac{1}{2}(60 \times 30) = 900$

---

### 经济学解析（基于上文知识连续性）

#### **Lolita 问题：EV、CV 与消费者剩余的实证验证**
- 上文知识点总结强调 **"拟线性偏好下，等价变化（EV）与补偿变化（CV）直接等于效用损失的货币值，且二者相等"**。当前图片中：  
  - **(e) 和 (f) 分别对应 EV 和 CV**。价格从 $0.50$ 升至 $1$，EV = CV = $1/8$，与上文推导的 $\Delta u = -0.125$ 一致（因 $U(x,y)$ 为拟线性，效用损失 $= u(p_0) - u(p_1) = [m + (1-p_0)^2/2] - [m + (1-p_1)^2/2]$；代入 $p_0=0.5$, $p_1=1$, $m=3$ 得效用差 $= 0.125$）。  
  - **(g) 直接量化消费者剩余**：在 $p=0.50$ 和 $m=3$ 时，CS $= (1-p)^2/2 = 1/8$，**印证上文核心结论——拟线性偏好中，CS 由价格决定且无需积分，直接等于效用函数的非货币部分**。此结果与上文 $(1/2, 11/4)$ 消费束（$u=3.125$）的福利分析无缝衔接。  
- **关键延续**：EF 和 CV 相等（"Same"）**直接验证上文 "拟线性偏好下 EV 与 CV 统一" 的命题**，且 $|\Delta CS| = 1/8$ 等于 EV/CV，强化了 "CS 变动是福利损失的简洁代理" 这一方法论。

#### **F. Flintstone 问题：消费者剩余变动的微观基础**
- **反需求函数 $P(b) = 30 - 2b$ 的拟线性本质**：  
  该形式与上文 lolita 案例 $p = 1 - x$ 同构（均为线性反需求），**揭示上文提到的 "拟线性偏好使需求独立于收入"**。例如，当前消费 $b=10$（$P=10$）与上文需求 $x=1-p$ 均由价格单一决定。  
- **CS 变动验证无谓损失原理**：  
  - 价格从 $\$10$ 升至 $\$14$，CS 从 $\$100$ 降至 $\$64$，变化 $\Delta CS = -36$。  
  - 计算 $\frac{1}{2}(16 \times 8) = 64$ 源于 **三角形面积公式**，即 $\frac{1}{2} \times (P_{\max} - P) \times Q$（$P_{\max}=30$），**复用上文 "CS 为线性需求下直观几何面积" 的逻辑**，无需复杂积分。  
  - **政策关联**：$\Delta CS = -36$ 比率（此处无政府税收数据，但隐含无谓损失）**呼应上文 "税收导致 $\Delta CS$ 绝对值大于税收额" 的一般结论**，为政策效率分析提供数值基础。

#### **Karl Kapitalist 问题：生产者剩余的拓展应用**
- **供给函数 $s = p/2 - 20$ 与拟线性对称性**：  
  该函数是需求案例的镜像（$s$ 类比 $x$，$p$ 类比效用），**延续上文 "拟线性框架下福利分析对称" 的隐含逻辑**。  
- **生产者剩余计算**：  
  $\frac{1}{2}(60 \times 30) = 900$ 源于 $\frac{1}{2} \times (P - P_{\min}) \times Q$（$P_{\min}=40$），**直接应用上文 "CS 几何解释" 的方法论至生产侧**。此例 **深化** 上文 **"福利变动可通过简单图形量化"** 的论点，表明拟线性偏好下的分析工具普适于供需两侧。

#### **整体知识接口**
- **Lolita 与 Flintstone 的交叉验证**：  
  二者共同实证 **"拟线性偏好中 CS 变动是 EV/CV 的精确度量"**（Lolita 中 $\Delta CS = -1/8 = \text{EV} = \text{CV}$；Flintstone 中 $\Delta CS = -36$ 量化价格变动的总福利损失）。  
- **方法论延续**：  
  Karl 案例将分析视角拓展至生产者，**印证上文 "福利分析逻辑可迁移至供给端" 的终点启示**，完整覆盖市场双方的无谓损失评估。  
- **效率启示**：  
  Flintstone 的 $\Delta CS = -36$ 与 Lolita 的 $1/8$ 共同 **支撑上文 "政策导致的货币化无谓损失指导效率改进"** 的结论，为税收/定价设计提供微观数值依据。

---
### Page/Slide 9



### 当前图片文字与数值提取  
- **文字内容**：  
  Her income is equal to $100 and the sexton allows her to ring the bell for 10 hours.  
  $(a)$ Due to complaints from the villagers, the sexton has decided to restrict Ms. Moto to 5 hours of bell ringing per day. This is bad news for Ms. Moto. In fact she regards it as just as bad as losing $15$ dollars of income.  
  $(b)$ The sexton relents and offers to let her ring the bells as much as she likes so long as she pays $2$ per hour for the privilege. How much ringing does she do now? $10$ hours. This tax on her activities is as bad as a loss of how much income? $20$.  
  $(c)$ The villagers continue to complain. The sexton raises the price of bell ringing to $4$ an hour. How much ringing does she do now? $0$ hours. This tax, as compared to the situation in which she could ring the bells for free, is as bad as a loss of how much income? $30$.  
- **关键数值**：$15$, $20$, $30$（单位：美元）。  
- **注**：无公式、无图表，仅含文字描述与福利损失量化结果。  

---

### 经济学解析（基于上文知识连续性）  
#### **与拟线性偏好框架的延续**  
当前场景直接实证上文 **"拟线性偏好下，EV/CV 等于消费者剩余变动且可直接货币化"** 的核心结论。Ms. Moto 的效用函数隐含 $U(m, x) = m + v(x)$（$m$ 为收入，$x$ 为钟声小时），其福利损失计算与 **Lolita 问题** 的逻辑一致：  
- **总量价值恒定 $v(10) - v(0) = 30$**：  
  由 $(c)$ 中价格升至 $\$4$ 时 $x=0$，损失等同 $\$30$ 收入，表明消费 $x=10$ 小时的总消费者剩余（CS）为 $\$30$。这与上文 **Lolita 案例** 中 $CS = (1-p)^2/2$ 的简化逻辑同构——无需积分，直接由价格-数量关系导出货币化福利值。  
- **需求特性与福利损失**：  
  - $(b)$ 中价格为 $\$2$ 时 $x=10$，表明边际价值 $v'(x) > 2$（上文 **Flintstone 问题** 的需求函数 $P(b)=30-2b$ 亦类似，需求独立于收入）。福利损失 $\$20$ 等于实际支出（$2 \times 10$），即 **CV 与 CS 变动精确匹配**（初始 CS $=30$，新 CS $=30 - 20 = 10$，损失 $=20$）。  
  - $(a)$ 中数量限制至 $x=5$，损失 $\$15$ 对应 **CS 损失**（消费区间 $x=5$ 至 $10$ 的剩余），与上文 Lolita 问题中 $|\Delta CS| = 1/8$ 的量化解析一致，印证 **"数量管制福利损失需通过非自由消费区间分割计算"**。  

#### **福利变动机制的强化验证**  
- **EV/CV 一致性在政策扭曲中的体现**：  
  - $(a)$ 限制 $x$ 等价损失 $\$15$：此为 **EV**（将限制视为与收入损失等价）。  
  - $(b)$ 从自由消费到征税的损失 $\$20$：此为 **CV**（维持效用需补偿的收入额）。  
  二者均基于拟线性结构，**无需区分 EV/CV**（上文 **Lolita 与 Flintstone 交叉验证** 结论），且数值严格遵循 **"福利损失 = 面积损失"** 原理（例如，$(a)$ 的 $\$15$ 是 $x=5$ 到 $10$ 的剩余损失，隐含线性需求下三角形面积 $\frac{1}{2} \times \Delta x \times \Delta v$）。  
- **政策效率启示**：  
  - $(c)$ 中完全禁止（$x=0$）导致全量 CS 损失 $\$30$，**验证上文 Karl Kapitalist 案例的延伸逻辑**——当价格高于 reservation price（此处为 $\$4$），市场退出引发无谓损失最大化。  
  - 对比 $(b)$ 与 $(c)$：价格从 $\$2$ 升至 $\$4$ 时，CS 损失从 $\$20$ 剧增至 $\$30$，**强化上文 Flintstone 问题中 "$\Delta CS$ 绝对值增速超价格变化" 的效率损失规律**，为税收设计提供阈值依据（价格临界点在 $\$3$，因总价值 $\$30$ 除以 $10$ 小时）。  

#### **知识接口与方法论收敛**  
- **需求曲线隐式构建**：  
  由 $\$30$（总价值）、$\$15$（消费 $5$ 小时损失）及价格点推断，**反需求函数为 $P(x) = 3$（$0 \leq x \leq 10$）**（常数边际价值）。这复用上文 **"拟线性偏好下线性需求导出恒定 CS"** 的工具，使福利变动仅需算术计算（如 $(b)$ 中损失 $= p \times x$）。  
- **消费者剩余分析的普适性**：  
  本例将上文 Lolita 问题（价格变动）与 Flintstone 问题（数量变动）统一于 CS 框架——  
  - 价格管制（$(b)$ 和 $(c)$）：CS 损失 $= \int_{p_0}^{p_1} x(p) dp$（此处简化为 $p \times \Delta x$）。  
  - 数量管制（$(a)$）：CS 损失 $= \int_{x_1}^{x_2} P(x) dx$（直接量为 $\$15$）。  
  **彻底印证上文 "CS 是拟线性下福利变动的简洁代理"** 且无需重复复杂推导。  

> **关键延续**：本场景以最小模型重复上文知识链（Lolita 的 EV/CV 验证 → Flintstone 的 CS 量化 → Karl 供给侧延伸），表明 **"福利分析工具在拟线性偏好中可无摩擦迁移至任何形式政策扭曲"**，为实证效率评估提供标准化路径。

---
### Page/Slide 10



### 图片内容解析  

#### 1. 提取文字与公式  
- **文字**：  
  `190  CONSUMER'S SURPLUS  (Ch. 14)`  

#### 2. 图表与逻辑衔接  
- **无图表**：当前图片仅为教材章节标题页（第190页），无图形或公式。  
- **与上文知识点的连续性**：  
  该标题对应教材第14章“消费者剩余”，**直接承接上文对Ms. Moto案例中福利变动的实证推导**。上文通过具体案例（如价格/数量管制下的EV/CV与CS等价性）验证了拟线性偏好下消费者剩余的货币化特性，而本章（第14章）应为理论系统化，将零散案例（Lolita、Flintstone、Karl Kapitalist）纳入标准分析框架。  
  - **核心对应**：  
    - 上文指出“CS是拟线性偏好下福利变动的简洁代理”，本章标题隐含**消费者剩余作为工具的理论完备性**，为前文实证结论（如“$30总价值”“$15损失”）提供教科书级定义与边界条件。  
    - 教材章节标识（Ch. 14）表明，前文案例实为本章核心原理的铺垫，后续内容可能进一步推导需求曲线积分、价格弹性对CS的影响等，但当前页仅作逻辑起点。  

#### 3. 知识点延伸  
- **无新增推导**：此页无实证数据或模型，但通过章节标题**强化上文结论的学术锚点**——即拟线性偏好下消费者剩余的分析具有教材普遍性，而非特例。  
- **与实证案例的关联**：  
  Ms. Moto的$30总剩余、$20税收损失等，本质是本章（Ch. 14）理论在单参数问题中的显化解，为后续多维度福利分析（如生产者剩余、市场均衡）奠定基础。
