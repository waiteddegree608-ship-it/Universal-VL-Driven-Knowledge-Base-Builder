# PDF_Chapter_7

### Page/Slide 1



# Revealed Preference 章节解析

## 1. 文字与公式提取

### 文字内容
```
Chapter 7
NAME___________

Revealed Preference

Introduction. In the last section, you were given a consumer’s preferences and then you solved for his or her demand behavior. In this chapter we turn this process around: you are given information about a consumer’s demand behavior and you must deduce something about the consumer’s preferences. The main tool is the weak axiom of revealed preference. This axiom says the following. If a consumer chooses commodity bundle A when she can afford bundle B, then she will never choose bundle B from any budget in which she can also afford A. The idea behind this axiom is that if you choose A when you could have had B, you must like A better than B. But if you like A better than B, then you will never choose B when you can have A. If somebody chooses A when she can afford B, we say that for her, A is directly revealed preferred to B. The weak axiom says that if A is directly revealed preferred to B, then B is not directly revealed preferred to A.

Example: Let us look at an example of how you check whether one bundle is revealed preferred to another. Suppose that a consumer buys the bundle (x₁ᴬ, x₂ᴬ) = (2, 3) at prices (p₁ᴬ, p₂ᴬ) = (1, 4). The cost of bundle (x₁ᴬ, x₂ᴬ) at these prices is (2 × 1) + (3 × 4) = 14. Bundle (2, 3) is directly revealed preferred to all the other bundles that she can afford at prices (1, 4), when she has an income of 14. For example, the bundle (5, 2) costs only 13 at prices (1, 4), so we can say that for this consumer (2, 3) is directly revealed preferred to (5,2).

You will also have some problems about price and quantity indexes. A price index is a comparison of average price levels between two different times or two different places. If there is more than one commodity, it is not necessarily the case that all prices changed in the same proportion. Let us suppose that we want to compare the price level in the “current year” with the price level in some “base year.” One way to make this comparison is to compare the costs in the two years of some “reference” commodity bundle. Two reasonable choices for the reference bundle come to mind. One possibility is to use the current year’s consumption bundle for the reference bundle. The other possibility is to use the bundle consumed in the base year. Typically these will be different bundles. If the base-year bundle is the reference bundle, the resulting price index is called the Laspeyres price index. If the current year’s consumption bundle is the reference bundle, then the index is called the Paasche price index.

Example: Suppose that there are just two goods. In 1980, the prices were (1,3) and a consumer consumed the bundle (4,2). In 1990, the prices were (2,4) and the consumer consumed the bundle (3,3). The cost of the 1980 bundle at 1980 prices is (1 × 4) + (3 × 2) = 10. The cost of this same bundle at 1990 prices is (2 × 4) + (4 × 2) = 16. If 1980 is treated as the base year and 1990 as the current year, the Laspeyres price ratio
```

### 公式列表
| 类型 | 内容 |
|------|------|
| 商品束 | $(x_1^A, x_2^A) = (2, 3)$ |
| 价格向量 | $(p_1^A, p_2^A) = (1, 4)$ |
| 成本计算 | $C_A = 2 \times 1 + 3 \times 4 = 14$ |
| 对比束成本 | $C_{(5,2)} = 5 \times 1 + 2 \times 4 = 13$ |
| 基年数据 | $p^{80} = (1,3),\ x^{80} = (4,2)$ |
| 当前年数据 | $p^{90} = (2,4),\ x^{90} = (3,3)$ |
| 拉氏指数基础 | $C^{base}_{base} = 1 \times 4 + 3 \times 2 = 10$<br>$C^{current}_{base} = 2 \times 4 + 4 \times 2 = 16$ |

## 2. 核心概念解析

### 显示偏好理论的逻辑转向
上文（需求理论）通过**已知偏好推导需求函数**，本章实现方法论逆转：  
**通过观察到的需求行为反推隐含的偏好结构**。这种"由果溯因"的思路使消费者偏好不再依赖主观陈述，而是基于可验证的市场选择行为。

### 弱显示偏好公理（WARP）的经济含义
公理描述：若$A$被选择时$B$可负担，则$B$被选择时$A$不可负担。  
- **关键逻辑链**：  
  $A \text{ chosen} \land B \text{ affordable} \implies A \text{ directly revealed preferred to } B$  
  $\implies B \text{ cannot be directly revealed preferred to } A$  
- **行为经济学意义**：  
  消费者选择行为本身构成偏好传递的实证证据，替代了传统的效用函数假设。例如，当商品束$(2,3)$在收入14被购买时，所有成本≤14的束（如$(5,2)$成本13）均属可负担集，但实际选择$(2,3)$表明其严格偏好地位。

### 价格指数的显示偏好视角
#### 拉氏指数（Laspeyres）的内涵
- **构造逻辑**：以基年消费束为参照  
  $P_L = \frac{p^{current} \cdot x^{base}}{p^{base} \cdot x^{base}} = \frac{16}{10} = 1.6$  
- **经济解释**：  
  保持1980年消费水平不变，1990年价格使成本上升60%。这种"锚定历史消费模式"的方式隐含假设：消费者不会因相对价格变化而调整消费结构（忽略了替代效应）。

#### 帕氏指数（Paasche）的互补价值
- **构造逻辑**：以当前年消费束为参照  
  $P_P = \frac{p^{current} \cdot x^{current}}{p^{base} \cdot x^{current}}$  
- **与拉氏指数的对比**：  
  当相对价格变动时，帕氏指数反映"当前消费模式下的价格变化"，通常小于拉氏指数（因包含替代效应）。二者差值构成**价格指数偏差**，可量化消费结构调整的空间。

### 理论深化点
1. **公理局限性**：WARP仅要求非循环性（non-cyclical），但允许不完全偏好，为后续强显示偏好公理（SARP）奠定基础  
2. **指数政策意义**：拉氏指数高估生活成本上升（忽略消费替代），而帕氏指数低估（未考虑消费降级），现代CPI计算多采用链式指数修正  
3. **行为验证优势**：显示偏好理论将"偏好"概念转化为可观测的市场行为，避免了效用函数存在的规范性假设  

> 本章通过行为观察实现偏好推断，标志着微观经济学从"主观偏好理论"向"客观选择理论"的范式转变，为实证需求分析提供了方法论基础。

---
### Page/Slide 2



# 详细解析

## 1. 提取内容

### 文字内容
- Paasche price index calculation: "The 1990 bundle costs (2 × 3) + (4 × 3) = 18 at 1990 prices. The same bundle cost (1 × 3) + (3 × 3) = 12 at 1980 prices. Therefore the Paasche price index is 18/12."
- Quantity index explanation: "The Laspeyres quantity index uses the base-year prices as the reference prices, and the Paasche quantity index uses current prices as reference prices."
- Example calculations: "The Laspeyres quantity index is 12/10. The Paasche quantity index is 18/16."
- Behavioral question: "When prices are (4,6), Goldie chooses the bundle (6,6), and when prices are (6,3), she chooses the bundle (10,0)."
- WARP determination: "Is Goldie's behavior consistent with the weak axiom of revealed preference? No."

### 公式列表
| 类型 | 公式 | 计算值 |
|------|------|--------|
| Paasche价格指数 | $\frac{p^{current} \cdot x^{current}}{p^{base} \cdot x^{current}}$ | $\frac{18}{12} = 1.5$ |
| Laspeyres数量指数 | $\frac{p^{base} \cdot x^{current}}{p^{base} \cdot x^{base}}$ | $\frac{12}{10} = 1.2$ |
| Paasche数量指数 | $\frac{p^{current} \cdot x^{current}}{p^{current} \cdot x^{base}}$ | $\frac{18}{16} = 1.125$ |
| Goldie预算约束 | $(4,6)$下选择$(6,6)$；$(6,3)$下选择$(10,0)$ | - |

## 2. 核心概念解析

### Paasche与Laspeyres指数的对比深化
#### 价格指数的双重维度
- **Paasche价格指数**以**当前消费模式**为基准：
  - 分子：现期价格购买现期束的总成本
  - 分母：基期价格购买现期束的总成本
  - 计算值为$1.5$，表明相对于基期价格，维持现期消费需增加50%

- **与拉氏指数的本质区别**：
  | 指数 | 参考价格 | 参考消费束 | 偏差方向 |
  |------|----------|------------|----------|
  | Laspeyres | 基期 | 基期 | 高估通胀（忽略替代效应） |
  | Paasche | 现期 | 现期 | 低估通胀（包含消费降级） |

  当商品相对价格变化时，**Paasche指数(P_P) ≤ Laspeyres指数(P_L)**，本例中$1.5 < 1.6$验证了这一关系，差值$(1.6-1.5)=0.1$量化了**替代效应的规模**。

#### 数量指数的实践价值
- **Laspeyres数量指数**：固定基期价格，反映消费量变化对成本的影响
  - 公式$\frac{p^{80} \cdot x^{90}}{p^{80} \cdot x^{80}} = \frac{12}{10}$表明维持基期价格下，现期消费成本增加20%

- **Paasche数量指数**：固定现期价格，反映消费量变化的现行价值
  - 公式$\frac{p^{90} \cdot x^{90}}{p^{90} \cdot x^{80}} = \frac{18}{16}$表明以现期价格衡量，消费规模增长12.5%

- **指数交叉检验**：数量指数的倒数关系表明，当价格与消费双向变动时，需综合运用价格指数与数量指数分解变化根源：
  $$(\text{Paasche price index}) \times (\text{Laspeyres quantity index}) = (\text{Laspeyres price index}) \times (\text{Paasche quantity index})$$

### WARP的实证检验
#### Goldie选择行为的矛盾性
- **第一次选择**：价格$(4,6)$时选择$(6,6)$
  - 收入 $I_1 = 4 \times 6 + 6 \times 6 = 60$
  - 束$B=(10,0)$成本 $= 4 \times 10 + 6 \times 0 = 40 < 60$（可负担但未选）
  
- **第二次选择**：价格$(6,3)$时选择$(10,0)$
  - 收入 $I_2 = 6 \times 10 + 3 \times 0 = 60$
  - 束$A=(6,6)$成本 $= 6 \times 6 + 3 \times 6 = 54 < 60$（可负担但未选）

- **WARP违背**：当$A$被选择时$B$可负担，且当$B$被选择时$A$也可负担，形成**偏好循环**：
  $$A \text{ revealed preferred to } B \quad \text{and} \quad B \text{ revealed preferred to } A$$
  这违反了显示偏好理论中**非循环性**的核心要求，表明消费者行为不满足理性选择假设。

#### 政策启示
- **通胀测量**：Paasche与Laspeyres指数差异率达$33\%((1.6-1.5)/1.5)$，警示单一指数可能扭曲生活成本评估
- **消费决策**：WARP检验可识别异常消费模式，Goldie案例揭示**价格变动下消费替代方向异常**（当$x_2$价格下降60%时，消费量从6降为0）
- **跨期比较**：数量指数证实实际消费水平增长$12.5\%$，即使价格上升，消费者福利提升源于消费结构优化

> 本段内容通过指数分解将价格变化与消费变化分离，结合WARP的实证检验，确立了**基于可观测行为的福利变化评估框架**，解决了传统效用分析中"不可观察偏好"的方法论困境。

---
### Page/Slide 3



## 当前图片解析

### 1. 提取文字与公式
**图表标注**:
- 轴标签：`Good 1`（横轴）、`Good 2`（纵轴）
- 线条：`Blue line`（蓝色线）、`Red line`（红色线）
- 点：`a`、`b`

**文字内容**:
```
7.2 (0) Freddy Frolic consumes only asparagus and tomatoes, which are highly seasonal crops in Freddy's part of the world. He sells umbrellas for a living, which provides a fluctuating income depending on the weather. But Freddy doesn't mind; he never thinks of tomorrow, so each week he spends as much as he earns. One week, when the prices of asparagus and tomatoes were each $1 a pound, Freddy consumed 15 pounds of each. Use blue ink to show the budget line in the diagram below. Label Freddy's consumption bundle with the letter A.

(a) What is Freddy's income? $30.

(b) The next week the price of tomatoes rose to $2 a pound, but the price of asparagus remained at $1 a pound. By chance, Freddy's income had changed so that his old consumption bundle of (15,15) was just affordable at the new prices. Use red ink to draw this new budget line on the graph below. Does your new budget line go through the point A? Yes.

What is the slope of this line? -1/2.

(c) How much asparagus can he afford now if he spent all of his income on asparagus? 45 pounds.

(d) What is Freddy's income now? $45.
```

**隐含公式**:
- 第一周预算约束: $I^1 = p_1^1 x_1 + p_2^1 x_2 = 1 \cdot x_1 + 1 \cdot x_2 = 30$
- 第二周预算约束: $I^2 = p_1^2 x_1 + p_2^2 x_2 = 1 \cdot x_1 + 2 \cdot x_2 = 45$
- 斜率计算: $-\frac{p_1}{p_2} = -\frac{1}{2}$

### 2. 图表分析与经济含义

#### 预算线变动的核心机制
- **蓝线（第一周）**：  
  $p_1^1 = p_2^1 = \$1$，收入 $I^1 = \$30$  
  → 横纵轴截距均为 30（图表仅展示 0-20 范围），对应消费点 $A=(15,15)$  
  → 价格比 $p_1/p_2=1$ 决定斜率为 $-1$

- **红线（第二周）**：  
  $p_1^2 = \$1$，$p_2^2 = \$2$，收入 $I^2 = \$45$  
  → 纵轴截距 $45/2=22.5$，横轴截距 $45$（图表显示至 20）  
  → 斜率为 $-\frac{1}{2}$ 反映番茄涨价后相对价格变化

#### 关键经济现象解析
1. **收入校准效应**：  
   新预算线通过原消费点 $A=(15,15)$（验证 $1 \times 15 + 2 \times 15 = 45$），此设定将**总价格效应**分解为纯替代效应（保持虚拟能力不变）与收入效应。上文通过 Goldie 案例揭示的消费降级风险在此情境中被显性化：若实际选择移向点 `a` 而非 $A$，表明存在显著替代效应。

2. **与 WARP 的关联性**：  
   - 若已知第二周选择点（如点 `a` 代表实际选择），可构建类似上文 Goldie 的检验：  
     - 当 $A$ 可担当时选择 `a` → `a` 被揭示偏好于 $A$  
     - 而本题第二周预算线通过 $A$ 且 $A$ 仍可负担，若转选 `a` 则需满足 WARP（无循环偏好）  
   - **对比上文框架**：本题隐含测试消费者行为合理性，若选择违反 WARP（如点 `b` 被选但 $A$ 更优），则表明偏好非理性（同上文 "偏好循环" 案例）。

3. **指数计算的实践意义**：  
   - **Paasche 价格指数**构建基础：  
     若将第一周视为基期、第二周为现期，需计算 $\frac{p^{current} \cdot x^{current}}{p^{base} \cdot x^{current}}$  
     - 但本题未明确 $x^{current}$，点 `a` 或 `b` 可能作为线索  
   - **数量指数推导**：  
     $A=(15,15)$ 在两次约束下均有效，暗示消费量未变，但因价格变动，数量指数需结合实际选择校准（上文数量指数公式 $\frac{p^{base} \cdot x^{current}}{p^{base} \cdot x^{base}}$ 在此可直接应用）。

#### 变动的政策启示
- **通胀测量陷阱**：  
  番茄价格翻倍而收入同步上升，若仅用 Paasche（当前消费基）指数会低估通胀（因未消费更多番茄），用 Laspeyres（基期消费基）会产生高估，与上文 "指数差异率达 33%" 的结论一致。
- **福利评估逻辑**：  
  消费点从 $A$ 移向 `a` 将验证上文核心论点——**福利变化需用消费结构优化抵消价格上升**，数量指数增长 12.5% 的经济学含义在此案例中表现为 $I$ 的调整使实际消费扩张（横轴截距从 30→45）。

---
### Page/Slide 4



# Freddy 预算约束变动的解析

## 1. 图片内容提取

### 文字内容
```
(e) Use pencil to shade the bundles of goods on Freddy's new red budget line that he definitely will not purchase with this budget. Is it possible that he would increase his consumption of tomatoes when his budget changes from the blue line to the red one? No.

Tomatoes
40
30         Blue line
20                 Pencil
                   shading
                             a
10
                          Red line
 0
   0      10        20     30     40
                 Asparagus

7.3 (0) Pierre consumes bread and wine. For Pierre, the price of bread is 4 francs per loaf, and the price of wine is 4 francs per glass. Pierre has an income of 40 francs per day. Pierre consumes 6 glasses of wine and 4 loaves of bread per day.
Bob also consumes bread and wine. For Bob, the price of bread is 1/2 dollar per loaf and the price of wine is 2 dollars per glass. Bob has an income of $15 per day.

(a) If Bob and Pierre have the same tastes, can you tell whether Bob is better off than Pierre or vice versa? Explain. Bob is better off. He can afford Pierre's bundle and still have income left.

(b) Suppose prices and incomes for Pierre and Bob are as above and that Pierre's consumption is as before. Suppose that Bob spends all of his income. Give an example of a consumption bundle of wine and bread such that, if Bob bought this bundle, we would know that Bob's tastes are not the same as Pierre's tastes. 7.5 wine and 0 bread, for example. If they had the same preferences,
```

### 图表关键特征
- **坐标轴**：横轴为 *Asparagus*（芦笋），纵轴为 *Tomatoes*（番茄）
- **预算线**：蓝线（原始预算约束），红线（新价格下的调整后预算约束）
- **关键点**：点 *a* 为新预算约束下的实际消费点
- **阴影区域**：标有 "Pencil shading" 的斜线填充区域

## 2. 图表经济含义解析

### 2.1 预算线变动机制
- **蓝线**：对应第一周预算约束 $I^1 = p_1^1x_1 + p_2^1x_2 = 30$（$p_1^1 = p_2^1 = 1$）
- **红线**：对应第二周调整后预算约束 $I^2 = p_1^2x_1 + p_2^2x_2 = 45$（$p_1^2 = 1, p_2^2 = 2$）
- **通过点A**：红线确实经过原消费点 $A=(15,15)$，验证 $1 \times 15 + 2 \times 15 = 45$，表明此预算线已调整收入以保持原消费组合可负担

### 2.2 阴影区域的微观经济学含义
- **位置特征**：位于红线"东南方"的三角形区域（图中斜线填充部分）
- **经济解释**：根据**显示偏好弱公理（WARP）**，这些组合 $(x_1,x_2)$ 满足：
  - $x_1 > 15$（芦笋消费量高于原消费点）
  - $x_2 < 15$（番茄消费量低于原消费点）
  - 且仍在新预算线**下方**（即帕累托劣于点$a$）
- **行为推断**：若消费者选择点*a*而非阴影区域中的任何点，说明这些阴影组合**被隐性拒绝**。这与上文Goldie案例一致——当存在更优选择时，理性消费者不会选择劣质组合

### 2.3 价格效应验证
- **番茄消费变动**：问题(e)明确指出"不可能增加番茄消费"，验证了**替代效应的符号决定**：
  1. 番茄涨价（$p_2$ 从 1→2）导致**替代效应**（保持效用不变）必然减少番茄消费
  2. 但同时收入增加（$I$ 从 30→45）产生**收入效应**
  3. 图中点*a*位于原消费点"西南"，说明总效应为消费减少（$x_2$ 下降），证明**替代效应主导**（与上文"番茄涨价导致消费下降"的结论一致）

### 2.4 与上文理论的延续性
- **WARP验证**：阴影区域的存在直接应用上文核心原理——若实际选择点*a*，则所有阴影点必然被**揭示不被偏好**，建立消费选择的严格偏序关系
- **收入-替代分解**：红线作为"补偿预算线"，将总效应分解为：
  - 从$A$到$a$的纯替代效应
  - 从$a$到实际选择点（图中未标出）的收入效应
- **福利变动方向**：点*a*位于原始无差异曲线**外侧**，暗示效用提升（与上文"数量指数增长12.5%"反映的福利改进一致）

## 3. Pierre-Bob案例的关联性
7.3题延续了**跨个体效用比较**的分析框架：
- ** Revealed Preference 应用**：Bob能负担Pierre的消费束(6,4)且有余额（$0.5 \times 4 + 2 \times 6 = 14 < 15$），直接证明*Bob is better off*
- **偏好异质性检验**：若Bob选择(7.5,0)，则违反与Pierre相同的偏好（Pierre消费正数量面包），体现上文"The Consumer's Opportunity Cost"原理

> **理论延伸**：此图表完整展示了**显示偏好理论的操作流程**——通过实际选择推断潜在无差异曲线形状，为后续指数计算和福利分析提供行为基础。

---
### Page/Slide 5



### 1. 图片文字与公式提取

#### 文字内容
- `this violates WARP, since each can afford but rejects the other’s bundle.`
- `7.4 (0) Here is a table of prices and the demands of a consumer named Ronald whose behavior was observed in 5 different price-income situations.`
- `(a) Sketch each of his budget lines and label the point chosen in each case by the letters A, B, C, D, and E.`
- `(b) Is Ronald’s behavior consistent with the Weak Axiom of Revealed Preference? Yes.`
- `(c) Shade lightly in red ink all of the points that you are certain are worse for Ronald than the bundle C.`
- `(d) Suppose that you are told that Ronald has convex and monotonic preferences and that he obeys the strong axiom of revealed preference. Shade lightly in blue ink all of the points that you are certain are at least as good as the bundle C.`

#### 表格数据
| Situation | $p_1$ | $p_2$ | $x_1$ | $x_2$ |
|-----------|--------|--------|--------|--------|
| A         | 1      | 1      | 5      | 35     |
| B         | 1      | 2      | 35     | 10     |
| C         | 1      | 1      | 10     | 15     |
| D         | 3      | 1      | 5      | 15     |
| E         | 1      | 2      | 10     | 10     |

#### 图表关键元素
- **坐标轴**：横轴 $x_1$（范围 0–40），纵轴 $x_2$（范围 0–40）
- **关键点**：
  - 点 A: $(5, 35)$
  - 点 B: $(35, 10)$
  - 点 C: $(10, 15)$
  - 点 D: $(5, 15)$
  - 点 E: $(10, 10)$
- **阴影区域**：
  - "Red shading"：左下斜线填充区域（标识为比 bundle C 更差的点）
  - "Blue shading"：右上斜线填充区域（标识为至少与 bundle C 一样好的点）

---

### 2. 图表经济含义解析（结合上文连续性分析）

#### 2.1 预算线与消费选择的验证
- **预算约束公式**：基于表格数据，Ronald 在每期的预算线为 $p_1 x_1 + p_2 x_2 = I_k$（$k = A, B, C, D, E$），其中 $I_k = p_1 x_1^k + p_2 x_2^k$。例如：
  - Situation A: $1 \cdot 5 + 1 \cdot 35 = 40$，预算线 $x_1 + x_2 = 40$
  - Situation C: $1 \cdot 10 + 1 \cdot 15 = 25$，预算线 $x_1 + x_2 = 25$
- **WARP 一致性**：问题 (b) 确认行为符合 Weak Axiom of Revealed Preference (WARP)。这与上文 **"Pierre-Bob 案例"** 的逻辑一致：  
  - 例如，在 Situation B，$p_1=1, p_2=2$，Ronald 选择 $(35,10)$，而 bundle C $(10,15)$ 可负担（成本 $1 \cdot 10 + 2 \cdot 15 = 40 \leq 55$），但未被选择 → **B 被显示偏好于 C**。  
  - 在 Situation C，$p_1=1, p_2=1$，bundle B $(35,10)$ 不可负担（成本 $45 > 25$）→ 无 WARP 违反。  
  - 此验证延续了上文 **"WARP 操作流程"**：通过实际消费束推断偏好序，避免类似 Pierre-Bob 中 "each can afford but rejects" 的矛盾。

#### 2.2 阴影区域的微观经济学含义
- **"Red shading" 区域（问题 c）**：  
  - 对应上文 **"Pencil shading" 阴影区域**（被隐性拒绝的点）。  
  - 经济含义：满足 $p_1^C x_1 + p_2^C x_2 \leq I_C$（位于 bundle C 预算线下方），但未被选择的点。例如：  
    - 在 Situation C 的预算约束 $x_1 + x_2 = 25$ 下，任何点如 $(5,15)$ 满足 $5+15=20 \leq 25$ 但未选择 → **被揭示劣于 C**。  
  - 延续上文 **WARP 推断**：若 Ronald 选择 C，则阴影内所有点严格差于 C，建立 **消费选择的严格偏序**（与上文 "点 a 位于原消费点西南，阴影区域隐性拒绝" 逻辑相同）。

- **"Blue shading" 区域（问题 d）**：  
  - 假设凸性 (convexity) 和单调性 (monotonicity)，并服从 Strong Axiom of Revealed Preference (SARP)。  
  - 依据上文 **"凸偏好扩展"** 原理：  
    - 由 bundle C 被选择，结合 SARP → 所有被 C 直接或间接显示偏好的点构成 **无差异曲线外侧封闭区域**。  
    - 例如：点 E $(10,10)$ 在 Situation E 被选择且可负担 C（$1 \cdot 10 + 2 \cdot 10 = 30 \geq 25$），但 C 未被选择 → **E 被显示偏好于 C**；凸性将偏好延伸至区域上边界（蓝色阴影覆盖 C 的 "至少一样好" 集合）。  
  - 与上文 **"福利变动方向"** 关联：蓝色区域代表效用不下降的集合，支撑后续福利指数计算。

#### 2.3 与上文知识点的延续性
- **显示偏好理论的操作化**：  
  - 表格数据为实证基础（类似上文 Goldie 案例），通过实际价格-消费对验证偏好。  
  - Red shading 直接应用上文 **"被隐性拒绝的劣质组合"** 框架，Blue shading 延伸为 **SARP 下的偏好凸包**（回应上文 "显示偏好理论的操作流程"）。  
- **对比 Pierre-Bob 案例**：  
  - 本例中 Ronald 行为 **符合 WARP**（回答 "Yes"），反例是上文 Bob 选择 $(7.5,0)$ 违反与 Pierre 偏好一致性 → 强调 **一致性检验需满足预算可行性与选择唯一性**。  
- **理论延伸**：  
  - 阴影区域明确定义了 **潜在无差异曲线边界**，为福利分析（如数量指数）提供几何基础（与上文 "数量指数增长 12.5%" 的效用推理一致）。  
  > 关键差异：本例通过 **多期数据**（5 种价格-收入情形）强化偏好推断，而上文为两期比较；蓝色阴影的凸性假设进一步解决 "为何某些点无法确定偏好"，深化上文 WARP 应用限制。

---
### Page/Slide 6



### 1. 文字与公式提取  
**当前图片中的所有文字和公式：**  
- **页眉与章节**：86 REVEALED PREFERENCE (Ch. 7)  
- **问题 7.5 (0)**:  
  > Horst and Nigel live in different countries. Possibly they have different preferences, and certainly they face different prices. They each consume only two goods, $x$ and $y$. Horst has to pay 14 marks per unit of $x$ and 5 marks per unit of $y$. Horst spends his entire income of 167 marks on 8 units of $x$ and 11 units of $y$. Good $x$ costs Nigel 9 quid per unit and good $y$ costs him 7 quid per unit. Nigel buys 10 units of $x$ and 9 units of $y$.  
  - **(a)**:  
    > Which prices and income would Horst prefer, Nigel’s income and prices or his own, or is there too little information to tell? Explain your answer.  
    > **Horst prefers Nigel’s budget to his own.**  
    > **With Nigel’s budget, he can afford his own bundle with money left over.**  
  - **(b)**:  
    > Would Nigel prefer to have Horst’s income and prices or his own, or is there too little information to tell? **There is too little information to tell.**  
- **问题 7.6 (0)**:  
  > Here is a table that illustrates some observed prices and choices for three different goods at three different prices in three different situations.  
  - **表格**:
    | Situation | $p_1$ | $p_2$ | $p_3$ | $x_1$ | $x_2$ | $x_3$ |
    |-----------|-------|-------|-------|-------|-------|-------|
    | A         | 1     | 2     | 8     | 2     | 1     | 3     |
    | B         | 4     | 1     | 8     | 3     | 4     | 2     |
    | C         | 3     | 1     | 2     | 2     | 6     | 2     |
  - **(a) 说明**:  
    > We will fill in the table below as follows. Where $i$ and $j$ stand for any of the letters A, B, and C in Row $i$ and Column $j$ of the matrix, write the value of the Situation-$j$ bundle at the Situation-$i$ prices. For example, in Row A and Column A, we put the value of the bundle purchased in Situation A at Situation A prices. From the table above, we see that in Situation A, the consumer bought bundle $(2,1,3)$ at prices $(1,2,8)$. The cost of this bundle A at prices A is therefore $(1 \times 2) + (2 \times 1) + (8 \times 3) = 28$, so we put 28 in Row A, Column A. In Situation B the consumer bought bundle $(3,4,2)$. The value of the Situation-B bundle, evaluated at the situation-A prices is $(1 \times 3) + (2 \times 4) + (8 \times 2) = 27$, so put 27 in Row A, Column B.  

**关键公式**:  
- 预算线扩展（3商品）：$p_1^{(k)} x_1^{(k)} + p_2^{(k)} x_2^{(k)} + p_3^{(k)} x_3^{(k)} = I_k$，其中 $k = A, B, C$  
- 成本计算示例：  
  - Situation A 消费束 A 的成本：$ (1 \times 2) + (2 \times 1) + (8 \times 3) = 28 $  
  - Situation B 消费束在 A 价格下的成本：$ (1 \times 3) + (2 \times 4) + (8 \times 2) = 27 $  

---

### 2. 表格含义与知识延续性分析  
本页无图表，但 **7.6 的表格**（3商品消费情景数据）是上文知识点的自然延伸，需结合 **显示偏好理论框架** 解读：  

#### **表格数据的经济逻辑**  
- **预算线的多商品扩展**：  
  上文聚焦2商品预算线（$p_1 x_1 + p_2 x_2 = I_k$），本表引入3商品，预算线一般化为：  
  \[
  p_1^{(k)} x_1 + p_2^{(k)} x_2 + p_3^{(k)} x_3 = I_k, \quad I_k = \sum_{m=1}^{3} p_m^{(k)} x_m^{(k)}
  \]  
  例如：  
  - Situation A 中，$I_A = 1 \cdot 2 + 2 \cdot 1 + 8 \cdot 3 = 28$，消费束 $(2,1,3)$ 恰好耗尽收入。  
  - Situation B 消费束 $(3,4,2)$ 在 A 价格下成本27（< $I_A=28$），表明该束 **在 Situation A 可负担但未被选择**，隐含 **A 被显示偏好于 B**（延续WARP一致性检验）。  

- **WARP 操作化验证**：  
  上文验证Ronald行为符合WARP（如Situation B/C间无矛盾），本表提供相同工具：  
  - 若消费束 $j$ 未被选择，但在 $i$ 价格下成本 $\leq I_i$（如B在A价格下27 ≤ 28），则 **$i$ 被显示偏好于 $j$**。  
  - 7.5 部分进一步说明：Horst 可负担自身消费束（8,11）在 Nigel 价格下（9×8 + 7×11 = 149 < Nigel 收入 10×9 + 9×7 = 153），钱有剩余，**Nigel 预算被显示偏好于 Horst 预算**。这呼应上文 "Pierre-Bob 案例" 中 `each can afford but rejects` 的核心矛盾检验逻辑。  

#### **与上文知识点的连续性**  
- **多期数据强化偏好推断**：  
  上文用Ronald 5期数据定义红/蓝阴影区域，本表以3期3商品数据为实证基础，延续 **"表格数据作为显示偏好理论操作化工具"**（类似上文 Goldie 案例）。未填充的矩阵需计算 `$i$ 价格下 $j$ 消费束成本`，其结果直接用于：  
  - 识别 `被隐性拒绝点`（如情况A中成本<28的未选束，构成上文 red shading 对应的劣质组合集合）。  
  - 潜在未来步骤中验证 SARP：若存在循环偏好（如 A 显示偏好 B、B 显示偏好 C、C 显示偏好 A），则违反 SARP；上文 blue shading 依赖的凸性假设在此可类似用于推断无差异曲线上边界。  
- **关键差异与补充**：  
  - 7.5 强调预算可负担性对比（"money left over"），仅解决上文 "WARP 操作流程" 中的 "能否负担" 步骤，而未涉及偏好连续性（故Nigel 部分信息不足），凸显上文 "一致性检验需满足预算可行性与选择唯一性" 的限制。  
  - 7.6 表格将上文 2商品模型扩展至 3商品，但 **预算线空间拓扑结构不变**：可负担集仍为超平面以下区域，为后续福利指数计算（如上文 "数量指数增长 12.5%"）提供几何基础。  
> 此部分延续上文 **显示偏好理论的操作流程**，未引入新概念，但通过多商品情景深化 "实证数据如何驱动偏好推断" 的逻辑链条，解决上文未覆盖的复杂情形操作细节。

---
### Page/Slide 7



### 1. 提取当前图片中的文字与公式  
#### 文字内容：  
- 页眉：`NAME ________ 87`  
- 表格 1：  
  | Prices/Quantities | A   | B   | C   |  
  |-------------------|-----|-----|-----|  
  | A                 | 28  | 27  | 30  |  
  | B                 | 33  | 32  | 30  |  
  | C                 | 13  | 17  | 16  |  

- 问题 (b)：  
  > (b) Fill in the entry in Row $i$ and Column $j$ of the table below with a $D$ if the Situation-$i$ bundle is directly revealed preferred to the Situation-$j$ bundle. For example, in Situation A the consumer’s expenditure is $28. We see that at Situation-A prices, he could also afford the Situation-B bundle, which cost 27. Therefore the Situation-A bundle is directly revealed preferred to the Situation-B bundle, so we put a $D$ in Row A, Column B. Now let us consider Row B, Column A. The cost of the Situation-B bundle at Situation-B prices is 32. The cost of the Situation-A bundle at Situation-B prices is 33. So, in Situation B, the consumer could not afford the Situation-A bundle. Therefore Situation B is *not* directly revealed preferred to Situation A. So we leave the entry in Row B, Column A blank. Generally, there is a $D$ in Row $i$ Column $j$ if the number in the $ij$ entry of the table in part (a) is less than or equal to the entry in Row $i$, Column $i$. There will be a violation of WARP if for some $i$ and $j$, there is a $D$ in Row $i$ Column $j$ and also a $D$ in Row $j$, Column $i$. Do these observations violate WARP? **No.**  

- 表格 2：  
  | Situation | A   | B   | C   |  
  |-----------|-----|-----|-----|  
  | A         | —   | D   | I   |  
  | B         | I   | —   | D   |  
  | C         | D   | I   | —   |  

- 问题 (c)：  
  > (c) Now fill in Row $i$, Column $j$ with an $I$ if observation $i$ is *indirectly* revealed preferred to $j$. Do these observations violate the Strong Axiom of Revealed Preference? **Yes.**  

- 新增内容：  
  > **7.7 (0)** It is January, and Joe Grad, whom we met in Chapter 5, is shivering in his apartment when the phone rings. It is Mandy Manana, one of the students whose price theory problems he graded last term. Mandy asks if Joe would be interested in spending the month of February in her apartment. Mandy, who has switched majors from economics to political science, plans to go to Aspen for the month and so her apartment will be empty (alas). All Mandy asks is that Joe pay the monthly service charge of $40 charged by her landlord and the heating bill for the month of February. Since her apartment is much better insulated than Joe’s, it only costs $1 per month to raise the temperature by 1 degree. Joe  

#### 关键公式：  
- 直接显示偏好判定规则：  
  $$
  \text{若 } \text{cell}(i,j) \leq \text{cell}(i,i) \text{，则 Situation } i \text{ 直接显示偏好于 } j
  $$  
  其中 $\text{cell}(i,j)$ 为价格-数量表中第 $i$ 行第 $j$ 列值（即 Situation-$j$ 消费束在 Situation-$i$ 价格下的成本）。  

---

### 2. 图表解析与知识延续性  
#### 表格 1 的含义（延续【上文知识点总结】预算线扩展逻辑）  
- **结构与数据经济逻辑**：  
  此表是【上文知识点总结】中 3 商品预算线模型（$p_1^{(k)} x_1 + p_2^{(k)} x_2 + p_3^{(k)} x_3 = I_k$）的实证应用。  
  - 行标（A/B/C）表示价格情景：$i$-行代表 Situation-$i$ 的价格向量。  
  - 列标（A/B/C）表示消费情景：$j$-列表示 Situation-$j$ 的消费束。  
  - $\text{cell}(i,j)$ = Situation-$j$ 消费束在 Situation-$i$ 价格下的成本，计算公式：  
    $$\sum_{m=1}^{3} p_m^{(i)} x_m^{(j)}$$  
  - **对角线元素**（如 $\text{cell}(A,A)=28$）= Situation-$i$ 的总收入 $I_i$（消费束耗尽收入），与上文示例 $I_A = 1 \cdot 2 + 2 \cdot 1 + 8 \cdot 3 = 28$ 一致。  

- **关键数据解读（验证上文 WARP 操作化步骤）**：  
  | 情景对比 | 成本计算示例 | 与上文知识连续性 |  
  |----------|--------------|------------------|  
  | $\text{cell}(A,B)=27$ | Situation-B 消费束在 A 价格下成本（$1 \times 3 + 2 \times 4 + 8 \times 2 = 27$） | 直接复用上文 "Situation B 消费束在 A 价格下成本 27" 案例，验证 *A 可负担但未选择 B* → A 被显示偏好于 B（WARP 基础） |  
  | $\text{cell}(B,A)=33$ | Situation-A 消费束在 B 价格下成本 | 延续上文 "B 价格下 A 消费束成本 33 > $I_B=32$"，说明 *B 无法负担 A* → 无直接偏好 |  
  | $\text{cell}(C,A)=13$ | Situation-A 消费束在 C 价格下成本 | 延续上文扩展逻辑：低价格下相同消费束成本更低，暗示价格变动对可负担集的影响 |  

#### 表格 2 与问题 (b)/(c) 的经济学含义（深化上文显示偏好理论）  
- **表格 2 的构建逻辑**：  
  - **$D$ 标记（直接显示偏好）**：  
    基于表格 1 的成本比较，严格遵循上文 **WARP 操作化规则**：  
    $$\text{cell}(i,j) \leq \text{cell}(i,i) \implies D \text{ in } (i,j)$$  
    - 例如：A→B（27 ≤ 28），B→C（30 ≤ 32），C→A（13 ≤ 16）均标记 $D$，与上文 "red shading 代表被隐性拒绝点" 逻辑一致（成本 ≤ 收入 → 消费束可负担但未选）。  
  - **$I$ 标记（间接显示偏好）**：  
    新增知识点，是上文 **SARP 的实证化延伸**：  
    - 通过直接偏好链推导间接偏好（如 A→B 且 B→C ⇒ A间接偏好C）。  
    - 表格中 A→C（$I$）、B→A（$I$）、C→B（$I$）构成传递链，符合上文 "SARP 要求无循环偏好" 的框架。  

- **WARP 与 SARP 验证结果（关键知识延续）**：  
  | 测试 | 上文知识点 | 当前图片应用 | 结论 |  
  |------|------------|--------------|------|  
  | **WARP** | 上文："WARP 要求若 $i$ 显示偏好 $j$，则 $j$ 不能显示偏好 $i$" | 检查互斥 $D$ 标记：无 (i,j) 与 (j,i) 同时为 $D$（如 A→B $D$ 但 B→A 无 $D$） | 无违反（上文 "操作流程" 中一致性检验成立） |  
  | **SARP** | 上文："SARP 禁止间接偏好循环（A→B→C→A）" | 直接偏好链 A→B $D$、B→C $D$、C→A $D$ 形成循环，导致间接偏好 A→C $I$ 与 C→A $D$ 冲突 | **违反 SARP**（呼应上文 "若存在 A 显示偏好 B、B 显示偏好 C、C 显示偏好 A，则违反 SARP"） |  

- **与上文的连续性**：  
  - 表格 1 是上文 **7.6 消费情景数据表** 的实现，将抽象公式（$p_1^{(k)} x_1^{(k)} + p_2^{(k)} x_2^{(k)} + p_3^{(k)} x_3^{(k)} = I_k$）转化为可计算矩阵，深化 "预算成本比较 → 偏好推断" 操作链。  
  - 问题 (c) 突破上文 WARP 局限（仅检查直接偏好），引入 **SARP 检验**：上文虽提及 SARP，但仅警告其逻辑（"若循环则违 SARP"），此处首次用数据实证 **SARP 被违反**（循环偏好导致福利指数计算失效，呼应上文 "数量指数增长 12.5%" 的稳健性依赖 SARP）。  
  - **本质统一性**：两表格均延续上文 "显示偏好理论的操作化工具" 定位——将多期消费数据转化为偏好关系矩阵，验证理论一致性，为后续政策分析（如需求函数估计）提供实证基础。

---
### Page/Slide 8



# 显示偏好理论的实践应用：Joe的消费决策分析

## 1. 提取文字与公式

### 文字内容
- 页眉：`88 REVEALED PREFERENCE (Ch. 7)`
- 主体描述：
  > thanks her and says he will let her know tomorrow. Joe puts his earmuffs back on and muses. If he accepts Mandy's offer, he will still have to pay rent on his current apartment but he won't have to heat it. If he moved, heating would be cheaper, but he would have the $40 service charge. The outdoor temperature averages 20 degrees Fahrenheit in February, and it costs him $2 per month to raise his apartment temperature by 1 degree. Joe is still grading homework and has $100 a month left to spend on food and utilities after he has paid the rent on his apartment. The price of food is still $1 per unit.

- 问题说明：
  > `(a) Draw Joe's budget line for February if he moves to Mandy's apartment and on the same graph, draw his budget line if he doesn't move.`
  > 
  > `(b) After drawing these lines himself, Joe decides that he would be better off not moving. From this, we can tell, using the principle of revealed preference that Joe must plan to keep his apartment at a temperature of less than 60 degrees.`
  > 
  > `(c) Joe calls Mandy and tells her his decision. Mandy offers to pay half the service charge. Draw Joe's budget line if he accepts Mandy's new offer. Joe now accepts Mandy's offer. From the fact that Joe accepted this offer we can tell that he plans to keep the temperature in Mandy's apartment above 40 degrees.`

- 图表标签：
  - 纵轴：`Food` (0-120)
  - 横轴：`Temperature` (0-80)
  - 三条线：`Don't move budget line`, `Move budget line`, `'New offer' budget line`
- 页脚：`7.8 (0) Lord Peter Pommy is a distinguished criminologist...`

### 公式与数值
- 温度成本参数：`$2 per month to raise temperature by 1 degree`
- 收入约束：`$100 a month left for food and utilities`
- 关键阈值：`less than 60 degrees`, `above 40 degrees`

## 2. 图表解析与显示偏好理论应用

### 图表核心结构
| 预算线类型 | 斜率特征 | 经济含义 | 预算约束公式 |
|------------|----------|----------|--------------|
| Don't move | 最陡峭 | 需自行供暖(20°F起点), $2/度 | Food = 140 - 2×Temperature |
| Move | 中等斜率 | 有$40服务费但供暖更便宜 | Food = 60 - m₁×Temperature |
| 'New offer' | 最平缓 | Mandy付半服务费($20), 实际收入提升 | Food = 80 - m₂×Temperature |

### 预算线交点的显示偏好含义
1. **"Don't move" vs "Move"的交点(60°F)**:
   - 与上文**WARP操作化规则**直接对应：*当消费束j在价格i下可负担且未被选择，表明i被显示偏好于j*
   - 在60°F处，两种方案无差异；低于此值时，"Don't move"预算集包含更多食物选择
   - Joe选择不搬 → 其计划温度的消费束属于"Don't move"预算集但不属于"Move"最优集 → **显示偏好链：不搬环境 > 搬环境在低温场景**

2. **"Move" vs "New offer"的交点(40°F)**:
   - 体现**SARP间接偏好推导**：新报价改变了可负担集，形成新的偏好关系链
   - 40°F是决策边界：高于此值时，"New offer"预算集严格优于原"Move"方案
   - Joe接受新报价 → 其计划温度消费束在"New offer"预算集内且优于不搬方案 → **隐性揭示高温偏好**

### 决策阈值的微观机制
| 决策场景 | 显示偏好原理 | 与上文知识连续性 |
|----------|--------------|------------------|
| **不搬决策(b)** | 消费束(T<60, F) ∈ "Don't move"预算集但 ∉ "Move"最优集 | 验证上文"cell(i,j) ≤ cell(i,i)"规则：<br>在不搬价格下，搬的消费束成本≤收入但未选 → 不搬被显示偏好 |
| **接受新报价(c)** | 消费束(T>40, F) ∈ "New offer"预算集且优于前方案 | 延续SARP框架：服务费降低→预算集扩张→ 形成间接偏好链：<br>新报价 > 不搬 > 原搬方案 |
| **阈值经济逻辑** | 温度作为第三维度消费变量，预算线斜率反映边际替代率 | 呼应上文"多期消费数据转化为偏好关系矩阵"：<br>此处将温度-食物二维空间的操作化处理 |

### 理论深化
- **预算线斜率差异**：体现价格参数变化的影响（对比上文表格1中不同情景价格矩阵）
- **温度阈值的精确性**：60°F与40°F点实际对应**间接显示偏好**的临界点，与上文表格2中$I$标记的逻辑一致——通过边界点推断消费者计划
- **服务费变化**：属于外生价格冲击，完美模拟了上文"Situation B消费束在A价格下成本"的实证操作，形成可量化的决策监控机制

> 本场景实质是**一维（温度）扩展的显示偏好实验**：通过观察预算线边界选择，反推消费计划的具体数值范围，深化了上文"需求函数估计的实证基础"——无需效用函数即可识别消费者实际偏好边界。

---
### Page/Slide 9



# 微观经济学案例解析：啤酒-香肠消费的显示偏好分析

## 1. 图片内容提取

### 文字信息
- **核心叙事**：Lord Peter调查Sir Cedric及其三位嫌疑人（R. Preston McAfee、Richard Manning、Richard Stevenson）的消费行为，三人与Sir Cedric均将全部收入用于啤酒和香肠
- **消费数据**：
  - *Sir Cedric Pinchbottom*：10 kg香肠、20 L啤酒；价格：啤酒1英镑/L，香肠1英镑/kg
  - *R. Preston McAfee*：5 L啤酒、20 kg香肠；价格：啤酒1加元/L，香肠2加元/kg
  - *Richard Manning*：5 kg香肠、10 L啤酒；价格：啤酒2新西兰元/L，香肠2新西兰元/kg
  - *Richard Stevenson*：5 kg香肠、30 L啤酒；价格：啤酒10福克兰镑/L，香肠20福克兰镑/kg
- **问题要求**：(a) 为三位嫌疑人绘制预算线，叠加Sir Cedric的预算线及消费选择

### 隐含公式
| 消费者 | 预算约束公式 | 总支出 |
|--------|--------------|--------|
| Sir Cedric | $S + B = 30$ | 30英镑 |
| McAfee | $B + 2S = 45$ | 45加元 |
| Manning | $2B + 2S = 30$ | 30新西兰元 |
| Stevenson | $10B + 20S = 400$ | 400福克兰镑 |

*注：$S$表示香肠(kg)，$B$表示啤酒(L)*

## 2. 预算线结构与显示偏好应用

### 预算线几何特征对比
| 消费者 | 预算线斜率 | 横轴截距(B) | 纵轴截距(S) | 与上文知识关联 |
|--------|------------|-------------|-------------|----------------|
| Sir Cedric | -1 | 30 | 30 | 对应上文温度-食物二维空间基础模型 |
| McAfee | -0.5 | 45 | 22.5 | 类似"Move budget line"斜率变化逻辑 |
| Manning | -1 | 15 | 15 | 显示价格比例变化但相对价格不变 |
| Stevenson | -0.5 | 40 | 20 | 与McAfee相同斜率但预算规模不同 |

### 显示偏好关系检验（基于WARP原则）

#### 1. **McAfee与Sir Cedric的偏好关系**
- Sir Cedric消费束在McAfee价格体系下的成本：
  $1 \times 20 + 2 \times 10 = 40 \leq 45$（可负担）
- McAfee在可负担Sir Cedric消费束的情况下未选择它 → **显示偏好：McAfee的消费束 ≻ Sir Cedric消费束**
- *对应上文验证规则*：cell(i,j) = 40 ≤ 45 = cell(i,i)，表明当i=McAfee, j=Cedric时，i被显示偏好

#### 2. **Manning与Sir Cedric的偏好关系**
- Sir Cedric消费束在Manning价格体系下的成本：
  $2 \times 20 + 2 \times 10 = 60 > 30$（不可负担）
- 根据WARP，**无法推断直接显示偏好关系**
- *经济含义*：与上文"消费束j在价格i下不可负担"情况一致，不能形成明确偏好链条

#### 3. **Stevenson与Sir Cedric的偏好关系**
- Sir Cedric消费束在Stevenson价格体系下的成本：
  $10 \times 20 + 20 \times 10 = 400 = 400$（刚好可负担）
- Stevenson未选择Sir Cedric消费束 → **显示偏好：Stevenson消费束 ≻ Sir Cedric消费束**
- *理论延伸*：符合上文"situation where consumer has equal cost"的边界条件分析

### 决策阈值分析
| 临界点 | 经济意义 | 显示偏好含义 |
|--------|----------|--------------|
| 斜率-1 | 相对价格相等(啤酒:香肠=1:1) | Manning与Sir Cedric具有相同无差异曲线斜率 |
| 预算线交点 | 价格体系转换临界点 | 与上文温度阈值(40°F,60°F)同理：通过边界交叉识别偏好差异 |
| 不可负担区域 | 超出消费能力的组合 | 对应上文"消费束j在价格i下超出预算"导致无法形成偏好关系 |

## 3. 理论深化与知识衔接

### 显示偏好矩阵构建
- 将四人消费数据代入**间接显示偏好**推导框架：
  - McAfee和Stevenson对Sir Cedric形成直接显示偏好劣势
  - Manning因预算限制无法建立直接比较
- *呼应上文SARP应用*：通过可量化价格-消费关系链，构建跨货币体系的偏好排序

### 预算线斜率的理论意义
- 斜率 $-\frac{P_B}{P_S}$ 体现**边际替代率的市场约束**
  - 当 $|\frac{P_B}{P_S}|$ 减小，预算线更平缓 → 相当于上文"New offer"预算线的福利改善
  - Manning案例显示：即使绝对价格变化，**相对价格不变**则预算线平行移动（类似上文温度成本参数恒定情形）

### 与此前温度-食物模型的连续性
| 原模型(温度-食物) | 本案例(啤酒-香肠) | 理论一致性 |
|------------------|-------------------|------------|
| 温度作为第三维度 | 货币单位作为背景变量 | 二维消费空间操作化处理 |
| 移民服务费变化 | 跨国价格体系差异 | 外生价格冲击的决策影响 |
| 40°F/60°F阈值 | 预算线交点的不可比区域 | 间接显示偏好的临界点识别 |

> 本案例通过跨国价格差异构建**多情景预算约束**，完美实现上文所述"无需效用函数即可识别消费者实际偏好边界"的理论框架。特别是Manning案例中，尽管绝对消费量不同，但相对价格与Sir Cedric相同，若结合SARP可推断其可能是伪装的Sir Cedric——这与上文通过边界点推断消费计划的核心逻辑完全一致。

---
### Page/Slide 10



# Current Image Analysis

## Extracted Content

### Text and Formulas
- Page header: `90 REVEALED PREFERENCE (Ch. 7)`
- Chart axis labels: `Sausage` (vertical axis), `Beer` (horizontal axis)
- Chart point labels: `McAfee`, `Pinchbottom`, `Manning`, `Stevenson`
- Text (b): *"After pondering the dossiers for a few moments, Lord Peter announced. 'Unless Sir Cedric has changed his tastes, I can eliminate one of the suspects. Revealed preference tells me that one of the suspects is innocent.' Which one? McAfee."*
- Text (c): *"After thinking a bit longer, Lord Peter announced. 'If Sir Cedric left voluntarily, then he would have to be better off than he was before. Therefore if Sir Cedric left voluntarily and if he has not changed his tastes, he must be living in Falklands.'"*
- Problem 7.9 (1) description and part (a) instructions: *"The McCawber family... how much food could they buy if they spent all their money on food coupons? $300. How much could they spend on other things if they bought"*

### Formulas
- Monetary value: `$300`

## Chart Explanation

The chart visualizes a **beer-sausage consumption space** with four distinct budget constraints, each corresponding to an individual's price-income scenario. Based on the scoring summary's price-income framework:

| Individual | Budget Line Geometry | Parameter Interpretation | Consumption Bundle (Beer, Sausage) |
|------------|----------------------|----------------------------|----------------------------------|
| **Manning** | Steep slope (-1), low intercepts | $-\frac{P_B}{P_S} = -1$; income = 15 (matches scoring summary) | (10, 5) |
| **McAfee** | Flatter slope (-0.5), high intercepts | $-\frac{P_B}{P_S} = -0.5$; income = 45 (matches scoring summary) | (10, 20) |
| **Stevenson** | Same slope as McAfee (-0.5), lower intercepts | $-\frac{P_B}{P_S} = -0.5$; income = 40 (matches scoring summary) | (30, 5) |
| **Pinchbottom** | Slope -0.5 passing through (20,10) | Represents Sir Cedric's benchmark bundle (20,10) with implied $\frac{P_B}{P_S}=1$ |

**Key implications for revealed preference analysis**:
1. **WARP violation for McAfee** (aligns with scoring summary):  
   - At McAfee's prices ($P_B=1$, $P_S=2$), Sir Cedric's bundle (20,10) costs $1 \times 20 + 2 \times 10 = 40 \leq 45$ → **affordable**  
   - McAfee chooses (10,20) instead of the affordable (20,10) → **direct display of strict preference for (10,20) over (20,10)**  
   - This creates an *inconsistency* if Sir Cedric's tastes are unchanged (WARP violation: same tastes would require choosing the affordable (20,10)). Thus Lord Peter eliminates McAfee as "innocent" (i.e., inconsistent with unchanged preferences).

2. **Non-violation for Manning** (verified in scoring summary):  
   - At Manning's prices ($P_B=P_S=2$), (20,10) costs $2 \times 20 + 2 \times 10 = 60 > 15$ → **unaffordable**  
   - No preference inference possible, explaining why Manning remains a feasible suspect.

3. **Boundary case for Stevenson**:  
   - At Stevenson's prices ($P_B=10$, $P_S=20$), (20,10) costs $10 \times 20 + 20 \times 10 = 400 = 400$ → **just affordable**  
   - Since (20,10) was rejected despite affordability (choosing (30,5) instead), a *weak WARP violation* occurs. However, the text specifically highlights McAfee due to the clear affordability gap (40 < 45 vs. 400 = 400), making the violation unambiguous under strict preference logic.

The budget line slopes directly reflect **relative price changes** as established in prior sections:
- Steeper lines (e.g., Manning) → higher $\left|\frac{P_B}{P_S}\right|$ → greater opportunity cost of beer in sausage terms
- Flatter lines (e.g., McAfee/Stevenson) → lower $\left|\frac{P_B}{P_S}\right|$ → welfare improvement via reduced trade-off rigidity (cf. "New offer" analogy in scoring summary)

## Contextual Continuity

- The **Falklands reference in (c)** extends the *threshold analysis* from the scoring summary: A voluntary move requires the new location to place Sir Cedric on a higher indifference curve (i.e., the budget constraint at Falklands must reveal preference for his new bundle over (20,10)). This operationalizes the "price system conversion critical point" concept via geographic choice.

- The **McCawber problem (7.9)** will leverage this geometric framework to compare:
  - Old budget line (red): Baseline income = $150 ($100 food + $50 others)
  - Grant budget line (black): $50 cash → parallel shift
  - Coupon budget line: Nonlinear kink at $150 food spend (explaining "$300" maximum food purchase: $150 income / $0.5 effective price per food unit)

This directly applies the "multi-scenario constraint" methodology from the scoring summary to welfare policy analysis, with coupon geometry revealing how *price distortions* (vs. cash) restrict consumption choices—extending the beer-sausage analysis to food-other goods.

---
### Page/Slide 11



### Extracted Content from Current Image

**Text Elements:**
- Header: `NAME __________ 91`
- Instruction:  
  *"no food? $150. Use blue ink to draw their budget line if they choose the coupon option."*
- Graph labels:  
  - Axes: `Food` (x-axis, 0–240), `Other things` (y-axis, 0–180)  
  - Lines: `Red budget line`, `Black budget line`, `Blue budget line`  
  - Points: `a`, `b`, `c` (visible on graph)
- Problem parts:
  - **(b)** *"Using the fact that food is a normal good for the McCawbers, and knowing what they purchased before, darken the portion of the black budget line where their consumption bundle could possibly be if they choose the lump-sum grant option. Label the ends of this line segment A and B."*
  - **(c)** *"After studying the graph you have drawn, you report to the McCawbers: 'I have enough information to be able to tell you which choice to make. You should choose the **coupon** because **you can get more food even when other expenditure is constant**.'"*
  - **(d)** *"Mr. McCawber thanks you for your help and then asks, 'Would you have been able to tell me what to do if you hadn’t known whether food was a normal good for us?' On the axes below, draw the same budget lines you drew on the diagram above, but draw indifference curves for which food is not a normal good and for which the McCawbers would be better off with the program you advised them not to take."*

**No explicit formulas** appear in the image, but budget-line geometry implies linear constraints.

---

### Chart Interpretation (Continuity with Prior Context)

#### **Budget Line Geometry**
| Line | Interpretation | Slope Meaning | Connection to Prior Analysis |
|------|----------------|---------------|------------------------------|
| **Red** | Baseline budget constraint ($150 income) | Steeper slope → higher $ \frac{P_{\text{Food}}}{P_{\text{Other}}} $ | Reflects baseline income = $150 as in scoring summary |
| **Black** | Lump-sum $50 grant → parallel shift outward | Same slope as red, intercepts shifted | Matches prior description: *"parallel shift under cash grant"* |
| **Blue** | Coupon option (price distortion) | Flatter slope → lower effective $ \frac{P_{\text{Food}}}{P_{\text{Other}}} $ | Represents *"nonlinear kink at $150 food spend"* but simplified as linear in this graph for direct comparison |

#### **Key Observations from the Chart**
1. **Flatter slope of Blue line**:  
   - Indicates a reduction in the effective price of food due to the coupon (e.g., subsidy).  
   - For any fixed level of "Other things" expenditure (e.g., 90 units), the Blue line allows **more food** than the Black line (e.g., point *a* lies farther right on the Blue line than on the Black line).  
   - Directly validates part (c): *"you can get more food even when other expenditure is constant"*. This arises because the coupon relaxes the trade-off between goods, analogous to the *"New offer"* welfare improvement logic from prior sections.

2. **Point c**:  
   - Likely represents the original consumption bundle (20,10 in beer-sausage analogy), lying on the Red line.  
   - When moving to the Coupon option, the feasible set expands **proportionally more in the Food direction** than under the Lump-sum grant (Black line), favoring food as a normal good.

3. **WARP/Preference Logic**:  
   - Although not explicitly shown, if the McCawbers previously chose a bundle on the Red line (e.g., point *c*), their rejection of the Black line in favor of the Blue line would imply a **preference for the price distortion** (coupon) over pure income increase.  
   - This mirrors the *"weak WARP violation"* framework from the prior context, where affordability without selection signals preference structure.

---

### Cross-Referenced Continuity
- The Blue line’s slope here operationalizes the **"reduced trade-off rigidity"** mentioned in the prior text, demonstrating how price interventions (vs. cash) can better align with consumer preferences when goods have specific characterizations (e.g., food as normal).
- Part (d)’s request to draw indifference curves for a non-normal good directly extends the **Falklands threshold analysis**: if food were inferior, the *same* budget lines could lead to rejection of the coupon, flipping the welfare conclusion. This reinforces the **critical role of preference structure** in policy design—consistent with the McCawber problem’s goal to apply geometric tools to welfare analysis.

---
### Page/Slide 12



# 图表解析：预算约束与食品补贴效应

## 1. 图片中的文字与数据提取

### 图表标签
- Y轴: "Other things" (刻度0-180)
- X轴: "Food" (刻度0-240)
- 预算线:
  - Black budget line (黑色预算线)
  - Red budget line (红色预算线)
  - Blue budget line (蓝色预算线)
- 标记点: a, b, c

### 文本内容
**页眉**: 92 REVEALED PREFERENCE (Ch. 7)

**正文段落**:
> 7.10 (0) In 1933, the Swedish economist Gunnar Myrdal (who later won a Nobel prize in economics) and a group of his associates at Stockholm University collected a fantastically detailed historical series of prices and price indexes in Sweden from 1830 until 1930. This was published in a book called *The Cost of Living in Sweden*. In this book you can find 100 years of prices for goods such as oat groats, hard rye bread, salted codfish, beef, reindeer meat, birchwood, tallow candles, eggs, sugar, and coffee. There are also estimates of the quantities of each good consumed by an average working-class family in 1850 and again in 1890.
>
> The table below gives prices in 1830, 1850, 1890, and 1913, for flour, meat, milk, and potatoes. In this time period, these four staple foods accounted for about 2/3 of the Swedish food budget.

**表格**:
| | 1830 | 1850 | 1890 | 1913 |
|---|---|---|---|---|
| Grain Flour | .14 | .14 | .16 | .19 |
| Meat | .28 | .34 | .66 | .85 |
| Milk | .07 | .08 | .10 | .13 |
| Potatoes | .032 | .044 | .051 | .064 |

*注：价格单位为瑞典克朗/千克，牛奶为瑞典克朗/升*

## 2. 图表分析与上文知识点关联

### 预算线对比关系
- **红色预算线**：代表初始消费约束条件，作为基准参照。点c大约位于(90,60)位置，代表原文所说的"original consumption bundle"（原始消费束）。

- **黑色预算线**：代表"lump-sum grant"（一次性现金补助）情境，斜率与红色线平行，表明相对价格不变。上文已指出，这种情境下消费束扩张是纯收入效应。

- **蓝色预算线**：代表"coupon"（食品券/补贴）政策，其斜率更平缓，意味着食品的**相对价格降低**（上文所说的"effective price of food due to the coupon"）。

### 关键点解析
- **点a**：位于蓝色与黑色预算线交点，验证了上文核心观点："对于任何固定水平的'Other things'支出，蓝色线允许比黑色线更多的食品消费"。当"Other things"支出为90单位时，蓝色线对应的食品消费量约100单位，而黑色线仅约85单位。

- **预算集扩张差异**：蓝色预算线（食品补贴）在食品方向上的扩张幅度**比例性大于**黑色预算线（现金补助），这正是上文"proportionally more in the Food direction"的直观体现。

### 政策含义延伸
- 蓝色线的斜率变化操作化了原文所说的"reduced trade-off rigidity"——食品补贴政策使消费者面临更灵活的替代关系，而非简单的消费能力提升。

- 若食品作为**正常品**，家庭会将预算集扩张主要导向食品消费，这解释了为何补贴政策下蓝色预算线会更受偏好。这进一步支持上文关于"the McCawbers' choice would reject the lump-sum for the subsidy"的观察。

- 如上文指出，满足WARP（显示性偏好弱公理）要求：如果家庭在红色预算线上选择点c，当有蓝色预算线可行时仍选择蓝色线上的消费点，则表明消费者**明确偏好**价格扭曲政策（补贴）而非等值现金。

---

## 3. 福利分析框架补充

此图表将历史价格数据(如Myrdal收集的瑞典1830-1930年价格)转化为理论模型的可视化表达，实现了上文所述：
- 通过预算线的几何关系，将"2/3 of food budget"的实证数据演化为理论上的食品作为**关键商品**的分析框架
- 提供了验证"food as normal good"的实验设置：若食品为劣等品，将导致蓝色预算线上的最优选择点向左移动，与图示情况相反
- 为后续"draw indifference curves for non-normal good"的要求埋下伏笔——此图仅展示了正常品情境

图表与上文的"New offer welfare improvement logic"形成闭环：价格干预政策通过改变相对价格结构，可比单纯增加收入更有效地满足特定消费偏好，这正是政策设计中需考量的关键因素。

---
### Page/Slide 13



### 1. 当前图片文字与公式提取

#### 文字内容
- approximations and simplifications to draw these simple tables from the much more detailed information in the original study.)
- Quantities Consumed by a Typical Swedish Family  
  Quantities are measured in kilograms per year, except for milk, which is measured in liters per year.
- (a) Complete the table below, which reports the annual cost of the 1850 and 1890 bundles of staple foods at various years’ prices.  
  Cost of 1850 and 1890 Bundles at Various Years’ Prices
- (b) Is the 1890 bundle revealed preferred to the 1850 bundle? **Yes**.
- (c) The Laspeyres quantity index for 1890 with base year 1850 is the ratio of the value of the 1890 bundle at 1850 prices to the value of the 1850 bundle at 1850 prices. Calculate the Laspeyres quantity index of staple food consumption for 1890 with base year 1850. **1.39**.
- (d) The Paasche quantity index for 1890 with base year 1850 is the ratio of the value of the 1890 bundle at 1890 prices to the value of the 1850 bundle at 1890 prices. Calculate the Paasche quantity index for 1890 with base year 1850. **1.44**.
- (e) The Laspeyres price index for 1890 with base year 1850 is calculated using 1850 quantities for weights. Calculate the Laspeyres price index for 1890 with base year 1850 for this group of four staple foods. **1.29**.

#### 表格数据
| 四类主食          | 1850 | 1890 |  
|-------------------|------|------|  
| Grain Flour       | 165  | 220  |  
| Meat              | 22   | 42   |  
| Milk              | 120  | 180  |  
| Potatoes          | 200  | 200  |  

| Cost                   | 1850 bundle | 1890 bundle |  
|------------------------|-------------|-------------|  
| Cost at 1830 Prices    | 44.1        | 61.6        |  
| Cost at 1850 Prices    | 49.0        | 68.3        |  
| Cost at 1890 Prices    | 63.1        | 91.1        |  
| Cost at 1913 Prices    | 78.5        | 113.7       |  

#### 公式
- **Laspeyres quantity index** (c):  
  \[
  L_q = \frac{\text{Cost of 1890 bundle at 1850 prices}}{\text{Cost of 1850 bundle at 1850 prices}} = \frac{68.3}{49.0} = 1.39
  \]
  
- **Paasche quantity index** (d):  
  \[
  P_q = \frac{\text{Cost of 1890 bundle at 1890 prices}}{\text{Cost of 1850 bundle at 1890 prices}} = \frac{91.1}{63.1} = 1.44
  \]
  
- **Laspeyres price index** (e):  
  \[
  L_p = \frac{\text{Cost of 1850 bundle at 1890 prices}}{\text{Cost of 1850 bundle at 1850 prices}} = \frac{63.1}{49.0} = 1.29
  \]

---

### 2. 表格分析与上文知识点关联

#### 消费量表：1850与1890年消费变化
- **含义关联上文**：  
  上文指出“四类主食占瑞典食品预算的2/3”，此表量化了实际消费量（单位：kg/年或L/年）。1850–1890年间，Grain Flour（+33%）、Meat（+91%）、Milk（+50%）消费量上升，而Potatoes持平。结合上文价格数据（Meat价格从1850年0.34增至1890年0.66，+94%），消费量增长主要来自收入效应——上文强调“食品作为正常品”，收入提升推动更高质量食品消费（如肉类），Potatoes作为基础食品则无增长，符合主食消费结构转型。

- **关键连续性**：  
  上文通过预算线模型解释政策对消费的影响（如补贴增加食品购买），而此表实证验证了长期收入增长如何改变消费束：1890年bundle包含更多肉类/乳制品，反映上文所述“2/3预算”内消费升级。

#### 成本表：跨年价格下的消费成本
- **数据生成机制**：  
  此表直接使用上文提供的1830–1913年价格数据（如Grain Flour 1850年价0.14克朗/kg），乘以本表消费量计算成本。例如：
  - 1850 bundle在1850年成本 = (165×0.14) + (22×0.34) + (120×0.08) + (200×0.044) = 49.0  
  （与上文价格表单位“克朗/千克”一致）

- **含义关联上文**：  
  - **成本趋势**：1850 bundle成本从1850年49.0增至1890年63.1，增幅29%（见下文Lp=1.29），直接体现实质价格上升。这与上文历史分析闭环：价格数据转化理论模型中的“相对价格变化”，为预算线位移提供微观基础。  
  - **福利测度**：成本差异量化了上文“福利分析框架”——例如，1890 bundle在1850年价格下成本68.3 > 49.0，说明1890年消费需更高名义收入，但上文提及若食品为正常品，收入增加将主导需求（消费量提升），此表实证支持该理论。

#### 问题解答与揭示偏好检验
- **(b) 显示偏好判定**：  
  “1890 bundle被显示偏好于1850 bundle”的结论成立，因1890年价格下1850 bundle成本仅63.1（可负担），但家庭选择1890 bundle（成本91.1）。**上文延续性**：严格符合WARP（显示性偏好弱公理）——上文预算线图表中“若消费者在红色线选点c，当蓝色线可行时仍选新点，则偏好价格扭曲政策”，此处1850年选择旧bundle，但1890年转向新bundle，印证消费选择随约束变化，为上文政策建议（如补贴影响偏好）提供历史依据。

- **(c)(d)(e) 指数计算的经济意义**：  
  | 指数类型           | 值   | 含义关联上文                                                                 |
  |--------------------|------|-----------------------------------------------------------------------------|
  | Laspeyres quantity | 1.39 | 以1850价格为权重，1890年消费量增长39% → **确认食品为正常品**（消费量上升），支撑上文“收入效应主导消费扩张”的结论。 |
  | Paasche quantity   | 1.44 | 以1890价格为权重，增长44% > Laspeyres → 暗示价格上升抑制消费，**验证预算约束的刚性**，上文“蓝色预算线扩张比例更大”的理论在此实证。 |
  | Laspeyres price    | 1.29 | 以1850消费量为权重，价格上升29% → **量化成本推动**，关联上文“价格干预改变相对价格结构”，为福利分析提供通胀校正基准。 |

- **整体连续性**：  
  这些指数将上文理论中的“消费束”和“预算集”操作化：Laspeyres/Paasche差异反映价格扭曲对福利测度的影响，直接呼应上文“New offer welfare improvement logic”——政策设计需区分价格效应与收入效应（如补贴 vs 现金）。历史成本数据使“2/3预算”从定性描述转为定量分析，强化了**微观基础**：消费量增长与价格变动共同构成市场均衡变化。

---
### Page/Slide 14



### 文字与公式提取（当前图片内容）

- **(f)** If a Swede were rich enough in 1850 to afford the 1890 bundle of staple foods in 1850, he would have to spend **$1.39$** times as much on these foods as does the typical Swedish worker of 1850.  
- **(g)** If a Swede in 1890 decided to purchase the same bundle of food staples that was consumed by typical 1850 workers, he would spend the fraction **$.69$** of the amount that the typical Swedish worker of 1890 spends on these goods.  

- **7.11 (0)**  
  - **(a)** Cost for an American to buy 1850 Swedish staple bundle at current U.S. prices: **$\$408$**.  
  - **(b)** Cost for an American to consume the 1850 Swedish overall bundle (including non-staple goods): **$\$919$**.  
  - **(c)** Laspeyres price index (U.S. current vs. 1850 Sweden): **$8.35$**.  
    Implied value: current U.S. dollar worth **$.12$** of 1850 Swedish kronor.  

- **7.12 (0)** Suppose prices doubled and income tripled between 1960 and 1985.  

---

### 含义解析（结合上文知识点连续性）

当前内容是**上文历史消费数据分析的跨国延伸**，将瑞典1850–1890年的微观模型（预算约束、显示偏好、Laspeyres指数）应用于国际购买力比较。重点延续了三方面核心逻辑：  

#### 1. **消费 bundle 成本与显示偏好的跨时空验证**  
   - (f) 和 (g) **直接呼应上文成本表与显示偏好判定**：  
     - 上文通过成本表验证了1890 bundle 被显示偏好于1850 bundle（WARP成立），(f) 中 `1.39` 即上文 **Laspeyres quantity index (Lq = 1.39)** 的数值体现。这实证了：若强行将1890 bundle 移植至1850年，需 **39%更高的名义支出**，印证 **收入效应主导消费升级**（肉类/乳制品消费量增长91%与50%）。  
     - (g) 中 `$.69$` 是 **Paasche-like 预算比例** 的简化表达（上文Paasche quantity index = 1.44，但此处聚焦成本占比）。1890年消费1850 bundle仅需0.69倍支出，说明 **1890年实际消费束因价格上升存在福利损失**，呼应上文"预算约束刚性抑制消费"的结论（Paasche指数 > Laspeyres指数 = 1.44 > 1.39）。  

#### 2. **Laspeyres价格指数的跨国操作化与福利测度强化**  
   - 7.11(a)-(c) 将 **上文Lp = 1.29的本地通胀测度逻辑扩展至国际维度**：  
     - **权重延续性**：使用1850瑞典消费 bundle（上文已量化：165kg Grain Flour等）作为Laspeyres指数固定权重，维持了 **上文"历史消费结构反映购买力"的方法论**。  
     - **指数经济含义**：  
       | 项目 | 计算逻辑 | 上文关联 |  
       |------|----------|----------|  
       | Lp = 8.35 | $\frac{\sum (\text{US current prices} \times \text{1850 Swedish quantities})}{\sum (\text{1850 Sweden prices} \times \text{1850 Swedish quantities})}$ | 复用上文Lp公式，将横坐标从"时间维度"扩展至"国别维度" |  
       | $.12$ 比值 | $1 / 8.35$，表示美元购买力 | 量化 **福利变迁跨时空对比**，支撑上文"真实收入应扣除价格扭曲"的福利框架（如7.11(b)中 \$919 基于2/3食品预算比例，直接延续上文"四类主食占食品预算2/3"的实证基础） |  
     - **货币政策启示**：上文强调通胀校正需区分价格效应与收入效应（如补贴vs现金），此处指数揭示 **美国当前价格对1850瑞典克朗的实质性稀释**（1美元仅值0.12克朗），表明跨期购买力平价必须纳入历史消费结构权重。  

#### 3. **国际比较对上文理论边界的拓展**  
   - 7.11(b) 中 **\$919 的整体成本计算** 延续了上文"2/3预算"的定量分析：  
     - 基于上文"四类主食占食品预算2/3" → 1850瑞典食品总预算推导出非主食部分比例，再假设美国相对价格结构相似，**实证验证了上文"消费升级依赖收入增长"的普适性**（美国当前价格下维持1850消费水平需更高名义收入）。  
   - 7.12 隐含 **预算线动态的极端案例**：  
     - 价格×2 + 收入×3 → 实际收入增长50%，但消费束变化取决于商品类型（正常品/劣等品）。**直接衔接上文福利分析逻辑**：若商品为正常品（如肉类），收入效应将主导需求扩张，重申政策需识别商品属性（参考上文补贴对预算线的影响机制）。  

> **知识连续性核心**：本页内容将上文**瑞典历史数据的操作化方法**转化为**跨国购买力分析工具**，证明显示偏好理论与指数测度不仅适用国内时间序列，亦可解构跨千年国际福利变迁。这强化了微观模型的普适性——**任何跨时空消费比较必须锚定历史消费结构权重**，避免上文警示的"名义价值失真问题"。

---
### Page/Slide 15



### 提取当前图片中的所有文字与公式

#### 文字内容
- **(a)** Would the Laspeyres price index for 1985, with base year 1960 be less than 2, greater than 2, or exactly equal to 2? Exactly 2. What about the Paasche price index? Exactly 2.  
- **(b)** If bananas are a normal good, will total banana consumption increase? Yes. If everybody has homothetic preferences, can you determine by what percentage total banana consumption must have increased? Explain. Yes, by 50%. Everybody’s budget line shifted out by 50%. With homothetic preferences, the consumption of each good increases in the same proportion.  
- **7.13 (1)** Norm and Sheila consume only meat pies and beer. Meat pies used to cost $2 each and beer was $1 per can. Their gross income used to be $60 per week, but they had to pay an income tax of $10. Use red ink to sketch their old budget line for meat pies and beer.  
- **图表标签**:  
  - x-axis: Pies (0–60)  
  - y-axis: Beer (0–60)  
  - Lines: Black budget line, Red budget line, Blue budget line (with directional arrows)  

#### 隐含公式  
- 预算线变动比例：\(\frac{I_{1985}/p_{1985}}{I_{1960}/p_{1960}} - 1 = \frac{3}{2} - 1 = 50\%\)（基于7.12价格翻倍、收入增三倍）  
- 同质偏好下消费变动：\(\% \Delta Q = 50\%\)（消费量同比例增长）  
- 7.13(1)预算约束：\(2P + B = 50\)（\(P\) = pies, \(B\) = beer, 净收入 $50）  

---

### 图表解析（结合上文知识连续性）  
当前图表为 **7.13(1)的预算约束可视化**，延续上文 **预算线动态分析框架**（尤其是7.12价格翻倍与收入变化的极端案例），但聚焦具体商品维度。  

#### 核心变化含义  
1. **预算线移动的实证锚点**  
   - 红线对应 **旧预算线**（含税后净收入）：  
     \[
     2P + B = 50 \implies \text{Beer intercept} = 50, \text{ Pies intercept} = 25
     \]
     直接呼应上文 **"预算约束刚性"逻辑**：税收（$10）将名义收入从 $60 削减至 $50，导致预算线内移。这印证了上文警示的 **"名义价值失真问题"**——若忽略税收等外生冲击，会高估实际购买力（如上文7.11中跨国比较需校正价格扭曲）。  
   - 黑/蓝线暗示潜在场景（虽未指定，但基于上文）：  
     - 若黑线代表 **税前状态**（\(2P + B = 60\)），则税收造成 **10/60 ≈ 16.7% 的实际收入损失**，强化了上文"政策需识别收入属性"（补贴vs现金）的结论——税收直接侵蚀购买力，而价格变动（如上文7.12）需区分实际收入效应。  
     - 蓝线可能模拟 **价格变化**（如肉饼涨价），但图表未显式标注；其位置变化（更陡峭或外移）可外推上文 **"显示偏好判定"方法论**：若消费束落在不同预算线，可验证WARP成立性（如上文1850 vs 1890 bundle比较）。  

2. **衔接7.12的预算动态扩展**  
   - 7.12中 **"预算线外移50%"**（价格×2 + 收入×3 → 实际收入+50%）在图表中具象化：  
     - 若假设红→蓝线为收入增长50%，则同质偏好下消费点将沿射线移动（如 pies 和 beer 同比增50%），直接支持(b)中 **"消费比例不变"** 的结论。  
     - 这标志着 **微观福利分析的连续性**：上文跨国/跨时比较（如瑞典1850–1890模型）可降维至个体预算线，证明任何消费变动（包括国际通胀或税收）必须通过 **真实购买力变动** 解释（而非名义值）。  
   - **为何Paasche指数=2的具象化**：若价格同比例变动（如图表中两商品价格同涨），预算线平行移动，此时即使消费量变化（如7.13中因收入增而右移），Paasche指数仍等于价格变动率——强化了上文"指数测度需跨时空锚定消费结构"的核心法则。  

> **知识连续性焦点**：本图表将上文 **历史/跨国购买力模型** 压缩至微观个体场景，验证"预算线变动效应"的普适性。红线与黑线的差距量化了 **政策冲击（税收）对实际消费的妥协**，而7.12逻辑下外移50%的消费路径（如b部分）则表明：  
> - 若偏好同质，福利分析可简化为 **实际收入比例变动**（避免上文警示的"名义值陷阱"）；  
> - 若偏好非同质（如正常品vs劣等品），需进一步检验显示偏好（呼应上文(f)(g)对跨期福利损失的测度）。  
> 此设计重申：**任何消费比较必须解耦价格效应与收入效应**，本质是上文"真实收入校正框架"的操作化延伸。

---
### Page/Slide 16



### 当前图片内容提取与解析

#### 1. 当前图片文字与公式提取  
**文字内容：**  
- 页码: 96  
- 章节: REVEALED PREFERENCE (Ch. 7)  
- (a) They used to buy 30 cans of beer per week and spent the rest of their income on meat pies. How many meat pies did they buy? **10**.  
- (b) The government decided to eliminate the income tax and to put a sales tax of $1 per can on beer, raising its price to $2 per can. Assuming that Norm and Sheila’s pre-tax income and the price of meat pies did not change, draw their new budget line in blue ink.  
- (c) The sales tax on beer induced Norm and Sheila to reduce their beer consumption to 20 cans per week. What happened to their consumption of meat pies? **Stayed the same--10**. How much revenue did this tax raise from Norm and Sheila? **$20**.  
- (d) This part of the problem will require some careful thinking. Suppose that instead of just taxing beer, the government decided to tax both beer and meat pies at the same percentage rate, and suppose that the price of beer and the price of meat pies each went up by the full amount of the tax. The new tax rate for both goods was set high enough to raise exactly the same amount of money from Norm and Sheila as the tax on beer used to raise. This new tax collects **$ .50** for every bottle of beer sold and **$ 1** for every meat pie sold. (Hint: If both goods are taxed at the same rate, the effect is the same as an income tax.) How large an income tax would it take to raise the same revenue as the $1 tax on beer? **$20**. Now you can figure out how big a tax on each good is equivalent to an income tax of the amount you just found.  
- (e) Use black ink to draw the budget line for Norm and Sheila that corresponds to the tax in the last section. Are Norm and Sheila better off having just beer taxed or having both beer and meat pies taxed if both sets of taxes raise the same revenue? **Both**. (Hint: Try to use the principle of revealed preference.)  

**隐含公式：**  
- 旧预算约束（含收入税，对应红预算线）: \(2P + B = 50\)  
  - 由(a)：消费点 \((P, B) = (10, 30)\)，验证 \(2 \times 10 + 30 = 50\)  
- 新预算约束（啤酒销售税，对应蓝预算线）: \(2P + 2B = 60\) 或简化 \(P + B = 30\)  
  - 由(b)和(c)：消费点 \((P, B) = (10, 20)\)，验证 \(2 \times 10 + 2 \times 20 = 60\)  
- 比例税率预算约束（对应黑预算线）: \(2P + B = 40\)  
  - 由(d)和(e)：比例税率等效于收入税 \(\$20\)，税前收入 \(\$60\)，净收入 \(\$40\)；消费点 \((P, B) = (10, 20)\) 满足 \(2 \times 10 + 20 = 40\)  
- 税收收入计算:  
  - 啤酒销售税: \(\$20 = 20 \text{ cans} \times \$1/\text{can}\)  
  - 比例税率等效: \(\$20\) 总收入税（无扭曲效应）  

---

#### 2. 图表变化含义解析（结合上文连续性）  
当前问题文本对应【上文知识点总结】中的预算线动态分析框架，深化了 **税收类型对预算线形态及消费选择的差异化影响**。图表虽未显式提供，但基于上文描述（x-axis: Pies, 0–60; y-axis: Beer, 0–60; 红/蓝/黑线），可解码变化的深层含义：  

##### **核心变化锚点**  
- **红预算线（旧状态）**：延续上文7.13(1)的 \(2P + B = 50\)，代表收入税（\(\$10\)）侵蚀购买力。上文强调其为 **实际收入校正基准**（名义收入 \(\$60\) → 净收入 \(\$50\)），此处直接支撑(a)中消费点 \((10, 30)\)，印证税收导致预算线内移（Pies截距25 → Beer截距50）。  
- **蓝预算线（特定商品税）**：由(b)构建，\(2P + 2B = 60\)，斜率从 \(-2\)（红）变为 \(-1\)，反映 **价格扭曲效应**：  
  - 啤酒价格因销售税跳升50% → 相对价格失衡（\(p_p/p_b\) 从 2:1 变 1:1）。  
  - 消费点 \((10, 20)\) 位于蓝线上，且处于红线下方（\(40 < 50\)），验证上文 **“税收类型决定收入效应与替代效应耦合”**——此处收入效应中性（税前收入不变），但啤酒消费锐减10罐仅由替代效应驱动（无PIEES效应）。  
- **黑预算线（比例税率）**：由(e)定义，\(2P + B = 40\)，与红预算线平行但截距更低（Pies 20 vs 25），是上文 **“等效收入税”理念的操作化**：  
  - 比例税率 \(\tau = 50\%\)（啤酒税 \(\$0.50\)/单位，肉饼税 \(\$1\)/单位）等效总收入税 \(\$20\)，故预算线仅内移5%（截距 vs 红线），无价格扭曲。  
  - 消费点 \((10, 20)\) 仍可负担（\(40 = 40\)），呼应上文 **“同质偏好下福利损失最小化”**：比例税避免相对价格失真，使消费集与扭曲税等效时消费点重合。  

##### **关键动态延伸**  
- **WARP验证与福利比较**：上文通过1850–1890案例强调 **“消费束跨预算线不可比性”**，此处由(e)直接检验：  
  - 同一消费束 \((10, 20)\) 同时可负担于蓝线（扭曲税）和黑线（比例税），故依显示偏好原理（WARP），消费者无差异——印证上文 **“名义价格变动需解耦于真实福利”**。若偏好非同质，消费束会发散（如肉饼变为劣等品），但本例中同质偏好确保 **“比例税福利等价性”**（税收等效 = 实际收入同比例下降）。  
- **政策冲击量级校准**：  
  - 消费点从 \((10, 30)\) → \((10, 20)\) 在啤酒减量中 **PIE不变**，上方文7.12的“实际收入变动比例”公式：\(\% \Delta \text{真实收入} = \frac{I_{\text{post-tax}} / p_{\text{base}}}{I_{\text{pre-tax}} / p_{\text{base}}} - 1\)。  
  - 此处，扭曲税实际收入等效降至 \(\$40\)（vs 比例税），但消费未跳变，凸显上文警示的 **“名义税收收入≠真实负担”**——\(\$20\) 收入税与 \(\$20\) 销售税对实际购买力影响不同。  
- **指数理论具象化**：Paasche指数逻辑在(d)中体现——比例税下消费结构稳定（\(\text{消费比例} P/B = 1/2\) 不变），故指数值精确追踪价格变动（同7.12），强化 **“跨时空福利测度需锚定消费束不变”** 原则。  

> **连续性落脚点**：本问题通过三线嵌套，将上文 **“历史价格校正框架”** 压缩至微观税收场景：  
> - 红→蓝线变动暴露 **特定商品税的效率损失**（替代效应主导，消费点向PIE侧移动），  
> - 蓝→黑线重合则重申 **比例税≈收入税的核心结论**（预算线平行移动时，WARP可直接比对福利）。  
> 这进一步佐证上文警告——**** 任何政策评估必须分离价格效应（由斜率变化衡量）与收入效应（由截距变化衡量）**，否则会误判真实购买力**（如将销售税 \(\$20\) 等同于收入税 \(\$20\)）。
