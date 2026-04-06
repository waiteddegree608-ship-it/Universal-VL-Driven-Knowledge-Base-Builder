# PDF_Chapter_15

### Page/Slide 1



# 当前图片内容解析

## 文字与公式提取

### 章节标题
Chapter 15  
Market Demand  

### 核心知识点
- **市场需求构造**：市场需求是给定价格下个体需求量的**水平相加**；当市场价格使个体需求归零时，市场需求曲线出现拐点(kink)。  
- **保留价格(reservation price)**：消费者无差异的临界价格 $ p^* $ 满足 $ u(0, m) = u(1, m - p^*) $。  
- **价格弹性公式**：若需求函数为 $ D(p) $，则：  
  $$
  \epsilon = \frac{dD(p)}{dp} \times \frac{p}{D(p)}
  $$

### 15.0 热身练习（弹性计算）
| 选项 | 需求函数 $ D(p) $ | 价格弹性表达式 |
|------|---------------------|----------------|
| (a)  | $ 60 - p $        | $ -\dfrac{p}{60 - p} $ |
| (b)  | $ a - bp $        | $ -\dfrac{bp}{a - bp} $ |
| (c)  | $ 40p^{-2} $      | $ -2 $ |
| (d)  | $ Ap^{-b} $       | $ -b $ |
| (e)  | $ (p + 3)^{-2} $  | $ -\dfrac{2p}{p + 3} $ |

## 知识点延伸说明
1. **线性需求弹性特征**：如 (a)(b) 项，线性需求函数 $ D(p) = a - bp $ 的弹性随价格动态变化，当 $ p \to 0 $ 时弹性趋近 0，当 $ p \to \frac{a}{b} $ 时弹性趋近 $ -\infty $。  
2. **幂函数需求的恒定弹性**：如 (c)(d) 项，需求函数 $ D(p) = Ap^{-b} $ 的弹性恒为 $ -b $，与价格无关，体现需求对价格的固定敏感度。  
3. **复合函数求导应用**：如 (e) 项，通过链式法则得 $ \frac{dD}{dp} = -2(p+3)^{-3} $，结合 $ \frac{p}{D(p)} = p(p+3)^2 $ 推导出弹性表达式，验证了非线性需求的局部弹性特性。  

（注：当前内容无图表，故无图表分析环节。）

---
### Page/Slide 2



# 当前图片内容解析

## 文字与公式提取
### 新增内容
- **公式 (f)**：  
  $ D(p) = (p + a)^{-b} $，  
  价格弹性表达式：$ -\dfrac{bp}{p + a} $。
- **15.1 (0) 问题描述**：  
  In Gas Pump, South Dakota, there are two kinds of consumers, Buick owners and Dodge owners. Every Buick owner has a demand function for gasoline $ D_B(p) = 20 - 5p $ for $ p \leq 4 $ and $ D_B(p) = 0 $ if $ p > 4 $. Every Dodge owner has a demand function $ D_D(p) = 15 - 3p $ for $ p \leq 5 $ and $ D_D(p) = 0 $ for $ p > 5 $. (Quantities are measured in gallons per week and price is measured in dollars.) Suppose that Gas Pump has 150 consumers, 100 Buick owners, and 50 Dodge owners.
- **子问题及答案**：  
  (a) If the price is $3, what is the total amount demanded by each individual Buick Owner? **5.** And by each individual Dodge owner? **6.**  
  (b) What is the total amount demanded by all Buick owners? **500.** What is the total amount demanded by all Dodge owners? **300.**  
  (c) What is the total amount demanded by all consumers in Gas Pump at a price of 3? **800.**  
  (d) On the graph below, use blue ink to draw the demand curve representing the total demand by Buick owners. Use black ink to draw the demand curve representing total demand by Dodge owners. Use red ink to draw the market demand curve for the whole town.  
  (e) At what prices does the market demand curve have kinks? **At $ p = 4 $ and $ p = 5 $.**  
  (f) When the price of gasoline is $1 per gallon, how much does weekly demand fall when price rises by 10 cents? **65 gallons.**  
  (g) When the price of gasoline is $4.50 per gallon, how much does weekly demand fall when price rises by 10 cents? **15 gallons.**  
  (h) When the price of gasoline is $10 per gallon, how much does weekly demand fall when price rises by 10 cents? **Remains at zero.**

## 知识点应用与延伸
### 市场需求构造的验证
- 该问题直接验证了**市场需求水平相加原理**：  
  - Buick车主总需求为 $ 100 \times D_B(p) $，Dodge车主总需求为 $ 50 \times D_D(p) $。  
    例如，当 $ p = 3 $ 时：  
    $ D_B(3) = 20 - 5 \times 3 = 5 $（个体），总Buick需求 $ = 100 \times 5 = 500 $；  
    $ D_D(3) = 15 - 3 \times 3 = 6 $（个体），总Dodge需求 $ = 50 \times 6 = 300 $；  
    市场总需求 $ = 500 + 300 = 800 $（问题c）。  
  - **拐点（kink）的成因**：当价格达到个体需求的截止点（即保留价格）时，市场需求曲线出现拐点。Buick需求在 $ p = 4 $ 处归零（$ D_B(4) = 0 $），Dodge需求在 $ p = 5 $ 处归零（$ D_D(5) = 0 $），导致市场总需求在 $ p = 4 $ 和 $ p = 5 $ 产生拐点（问题e）。这与上文“当市场价格使个体需求归零时，市场需求曲线出现拐点”的原理完全一致。

### 价格弹性的实践应用
- **弹性公式的延伸**：  
  公式 (f) $ D(p) = (p + a)^{-b} $ 的弹性 $ -\dfrac{bp}{p + a} $ 是对上文**幂函数需求弹性**的扩展：  
  - 当 $ a = 0 $ 时，退化为 $ D(p) = Ap^{-b} $（$ A = 1 $），弹性恒为 $ -b $（上文d项）；  
  - 当 $ a \neq 0 $ 时，弹性变为价格的函数（如问题 (f)(g)(h) 中需求变动的非线性特征），体现需求敏感度随价格变化。  
- **有限价格变动的实际意义**：  
  问题 (f)(g)(h) 通过价格上升 10 美分的需求变动量，揭示了**局部弹性**的核心概念：  
  - 在 $ p = 1 $（问题f）：需求下降 65 加仑，结合市场总需求 $ D(1) = 100(20-5) + 50(15-3) = 2100 $，近似点弹性 $ \epsilon \approx \frac{\Delta D / D}{\Delta p / p} = \frac{-65 / 2100}{0.1 / 1} \approx -0.31 $，表明低价格区域需求刚性较强。  
  - 在 $ p = 4.5 $（问题g）：需求下降 15 加仑，此时仅Dodge车主有需求（Buick需求为零），弹性绝对值更小，印证上文“线性需求在高价区域弹性趋近 $ -\infty $”的规律——但因截止点存在，实际变动被压缩。  
  - 在 $ p = 10 $（问题h）：需求为零且无变动，体现了需求函数边界条件（$ p > 5 $ 时所有需求归零）对弹性的决定性作用。

### 保留价格的隐性体现
- Buick和Dodge需求函数中的 $ p \leq 4 $ 和 $ p \leq 5 $ 直接定义了**保留价格**（即 $ D(p) = 0 $ 的临界点）：  
  - 由 $ u(0, m) = u(1, m - p^*) $ 可得，Buick保留价格 $ p^*_B = 4 $，Dodge保留价格 $ p^*_D = 5 $。  
  - 这解释了问题 (e) 中拐点位置：当价格跨越保留价格时，部分消费者退出市场，导致需求曲线斜率突变，这与上文保存留价格是市场需求构造的天然节点原理相符。

---
### Page/Slide 3



# 需求曲线分析：图形与解析

## 1. 图表提取

**坐标轴：**
- 纵轴：Dollars per gallon（每加仑美元），刻度0~6
- 横轴：Gallons per week（每周加仑），刻度0~3000

**曲线：**
- Black line（黑线）：最陡峭，显示低弹性特征
- Blue line（蓝线）：中等斜率
- Red line（红线）：最平缓，显示高弹性特征

## 2. 图形含义解析（结合上文知识点）

### 需求曲线斜率与弹性关系
- **黑线**代表**低弹性需求**：斜率陡峭，表明价格变动对需求数量影响小，对应上文"低价格区域需求刚性较强"现象（如问题f中p=1时的65加仑下降量）
- **红线**代表**高弹性需求**：斜率平缓，表明需求对价格敏感，符合上文"线性需求在高价区域弹性趋近-∞"规律
- 三条曲线交汇于一点，暗示**市场需求拐点( kink)位置**：
  - 该交点价格可能代表某个群体保留价格的临界值
  - 当价格跨越此点，某一消费群体完全退出市场，导致总需求曲线斜率突变（与上文"拐点的成因"原理一致）

### 与市场需求构造原理的联系
- 曲线形态体现**水平相加原理**：
  - 若黑线、蓝线代表不同消费者群体（如上文Buick/Dodge车主），则总需求曲线应为三线水平相加后的形状
  - 在不同价格区间，曲线数量变化原因：
    - 低价区间：所有群体都参与消费，总需求为三条线水平加总
    - 中价区间：某群体已达保留价格退出，只剩两条线
    - 高价区间：仅剩一条线，如上文"p>5所有需求归零"类似场景

## 3. 文字与公式提取及延伸分析

### 15.2 (0) 需求曲线与反需求曲线
(a) $ D(p) = \max\{10 - 2p, 0\} $ → $ p(q) = 5 - q/2 $ (if $ q < 10 $)
- **含义**：当 $ p = 5 $ 时需求归零（保留价格为5），与上文"需求函数截止点"原理一致
- **弹性特征**：线性需求，价格弹性随价格变动，非恒定（验证上文"弹性变为价格函数"观点）

(b) $ D(p) = 100/\sqrt{p} $ → $ p(q) = 10,000/q^2 $
- **幂函数形式**：属于上文提及 $ D(p)=Ap^{-b} $ 的扩展（此处 $ A=100, b=0.5 $）
- **弹性特性**：恒定弹性 $ -0.5 $，对应上文"当 $ a=0 $ 时弹性恒为 $-b$"的结论

(c) $ \ln D(p) = 10 - 4p $ → $ p(q) = (10 - \ln q)/4 $
- **对数需求函数**：体现非线性弹性特征，需求对价格敏感度随价格变化
- **应用关联**：类似于上文(f)(g)(h)问题，价格小波动产生的需求变化量不恒定

(d) $ \ln D(p) = \ln 20 - 2\ln p $ → $ p(q) = \sqrt{20/q} $
- **幂函数导出**：可转化为 $ D(p) = 20/p^2 $，是上文幂函数弹性的直接例证
- **弹性值**：恒定弹性 $ -2 $，展示需求对价格的高度敏感

### 15.3 (0) 分群体需求分析
- **Dog breeders需求**：$ q_b = \max\{200 - p, 0\} $
- **Pet owners需求**：$ q_o = \max\{90 - 4p, 0\} $

**(a) 价格弹性分析：**
- Dog breeders弹性：$ -p/(200 - p) $
  - 体现**保留价格边界效应**（当 $ p→200 $，弹性→-∞，印证上文"需求函数边界条件对弹性的决定性作用"）
- Pet owners弹性：$ -4p/(90 - 4p) $
  - 其系数4表明敏感度是breeder群体的4倍，对应上文"弹性变为价格的函数"特征

## 4. 知识连续性总结

1. **需求曲线斜率**：图中三线差异直观展示了不同价格敏感度，解释了为何"p=1时需求降幅大"与"p=4.5时降幅小"的现象（上文f/g问题）
2. **反需求函数**：15.2各题验证了上文需求函数形式的多变性，解释了为何"价格上升10美分的需求变动量不恒定"
3. **分群体需求**：15.3问题复现了上文Buick/Dodge车主需求结构，再次证明：
   - 市场需求由子群体需求**水平相加**构成
   - 子群体不同**保留价格**（200 vs 90）导致总需求曲线出现**拐点**（与上文$ p=4 $和$ p=5 $拐点形成机制相同）

---
### Page/Slide 4



# 市场需求构造中的拐点与弹性分析

## 1. 文字与公式提取

### 文字内容
- (b) At what price is the dog breeders' elasticity equal to −1? $100.  
  At what price is the pet owners' elasticity equal to −1? $11.25.  
- (c) On the graph below, draw the dog breeders' demand curve in blue ink, the pet owners' demand curve in red ink, and the market demand curve in pencil.  
- (d) Find a nonzero price at which there is positive total demand for dog polishers and at which there is a kink in the demand curve. $22.50.  
  What is the market demand function for prices below the kink? 290−5p.  
  What is the market demand function for prices above the kink? 200 − p.  
- (e) Where on the market demand curve is the price elasticity equal to −1? $100.  
  At what price will the revenue from the sale of electric dog polishers be maximized? $100.  
  If the goal of the sellers is to maximize revenue, will electric dog polishers be sold to breeders only, to pet owners only, or to both? Breeders only.  

### 公式提取
- 市场需求函数（低于拐点）： $ Q = 290 - 5p $  
- 市场需求函数（高于拐点）： $ Q = 200 - p $  

## 2. 原理解析：拐点形成与市场动态（基于上文知识点）

### 拐点的天然节点机制
- **Kink价格（$22.50）的成因**：  
  该点是市场需求构造的**天然节点**，直接对应上文“市场需求构造的天然节点原理”。当价格 $ p = 22.50 $ 时，宠物主人群体（$ q_o = \max\{90 - 4p, 0\} $）达到保留价格边界（$ 90/4 = 22.5 $），需求瞬间归零。此时，只留下狗育种者群体（$ q_b = \max\{200 - p, 0\} $），导致总需求曲线斜率突变：
  - **低于拐点（$ p \leq 22.50 $）**：总需求为两群体水平相加（$ Q = (200 - p) + (90 - 4p) = 290 - 5p $），斜率为 -5，体现高弹性区域（与上文图表中“蓝线/红线”斜率相似）。
  - **高于拐点（$ p > 22.50 $）**：仅剩狗育种者需求（$ Q = 200 - p $），斜率为 -1，体现低弹性区域（与上文“黑线”一致）。
  此拐点验证了上文所述“当价格跨越临界值，特定群体退出市场，导致总需求曲线斜率变化”的核心原理。

### 弹性与收入最大化逻辑
- **市场弹性 = -1 与收入最大化的关联**：  
  在 $ p = 100 $ 时，市场弹性等于 -1（仅适用于 $ p > 22.50 $ 的高弹性区域）。此处：
  - 宠物主人需求已归零（$ q_o = 0 $，因 $ p = 100 > 22.50 $），故市场弹性完全由狗育种者需求 $ q_b = 200 - p $ 决定（其弹性 $ -p/(200 - p) $ 在 $ p = 100 $ 时为 -1）。
  - 符合上文“收入最大化的充要条件为市场弹性等于 -1”，且此时**仅狗育种者贡献收入**（$ Q = 100 $），故最优策略是“仅售予育种者”。
  这延伸了上文“弹性变为价格函数”的结论——价格 $ p = 100 $ 恰是子群体保留价格边界（$ 200 $）的一半，印证了“需求函数边界对弹性动态的关键影响”。

### 与上文知识的连续性
- 拐点价格 $ 22.50 $ 精确对应宠物主人的保留价格，复现上文“线性需求在高价区域弹性趋近 $ -\infty $”的递变动态（当 $ p \to 22.50^- $，宠物主人群体弹性趋向 $ -\infty $）。
- 市场需求函数分段表达（$ 290 - 5p $ 和 $ 200 - p $）实证了上文“市场需求由子群体需求水平相加构成”的构造原理，强调天然节点是群体退出的必然结果——与上文问题 (f)(g)(h) 中“价格小波动导致需求变化量不恒定”的微观机制一致。

---
### Page/Slide 5



### 1. 文字与公式提取  
#### 图表标注文字  
- 纵轴：`Price`（刻度：0, 50, 100, 150, 200, 250, 300）  
- 横轴：`Quantity`（刻度：0, 50, 90, 100, 150, 200, 250, 290, 300）  
- 曲线标注：  
  - **Blue line**：指向蓝色虚线（狗育种者需求曲线）  
  - **Red line**：指向红色实线（宠物主人需求曲线）  
  - **Pencil line**：指向铅笔绘制的折线（市场总需求曲线）  
- 关键数值标注：`22.5`（Price轴）、`90`（Quantity轴）  

#### 数学公式  
- 图表下方文本中独立问题（与上文知识点无关）：  
  - $ \ln D(p) = 1,000 - p + \ln m $（猫砂需求函数）  
  - 价格弹性计算结果：当 $ p=2, m=500 $ 时弹性为 $-2$；$ p=3, m=500 $ 时为 $-3$  

---

### 2. 图表解析：需求曲线的分段结构与拐点机制  
#### （1）曲线含义与关键节点  
| 曲线          | 代表群体       | 需求函数                 | 特征与关键点                     |  
|---------------|----------------|--------------------------|----------------------------------|  
| **Red line**  | 宠物主人       | $ q_o = \max\{90 - 4p, 0\} $ | 当 $ p = 22.5 $ 时，$ q_o = 0 $（保留价格边界） |  
| **Blue line** | 狗育种者       | $ q_b = \max\{200 - p, 0\} $ | 从 $ (q=200, p=0) $ 延伸至 $ (q=0, p=200) $ |  
| **Pencil line** | 市场总需求     | 分段函数 <br> $ Q = \begin{cases} 290 - 5p & p \leq 22.5 \\ 200 - p & p > 22.5 \end{cases} $ | 在 $ (q=177.5, p=22.5) $ 处出现拐点 |  

#### （2）拐点形成机制（$ p = 22.5 $）  
- **低于拐点（$ p \leq 22.5 $）**：  
  - 总需求为两群体需求水平相加：$ Q = (200 - p) + (90 - 4p) = 290 - 5p $。  
  - **斜率 $-5$**（比单一群体更陡峭），体现高弹性区域（与红、蓝线斜率叠加一致）。  
- **高于拐点（$ p > 22.5 $）**：  
  - 宠物主人群体退出市场（$ q_o = 0 $），仅剩狗育种者需求：$ Q = 200 - p $。  
  - **斜率 $-1$**（与蓝线一致），体现低弹性区域（市场由单一高保留价格群体主导）。  

#### （3）与上文知识点的连续性验证  
- **拐点价格 $ 22.5 $** 的生成：  
  直接对应宠物主人保留价格 $ \frac{90}{4} = 22.5 $，验证上文“群体退出导致需求曲线斜率突变”的机制。  
- **总需求分段函数**：  
  - $ 290 - 5p $（$ p \leq 22.5 $）→ 红线（$ -4 $）与蓝线（$ -1 $）的水平叠加结果。  
  - $ 200 - p $（$ p > 22.5 $）→ 仅蓝线的作用区域。  
- **市场动态演化**：  
  - 当 $ p \to 22.5^- $，宠物主人需求弹性趋向 $ -\infty $（价格微升导致需求骤降），符合上文“高价区域弹性趋近 $ -\infty $”的递变规律。  
  - 拐点处 **$ Q = 177.5 $**（$ 290 - 5 \times 22.5 $），为红、蓝线在该价格下的需求量叠加值（$ q_b = 200 - 22.5 = 177.5 $, $ q_o = 0 $）。  

#### （4）图表与理论的映射  
- **Red line 的截断**：  
  红线在 $ p = 22.5 $ 处终止（$ q=0 $），直观体现“群体退出的离散性”——价格轻微超过保留阈值即导致需求归零。  
- **Pencil line 的斜率突变**：  
  拐点后铅笔线斜率从 **-5** 变为 **-1**，直接反映上文“市场需求构造的天然节点”原理——群体退出导致总量对价格的敏感度下降。  

> **注**：图表下方猫砂弹性问题与上文知识点无关，系独立习题，故不纳入分析。

---
### Page/Slide 6



### 提取的文字和公式

#### 标题与页码
- **196**  
  **MARKET DEMAND (Ch. 15)**

#### 独立问题文本
```
(c) What is the price elasticity of demand when price is $p$ and income is $m$?  
$-p$. The income elasticity of demand?  
$\mathbf{1}$.

Calculus 15.5 (0) The demand function for drangles is $q(p) = (p+1)^{-2}$.  
(a) What is the price elasticity of demand at price $p$?  
$-2p/(p+1)$.  
(b) At what price is the price elasticity of demand for drangles equal to $-1$?  
When the price equals $1$.  
(c) Write an expression for total revenue from the sale of drangles as a function of their price.  
$R(p) = pq = p/(p+1)^2$. Use calculus to find the revenue-maximizing price. Don't forget to check the second-order condition.  
Differentiating and solving gives $p = 1$.  
(d) Suppose that the demand function for drangles takes the more general form $q(p) = (p+a)^{-b}$ where $a > 0$ and $b > 1$. Calculate an expression for the price elasticity of demand at price $p$.  
$-bp/(p+a)$. At what price is the price elasticity of demand equal to $-1$?  
$p = a/(b-1)$.

15.6 (0) Ken's utility function is $u_K(x_1,x_2) = x_1 + x_2$ and Barbie's utility function is $u_B(x_1,x_2) = (x_1+1)(x_2+1)$. A person can buy 1 unit of good 1 or 0 units of good 1. It is impossible for anybody to buy fractional units or to buy more than 1 unit. Either person can buy any quantity of good 2 that he or she can afford at a price of \$1 per unit.  
(a) Where $m$ is Barbie's wealth and $p_1$ is the price of good 1, write an equation that can be solved to find Barbie's reservation price for good 1.  
$(m - p_1 + 1)2 = m + 1$. What is Barbie's reservation price for good 1?  
$p = (m+1)/2$. What is Ken's reservation price for good 1?  
\$1.  
(b) If Ken and Barbie each have a wealth of 3, plot the market demand curve for good 1.
```

---

### 详细解析

#### 1. **与上文知识点的连续性说明**  
- 上文知识点总结聚焦于**分段需求曲线**（如宠物主人与狗育种者的市场总需求拐点机制），并强调图表下方“独立问题”与核心理论无关（例如猫砂需求函数 $\ln D(p) = 1,000 - p + \ln m$ 及弹性计算）。  
- **当前图片内容属于同类独立问题**：  
  - 纯文本习题（无图表），涉及价格弹性、总收益最大化和个体需求推导，与上文核心知识点（分段需求曲线拐点）**无直接关联**。  
  - 但延续了微观经济学中**需求理论的通用框架**：  
    - 问题中反复出现的价格弹性公式（如 $-2p/(p+1)$）呼应上文对弹性的定性描述（例如拐点处弹性趋向 $-\infty$）；  
    - 效用函数 $u_B(x_1,x_2) = (x_1+1)(x_2+1)$ 的保留价格计算，隐含了上文“群体退出的离散性”逻辑（当价格超过保留阈值时需求骤降为 0）。  

#### 2. **关键问题与理论映射**  
| 问题类型          | 本页内容                                                                 | 与上文知识点的逻辑联系                                                                 |
|-------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **价格弹性**      | - Drangles 需求 $q(p) = (p+1)^{-2}$ 的弹性 $-2p/(p+1)$<br>- 一般形式 $q(p) = (p+a)^{-b}$ 的弹性 $-bp/(p+a)$ | 弹性计算是上文“拐点前高弹性区域”（斜率 $-5$）的微观基础；验证了 **弹性随价格变动** 的原理（如 $p=1$ 时弹性为 $-1$，对应总收益最大点）。 |
| **总收益最大化**  | $R(p) = p/(p+1)^2$ 通过微分得 $p=1$ 为极值点                              | 解释了上文知识中“**需求曲线斜率与弹性**”的关系：当弹性 $=-1$ 时，边际收益为零（对应拐点前的单一群体需求阶段）。 |
| **保留价格推导**  | Barbie 的保留价格方程 $(m - p_1 + 1)2 = m + 1$ → $p = (m+1)/2$            | 直接体现上文“**群体退出的离散性**”：价格 $> p$ 时需求归零，与宠物主人曲线在 $p=22.5$ 处截断逻辑一致。 |

> **注**：  
> - 页首 (c) 问的价格弹性 ($-p$) 指向标准对数需求函数 $\ln D(p) = \alpha - p + \ln m$ 的特性，虽未明示，但与上文猫砂问题 $\ln D(p) = 1,000 - p + \ln m$ **公式结构相同**（此处 $\alpha=0$），进一步确认：  
>   $$\text{价格弹性} = \frac{d \ln D(p)}{d \ln p} = -p \quad \text{（当 } \ln D(p) = \text{const} - p + \ln m\text{）}$$  
> - 习题 15.6(b) 要求绘制市场总需求曲线，**但本页无图**；若按上文逻辑，需叠加 Ken 和 Barbie 的分段需求（类似铅笔线构造机制），此处仅提供方程基础。  
> - **与上文核心结论的区分**：所有问题均属技术性练习，不涉及需求曲线的**斜率突变拐点**（如 $p=22.5$），故不修改上文对市场总需求的核心论证。

---
### Page/Slide 7



# 微观经济学问题解析

## 1. 文字与公式提取

### 图表数据
- 坐标系：Price (Y轴，0-4) vs Quantity (X轴，0-4)
- 垂直线段1：从(1,1)到(1,2)，附带一个黑点
- 垂直线段2：从(2,0)到(2,1)，附带一个黑点

### 文字与公式内容

**15.7 (0)**  
- 需求函数：$D(p,M) = 4 - 2p + \frac{1}{100}M$
- 已知条件：$M = 100$, $p = 1$
  - (a) 收入需求弹性：$1/3$
  - (b) 价格需求弹性：$-2/3$

**15.8 (0)**  
- 需求函数：$P = 10 - Q$
  - (a) 总收益最大化价格：$P = 5$
  - (b) 对应销售量：$Q = 5$

**15.9 (0)**  
- 需求函数：$D(p) = 200,000 - 10,000p$
- 约束条件：体育馆容量100,000人
  - (a) 逆需求函数：$p(q) = 20 - \frac{q}{10,000}$

## 2. 图表分析与理论映射

### 图表含义解析
该图表展示了**阶梯式需求曲线**，与上文"分段需求曲线"核心概念直接对应：

- **垂直线段的经济学意义**：
  - 位于 $Q=1$ 的垂直线段（P从1到2）：表示当价格处于 $[1,2]$ 区间时，**单一消费者**愿意购买1单位
  - 位于 $Q=2$ 的垂直线段（P从0到1）：表示当价格处于 $[0,1]$ 区间时，**第二位消费者**进入市场，总需求变为2单位

- **与上文"群体退出的离散性"逻辑的延续**：
  - 当价格 $>2$ 时：无消费者购买，需求为0
  - 当 $1<p\leq2$ 时：仅高保留价格消费者购买（$Q=1$）
  - 当 $p\leq1$ 时：低保留价格消费者也进入市场，需求跃升至2单位
  
此结构验证了上文核心论点：**市场需求由不同保留价格的消费者分段构成**，价格变化导致消费者群体"离散性"进入/退出市场，形成需求曲线的阶梯式转折。

### 与上文知识点的连续性
| 本图特征                | 上文核心概念                          | 理论一致性                                  |
|-------------------------|--------------------------------------|-------------------------------------------|
| 阶梯式需求曲线结构      | 分段需求曲线的拐点机制               | 价格阈值处需求量的阶跃变化，体现消费者群体离散性 |
| $Q=1$ 时的价格区间      | "宠物主人"高保留价格群体             | 对应上文 $p=22.5$ 处的拐点前单一群体阶段    |
| $Q=2$ 时的需求跃升      | "狗育种者"低保留价格群体进入         | 延续了"群体退出/进入导致需求曲线突变"原理    |
| 图表中的价格区间        | 保留价格阈值                         | 与 Barbie 的 $p=(m+1)/2$ 保留价格公式逻辑一致 |

> **关键洞察**：虽然本页习题（15.7-15.9）聚焦弹性计算与收益最大化等技术性内容，但图表直观呈现了**市场总需求曲线的形成机制**——正是上文阐述的"不同保留价格消费者的叠加效应"。当价格下降突破第二位消费者的保留价格阈值时，需求量发生离散跳跃，完全符合上文"群体退出/进入的离散性"核心原理。

---
### Page/Slide 8



# 微观经济学问题解析（续）

## 1. 文字与公式提取

### 文字内容
- **(b)** Write expressions for total revenue $ R(q) = 20q - q^2 / 10,000 $ and marginal revenue $ \text{MR} = 20 - q / 5,000 $ as a function of the number of tickets sold.
- **(c)** On the graph below, use blue ink to draw the inverse demand function and use red ink to draw the marginal revenue function. On your graph, also draw a vertical blue line representing the capacity of the stadium.
- **(d)** What price will generate the maximum revenue? `$10`. What quantity will be sold at this price? `100,000`.
- **(e)** At this quantity, what is marginal revenue? `0`. At this quantity, what is the price elasticity of demand? `-1`. Will the stadium be full? `Yes`.
- **(f)** A series of winning seasons caused the demand curve for football tickets to shift upward. The new demand function is $ q(p) = 300,000 - 10,000p $. What is the new inverse demand function? $ p(q) = 30 - q / 10,000 $.

### 图表数据
- **坐标轴**:
  - Y轴：Price（范围 0-30）
  - X轴：Quantity × 1000（范围 0-160，即实际数量 0-160,000）
- **标注线条**:
  - Vertical blue line at quantity=100 (×1000): "Stadium capacity"（容量为 100,000 张票）
  - Linear lines:
    - Blue line: Inverse demand function (labeled but partially obscured)
    - Black line: Alternative demand curve (labeled "Black line")
    - Two red lines: Marginal revenue functions (labeled "Red line")

## 2. 图表分析与理论映射

### 图表动态机制解析
该图表**量化呈现了容量约束对线性需求市场的支配性影响**，其核心特征与上文"分段需求曲线"框架形成重要呼应，但需明确技术边界：

- **容量约束的本质**:
  - 垂直蓝线（Stadium capacity）在 $ q=100,000 $ 处**并非需求曲线内在拐点**，而是外部物理限制。当价格低于 $ p = 20 - 100,000/10,000 = \$10 $ 时，需求量本可超过 100,000，但容量强制截断需求，形成有效需求边界。
  - 此处与上文"群体离散退出"（如 $ p=22.5 $ 拐点）的核心区别：  
    > 体育馆容量约束源于供给方限制，**非消费者保留价格离散性**。若移除此约束（如扩建场馆），需求曲线保持光滑线性，无内在转折——故仍属"技术性练习"范畴，不触及上文对市场总需求曲线的结构性论证。

- **边际收入与弹性的联动验证**:
  - 红色边际收入线与 $ q=100,000 $ 垂直线交点处 $ \text{MR}=0 $，对应需求弹性 $ \epsilon_d = -1 $（由 $ \text{MR} = p(1 + 1/\epsilon_d) $ 推导）。
  - 这直接印证上文"收入最大化需弹性绝对值 $ =1 $" 的普适原理，但**未引入新拐点**：弹性变化沿平滑需求曲线连续发生，截断仅发生在容量边界。

### 与上文逻辑的连续性统一
| **当前图表特征**       | **上文核心论点**                          | **理论一致性说明**                                  |
|------------------------|------------------------------------------|---------------------------------------------------|
| 容量导致的需求截断     | 外部约束≠需求内在拐点（如 $ p=22.5 $）  | 延续"斜率突变仅由消费者群体离散变化引发"的界定     |
| $ q=100,000 $ 时 $ \text{MR}=0 $ | 弹性 $ =-1 $ 为收入最大点              | 验证通用规则，但线性需求无分段，避免上文讨论的阶梯式离散 |
| 需求右移后 $ p(q)=30 - q/10,000 $ | 容量可能改变有效市场均衡               | 若新需求与容量线交点处弹性 $ \neq -1 $，体育场将不满员——**容量仅强化外生约束角色**，不创造新需求结构 |

> **关键结论**：图表通过容量约束展示了"需求与供给交互"的技术场景，但**需求曲线本身保持平滑线性**，符合上文"无斜率突变拐点"的判定。这进一步确证：市场总需求曲线的阶梯式转折**必须依赖消费者异质性**（如上文 Ken/Barbie 案例），而非物理容量限制等外生因素。习题 (f) 的需求移动训练了"如何处理外生冲击"，但未挑战需求曲线形成的基本微观基础。

---
### Page/Slide 9



### 详细解析

#### 1. 文字与公式提取  
- **问题 (g)**  
  - 表述：*Write an expression for marginal revenue as a function of output.*  
  - 公式：$ MR(q) = 30 - q / 5,000 $  
  - 指令：*Use red ink to draw the new demand function and use black ink to draw the new marginal revenue function.*  

- **问题 (h)**  
  - 表述：*Ignoring stadium capacity, what price would generate maximum revenue? What quantity would be sold at this price?*  
  - 答案：`$15`，`150,000`  

- **问题 (i)**  
  - 表述：*The quantity that would maximize total revenue... is greater than the capacity... marginal revenue is positive... up to the capacity... should sell 100,000 tickets at a price of $20.*  
  - 关键值：`100,000 tickets`，`$20`  

- **问题 (j)**  
  - 表述：*When he does this, marginal revenue from selling an extra seat is... The elasticity of demand... is $\epsilon = -2$.*  
  - 关键值：`10`（边际收入），`$\epsilon = -2$`（需求弹性）  

- **问题 15.10**  
  - 需求函数：$ q(p) = 300,000 - 10,000p $  
  - **(a)** 表述：*How much could... increase total revenue... by adding 1,000 new seats?*  
    答案：`9,900`  
  - **(b)** 表述：*How much could he increase revenue by adding 50,000 new seats? 60,000 new seats?*  
    答案：`$250,000`（50,000 seats），`$250,000`（60,000 seats）  
  - **(c)** 表述：*How large a stadium should he choose?*  
    答案：`150,000 seats`  

---

#### 2. 内容解析与知识连续性  
当前文本是上文**容量约束分析框架**的延伸实证，无新增图表，但文字逻辑完整承接上文核心论点。关键解析如下：  

- **边际收入函数的理论验证（问题 g）**  
  - 公式 $ MR(q) = 30 - q / 5,000 $ 由逆需求 $ p(q) = 30 - q / 10,000 $ 推导：  
    $$
    R(q) = p(q) \cdot q = \left(30 - \frac{q}{10,000}\right) q, \quad MR(q) = \frac{dR}{dq} = 30 - \frac{q}{5,000}
    $$  
  - **与上文连续性**：直接印证上文"线性需求下 MR 斜率为需求曲线两倍"的通用规则，但需注意：  
    > 该 MR 函数**无内在拐点**，因需求本身光滑线性（$ q(p) = 300,000 - 10,000p $），仅受外部容量约束干预。这强化了上文结论：*市场总需求曲线的斜率突变仅源于消费者群体离散性，非供给限制*。

- **容量约束对均衡的扭曲效应（问题 h–i）**  
  - 理论最优（无约束）：$ MR=0 $ 时 $ q=150,000 $、$ p=\$15 $（问题 h）。  
  - 实际决策（有约束）：容量 $ q=100,000 < 150,000 $，故以 $ p=\$20 $ 卖满容量（问题 i）。  
  - **关键机制**：  
    - 在 $ q=100,000 $ 时 $ MR=10>0 $（问题 j），表明需求仍处于弹性区域（$ |\epsilon|>1 $），但容量强制截断交易。  
    - 弹性 $ \epsilon = -2 $ 与 MR 正相关：$ MR = p \left(1 + \frac{1}{\epsilon}\right) = 20 \left(1 - \frac{1}{2}\right) = 10 $，验证上文公式 $ MR = p(1 + 1/\epsilon_d) $。  
  - **与上文连续性**：  
    > 容量约束使有效需求退化为垂直线（$ q=100,000 $），但**未改变需求曲线本身的光滑性**。这再次证明上文判据：*若移除供给约束（如扩建），需求曲线保持连续，无内在转折点*。偏离理论最优仅因外生物理限制，非需求结构变化。

- **扩建决策的经济逻辑（问题 15.10）**  
  - **增量收益边界**：  
    - 新增 1,000 座位（总容量 101,000）：收入增加 9,900（问题 a），因 $ q<150,000 $ 时 $ MR>0 $，边际收益递减。  
    - 新增 50,000/60,000 座位：收入均增 $250,000（问题 b），因最优点 $ q=150,000 $ 处 $ MR=0 $；超此点后 $ MR<0 $，故 60,000 新座位收益无增量。  
  - **容量扩张的临界点**：  
    - 问题 (c) 中，为最大化满员收入，选择 $ S=150,000 $（$ \max R(S) = (30 - S/10,000)S $，解得 $ S=150,000 $）。  
  - **与上文连续性**：  
    > 扩建收益递减至 $ q=150,000 $ 后归零，直接呼应上文"收入最大化需满足 $ \epsilon_d = -1 $"。**关键延续**：  
    > - 当 $ q < 150,000 $ 时，容量是瓶颈，扩张可提升收入；  
    > - 当 $ q \geq 150,000 $ 时，需求决定上限，容量冗余无价值。  
    > 这巩固了上文结论：*外生约束仅影响均衡位置，不改变需求曲线的基础形态；阶梯式需求拐点必须依赖消费者分化*。  

**总结**：当前文本通过边际收入、弹性和扩建计算，实证了上文"容量约束作为外生因素"的论点。所有结论均基于线性需求的连续特性，未引入新需求结构，进一步证明：**供给侧限制仅导致交易量截断，而非需求曲线本身的分段转折**。

---
### Page/Slide 10



### 当前图片解析：页眉信息与知识连续性

#### 1. 图片文字提取
- **纯文本内容**：  
  `200  MARKET DEMAND  (Ch. 15)`  
  （无公式、无图表）

#### 2. 知识连续性解析  
当前图片仅为章节页眉，其核心作用是**定位本章主题与前文逻辑衔接点**，无新增分析要素，但需强调其与上文容量约束分析的深层关联：  
- **标题功能**：  
  `MARKET DEMAND (Ch. 15)` 直接呼应上文实证案例的理论根基——**市场总需求曲线的连续性与外生约束的区分**。上文通过容量约束（如体育场座位）证实：  
  - 需求曲线本身光滑无拐点（由消费者行为决定），  
  - 观测到的“截断”（如满员价格 $ p=20 $）仅源于供给侧约束（物理容量 $ q=100,000 $），而非需求结构突变。  
  本章标题将此案例纳入更广的`市场需求`理论框架，为后续系统性讨论（如需求叠加、弹性应用）提供入口。  
- **页码意义**：  
  页码 `200` 暗示内容承前启后——上文（第15章中前节）聚焦单场景容量约束，本页开启对市场总需求（如多消费者群体）的延伸分析，**延续了“约束仅扭曲均衡位置，不改变需求基础形态”的核心判据**。  

> **关键延续点**：  
> 上文已通过 $ MR(q) = 30 - q / 5,000 $ 和弹性 $ \epsilon = -2 $ 验证需求光滑性；本章将拓展至 **多市场/多消费者情境**，但“阶梯式需求拐点必源于消费者分化”的结论仍依赖相同逻辑，无新增理论修正。当前页眉即此逻辑链条的章节锚点。
