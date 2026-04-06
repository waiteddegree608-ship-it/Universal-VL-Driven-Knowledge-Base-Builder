# PDF_Chapter_6

### Page/Slide 1



# 需求章节解析

## 1. 文字与公式提取

**章节标题**  
Chapter 6  
Demand  

**Introduction**  
In the previous chapter, you found the commodity bundle that a consumer with a given utility function would choose in a specific price-income situation. In this chapter, we take this idea a step further. We find *demand functions*, which tell us for *any* prices and income you might want to name, how much of each good a consumer would want. In general, the amount of each good demanded may depend not only on its own price, but also on the price of other goods and on income. Where there are two goods, we write demand functions for Goods 1 and 2 as $x_1(p_1, p_2, m)$ and $x_2(p_1, p_2, m)$.*  

When the consumer is choosing positive amounts of all commodities and indifference curves have no kinks, the consumer chooses a point of tangency between her budget line and the highest indifference curve that it touches.  

**Example**  
Consider a consumer with utility function $U(x_1, x_2) = (x_1 + 2)(x_2 + 10)$. To find $x_1(p_1, p_2, m)$ and $x_2(p_1, p_2, m)$, we need to find a commodity bundle $(x_1, x_2)$ on her budget line at which her indifference curve is tangent to her budget line. The budget line will be tangent to the indifference curve at $(x_1, x_2)$ if the price ratio equals the marginal rate of substitution. For this utility function, $MU_1(x_1, x_2) = x_2 + 10$ and $MU_2(x_1, x_2) = x_1 + 2$. Therefore the “tangency equation” is $p_1/p_2 = (x_2 + 10)/(x_1 + 2)$. Cross-multiplying the tangency equation, one finds $p_1x_1 + 2p_1 = p_2x_2 + 10p_2$.  

The bundle chosen must also satisfy the budget equation, $p_1x_1 + p_2x_2 = m$. This gives us two linear equations in the two unknowns, $x_1$ and $x_2$. You can solve these equations yourself, using high school algebra. You will find that the solution for the two “demand functions” is  
$$
x_1 = \frac{m - 2p_1 + 10p_2}{2p_1}
$$
$$
x_2 = \frac{m + 2p_1 - 10p_2}{2p_2}
$$

There is one thing left to worry about with the “demand functions” we just found. Notice that these expressions will be positive only if $m - 2p_1 + 10p_2 > 0$ and $m + 2p_1 - 10p_2 > 0$. If either of these expressions is negative, then it doesn’t make sense as a demand function. What happens in this  

**Footnote**  
* For some utility functions, demand for a good may not be affected by all of these variables. For example, with Cobb-Douglas utility, demand for a good depends on the good’s own price and on income but not on the other good’s price. Still, there is no harm in writing demand for Good 1 as a function of $p_1$, $p_2$, and $m$. It just happens that the derivative of $x_1(p_1, p_2, m)$ with respect to $p_2$ is zero.  

---

## 2. 核心推导逻辑（无图表，聚焦公式经济含义）

本章延续上文**效用最大化的一阶条件**（MRS = 价格比），通过具体效用函数展示如何将理论转化为一般需求函数。关键逻辑如下：  

1. **切点条件的数学化**  
   - 由 $MU_1/MU_2 = p_1/p_2$ 推导出 $p_1/p_2 = (x_2 + 10)/(x_1 + 2)$，揭示**相对价格直接制约消费者替代行为**。  
   - 交叉相乘后 $p_1x_1 + 2p_1 = p_2x_2 + 10p_2$ 将边际替代率显式关联至预算约束的结构参数（截距项 2 和 10 源自效用函数平移）。

2. **需求函数的交叉依赖性**  
   - $x_1 = \frac{m - 2p_1 + 10p_2}{2p_1}$ 中 $+10p_2$ 项表明：**商品 2 价格 $p_2$ 上升会增加商品 1 需求**（间接替代效应），体现二元需求函数对交叉价格的依赖——与上文“需求可能受其他商品价格影响”的论断直接呼应。  
   - 分母 $2p_1$ 说明 $x_1$ 对自身价格 $p_1$ 呈非线性递减（价格翻倍时需求减幅>50%）。

3. **经济合理性约束**  
   - $m - 2p_1 + 10p_2 > 0$ 和 $m + 2p_1 - 10p_2 > 0$ 是**需求有效的必要条件**。若不成立，消费者将调整至边界解（如 $x_1=0$），说明需求函数隐含**内点解的前提假设**——这与上文“正消费量且无凹角无差异曲线”条件形成逻辑闭环。

4. **需求函数的普适性表述**  
   - 脚注强调：即使Cobb-Douglas型效用函数中 $\partial x_1/\partial p_2 = 0$，仍统一写作 $x_1(p_1,p_2,m)$。这体现**本章方法论核心**：将需求函数构建为包含所有潜在变量的数学对象，后续可通过具体效用函数筛选无关变量（而非预先限定函数形式）。

---
### Page/Slide 2



### 提取内容  
**文字：**  
- 当消费者选择“边界解”（boundary solution）时，她只消费一种商品，此时无差异曲线与预算线不相切。  
- 当无差异曲线存在折点（kinks）时，可通过图形和代数求解需求函数：通常无需切点方程，而是利用“折点位置”方程与预算方程联立求解。  
- 关注凹点无差异曲线等“特殊案例”的原因：计算简单，但需图形思考以培养分析习惯（而非死记公式）。  
- 本章学习目标：  
  - 求Cobb-Douglas等效用函数的需求函数  
  - 求拟线性效用函数的需求函数  
  - 求凹点/直线无差异曲线的需求函数  
  - 从需求曲线识别互补/替代品  
  - 从需求数据区分正常品、劣等品、奢侈品、必需品  
  - 给定简单需求方程，计算反需求曲线方程  
- 例6.1(C) Charlie的效用函数为 $ U(x_A, x_B) = x_A x_B $，需求函数为 $ x_A(p_A, p_B, m) $ 和 $ x_B(p_A, p_B, m) $。  

**公式：**  
- 预算线方程： $ p_A x_A + p_B x_B = m $  
- 无差异曲线斜率： $ -\frac{MU_1(x_A, x_B)}{MU_2(x_A, x_B)} = -\frac{x_B}{x_A} $  
- 预算线斜率： $ -\frac{p_A}{p_B} $  
- 切点条件： $ \frac{p_A}{p_B} = \frac{x_B}{x_A} $  

---

### 解析（基于上文知识点）  
#### 1. **边界解的经济含义**  
上文指出需求函数有效性需满足 $ m - 2p_1 + 10p_2 > 0 $ 和 $ m + 2p_1 - 10p_2 > 0 $；**当前图片直接衔接此条件**，说明当不等式不成立时消费者选择边界解（仅消费单一商品）。这验证了上文“需求函数隐含内点解假设”的结论——边界解是经济合理性约束失效时的替代方案，此时切点条件（MRS=价格比）不再适用，与上文逻辑闭环一致。  

#### 2. **凹点无差异曲线与需求求解逻辑**  
- 上文脚注提及需求函数可能包含无关变量（如Cobb-Douglas中 $ \partial x_1 / \partial p_2 = 0 $），但需统一表示为 $ x_1(p_1, p_2, m) $。  
- **当前图片深化此方法论**：当无差异曲线存在凹点时（如拟线性或完全互补效用函数），切点条件可能失效，需通过“折点位置方程”替代。例如，若效用函数含凹点，需求解由预算约束与折点方程联立决定（如 $ x_2 = kx_1 $），而非严格依赖 $ \text{MRS} = p_1/p_2 $。这呼应了上文“需求函数构建需包容各类效用形态”的核心思想。  

#### 3. **Charlie的Cobb-Douglas案例与上文推导的关联**  
- 图片中切点条件 $ \frac{p_A}{p_B} = \frac{x_B}{x_A} $ **直接对应上文一阶条件**（$ MU_1/MU_2 = p_1/p_2 $），其中 $ MU_A = x_B $, $ MU_B = x_A $ 由效用函数 $ U = x_A x_B $ 推导得出。  
- **关键衔接**：结合预算方程 $ p_A x_A + p_B x_B = m $，可解出：  
  $$
  x_A = \frac{m}{2p_A}, \quad x_B = \frac{m}{2p_B}
  $$  
  此结果验证上文脚注：**Cobb-Douglas需求函数对交叉价格不敏感**（$ \partial x_A / \partial p_B = 0 $），与上文展示的 $ +10p_2 $ 交叉依赖项形成对比，凸显效用函数形态对需求结构的决定性作用。  
- **经济含义**：此处 $ x_A $ 与 $ p_B $ 无关，反映商品间无替代效应（满足上文“需求可能不受其他商品价格影响”）；而上文示例中 $ +10p_2 $ 项的存在，说明商品间替代效应显著，二者共同印证“需求函数需以通用形式 $ x_1(p_1,p_2,m) $ 表述”的必要性。  

#### 4. **学习目标对上文方法论的延伸**  
- “识别互补/替代品”和“分析商品类型”能力要求，**直接依赖上文需求函数推导逻辑**：  
  - 替代品的判定基于 $ \partial x_1 / \partial p_2 > 0 $（如上文 $ x_1 $ 中 $ +10p_2 $ 项）；  
  - 劣等品判定需分析 $ \partial x_1 / \partial m < 0 $，这要求需求函数显式包含收入 $ m $（如上文 $ x_1 = \frac{m - 2p_1 + 10p_2}{2p_1} $）。  
- 强调“图形思考”呼应上文切点条件的几何解释（MRS=价格比），补充了公式推导的直观维度，强化“避免死记公式”的连贯训练目标。

---
### Page/Slide 3



# 当前图片解析

## 1. 提取文字与公式

**文字内容：**

- (b) You now have two equations, the budget equation and the tangency equation, that must be satisfied by the bundle demanded. Solve these two equations for $ x_A $ and $ x_B $. Charlie’s demand function for apples is $ x_A(p_A, p_B, m) = \frac{m}{2p_A} $, and his demand function for bananas is $ x_B(p_A, p_B, m) = \frac{m}{2p_B} $.

- (c) In general, the demand for both commodities will depend on the price of both commodities and on income. But for Charlie’s utility function, the demand function for apples depends only on income and the price of apples. Similarly, the demand for bananas depends only on income and the price of bananas. Charlie always spends the same fraction of his income on bananas. What fraction is this? $ 1/2 $.

- 6.2 (0) Douglas Cornfield’s preferences are represented by the utility function $ u(x_1, x_2) = x_1^2 x_2^3 $. The prices of $ x_1 $ and $ x_2 $ are $ p_1 $ and $ p_2 $.

  - (a) The slope of Cornfield’s indifference curve at the point $ (x_1, x_2) $ is $ -2x_2 / 3x_1 $.

  - (b) If Cornfield’s budget line is tangent to his indifference curve at $ (x_1, x_2) $, then $ \frac{p_1 x_1}{p_2 x_2} = 2/3 $. (Hint: Look at the equation that equates the slope of his indifference curve with the slope of his budget line.) When he is consuming the best bundle he can afford, what fraction of his income does Douglas spend on $ x_1 $? $ 2/5 $.

  - (c) Other members of Doug’s family have similar utility functions, but the exponents may be different, or their utilities may be multiplied by a positive constant. If a family member has a utility function $ U(x, y) = c x_1^a x_2^b $ where $ a $, $ b $, and $ c $ are positive numbers, what fraction of his or her income will that family member spend on $ x_1 $? $ a/(a+b) $.

- 6.3 (0) Our thoughts return to Ambrose and his nuts and berries. Ambrose’s utility function is $ U(x_1, x_2) = 4\sqrt{x_1} + x_2 $, where $ x_1 $ is his consumption of nuts and $ x_2 $ is his consumption of berries.

  - (a) Let us find his demand function for nuts. The slope of Ambrose’s indifference curve at $ (x_1, x_2) $ is $ -2 / \sqrt{x_1} $. Setting this slope equal to the slope of the budget line, you can solve for $ x_1 $ without even using the budget equation. The solution is $ x_1 = \left( \frac{2p_2}{p_1} \right)^2 $.

**公式汇总：**

- $ x_A = \dfrac{m}{2p_A} $
- $ x_B = \dfrac{m}{2p_B} $
- 无差异曲线斜率（Douglas）： $ -\dfrac{2x_2}{3x_1} $
- 切点条件（Douglas）： $ \dfrac{p_1 x_1}{p_2 x_2} = \dfrac{2}{3} $
- 支出份额（Douglas）： $ \dfrac{2}{5} $
- 一般支出份额： $ \dfrac{a}{a+b} $
- 无差异曲线斜率（Ambrose）： $ -\dfrac{2}{\sqrt{x_1}} $
- 需求函数（Ambrose）： $ x_1 = \left( \dfrac{2p_2}{p_1} \right)^2 $

## 2. 解析（基于上文知识点）

### 2.1 Charlie需求函数的内点解验证  
图片(b)部分呈现的 $ x_A = \dfrac{m}{2p_A} $ 和 $ x_B = \dfrac{m}{2p_B} $ **直接量化上文切点条件推导结果**：  
- 由 $ \dfrac{p_A}{p_B} = \dfrac{x_B}{x_A} $ 与预算约束联立，解得严格内点解（无边界解约束条件，因 $ m > 0 $, $ p_A, p_B > 0 $）。  
- **支出份额本质**：$ p_A x_A = \dfrac{m}{2} $ 表明收入恒半用于苹果，**验证上文"Charlie always spends the same fraction"的抽象结论**，并解释为何交叉项 $ \dfrac{\partial x_A}{\partial p_B} = 0 $ ——Cobb-Douglas效用函数下需求仅由自身价格决定，呼应上文"需求函数需统一表示为 $ x_1(p_1,p_2,m) $，但实际可能无交叉依赖"的辩证方法论。

### 2.2 Cobb-Douglas需求函数的参数化推广  
图片6.2部分通过 $ u(x_1, x_2) = x_1^2 x_2^3 $ **系统化拓展上文Charlie案例**：  
- **斜率生成逻辑**：无差异曲线斜率 $ -\dfrac{2x_2}{3x_1} $ 由 $ \text{MRS} = -\dfrac{MU_1}{MU_2} = -\dfrac{2x_1 x_2^3}{3x_1^2 x_2^2} $ 推导，**强化上文"需掌握函数形式与斜率关联"的训练目标**。  
- **支出份额公式化**：切点条件 $ \dfrac{p_1 x_1}{p_2 x_2} = \dfrac{2}{3} $ 直接导出支出份额 $ \dfrac{p_1 x_1}{m} = \dfrac{2}{5} $，**验证上文一般结论**：对 $ u = x_1^a x_2^b $，需求函数必隐含 $ \dfrac{a}{a+b} $ 的支出比例（图片6.2(c)）。  
  - **学习目标落地**：支出比例与参数 $ a,b $ 的显性关联，**为"从需求数据区分必需品/奢侈品"提供操作依据**——必需品对应 $ \dfrac{a}{a+b} < 0.5 $ 的参数组合（因支出增长慢于收入）。

### 2.3 拟线性效用函数的边界解隐含逻辑  
图片6.3部分以 $ U = 4\sqrt{x_1} + x_2 $ **深化上文拟线性需求函数解析**：  
- **MRS的特殊性**：斜率 $ -\dfrac{2}{\sqrt{x_1}} $ 仅依赖 $ x_1 $，体现拟线性效用函数关键特征（MRS与 $ x_2 $ 无关）。此性质**使切点条件可独立于预算约束求解 $ x_1 $**，但上文强调的边界解风险仍存在——当 $ m < p_1 \left( \dfrac{2p_2}{p_1} \right)^2 $ 时，内点解失效，需切换至边界解（如 $ x_1=0 $），此条件未在图片显式给出却隐含于求解过程。  
- **经济含义延伸**：需求函数 $ x_1 = \left( \dfrac{2p_2}{p_1} \right)^2 $ **不含收入 $ m $**，印证上文"拟线性效用下部分商品需求可能与收入无关"的关键结论，而支出份额 $ \dfrac{p_1 x_1}{m} $ 会随收入变化——当 $ m $ 增大时，$ x_1 $ 固定而 $ x_2 $ 增加，契合"必需品"定义（上文学习目标要求）。  

---

**知识连续性说明**：本图片通过参数化Cobb-Douglas与拟线性案例，将上文抽象方法论转化为可复现的解题流程，特别是支出份额公式的推导，为后续"从需求数据区分商品类型"提供量化工具。图片中未显式验证的边界解条件（如 $ m < p_1 x_1 $ 时解的失效），恰呼应上文"需求函数隐含内点解假设"的核心警示。

---
### Page/Slide 4



### 3. 当前图片解析

#### 3.1 文字与公式提取
- **(b) 部分文字与公式**  
  `Let us find his demand for berries. Now we need the budget equation. In Part (a), you solved for the amount of $x_1$ that he will demand. The budget equation tells us that $p_1 x_1 + p_2 x_2 = M$. Plug the solution that you found for $x_1$ into the budget equation and solve for $x_2$ as a function of income and prices. The answer is $x_2 = \dfrac{M}{p_2} - 4 \dfrac{p_2}{p_1}$.`

- **(c) 部分文字与公式**  
  `When we visited Ambrose in Chapter 5, we looked at a "boundary solution," where Ambrose consumed only nuts and no berries. In that example, $p_1 = 1$, $p_2 = 2$, and $M = 9$. If you plug these numbers into the formulas we found in Parts (a) and (b), you find $x_1 = \underline{16}$, and $x_2 = \underline{-3.5}$. Since we get a negative solution for $x_2$, it must be that the budget line $x_1 + 2x_2 = 9$ is not tangent to an indifference curve when $x_2 \ge 0$. The best that Ambrose can do with this budget is to spend all of his income on nuts. Looking at the formulas, we see that at the prices $p_1 = 1$ and $p_2 = 2$, Ambrose will demand a positive amount of both goods if and only if $M > \underline{16}$.`

- **6.4 (0) 部分文字与公式**  
  - `Donald Fribble is a stamp collector... utility function $u(s,t) = s + \ln t$... $p_s$ is the price of stamps, $p_t$ is the price of Twinkies, income $m$.`  
  - **(a)** `$1/t = p_t / p_s$`  
  - **(b)** `Demand function for Twinkies: $t(p_s, p_t, m) = p_s / p_t$`  
  - **(c)** `Expenditure on Twinkies: $p_t t(p_s, p_t, m)$ depends only on $p_s$`  

---

#### 3.2 结合上文解析
##### 3.2.1 Ambrose 边界解的数值验证（对接 [上文] 2.3 节）
- **公式关联**：  
  - 图片中 $x_1 = \left( \dfrac{2p_2}{p_1} \right)^2$（隐含，由第 (c) 部分数值 $p_1=1, p_2=2$ 得 $x_1=16$）**直接验证上文需求函数（Ambrose）**。  
  - 边界条件 $M > 16$ 等价于 $M > p_1 \left( \dfrac{2p_2}{p_1} \right)^2$，**显式化上文隐含逻辑**：当 $m < p_1 x_1^*$ 时内点解失效（$x_2 <0$），需切换至边界解（仅消费 $x_1$）。  
- **经济含义深化**：  
  - 此处 $x_2 = -3.5$ 不可实现（$x_2 \ge 0$ 约束），**回应上文边界解限定条件**，解释为何拟线性效用需严格区分内点解与边界解。  
  - 支出份额 $p_1 x_1 / M$ 在 $M=9$ 时为 $1$（全部收入用于坚果），但当 $M > 16$ 时降至 $p_1 x_1 / M <1$ 且随 $M$ 递增，**强化上文"支出份额动态变化"结论**——拟线性下需求结构随收入非均匀调整。

##### 3.2.2 Fribble 案例：拟线性效用拓展（扩展 [上文] 2.3 节）
- **MRS 与切点条件**：  
  - $ \text{MRS} = -\dfrac{MU_t}{MU_s} = -\dfrac{1/t}{1} = -1/t $，**印证上文拟线性函数特性**：MRS 仅依赖 $x_1$（此处为 $t$），与 $s$ 无关。  
  - 切点条件 $1/t = p_t / p_s$ 推导出需求函数 $t = p_s / p_t$，**严丝合缝衔接上文需求函数（Ambrose）**，但形式更简洁（因 $\ln t$ 替代 $\sqrt{x_1}$）。  
- **支出属性与商品类型**：  
  - 支出项 $p_t t = p_s$ **不含收入 $m$**，**验证上文拟线性需求与收入无关的核心结论**。  
  - 支出份额 $\dfrac{p_s}{m}$ 随 $m$ 递增而递减，**具象化上文"必需品"定义**：收入增加时，Twinkies 支出占比下降，符合必需品 *需求收入弹性 $<1$* 的量化特征。  
  - 此特性**呼应知识连续性**：上文以 Ambrose 案例建立"支出份额动态关联商品类型"框架，本图通过 $p_t t = p_s$ 提供新案例，**强化"从需求数据区分必需品"的操作路径**。  

---

#### 3.3 知识连续性说明
- **边界解条件显式化**：Ambrose 例将上文" $m < p_1 \left( \dfrac{2p_2}{p_1} \right)^2 $ 时内点解失效"转化为精确阈值 $M>16$，**填补上文案例缺口**。  
- **拟线性普适性强化**：Fribble 案例证明 $u(s,t)=s+\ln t$ 与上文 $U=4\sqrt{x_1}+x_2$ 结构一致，**扩展"部分商品需求独立于收入"的适用边界**，为后续实证问题（如 6.4(c)）提供方法论锚点。  
- **支出份额逻辑闭环**：$p_t t = p_s$ 直接导出支出份额 $p_s/m$，**无缝衔接上文"支出份额随收入变化"分析**，奠定需求数据区分商品类型的量化基础。

---
### Page/Slide 5



### 当前图片解析

#### 1. 文字与公式提取
```text
(d) Since there are only two goods, any money that is not spent on Twinkies must be spent on stamps. Use the budget equation and Donald’s demand function for Twinkies to find an expression for the number of stamps he will buy if his income is m, the price of stamps is p_s and the price of Twinkies is p_t.  
$s = \dfrac{m}{p_s} - 1$.

(e) The expression you just wrote down is negative if $m < p_s$. Surely it makes no sense for him to be demanding negative amounts of postage stamps. If $m < p_s$, what would Fribble’s demand for postage stamps be?  
$s = 0$  
What would his demand for Twinkies be? $t = \dfrac{m}{p_t}$.  
(Hint: Recall the discussion of boundary optimum.)

(f) Donald’s wife complains that whenever Donald gets an extra dollar, he always spends it all on stamps. Is she right? (Assume that $m > p_s$.)  
Yes.

(g) Suppose that the price of Twinkies is $2 and the price of stamps is $1. On the graph below, draw Fribble’s Engel curve for Twinkies in red ink and his Engel curve for stamps in blue ink. (Hint: First draw the Engel curves for incomes greater than $1, then draw them for incomes less than $1.)

[图表：坐标系 x-axis "Quantities" (0-8), y-axis "Income" (0-8)]  
- Red line: Vertical line at quantity = 0.5  
- Blue line: Straight line with slope 1, passing through (0.5, 1) and (6, 7) approximately

6.5 (0) Shirley Sixpack, as you will recall, thinks that two 8-ounce cans of beer are exactly as good as one 16-ounce can of beer. Suppose that these are the only sizes of beer available to her and that she has $30 to spend on beer. Suppose that an 8-ounce beer costs $.75 and a 16-ounce beer costs $1. On the graph below, draw Shirley’s budget line in blue ink, and draw some of her indifference curves in red.
```

#### 2. 图表解析（结合上文）
- **图表结构**：  
  - **横轴 (x-axis)**：商品数量（Quantities），范围 [0, 8]。  
  - **纵轴 (y-axis)**：收入（Income），范围 [0, 8]。  
  - **红线 (Twinkies)**：垂直线固定在数量 $t = 0.5$ 处（对应 $p_t = \$2, p_s = \$1$）。  
  - **蓝线 (Stamps)**：斜率为 1 的直线（当 $m \geq p_s = \$1$ 时，$s = m - 1$）。  

- **变化含义（结合上文知识连续性）**：  
  - **红线 (Twinkies) 的垂直特性**：  
    - 直接验证上文需求函数 $t(p_s, p_t, m) = p_s / p_t$（本例中 $t = 1/2 = 0.5$ 为常数）。  
    - 仅当 $m > p_s$ 时成立（收入阈值 $\$1$），**解释上文 "支出份额随收入递减" 的核心机制**：因 $t$ 恒定，支出 $p_t t = p_s$ 不变，故支出份额 $p_s / m$ 随 $m$ 严格递减。  
    - 此垂直线是拟线性效用（$u = s + \ln t$）的典型表现：与上文 Ambrose 案例（$U = 4\sqrt{x_1} + x_2$）同构，**强化 "必需品需求收入弹性 = 0" 的量化特征**（当 $m > p_s$ 时）。  

  - **蓝线 (Stamps) 的线性增长**：  
    - 对应 $s = m / p_s - 1$（$p_s = 1$，故 $s = m - 1$），**证实上文 (f) 项结论**：当 $m > p_s$ 时，额外收入全用于 stamps（$\Delta m = \Delta s$），因 Twinkies 需求饱和。  
    - 斜率为 1 意味着收入弹性随收入递减（例如 $m = 2$ 时弹性为 2，$m = 3$ 时为 1.5），但整体为正常品，**补充上文 "拟线性下非必需品的需求动态"**：与 Twinkies 的必需品属性形成对比，凸显需求结构二分性。  

  - **边界条件在图表中的体现**：  
    - 图表仅显式绘制 $m > \$1$ 部分（红线垂直、蓝线斜直），隐含上文边界解逻辑：当 $m < p_s$ 时需求切换至 $s = 0, t = m / p_t$（需单独绘制，但本图聚焦内点解有效区域）。  
    - **衔接上文 3.2.2 节**：此图将 Fribble 案例从一般公式扩展为数值实例，**实证化 "收入阈值 $p_s$ 决定解类型" 的论点**，并呼应 Ambrose 案例中 $M > 16$ 的边界条件设定逻辑。  

  - **商品类型区分的操作验证**：  
    - 红线垂直 → Twinkies 为必需品（支出份额 $\downarrow$，收入弹性 $\to 0$）；  
    - 蓝线正斜率 → Stamps 为正常品（需求随收入 $\uparrow$）。  
    - **闭环上文 "支出份额→商品分类" 框架**：本图通过 $t=0.5$ 的常量需求，直接显化 "必需品" 的量化基准（必需品在收入超过最小支出后需求恒定），为 6.4(c) 类问题提供可视化解析路径。

---
### Page/Slide 6



### 文字与公式提取

#### 图表标签
- 横轴：`16-ounce cans`（范围 0–40）
- 纵轴：`8-ounce cans`（范围 0–40）
- 蓝色线：`Blue budget line`
- 红色线：`Red curves`（两处标注）

#### 题干与解答
- **题干**  
  *"Shirley Sixpack thinks that two 8-ounce cans of beer are exactly as good as one 16-ounce can of beer. She has $30 to spend. 8-ounce beer costs $0.75, 16-ounce beer costs $1."*

- **解答**  
  (a) At these prices, which size can will she buy? **16-ounce cans.**  
  (b) If 8-ounce price falls to $0.55? Will she buy more 8-ounce? **No.**  
  (c) If 8-ounce price falls to $0.40? How many? **75 cans.**  
  (d) If she buys both, what must 8-ounce price be? **$0.50.**  
  (e) Demand function for 16-ounce beers:  
  $$
  x_{16} = 
  \begin{cases} 
  \dfrac{m}{p_{16}} & \text{if } p_{16} < 2p_8 \\
  0 & \text{if } p_{16} > 2p_8 \\
  \text{any affordable combination} & \text{if } p_{16} = 2p_8 
  \end{cases}
  $$

---

### 图表解析（结合上文知识连续性）

#### 核心结构与偏好特征
- **预算线（蓝色）**：  
  - 截距为 $(0, 40)$（$m/p_8 = 30/0.75$）和 $(30, 0)$（$m/p_{16} = 30/1$），斜率 $= -p_{16}/p_8 = -4/3$。  
  - **区别于上文拟线性案例**：此处无收入阈值（预算约束严格线性），但需求解由价格比率决定，**验证了 "完全替代品下预算线斜率与MRS的比较决定消费组合" 的一般原理**，与上文Twinkies/Stamps案例（必需品 vs 非必需品）形成鲜明对比。

- **无差异曲线（红色）**：  
  - 由题干 $u = x_{16} + \frac{1}{2}x_8$ 定义，MRS $= 2$（放弃 1 单位 16oz 需 2 单位 8oz 补偿），故曲线应为斜率 $-2$ 的直线。  
  - 图中红线呈陡峭形态，**并非上文所见垂直线**，而是因绘图比例导致视觉偏差；其线性特征 **强化了 "完全替代品无差异曲线为直线" 的核心假设**，反映商品间固定替代比例（2:1）。

#### 价格突变下的边界条件
- **当 $p_{16} < 2p_8$ 时**（如原始情形 $1 < 2 \times 0.75$）：  
  - 预算线斜率 $| -4/3 | < | \text{MRS} | = 2$，导致 **角点解**（仅购 16oz），对应解答 (a)。  
  - **衔接上文收入弹性分析**：此处需求不随收入连续变化（解类型跳跃），但符合 "价格比率决定解类型" 逻辑，**解释为何上例 Twinkies 需求恒定而此例需求为离散选择**。

- **临界价格 $p_8 = p_{16}/2 = \$0.50$**：  
  - 直接引出解答 (d)，此时预算线与无差异曲线重合，**形成连续解集**（任意组合均可行）。  
  - **拓展上文边界解框架**：将上例中 "收入阈值 $p_s$" 替换为 "价格比率阈值 $p_{16}/2$"，体现约束条件由收入转向价格结构。

- **价格降至 $p_8 = \$0.40$ 时**（解答 c）：  
  - 满足 $p_{16} > 2p_8$（$1 > 2 \times 0.40$），需求切换至纯 8oz 消费，**量化验证 (e) 式角点解条件**。  
  - **凸显商品类型二分性**：与上文拟线性效用中必需品需求稳定不同，此处 **完全替代品需求在临界价处陡变**，呼应 "偏好结构直接决定需求连续性" 的结论。

#### 理论闭环
- 本图 **实证化完美替代品的需求函数**：通过 $p_{16}$ 与 $2p_8$ 的关系，将效用理论（$u = x_{16} + \frac{1}{2}x_8$）转化为分段需求函数，**补充上文 "必需品需求收入弹性 = 0" 的案例库**，展示微观模型在不同类型偏好下的适用性。  
- 红线（斜率固定）与蓝线（价格决定斜率）的交互，**显式演绎 "相对价格驱动选择" 的微观机制**，为 6.6 节互补品（如 Miss Muffet 的 curds/whey）提供对比基准。

---
### Page/Slide 7



### 图片解析（基于上文知识连续性）

#### 1. 提取内容  
**文字与公式：**  
- 问题 (a): "How many units of curds will Miss Muffet demand in this situation? **8 units.** How many units of whey? **16 units.**"  
- 问题 (b): "Miss Muffet’s demand function for whey:  
  $D(p_c, p_w, m) = \dfrac{m}{p_w + p_c / 2}$"  
- 图表标签:  
  - 坐标轴: X-axis = "Curds" (0–32), Y-axis = "Whey" (0–32)  
  - 曲线: $w = 2c$, "Indifference curves" (L-shaped), "Budget line" (downward-sloping line)  

---

#### 2. 图表解析（结合上文理论）  
**核心结构与偏好特征**  
- **无差异曲线（L-shaped）**：  
  - 与上文啤酒案例的**直线无差异曲线**形成根本对比。L形表明 Miss Muffet 对 curds 和 whey 的偏好为**完全互补品**（固定消费比例 $w = 2c$）。  
  - **衔接上文逻辑**：上文完全替代品中，无差异曲线斜率固定（MRS=2）；此处互补品中，**无差异曲线角点位于 $w=2c$ 线上**，反映商品间不可替代性，与啤酒案例的"替代弹性无穷大"形成互补 vs 替代的二分框架。  
- **预算线与最优解**：  
  - 预算线与 $w=2c$ 线交点（标注 $c=8, w=16$）即为需求解。  
  - **关键机制**：互补品下消费者必在 $w=2c$ 线上消费（因偏离比例不增加效用），**直接推导出需求函数** $D = m / (p_w + p_c / 2)$。这与上文啤酒案例的**价格阈值驱动角点解**截然不同——互补品需求由收入约束**连续决定**（无价格突变点）。  

**理论对比与延伸**  
- **需求连续性差异**：  
  | **偏好类型** | **啤酒案例（完全替代品）** | **本例（完全互补品）** |  
  |--------------|---------------------------|------------------------|  
  | **解的性质** | 价格阈值引发离散跳跃（仅买16oz 或 8oz） | 需求随收入/价格连续变化（始终满足 $w=2c$） |  
  | **需求函数** | 分段函数（$p_{16}$ vs $2p_8$ 比较） | 单一公式 $D = m / (p_w + p_c / 2)$ |  
  - **实证印证**：本例中 $c=8, w=16$ 代入需求函数，若 $m=30, p_c=1, p_w=1$，则 $D_w = 30 / (1 + 1/2) = 20$（但 whey 需求应为 $2c$，实际求解需联立 $w=2c$ 与预算约束，吻合文本答案）。  
- **对上文知识的扩展**：  
  - 上文拟线性效用（Twinkies/Stamps）中，必需品需求**不随收入变化**；本例互补品中，**两类商品需求同比例随收入变化**（收入弹性均为正且相等）。  
  - **边界解消失**：互补品无上文啤酒案例的"价格临界点"，因预算线斜率变化**不会导致消费组合跳跃**，仅改变切点位置——这解释了为何上文问题 (d) 的"混合消费"需精确价格匹配，而互补品**天然要求比例消费**。  

---

#### 3. 理论闭环  
- 本图**实证化完全互补品的需求逻辑**：通过 $w=2c$ 的刚性比例约束，将效用理论转化为可直接量化的线性需求函数，**补充上文"完全替代品/拟线性"案例库**。  
- 与啤酒案例的**强对比**：  
  - 替代品：需求由 $p_{16} \stackrel{?}{=} 2p_8$ 标志选择逻辑（离散）；  
  - 互补品：需求由 $m = p_c c + p_w \cdot 2c$ 直接求解（连续）。  
- **微观机制显式化**：L形无差异曲线与预算线的切点**必然落在 $w=2c$ 线上**，突显"互补品下消费者不会多消费一种商品"的核心原理，为后续章节（如 6.6 节）提供基准模型。

---
### Page/Slide 8



#### 1. 提取内容  
**文字与公式：**  
- 页码：74 DEMAND (Ch. 6)  
- (c) If Mary had only 144 square feet in her garden, how many cockle shells would she grow? **36**.  
- (d) If Mary grows both silver bells and cockle shells, then we know that the number of square feet in her garden must be greater than **192**.  
- **6.8 (0)** Casper consumes cocoa and cheese. He has an income of $16$. Cocoa is sold unusually: $x$ units cost total $x^2$ dollars. Cheese at $2 per unit. Budget equation:  
  $x^2 + 2y = 16$ where $x$ = cocoa consumption, $y$ = cheese consumption.  
  Utility function: $U(x, y) = 3x + y$.  
- **(a)** Graph request: Draw boundary of Casper’s budget set in blue ink; sketch two or three indifference curves in red ink.  
- **图表标签:**  
  - X-axis: "Cocoa" (0–16)  
  - Y-axis: "Cheese" (0–16)  
  - Elements: "Blue budget line" (curved line), "Red indifference curves" (straight lines)  
- **(b)** Slope condition equation:  
  $\dfrac{2x}{2} = \dfrac{3}{1}$  
  Casper demands **3 units of cocoa** and **3.5 units of cheese**.  
- **6.9 (0)** Brief text on U.S. Bureau of Labor Statistics family budget studies.  

---

#### 2. 图表解析（结合上文理论）  
**核心结构与微观机制**  
- **预算线形态（曲线）**:  
  - 预算约束 $x^2 + 2y = 16$ 生成**向下弯曲的抛物线**（$y = \frac{16 - x^2}{2}$），反映 **cocoa 的边际成本递增**（$P_x = \frac{d(x^2)}{dx} = 2x$）。这拓展了上文“相对价格”框架：**价格非外生恒定，而是内生消费量函数**。  
  - **衔接上文逻辑**：上文互补品（如 $w=2c$）需刚性比例抵消价格波动；此处非线性价格使 **收入约束与边际成本动态耦合**——消费者通过调整 $x$ 使 $P_x / P_y$ 匹配 MRS，强化“相对价格驱动选择”机制。  

- **无差异曲线与最优解**:  
  - 效用函数 $U=3x+y$ 产生 **直线无差异曲线**（斜率 $-3$，MRS 恒为 $3$），表明 cocoa 与 cheese 为 **完全替代品**。  
  - 最优点 $(x=3, y=3.5)$ 由 $MRS = P_x / P_y$ 决定：  
    \[
    3 = \frac{2x}{2} \implies x=3
    \]  
    代入预算方程得 $y=3.5$。此解 **实证上文微观机制**——即使价格非线性，消费者仍选择 $MU_x / MU_y = P_x / P_y$ 的均衡点。与上文啤酒案例的“离散角点解”对比，此处因无差异曲线线性且预算线凸曲，**需求对价格变化连续响应**（无价格阈值跳跃）。  

**与上文知识的连续性扩展**  
- **非线性约束下的相对价格演绎**:  
  | **维度** | **上文线性预算案例** | **本例非线性预算案例** |  
  |----------|----------------------|------------------------|  
  | **价格特性** | 价格外生恒定（如啤酒单价） | cocoa 价格 $P_x=2x$ 随消费量递增 |  
  | **均衡条件** | $MRS = p_x / p_y$ | $MRS = \frac{P_x}{P_y} = x$（内生价格匹配） |  
  | **收入效应** | 拟线性效用中 $x$ 需求不随收入变 | $x$ 需求固定（由 $MRS$ 确定），收入仅影响 $y$ |  
  - **关键延伸**：上文互补品需求始终满足 $w=2c$（比例刚性）；本例因 **完全替代+非线性价格**，$x$ 需求由 MRS 直接锁定 ($x=3$)，$y$ 需求 **仅由剩余收入决定**（$y = \frac{m - x^2}{p_y}$），呼应拟线性效用中“目标商品需求弹性为零”的特征。  
- **对比上文互补品框架**:  
  - 互补品（6.6节）：L形无差异曲线使消费比例固定，**预算线斜率变化不扭曲比例**。  
  - 本例：直线无差异曲线 + 曲线预算线，**价格递增强制内部解**，但机制本质相同——消费者总在 $MRS = \text{边际成本率}$ 处优化。  
  - **理论闭环**：本图证明，无论价格是否线性，“相对价格驱动选择”原理万变不离其宗。当 $P_x$ 内生（非上文啤酒案例的外生价格），均衡点由 $\frac{2x}{2} = 3$ 精确刻画，为分析现实市场（如阶梯定价）提供原型。  

> 注：本例与上文互补品形成互补-替代光谱的另一端，共同阐释需求生成的普适逻辑——**禁锢于比例（互补） vs 由价格引导（替代）**。

---
### Page/Slide 9



### 1. 提取图片中的文字与数据  
**引言部分：**  
> tables below report total current consumption expenditures and expenditures on certain major categories of goods for 5 different income groups in the United States in 1961. People within each of these groups all had similar incomes. Group A is the lowest income group and Group E is the highest.  

---

**Table 6.1**  
*Expenditures by Category for Various Income Groups in 1961*  

| Income Group              | A     | B     | C     | D     | E     |
|---------------------------|-------|-------|-------|-------|-------|
| Food Prepared at Home     | 465   | 783   | 1078  | 1382  | 1848  |
| Food Away from Home       | 68    | 171   | 213   | 384   | 872   |
| Housing                   | 626   | 1090  | 1508  | 2043  | 4205  |
| Clothing                  | 119   | 328   | 508   | 830   | 1745  |
| Transportation            | 139   | 519   | 826   | 1222  | 2048  |
| Other                     | 364   | 745   | 1039  | 1554  | 3490  |
| **Total Expenditures**    | 1781  | 3636  | 5172  | 7415  | 14208 |

---

**Table 6.2**  
*Percentage Allocation of Family Budget*  

| Income Group              | A   | B    | C    | D    | E    |
|---------------------------|-----|------|------|------|------|
| Food Prepared at Home     | 26  | 22   | 21   | 19   | 13   |
| Food Away from Home       | 3.8 | 4.7  | 4.1  | 5.2  | 6.1  |
| Housing                   | 35  | 30   | 29   | 28   | 30   |
| Clothing                  | 6.7 | 9.0  | 9.8  | 11   | 12   |
| Transportation            | 7.8 | 14   | 16   | 17   | 14   |

---

**问题与解答：**  
- **(a)** Complete Table 6.2.  
- **(b)** Which of these goods are normal goods? **All of them.**  
- **(c)** Which of these goods satisfy your textbook’s definition of luxury goods at most income levels? **Food away from home, clothing, transportation.**  

---

### 2. 数据解析（结合上文理论）  
#### **核心机制：收入效应与需求分类**  
1. **正常商品的实证验证**：  
   - 表格中所有商品的**绝对支出随收入上升而增加**（如 `Food Prepared at Home` 从 465 → 1848；`Clothing` 从 119 → 1745），符合上文隐含的“收入-需求正相关”逻辑。  
   - **关键区别**：商品是否为正常品取决于**绝对支出趋势**而非占比。例如，`Food Prepared at Home` 的百分比下降（26% → 13%），但绝对值扩大 4 倍，印证“收入弹性 >0 即为正常品”的微观原理。  
   - **理论连续性**：与上文拟线性效用模型（如 $U=3x+y$）中“收入仅影响非目标商品”的结论呼应——需求结构由收入规模内生决定。  

2. **奢侈品的识别**：  
   - **奢侈品定义**：收入弹性 >1，表现为**百分比支出随收入上升而增加**。  
   - **实证表现**：  
     - `Food Away from Home`（6.1 → 6.1%）、`Clothing`（6.7% → 12%）、`Transportation`（7.8% → 16%）的占比在高收入组显著上升，符合“奢侈品”定义。  
     - **对比上文互补品案例**：互补品（如啤酒案例）需求比例固定，而此处奢侈品需求比例随收入动态变化，体现**偏好异质性**——高收入群体通过调整消费组合优化效用。  

3. **预算分配的微观逻辑**：  
   - **生存品刚性**：`Housing` 占比稳定在 28–35%，反映基本生存需求的**必需性（income-inelastic demand）**，与上文“互补品需刚性比例”形成行为逻辑一致性。  
   - **替代弹性释放**：`Food Away from Home` 等奢侈品占比上升，说明收入提升后消费者减少“时间成本高”的居家烹饪，转向更高效的消费方式——体现**边际替代率随收入变化**的效用优化路径。  

#### **与上文知识的扩展衔接**  
| **维度**          | **上文非线性价格案例**                     | **本例收入分组数据**                     |  
|--------------------|------------------------------------------|------------------------------------------|  
| **约束变化驱动**   | 价格内生导致预算线弯曲                   | 收入分层导致预算集扩张                   |  
| **需求响应特征**   | 完全替代品下 $x$ 需求固定，$y$ 随预算变 | 奢侈品需求占比上升，生存品占比下降       |  
| **均衡机制**       | $MRS = P_x/P_y$ 决定内部解             | 恩格尔曲线斜率决定商品分类               |  
- **理论深化**：上文通过公式 $\frac{2x}{2} = 3$ 量化价格-需求关系，本例通过百分比分配实证 **“收入是隐性价格”**——高收入群体因时间成本上升，隐性提高非必需品的边际效用，驱动奢侈品需求（如 `Food Away from Home`）。  
- **政策启示**：BLS 数据（6.9节）与微观模型结合，揭示：**阶梯定价政策对奢侈品的影响可能大于生存品**（如对 `Transportation` 征税，低收入群体敏感度更高），为公共经济学提供行为依据。  

> 注：本例将消费者选择理论从**静态价格-效用匹配**（上文）拓展至**动态收入-结构演化**，完整呈现“价格、收入双约束下的需求生成机制”。

---
### Page/Slide 10



### 3. 当前图片解析（基于上文知识连续性）

#### **1. 提取文字与公式**  
- **文字内容**：  
  - `(d) Which of these goods satisfy your textbook’s definition of necessity goods at most income levels? Food prepared at home, housing.`  
  - `(e) On the graph below, use the information from Table 6.1 to draw “Engel curves.” (Use total expenditure on current consumption as income for purposes of drawing this curve.) Use red ink to draw the Engel curve for food prepared at home. Use blue ink to draw an Engel curve for food away from home. Use pencil to draw an Engel curve for clothing. How does the shape of an Engel curve for a luxury differ from the shape of an Engel curve for a necessity? The curve for a luxury gets flatter as income rises, the curve for a necessity gets steeper.`  
  - `6.10 (0) Percy consumes cakes and ale. His demand function for cakes is \( q_c = m - 30p_c + 20p_a \), where \( m \) is his income, \( p_a \) is the price of ale, \( p_c \) is the price of cakes, and \( q_c \) is his consumption of cakes. Percy’s income is $100, and the price of ale is $1 per unit.`  
  - `(a) Is ale a substitute for cakes or a complement? Explain. A substitute. An increase in the price of ale increases demand for cakes.`  

- **公式**：  
  \[
  q_c = m - 30p_c + 20p_a
  \]

#### **2. 图表解析：Engel 曲线形状的实证含义**  
当前图片包含一个 Engel 曲线图（横轴为**商品支出总额（千美元）**，纵轴为**特定商品支出**），结合上文知识点总结（重点在收入-需求结构演化），解析如下：  

##### **(1) 必需品与奢侈品的曲线差异机制**  
- **红色曲线（食品在家准备，必需品）**：  
  - 对应上文定义的 `Food prepared at home`，其支出占比随收入上升而下降（上文 2.1 节），但绝对支出增长。  
  - **形状解读**：曲线随收入上升**变陡峭**（steeper），表明 **d(总支出)/d(商品支出) 的斜率递增**。  
    - **微观逻辑连续性**：这验证了上文“必需品在高收入阶段支出增速放缓”的隐含结论（生存品刚性）。随着收入扩张，消费者对必需品的边际支出率（marginal propensity to consume）下降，但因基础需求刚性，支出增速在初始阶段较快（低收入区曲线较平），高收入区趋缓（上文“收入弹性 <1”），导致整体曲线斜率递增，体现**恩格尔曲线斜率对收入弹性判断的关键作用**。  

- **蓝色曲线（外出就餐，奢侈品）**：  
  - 对应上文定义的 `Food away from home`（奢侈品仅因 **支出占比上升**，符合上文 2.2 节“收入弹性 >1”）。  
  - **形状解读**：曲线随收入上升**变平缓**（flatter），表明 **d(总支出)/d(商品支出) 的斜率递减**。  
    - **微观逻辑连续性**：这与上文“奢侈品需求占比动态上升”直接呼应。高收入下，消费者通过优化边际替代率（如降低时间成本，转向高效消费方式）增加奢侈品支出，但增速渐缓（上文“收入作为隐性价格”机制），导致斜率递减。此现象是“需求结构内生演化”的典型实证（与上文互补品刚性比例形成对比）。  

- **铅笔线（服装，奢侈品）**：  
  - 同样满足奢侈品定义（上文 2.2 节），曲线趋平缓趋势与蓝色线一致。  
  - **关键区别**：相比外出就餐，服装的奢侈品属性在高收入段更显著（占比从 6.7%→12%），反映**高收入群体通过消费组合调整强化边际效用优化**（与上文“预算分配中时间成本隐性提高”的扩展衔接一致）。  

##### **(2) 与上文理论的深化衔接**  
| **维度**         | **上文知识点总结**                     | **本图实证体现**                     |  
|------------------|--------------------------------------|--------------------------------------|  
| **收入-需求响应** | “奢侈品需求占比上升，生存品占比下降” | 必需品曲线变陡 → 支出占比下降；奢侈品曲线变平 → 支出占比上升 |  
| **恩格尔曲线本质** | “恩格尔曲线斜率决定商品分类”         | 纵轴-横轴定义（总支出 vs. 商品支出）直接量化 **d(总支出)/d(商品支出)**，作为收入弹性的代理指标 |  
| **动态演化机制** | “收入提升后替代弹性释放”             | 曲线形状变化反映边际替代率调整：必需品趋向低弹性（陡峭），奢侈品趋向高弹性（平缓） |  

- **理论深化点**：  
  - 本图将上文隐含的“收入是隐性价格”模型（如 6.9 节 BLS 数据）**动态可视化**：必需品曲线变陡，说明高收入区时间成本隐性抬高必需品的相对价格，抑制支出增长；奢侈品曲线变平，说明收入扩张使消费者能更高效分配资源，需求响应从激进转向理性（与上文“阶梯定价政策对奢侈品影响可能大于生存品”形成行为基础）。  
  - 避免重复上文“正常商品绝对支出增加”等基础结论，聚焦图表对**收入分层下需求结构转折点**的刻画（如必需品曲线从低收入平缓至高收入陡峭，反映 BLS 数据中生存需求的阶段性刚性破点）。  

> **核心连续性**：上文通过 BLS 数据组论证“收入-需求关系”，本图以 Engel 曲线斜率变化**锚定商品分类的动态阈值**，完整呈现从“理论模型 → 实证数据 → 形状趋势”的需求生成机制，为政策设计（如必需品补贴）提供可量化依据。

---
### Page/Slide 11



### 1. 提取当前图片中的所有文字、公式  

#### 文字内容  
- `(b) Write an equation for Percy’s demand function for cakes where income and the price of ale are held fixed at $100 and $1. `  
- `(c) Write an equation for Percy’s inverse demand function for cakes where income is $100 and the price of ale remains at $1. At what price would Percy buy 30 cakes? $3. Use blue ink to draw Percy’s inverse demand curve for cakes.`  
- `(d) Suppose that the price of ale rises to $2.50 per unit and remains there. Write an equation for Percy’s inverse demand for cakes. Use red ink to draw in Percy’s new inverse demand curve for cakes.`  
- `Price` (Y-axis label)  
- `Number of cakes` (X-axis label)  
- `Blue Line` (annotation pointing to blue solid line in graph)  
- `Red Line` (annotation pointing to red dashed line in graph)  
- `6.11 (0) Richard and Mary Stout have fallen on hard times, but remain rational consumers. They are making do on $80 a week, spending $40 on food and $40 on all other goods. Food costs $1 per unit. On the graph below, use black ink to draw a budget line. Label their consumption bundle with the letter A.`  
- `(a) The Stouts suddenly become eligible for food stamps. This means that they can go to the agency and buy coupons that can be exchanged for $2 worth of food. Each coupon costs the Stouts $1. However, the maximum number of coupons they can buy per week is 10. On the graph, draw their new budget line with red ink.`  

#### 公式  
- \( q_c = 120 - 30p_c \)  
- \( p_c = 4 - \frac{q_c}{30} \)  
- \( p_c = 5 - \frac{q_c}{30} \)  

---

### 2. 图表解析：需求曲线移动的实证含义  
图表展示 **Prices** 与 **Number of cakes** 的关系，包含两条逆需求曲线：  
- **Blue Line**：对应 ale 价格 \( p_a = \$1 \)，逆需求方程为 \( p_c = 4 - \frac{q_c}{30} \)。  
- **Red Line**：对应 ale 价格 \( p_a = \$2.50 \)，逆需求方程为 \( p_c = 5 - \frac{q_c}{30} \)。  

#### 核心变化含义（结合上文知识点总结）  
上文明确指出：*“Increase in the price of ale increases demand for cakes”*，并推导出需求函数 \( q_c = m - 30p_c + 20p_a \)。图表动态验证了这一机制：  
- **移动本质**：当 \( p_a \) 从 \$1 升至 \$2.50，逆需求曲线**上移**（Y 截距从 4 增至 5），而非平行移动。  
  - **微观逻辑连续性**：上文公式中 \( +20p_a \) 项表明 ale 与 cakes 为**替代品**（\(\frac{\partial q_c}{\partial p_a} > 0\)）。这一关系直接驱动需求曲线移动：  
    - 原均衡（Blue Line）：\( p_a = \$1 \) 时，最大支付意愿为 \$4（当 \( q_c = 0 \)）。  
    - 新均衡（Red Line）：\( p_a = \$2.50 \) 时，最大支付意愿升至 \$5，**等价于需求量在任意价格下增长 30 单位**（例如，当 \( p_c = \$2 \)，\( q_c \) 从 60 增至 90）。  
  - **图表斜率一致性**：曲线斜率不变（均为 \(-1/30\)），表明自有价格弹性未变，但**交叉价格效应集中体现在需求曲线位置**（与上文“价格变动通过互补/替代关系影响需求”逻辑一脉相承）。  
- **关键隐含结论**：  
  - 上文强调 *“price of ale increases demand for cakes”* 的**非替代品例外性**（若为互补品，需求应下降），而此处曲线右移**直接量化了替代强度**：\( \Delta p_a = +\$1.50 \) 导致截距增加 \$1，与上文公式系数 \( 20 \times 1.50 / 30 = 1 \) 精确匹配（20 为交叉价格效应系数，30 为自有价格效应系数）。  
  - 此现象**避免重复上文基础定义**（如正常商品属性），聚焦**政策模拟的实证基础**：例如，若 ale 价格受外生冲击（如税收），cakes 的需求波动可直接由曲线移动幅度预测，为交叉价格弹性应用提供图解框架。  

#### 与上文动态衔接  
| **维度**               | **上文知识点总结**                          | **本图实证体现**                                  |  
|------------------------|------------------------------------------|-------------------------------------------------|  
| **商品间关系**         | “ale 价格上涨增加 cake 需求”（替代品）    | 曲线移动方向与幅度量化替代强度（截距变化= \$1） |  
| **需求结构韧性**       | 未明确定义替代品动态响应                 | 曲线斜率不变 → 替代效应完全由位置移动承载        |  
| **实证扩展性**         | 公式 \( q_c = m - 30p_c + 20p_a \)       | 固定 \( m=\$100 \) 后，曲线移动验证局部均衡路径  |  

> **理论深化**：本图将上文隐含的跨商品价格弹性**行为化**，直接体现“替代效应在预算约束下的显性表现”（对比上文 Engel 曲线聚焦收入效应）。Red Line 的上移幅度（截距 +1）与上文公式交叉项系数一致，强化了**需求函数参数可直接映射政策冲击效果**的认知——例如，ale 价格变动 1% 对 cake 需求的影响可从截距变化线性推导，为反垄断或税收分析提供微观图解工具。

---
### Page/Slide 12



### 提取内容  
**文字与公式：**  
- 页眉：`78 DEMAND (Ch. 6)`  
- 问题 (b)：`If the Stouts have homothetic preferences, how much more food will they buy once they enter the food stamp program? 5 units.`  
- 图表标签：  
  - y-axis：`Dollars worth of other things`（刻度：20, 40, 60, 80, 100, 120）  
  - x-axis：`Food`（刻度：0, 20, 40, 60, 80, 100, 120）  
  - 图表内标记：`a`, `New consumption point`, `Red budget line`, `Black budget line`  
- 后续文本：  
  ```  
  Calculus 6.12 (2) As you may remember, Nancy Lerner is taking an economics course in which her overall score is the minimum of the number of correct answers she gets on two examinations. For the first exam, each correct answer costs Nancy 10 minutes of study time. For the second exam, each correct answer costs her 20 minutes of study time. In the last chapter, you found the best way for her to allocate 1200 minutes between the two exams. Some people in Nancy’s class learn faster and some learn slower than Nancy. Some people will choose to study more than she does, and some will choose to study less than she does. In this section, we will find a general solution for a person’s choice of study times and exam scores as a function of the time costs of improving one’s score.  
  (a) Suppose that if a student does not study for an examination, he or she gets no correct answers. Every answer that the student gets right on the first examination costs \( P_1 \) minutes of studying for the first exam. Every answer that he or she gets right on the second examination costs \( P_2 \) minutes of studying for the second exam. Suppose that this student spends a total of \( M \) minutes studying for the two exams and allocates the time between the two exams in the most efficient possible way. Will the student have the same number of correct answers on both exams?  
  ```  
- 显式公式：\( P_1 \), \( P_2 \), \( M \)（未给出闭合公式，但隐含约束 \( P_1 \cdot s_1 + P_2 \cdot s_2 = M \)，其中 \( s_1, s_2 \) 为两科正确答案数）。  

---

### 图表解析：预算约束移动的实证含义  
图表展示 **Food** 与 **Dollars worth of other things** 的关系，包含两条预算线：  
- **Black budget line**：初始预算约束，通过点 \((0, 80)\) 和 \((80, 0)\)，隐含线性约束 \( y = 80 - x \)（\( x \) 为食物消费量，\( y \) 为其他商品支出）。  
- **Red budget line**：食物券计划引入后的预算约束，消费点从 **a**（约 \((40, 40)\)）移动至 **New consumption point**（约 \((45, 45)\)）。  

#### 核心变化含义（结合上文知识点总结）  
上文聚焦**价格变动通过替代效应驱动需求曲线移动**，而本图通过预算约束变动验证**收入效应在特定偏好下的量化表现**，形成消费者理论的平行逻辑：  
- **移动本质**：  
  - 食物券计划等价于**条件收入增强**（仅针对食物消费），而非一般收入增加。  
    - Black budget line 起点 \((0, 80)\) 表示初始收入限制；Red budget line 未显示截距变化，但消费点位移 \((40,40) \to (45,45)\) 表明：**对于同位偏好，预算扩展导致食物消费同比例增长**（5 单位，如上文答案所示）。  
    - *微观逻辑连续性*：上文需求函数 \( q_c = m - 30p_c + 20p_a \) 中 \( m \) 为收入项，此处同位偏好下 \( \frac{\partial x}{\partial m} = \text{constant} \)（收入弹性恒定），直接解释消费量增长 5 单位。  
  - **图表斜率一致性**：两条预算线斜率相同（\(-1\)），表明**食物与“其他商品”价格比未变**。这与上文需求曲线斜率不变（\(-1/30\)）逻辑一致——**自有价格弹性稳定下，外部冲击（如食物券）仅影响消费水平**，而非替代结构。  
- **关键隐含结论**：  
  - 本图**避开交叉价格效应**（上文核心），转而聚焦**收入效应的实际测定**：食物券计划作为外生干预，其效果精确量化为消费点右移 5 单位（x 轴从 40 到 45），这与上文“policy simulation”框架呼应——若将食物券视为针对特定商品的收入补贴，其需求响应幅度可从偏好类型直接推导（同位偏好下响应可预测）。  
  - *避免重复定义*：不重新阐述同位偏好，但强化其与上文**需求结构韧性**的隐含关联——上文需求曲线位置移动由交叉价格效应承载，此处消费量增长由收入效应驱动，共同体现“外部冲击通过参数传导至消费行为”的统一机制。  

#### 与上文动态衔接  
| **维度**               | **上文知识点总结**                          | **本图实证体现**                                  |  
|------------------------|------------------------------------------|-------------------------------------------------|  
| **外部冲击响应**       | 价格变动通过替代关系影响需求（需求曲线移动） | 食物券计划通过收入效应影响消费（消费点位移）     |  
| **参数映射实证效果**   | 需求函数系数量化替代强度（截距变化= \$1） | 同位偏好下消费增量直接反映冲击幅度（+5 units）  |  
| **政策分析工具**       | 交叉价格弹性提供图解框架                  | 预算约束移动为收入政策（如补贴）提供微观验证     |  

> **理论深化**：本图将上文隐含的**收入-消费路径显性化**，突出与替代效应的区分。Red budget line 对应的消费点增益（5 单位食物）印证了：**当偏好满足同位性时，定向收入干预的需求效应可由消费比例直接校准**，为评估福利政策效率提供微观图解——例如，对比上文 ale 价格冲击对蛋糕需求的线性影响，此处食物券效果验证收入弹性在局部均衡中的稳定性。

---
### Page/Slide 13



### 提取当前图片中的所有文字、公式

#### 文字内容
```
NAME ________________ 79

Yes. Write a general formula for this student’s overall score for the course as a function of the three variables, $P_1, P_2,$ and $M$: $S = \frac{M}{P_1 + P_2}$. If this student wants to get an overall score of $S$, with the smallest possible total amount of studying, this student must spend $P_1 S$ minutes studying for the first exam and $P_2 S$ studying for the second exam.

(b) Suppose that a student has the utility function
\[
U(S, M) = S - \frac{A}{2} M^2,
\]
where $S$ is the student’s overall score for the course, $M$ is the number of minutes the student spends studying, and $A$ is a variable that reflects how much the student dislikes studying. In Part (a) of this problem, you found that a student who studies for $M$ minutes and allocates this time wisely between the two exams will get an overall score of $S = \frac{M}{P_1 + P_2}$. Substitute $\frac{M}{P_1 + P_2}$ for $S$ in the utility function and then differentiate with respect to $M$ to find the amount of study time, $M$, that maximizes the student’s utility. $M = \frac{1}{A (P_1 + P_2)}$. Your answer will be a function of the variables $P_1, P_2,$ and $A$. If the student chooses the utility-maximizing amount of study time and allocates it wisely between the two exams, he or she will have an overall score for the course of $S = \frac{1}{A (P_1 + P_2)^2}$.

(c) Nancy Lerner has a utility function like the one presented above. She chose the utility-maximizing amount of study time for herself. For Nancy, $P_1 = 10$ and $P_2 = 20$. She spent a total of $M = 1,200$ minutes studying for the two exams. This gives us enough information to solve for the variable $A$ in Nancy’s utility function. In fact, for Nancy, $A = \frac{1}{36,000}$.

(d) Ed Fungus is a student in Nancy’s class. Ed’s utility function is just like Nancy’s, with the same value of $A$. But Ed learns more slowly than Nancy. In fact it takes Ed exactly twice as long to learn anything as it takes Nancy, so that for him, $P_1 = 20$ and $P_2 = 40$. Ed also chooses his amount of study time so as to maximize his utility. Find the ratio of the amount of time Ed spends studying to the amount of time Nancy spends studying. $1/2$. Will his score for the course be greater than half, equal to half, or less than half of Nancy’s? Less than half.

6.13 (1) Here is a puzzle for you. At first glance, it would appear that there is not nearly enough information to answer this question. But when you graph the indifference curve and think about it a little, you will see that there is a neat, easily calculated solution.
```

#### 公式总结
- 核心约束：$ S = \frac{M}{P_1 + P_2} $
- 效用函数：$ U(S, M) = S - \frac{A}{2} M^2 $
- 最优学习时间：$ M = \frac{1}{A (P_1 + P_2)} $
- 最优分数：$ S = \frac{1}{A (P_1 + P_2)^2} $
- Nancy 的参数：$ P_1 = 10 $, $ P_2 = 20 $, $ M = 1,200 $, $ A = \frac{1}{36,000} $
- Ed 的参数：$ P_1 = 20 $, $ P_2 = 40 $, 时间比 $ = \frac{1}{2} $, 分数相对结果：Less than half

---

### 内容解析（基于上文知识点总结）

当前内容实证化了【上文知识点总结】中隐含的约束机制，并扩展至效用最大化框架，形成与消费者理论的直接映射：

#### 1. **约束结构的显性验证**
- 上文隐含约束 $ P_1 \cdot s_1 + P_2 \cdot s_2 = M $（$ s_1, s_2 $ 为正确答案数）在此转化为闭合公式 $ S = \frac{M}{P_1 + P_2} $，其中：
  - $ P_1, P_2 $ 作为“学习效率参数”，等价于上文中的商品价格（price effect）；
  - $ M $ 为总学习时间，对应预算约束中的总收入；
  - $ S $ 为分数，相当于“分数商品”的消费量。
- **知识连续性**：  
  资源最小化条件（“spend $ P_1 S $ minutes... $ P_2 S $ minutes”）严格遵循 $ M = P_1 S + P_2 S $，印证上文“预算约束的线性隐含关系”，但将场景迁移至时间与分数的权衡，为后续效用分析铺垫。

#### 2. **效用最大化与需求函数延伸**
- 代入效用函数 $ U(S, M) = S - \frac{A}{2} M^2 $ 后，导出最优解：
  $$
  M = \frac{1}{A (P_1 + P_2)}, \quad S = \frac{1}{A (P_1 + P_2)^2}
  $$
- **关键映射关系**：
  - $ A $ 量化学习负效用，等效于上文的“偏好参数”，其倒数直接影响需求弹性；
  - $ S $ 关于 $ (P_1 + P_2) $ 的 **负二次响应**（$ S \propto (P_1 + P_2)^{-2} $）揭示：  
    *外部价格参数变动的综合效应强度倍增于线性需求模型*（上文需求函数 $ q_c = m - 30p_c + 20p_a $ 的线性响应）。  
    例如，Ed 的 $ P_1, P_2 $ 翻倍（$ P_1 + P_2 $ 翻倍）导致 $ S $ 降至 $ \frac{1}{4} $，而时间 $ M $ 仅降至 $ \frac{1}{2} $，**验证自有价格弹性为 -2**。
- **与上文逻辑衔接**：  
  上文需求曲线移动源于交叉价格效应（$ +20p_a $ 项），此处则体现**总量价格冲击的非线性收入-替代叠加效应**：  
  - $ M $ 的 $ (P_1 + P_2)^{-1} $ 关系对应收入效应（平均学习时间与价格和成反比）；  
  - $ S $ 的 $ (P_1 + P_2)^{-2} $ 关系强化替代强度（分数对综合价格更敏感）。

#### 3. **实证案例的政策启示**
- **Nancy/Ed 比较**（$ P_1 + P_2 $ 翻倍）：
  - 学习时间比 $ \frac{1}{2} $ 直接反映收入效应强度（$ M $ 与 $ P_1 + P_2 $ 比例移动）；  
  - 分数 $ S $ 降至 $ \frac{1}{4} $（“Less than half”）证实：  
    *当价格冲击影响所有商品（此处为双科习效率）时，需求响应幅度随隐含弹性指数级放大*，超越上文仅针对单一商品价格变动的线性分析。
- **动态衔接上文政策模拟**：  
  | **维度**               | **上文知识点总结**                          | **当前内容实证**                               |
  |------------------------|------------------------------------------|----------------------------------------------|
  | **外部冲击形式**       | 交叉价格变动（如 $ p_a $ 变化）          | 综合价格变动（$ P_1 + P_2 $ 翻倍）          |
  | **需求响应函数**       | 线性截距移动（$ \Delta \text{intercept} = \$1 $） | 次级响应（$ S \propto \text{price}^{-2} $） |
  | **政策分析意义**       | 需求曲线移动量测替代效应                 | **分数损失率量化价格冲击的复合福利影响**     |

> **理论深化**：当前内容将上文“隐含约束”具象为**时间-分数转换效率模型**，$ A $ 作为偏好参数提供高度结构化需求方程，使价格冲击的模拟具备闭合解。Ed 的案例证明：**当外部冲击提升所有商品价格（非定向补贴）时，需求下降幅度可能远超收入损失比例**（分数降为 25% vs 时间降 50%），为评估教育干预政策效率提供微观机制——如上文食物券计划的收入效应分析，此处进一步揭示**价格参数叠加对效用损失的非线性放大作用**。

---
### Page/Slide 14



### 1. Text and Formula Extraction from Current Image  
**All extracted text and formulas:**  
- Utility function: $ U(x, y) = \min\{4x, 2x + y\} $, where $ x $ = consumption of whips, $ y $ = consumption of leather jackets.  
- Kinko consumes 15 whips and 10 leather jackets; price of whips is \$10.  
- (a) Slope of indifference curve at $(15,10)$: **$-2$**.  
- Price of leather jackets: **\$5**.  
- Income calculation: $ 15 \times 10 + 10 \times 5 = 200 $.  
- Chart elements:  
  - Axes: Horizontal = "Whips" (0–40), Vertical = "Leather jackets" (0–40).  
  - Key equations: $ 4x = 40 $ (vertical line at $ x=10 $), $ 2x + y = 40 $ (line with slope $-2$).  
  - Point $(15,10)$ marked on indifference curve.  

---

### 2. Chart Interpretation with Knowledge Continuity  
The chart illustrates Kinko’s utility maximization under a budget constraint, **directly extending the prior resource allocation framework** (e.g., M = P₁S + P₂S in the learning model). Key insights:  

#### **Indifference Curve and Slope Meaning**  
- The indifference curve for $ U = 40 $ (passing through $(15,10)$) consists of two segments:  
  - **Vertical segment ($ 4x = 40 $)**: Valid where $ y \geq 2x $ (i.e., $ U = 4x $). Here, whips are "bottleneck" for utility.  
  - **Downward-sloping segment ($ 2x + y = 40 $)**: Valid where $ y \leq 2x $ (i.e., $ U = 2x + y $). The slope $-2$ reflects the **marginal rate of substitution (MRS)** at $(15,10)$, meaning Kinko must sacrifice 2 leather jackets per additional whip to maintain utility.  
- **Critical link to prior context**: The MRS here is analogous to the "learning efficiency trade-off" in the previous model. Just as the slope of the marginal utility curve (e.g., $ \partial U / \partial M $) implied time allocation efficiency, this MRS quantifies the feasibility frontier for good substitution—both derive from constrained optimization where **MRS equals the price ratio at optimum**.  

#### **Budget Constraint and Optimal Point**  
- The budget line (implied but not drawn) passes through $(15,10)$ with slope $ -p_x / p_y = -10 / 5 = -2 $, matching the IC slope. This confirms **utility maximization**, as required by the tangency condition.  
- **Continuity with prior learning model**: The income calculation $ M = 15 \times 10 + 10 \times 5 = 200 $ is a **direct application of the budget constraint closure** ($ M = P_1 S + P_2 S $). Here:  
  - $ p_x, p_y $ = resource "prices" (analogous to $ P_1, P_2 $ in learning efficiency),  
  - $ x, y $ = "consumption" of goods (analogous to "score" $ S $ as a composite output),  
  - $ M $ = total budget (analogous to total learning time).  
- This demonstrates the **universality of the linear budget constraint** in microeconomic optimization, whether allocating money (current image) or time (prior context).  

#### **Policy-Relevant Contrast with Prior Elasticity Analysis**  
- The min utility function here generates **kinked demands** with muted price sensitivity (e.g., demands may not adjust if prices change but the optimum stays on the same IC segment). This contrasts sharply with the prior model’s $ S \propto (P_1 + P_2)^{-2} $, where a doubling of "prices" $(P_1 + P_2)$ slashed $ S $ by 75% (elasticity = -2).  
- **Why it matters**: While the prior model revealed *non-linear vulnerability* to aggregate price shocks (e.g., Ed’s score dropping to 25%), this case shows how specific functional forms (e.g., complementarities in min utilities) can **insulate demand from moderate price variations**. This refines the policy insight:  
  > *Price shock impacts depend critically on preference structure—high elasticity in the prior model signaled severe welfare loss, whereas kinked utilities here imply resilience within slump segments.*  

#### **Core Takeaway for Continuity**  
The chart operationalizes the **"spend $ P_1 S $ minutes..."** principle from the prior section into a discrete goods context. It confirms that:  
1. Budget constraints dictate feasible sets (here: $ p_x x + p_y y = M $),  
2. MRS conditions pin optimal points (here: MRS = $ p_x / p_y $),  
but **does not replicate the prior model’s extreme elasticity**—highlighting how utility specifications determine the severity of demand responses. This bridges to the prior emphasis on "composite price effects" while underscoring functional form’s role in shaping policy outcomes.
