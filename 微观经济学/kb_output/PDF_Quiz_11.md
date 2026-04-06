# PDF_Quiz_11

### Page/Slide 1



# 图片内容解析

## 提取文字与公式

### 标题与标识
- Quiz 11
- NAME_________
- Asset Markets

### 问题 11.1
**题目文本**  
Ashley, in Problem 11.6, has discovered another wine, Wine D. Wine drinkers are willing to pay 40 dollars to drink it right now. The amount that wine drinkers are willing to pay will rise by 10 dollars each year that the wine ages. The interest rate is 10%. How much would Ashley be willing to pay for the wine if he buys it as an investment? (Pick the closest answer.)

**选项**  
(a) $56  
(b) $40  
(c) $100  
(d) $440  
(e) $61  

**隐含公式**  
$$ PV(n) = \frac{40 + 10n}{(1 + 0.1)^n} $$

### 问题 11.2
**题目文本**  
Chillingsworth, from Problem 11.10 has a neighbor, Shivers, who faces the same options for insulating his house as Chillingsworth. But Shivers has a larger house. Shivers’s annual fuel bill for home heating is 1,000 dollars per year. Plan A will reduce his annual fuel bill by 15%, plan B will reduce it by 20%, and plan C will eliminate his need for heating fuel altogether. The Plan A insulation job would cost Shivers 1,000 dollars, Plan B would cost him 1,900 dollars, and Plan C would cost him 11,000 dollars. If the interest rate is 10% and his house and the insulation job last forever, which plan is the best for Shivers?

**选项**  
(a) Plan A.  
(b) Plan B.  
(c) Plan C.  
(d) Plans A and B are equally good.  
(e) He is best off using none of the plans.  

**隐含公式**  
$$ PV = \frac{\text{年节省额}}{r} $$
$$ NPV = PV - \text{初始成本} $$

### 问题 11.3
**题目文本**  
The price of an antique is expected to rise by 2% during the next year. The interest rate is 6%. You are thinking of buying an antique and selling it a year from now. You would be willing to pay a total of 200 dollars for the pleasure of owning the antique for a year. How much would you be willing to pay to buy this antique? (See Problem 11.5.)

**隐含公式**  
$$ \frac{0.02P + 200}{P} = 0.06 $$

## 经济学解析

### 问题 11.1 价值形成机制
资产价格由**未来现金流现值最大化**决定。Wine D的消费价值随陈年时间线性增长（$40 + 10n$），需通过市场利率贴现。理性投资者选择持有期 $n$ 使：
$$
PV(n) = \frac{40 + 10n}{1.1^n}
$$
计算得 $n=6$ 或 $7$ 时 $PV \approx 56.45$，最接近选项 (a)。这体现资产定价核心：**均衡价格等于边际投资者的最高支付意愿**，由跨期替代与时间偏好共同决定。

### 问题 11.2 投资决策逻辑
永久性节能投资的决策依赖**净现值（NPV）最大化**：
- Plan A: $NPV = \frac{150}{0.1} - 1,000 = 500$
- Plan B: $NPV = \frac{200}{0.1} - 1,900 = 100$
- Plan C: $NPV = \frac{1,000}{0.1} - 11,000 = -1,000$

Plan A 最优验证了核心投资准则：**当资本成本固定时，选择 NPV > 0 且最大的项目**。该结果反映边际投资效率（节省额/成本）是决策的关键指标。

### 问题 11.3 资产定价双因素
古董定价需同时考虑：
1. 预期资本增值（2%）
2. 非货币使用价值（200美元）

均衡条件为总收益率等于市场利率：
$$
\frac{(1.02P - P) + 200}{P} = 0.06 \implies P = 5,000
$$
该模型揭示资产价格的双重决定机制：**使用价值会降低投资者对资本增值的要求**，使均衡价格高于仅考虑资本收益的情形。

## 与上文知识的连续性
- 延续**跨期消费选择**框架（11.1），强化资产价格由边际投资者的最优持有期决定的核心思想
- 拓展**耐用品投资决策**（11.2），运用永续年金模型验证净现值准则的适用条件
- 整合**消费效用与资产定价**（11.3），说明非货币收益如何内化到资产价格中，深化对"总回报率"概念的理解

---
### Page/Slide 2



### 文字与公式提取

**页码与标题**  
466 ASSET MARKETS (Ch. 11)  

**选项列表**  
- (a) $3,333.33  
- (b) $4,200  
- (c) $200  
- (d) $5,000  
- (e) $2,000  

**问题 11.4**  
A bond has a face value of 9,000 dollars. It will pay 900 dollars in interest at the end of every year for the next 46 years. At the time of the final interest payment, 46 years from now, the company that issued the bond will “redeem the bond at face value.” That is, the company buys back the bond from its owner at a price equal to the face value of the bond. If the interest rate is 10% and is expected to remain at 10%, how much would a rational investor pay for this bond right now?  
- **选项**  
  - (a) $9,000  
  - (b) $50,400  
  - (c) $41,400  
  - (d) More than any of the above numbers.  
  - (e) Less than any of the above numbers.  

**问题 11.5**  
The sum of the infinite geometric series $1, 0.86, 0.86^2, 0.86^3, \ldots$ is closest to which of the following numbers?  
- **选项**  
  - (a) infinity.  
  - (b) 1.86.  
  - (c) 7.14.  
  - (d) 0.54.  
  - (e) 116.28.  

**问题 11.6**  
If the interest rate is 11%, and will remain 11% forever, how much would a rational investor be willing to pay for an asset that will pay him 5,550 dollars one year from now, 1,232 dollars two years from now, and nothing at any other time?  
- **选项**  
  - (a) $6,000  
  - (b) $5,000  
  - (c) $54,545.45  
  - (d) $72,000  
  - (e) $7,000  

**隐含公式**  
- 问题 11.4（债券定价）:  
  $$
  PV = \left( C \times \frac{1 - (1 + r)^{-n}}{r} \right) + \frac{F}{(1 + r)^n}
  $$  
  其中 $C = 900$（年息），$r = 0.10$，$n = 46$，$F = 9,000$（面值）。  
- 问题 11.5（无限几何级数和）:  
  $$
  S = \frac{a}{1 - r}
  $$  
  其中 $a = 1$（首项），$r = 0.86$（公比）。  
- 问题 11.6（多期现金流现值）:  
  $$
  PV = \frac{C_1}{(1 + r)} + \frac{C_2}{(1 + r)^2}
  $$  
  其中 $C_1 = 5,550$，$C_2 = 1,232$，$r = 0.11$。  

---

### 经济学解析

#### 问题 11.4: 债券定价与现值应用
- **公式关联与含义**：  
  本题延续上文问题 11.2 的永续年金模型，但**扩展至有限期债券**。上文隐含公式 $PV = \frac{\text{年节省额}}{r}$ 仅适用于永续现金流，而此处需计算年金现值（46 年期）与面值终值现值之和。  
  - 关键点：票面利率（$900 / 9,000 = 10\%$）等于市场利率（$10\%$），根据现值原理，**债券价格应等于面值**（$9,000$）。  
  - 计算验证：  
    $$
    PV_{\text{年金}} = 900 \times \frac{1 - (1.10)^{-46}}{0.10} \approx 8,999.99, \quad PV_{\text{面值}} = \frac{9,000}{(1.10)^{46}} \approx 0.01
    $$  
    总和 $PV \approx 9,000$，对应选项 (a)。  
  - 与上文连续性：强化了**资产价格由边际投资者现值计算决定**的核心原则（上文 11.1 和 11.2），但凸显了期限对贴现的影响——永续假设（如 11.2）简化了计算，而有限期需显式处理终值。

#### 问题 11.5: 无限几何级数与永续年金基础
- **公式关联与含义**：  
  本题直接应用上文问题 11.2 隐含的**永续年金现值逻辑**。$PV = \frac{C}{r}$ 的推导依赖于无限几何级数求和公式 $S = \frac{a}{1 - r}$（此处 $a$ 为第一期现金流调整项）。  
  - 计算：  
    $$
    S = \frac{1}{1 - 0.86} = \frac{1}{0.14} \approx 7.1428
    $$  
    结果匹配选项 (c) $7.14$。  
  - 与上文连续性：上文 11.2 的 $PV = \frac{150}{0.1} = 1,500$ 实质是几何级数求和（$150 \times \frac{1}{1 - 1/1.1} = 150 \times 10$）。本题验证了**几何级数是永续资产定价的数学基础**，深化了上文对 "未来现金流现值" 的定义。

#### 问题 11.6: 多期现金流现值计算
- **公式关联与含义**：  
  本题直接扩展上文问题 11.3 的**总收益率均衡框架**。上文隐含公式 $\frac{\text{资本增值} + \text{非货币收益}}{P} = r$ 适用于单期，而此处需分步贴现多期现金流。  
  - 计算：  
    $$
    PV = \frac{5,550}{1.11} + \frac{1,232}{(1.11)^2} = 5,000 + 1,000 = 6,000
    $$  
    （注：$5,550 / 1.11 = 5,000$；$1,232 / (1.11)^2 \approx 1,232 / 1.2321 = 1,000$）  
    结果匹配选项 (a) $6,000$。  
  - 与上文连续性：上文 11.3 强调 "使用价值内化到价格"，而本题**无非货币收益**，纯货币现金流直接应用 $NPV$ 准则。这巩固了上文 11.2 的投资决策逻辑——**理性支付意愿等于所有未来现金流贴现和**，即使期限有限。  

#### 知识体系衔接
- 本图片问题系统性地将上文 **跨期选择框架（11.1）** 拓展至：  
  - 有限期限资产（11.4）：与上文永续假设对比，凸显期限对价格的敏感性。  
  - 数学工具验证（11.5）：为上文 11.2 的永续模型提供理论支撑。  
  - 多期现金流（11.6）：延伸上文 11.3 的单期定价至一般情形，体现 **总回报率均衡** 的普适性。  
- 核心延续：所有问题均基于 **"现值最大化" 原则**，具体化上文 "资产价格由边际投资者的最优支付意愿决定" 的结论，无新假设，仅场景深化。
