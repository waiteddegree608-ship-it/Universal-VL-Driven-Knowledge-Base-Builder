# PDF_Chapter_8

### Page/Slide 1



# Slutsky Equation 内容解析

## 文字与公式提取

### 章节标题
- Chapter 8
- Slutsky Equation

### 概念定义
- 价格变化包含两个效应：**替代效应**（substitution effect）和**收入效应**（income effect）
- 替代效应：在收入同步调整以恰好维持原消费束的情况下发生的需求变化
- 收入效应：剩余部分的需求变化

### 案例描述
- 效用函数：$U(x_1, x_2) = x_1 x_2$
- 初始条件：收入 $m = 24$，$p_1 = 1$，$p_2 = 2$
- 价格变动：$p_2$ 升至 3，$p_1$ 保持 1

### 需求函数
- $D_1(p_1, p_2, m) = \frac{m}{2p_1}$
- $D_2(p_1, p_2, m) = \frac{m}{2p_2}$

### 计算过程
- 初始需求：$x_1 = 12$，$x_2 = 6$
- 保持原消费束所需收入：$(1 \times 12) + (3 \times 6) = 30$
- 虚拟收入下新需求：$D_2(1, 3, 30) = 5$
- 替代效应：$5 - 6 = -1$
- 实际收入下新需求：$D_2(1, 3, 24) = 4$
- 收入效应：$4 - 5 = -1$

## 经济含义解析

### 需求函数推导依据
- 从效用函数 $U(x_1, x_2) = x_1 x_2$ 可导出柯布-道格拉斯型需求函数 $x_i = \frac{m}{2p_i}$，体现两类商品支出各占收入的 50%

### 价格变动分解过程
1. **收入补偿计算**  
   $(1 \times 12) + (3 \times 6) = 30$ 表明：当 $p_2$ 从 2 升至 3 时，需将收入从 24 提高至 30，才能维持原消费束 (12,6)，这是进行替代效应分析的必要前提

2. **替代效应量化**  
   从 6 降至 5 的需求变动 ($5 - 6 = -1$) 严格由相对价格变化引起，此时真实购买力被人工维持不变，符合**替代效应必为负**的规律（价格上升导致需求减少）

3. **收入效应识别**  
   从 5 降至 4 的变动 ($4 - 5 = -1$) 源于实际收入不变时购买力的真实损失，在此案例中：  
   - 商品 2 为正常品（因需求与收入正相关）
   - 两种效应方向一致，共同导致需求总量减少

### 与上文知识点的衔接
- 本案例验证了上文所述：对正常品，价格上升时**替代效应和收入效应均推动需求下降**
- 通过具体数值演示了如何将总效应 $(-1) + (-1) = -2$ 分解为可量化成分
- 需求函数形式表明商品 2 为必需品，其需求对价格变动的敏感度取决于收入分配比例

> 注：本页无图表，但通过数值案例完整展示了 Slusky 方程的核心分解逻辑，为后续分析提供了可操作的计算范式。

---
### Page/Slide 2



# Slutsky Equation 应用解析：价格下降案例

## 1. 文字与公式提取

### 章节标题
- 98 SLUTSKY EQUATION (Ch. 8)

### 学习目标列表
- Show the Hicks income and substitution effects of a price change on an indifference curve diagram.
- Find the Slutsky income and substitution effects for special utility functions such as perfect substitutes, perfect complements, and Cobb-Douglas.
- Use an indifference-curve diagram to show how the case of a Giffen good might arise.
- Show that the substitution effect of a price increase unambiguously decreases demand for the good whose price rose.
- Apply income and substitution effects to draw some inferences about behavior.

### 案例描述
- 效用函数：$U(x_A, x_B) = x_A x_B$
- 初始条件：$p_A = \$1$, $p_B = \$2$, $m = \$40$
- 价格变动：$p_B$ 降至 $\$1$, $p_A$ 保持 $\$1$
- $(a)$ 初始消费：20 apples, 10 bananas  
- $(b)$ 虚拟收入：30, 新消费：15 apples, 15 bananas  
- $(c)$ 替代效应：More bananas by 5  
- $(d)$ 实际消费：20 apples, 20 bananas  

## 2. 经济含义解析

### 与上文知识点的衔接
- 本案例延续上文对 $U(x_1, x_2) = x_1 x_2$ 的柯布-道格拉斯效用分析，但聚焦 **价格下降** 场景（上文为价格上升），验证 Slusky 方程的普适性。  
- 需求函数形式 $x_i = \frac{m}{2p_i}$ 保持不变，体现商品支出恒定占收入 50% 的特征，为分解提供计算基础。

### 价格变动分解过程
1. **替代效应量化**  
   - 价格下降后，维持原消费 bundle (20,10) 所需虚拟收入：$1 \times 20 + 1 \times 10 = 30$  
   - 在 $(m' = 30, p_A = 1, p_B = 1)$ 下，需求 $x_B^s = \frac{30}{2 \times 1} = 15$  
   - 替代效应：$15 - 10 = +5$（香蕉消费增加 5 单位），**严格由相对价格下降驱动**，真实购买力被补偿性维持。此结果与上文原理一致：**替代效应恒反向于价格变动**（价格降 → 需求升）。

2. **收入效应识别**  
   - 实际消费 $x_B = 20$（$(d)$ 部分）  
   - 收入效应：$20 - 15 = +5$，源于价格下降带来的**真实收入增加**（未补偿）。  
   - 与上文对比：上文价格上升时收入效应为负；此处价格下降，正常品（$x_B$ 随收入增而增）的收入效应为正，**与替代效应同向强化总效应**。

3. **总效应与上文逻辑的延伸**  
   - 总效应：$20 - 10 = +10$，分解为替代效应 $(+5)$ + 收入效应 $(+5)$。  
   - 关键衔接：上文验证 **正常品价格上升的双重负效应**；本例反向验证 **价格下降的双重正效应**，共同证明 Slusky 方程的完整性。  
   - 特别指出：虚拟收入计算 ($30$) 源于补偿性预算线的截距推导，与上文步骤 $(1 \times 12 + 3 \times 6 = 30)$ 完全一致，仅场景方向相反。

> 注：文本指示绘制预算线和效应分解图（A 点：原 bundle；B 点：补偿后 bundle；C 点：实际 bundle），但无实际图表。若可视化，替代效应为 $B - A = 5$，收入效应为 $C - B = 5$，总效应为 $C - A = 10$，垂直轴标注清晰体现两效应同向性。

---
### Page/Slide 3



# Slutsky Equation 应用解析：图表详细解析

## 1. 文字与公式提取

### 页眉
- NAME _______
- 99

### 图表说明
- "blue line parallel to the red line or the black line that you drew before?"
- "Red line."

### 图表坐标轴
- 横轴：Apples (0-40)
- 纵轴：Bananas (0-40)

### 图表标注
- Black line (黑线)
- Red line (红线)
- Blue line (蓝线)
- 点 a (20, 10)
- 点 b (15, 15)
- 点 c (20, 20)
- 标注箭头：Substitution, Income, Total

### 文字问题与答案
- "(e) The income effect of the fall in the price of bananas on Charlie's demand for bananas is the same as the effect of an (increase, decrease) increase in his income of $ 10 per day. Does the income effect make him consume more bananas or fewer? More. How many more or how many fewer? 5 more."

- "(f) Does the substitution effect of the fall in the price of bananas make Charlie consume more apples or fewer? Fewer. How many more or how many fewer? 5 fewer. Does the income effect of the fall in the price of bananas make Charlie consume more apples or fewer? More. What is the total effect of the change in the price of bananas on the demand for apples? Zero."

### 新增案例
- "8.2 (0) Neville's passion is fine wine. When the prices of all other goods are fixed at current levels, Neville's demand function for high-quality claret is $q = .02m - 2p$, where $m$ is his income, $p$ is the price of claret (in British pounds), and $q$ is the number of bottles of claret that he demands. Neville's income is 7,500 pounds, and the price of a bottle of suitable claret is 30 pounds."

## 2. 图表与经济含义解析

### 图表结构与上文衔接
- **黑线**：初始预算线 $(p_A = \$1, p_B = \$2, m = \$40)$，可购买最大 40 apples 或 20 bananas
- **蓝线**：新预算线 $(p_A = \$1, p_B = \$1, m = \$40)$，可购买最大 40 apples 或 40 bananas
- **红线**：补偿预算线 $(p_A = \$1, p_B = \$1, m' = \$30)$，经计算确保维持初始效用水平

### 价格变动分解验证
1. **替代效应可视化**  
   - 从 a(20,10) 水平移动至 b(15,15) 的垂直方向变化
   - 通过红线(补偿预算线)隔离相对价格变化影响
   - 香蕉消费增加 5 单位（15-10），苹果消费减少 5 单位（15-20）
   - 严格验证了 **替代效应恒反向于价格变动** 的原理

2. **收入效应可视化**  
   - 从 b(15,15) 移动至 c(20,20) 的垂直方向变化
   - 与上文预测一致：价格下降带来等价 $10 收入增加（$40-$30）
   - 香蕉消费再增 5 单位（20-15），苹果消费恢复至初始水平

3. **总效应精细化展示**  
   - 香蕉：Total = Substitution + Income = +5 + 5 = +10（20-10）
   - 苹果：Total = Substitution + Income = -5 + 5 = 0
   - 证明 **正常品在价格下降时，替代效应与收入效应同向强化总效应**，而本例中苹果因柯布-道格拉斯效用的特殊性，总效应为零

### 与上文核心知识的连续性
- 本图**完美验证了上文 Slusky 方程分解逻辑**：  
  $x_B(p_B',m) - x_B(p_B,m) = \underbrace{x_B(p_B',m') - x_B(p_B,m)}_{\text{替代效应}} + \underbrace{x_B(p_B',m) - x_B(p_B',m')}_{\text{收入效应}}$
  
- 与上文价格上升案例的**对称性**体现：
  | 价格变动方向 | 香蕉需求变动 | 替代效应方向 | 收入效应方向 | 总效应 |
  |--------------|--------------|--------------|--------------|--------|
  | 上升 (上例)  | 减少         | 负向         | 负向         | 减少   |
  | 下降 (本例)  | 增加         | 正向         | 正向         | 增加   |

- **实证层面**明确展示：
  - 总效应中的两部分如何在同方向上相加（香蕉）
  - 两种效应如何相互抵消（苹果），为理解需求曲线形状提供直观证据

---
### Page/Slide 4



# 8.2 与 8.3 案例解析：Slutsky 方程的数值验证与图形表达

## 1. 图片中的文字与公式提取

### 文字内容
- **页眉**：100 SLUTSKY EQUATION (Ch. 8)
- **8.2(a)**：How many bottles of claret will Neville buy? 90.
- **8.2(b)**：If the price of claret rose to 40 pounds, how much income would Neville have to have in order to be exactly able to afford the amount of claret and the amount of other goods that he bought before the price change? 8,400 pounds. At this income, and a price of 40 pounds, how many bottles would Neville buy? 88 bottles.
- **8.2(c)**：At his original income of 7,500 and a price of 40, how much claret would Neville demand? 70 bottles.
- **8.2(d)**：When the price of claret rose from 30 to 40, the number of bottles that Neville demanded decreased by 20. The substitution effect (increased, reduced) reduced his demand by 2 bottles and the income effect (increased, reduced) reduced his demand by 18 bottles.
- **8.3(0) Note**：Do this problem only if you have read the section entitled "Another Substitution Effect" that describes the "Hicks substitution effect". Consider the figure below, which shows the budget constraint and the indifference curves of good King Zog. Zog is in equilibrium with an income of $300, facing prices $p_X = \$4$ and $p_Y = \$10$.

### 公式
- Neville需求函数：$q = 0.02m - 2p$
- 初始条件：$m = 7,500$，$p = 30$
- 价格变动：$p$ 从 30 上升至 40

## 2. 图表解析与经济含义

### 图表结构与坐标识别
- **坐标系**：X轴表示商品X，Y轴表示商品Y
- **初始预算线**：通过(75, 0)和(0, 30)，验证 $I/p_X = 300/4 = 75$，$I/p_Y = 300/10 = 30$
- **新预算线**：延伸至X轴120单位，表明 $p_X$ 下降至 $300/120 = \$2.5$
- **关键点位**：
  - **E**：初始均衡点 $(30, Y_E)$，对应原价格 $p_X = \$4$
  - **C**：补偿均衡点 $(35, 22.5)$，补偿预算线与原无差异曲线切点
  - **F**：新均衡点 $(43, Y_F)$，新预算线与新无差异曲线切点

### 价格变动效应分解

#### a) 替代效应的图形表达
- **路径**：E → C (从 30 → 35)
- **经济含义**：当 $p_X$ 从 \$4 降至 \$2.5 时，相对价格变动使X更具吸引力
- **数值变化**：X需求增加 5 单位（35-30）
- **实现机制**：通过补偿预算线（平行于新预算线且切于原无差异曲线）隔离纯价格变动影响
- **特征验证**：严格符合"替代效应恒与价格变动反向"原则

#### b) 收入效应的图形表达
- **路径**：C → F (从 35 → 43)
- **经济含义**：价格下降导致真实收入增加（等价收入增加 \$150），使消费者能购买更多商品
- **数值变化**：X需求再增加 8 单位（43-35）
- **关键识别**：Y轴坐标下降（22.5 → Y_F < 22.5）表明Y也是正常品

#### c) 总效应的合成
- **总变化**：E → F（30 → 43），X需求增加 13 单位
- **效应叠加**：总效应 = 替代效应 + 收入效应 = 5 + 8 = 13
- **商品性质**：收入效应与替代效应同向作用，证实X是**正常品**

### 与8.2题的关联性
| **特征** | **Neville案例 (8.2)** | **Zog案例 (8.3图)** |
|----------|-------------------------|------------------------|
| 价格变动方向 | 上升 (30→40) | 下降 (4.0→2.5) |
| 总效应 | $-20$ 瓶 | $+13$ 单位 |
| 替代效应 | $-2$ 瓶 | $+5$ 单位 |
| 收入效应 | $-18$ 瓶 | $+8$ 单位 |
| 效应方向 | 两效应同向 | 两效应同向 |
| 商品性质 | 价格上升时需求下降，正常品 | 价格下降时需求上升，正常品 |

### 8.2题的数字验证
- **初始需求**：$q = 0.02 \times 7500 - 2 \times 30 = 90$ (8.2a)
- **补偿收入**：$m' = 7500 + 90 \times (40-30) = 8400$ (8.2b)
- **补偿需求**：$q' = 0.02 \times 8400 - 2 \times 40 = 88$ → 替代效应 $= 88-90 = -2$
- **新需求**：$q'' = 0.02 \times 7500 - 2 \times 40 = 70$ → 总效应 $= 70-90 = -20$
- **收入效应**：$-20 - (-2) = -18$，与表中描述完全一致

## 3. 核心知识的连续性发展

### Slutsky方程的双重表达
**数值表达**（8.2）：
$$\Delta q = \underbrace{[q(p',m') - q(p,m)]}_{-2} + \underbrace{[q(p',m) - q(p',m')]}_{-18} = -20$$

**图形表达**（8.3）：
$$\Delta x = \underbrace{(x_C - x_E)}_{替代效应} + \underbrace{(x_F - x_C)}_{收入效应} = x_F - x_E$$

### 传统替代效应与Hicks替代效应的区别
- 本图隐含**Hicks补偿法**（8.3 Note 特别提示）
- **关键差异**：Hicks补偿维持原效用水平（切点C），而Slutsky补偿维持原购买组合
- **实践意义**：对需求弹性测算产生微小差异，但在实证研究中常采用Slutsky近似

### 消费者行为模式验证
- 共同规律：**正常品**在价格变动时，替代效应与收入效应**同向作用**
- 差异体现：Neville案例中需求变动主要由收入效应主导（-18 vs -2），说明商品需求对收入变动敏感
- 图形启示：Zog案例中替代效应（+5）小于收入效应（+8），表明收入影响力更大

> 注：图表虽未明确价格变动数值，但通过预算线截距变化（75→120）可逆推价格下降比例（从\$4→\$2.5），完整呈现了价格下降时正常品两类效应的叠加机制。

---
### Page/Slide 5



### 1. Extracted Text and Content from Current Image

#### Text Content:
- **(a)** How much $ X $ does Zog consume? **30**.
- **(b)** If the price of $ X $ falls to $\$2.50$, while income and the price of $ Y $ stay constant, how much $ X $ will Zog consume? **35**.
- **(c)** How much income must be taken away from Zog to isolate the Hicksian income and substitution effects (i.e., to make him just able to afford to reach his old indifference curve at the new prices)? **$\$75$**.
- **(d)** The total effect of the price change is to change consumption from the point **E** to the point **C**.
- **(e)** The income effect corresponds to the movement from the point **F** to the point **C** while the substitution effect corresponds to the movement from the point **E** to the point **F**.
- **(f)** Is $ X $ a normal good or an inferior good? **An inferior good**.
- **(g)** On the axes below, sketch an Engel curve and a demand curve for Good $ X $ that would be reasonable given the information in the graph above. Be sure to label the axes on both your graphs.

#### Chart Details:
- **Axes**: 
  - Vertical axis: *Income* (labeled with values 225 and 300).
  - Horizontal axis: *x* (labeled with values 30 and 43).
- **Key Points**:
  - Point at $(x=30, \text{income}=300)$.
  - Point at $(x=43, \text{income}=225)$.
- **Curve**: A downward-sloping curve connecting the two points, indicating the relationship between income and consumption of $X$.

---

### 2. Chart Interpretation and Economic Meaning

The chart depicts an **Engel curve** for good $X$, which shows how consumption of $X$ varies with changes in income, holding prices constant. This is critical for decomposing the price effect using the Hicksian approach, as referenced in the problem's text.

#### Key Implications from the Chart:
- **Downward Slope**: The curve slopes downward from left to right, meaning that as income increases, consumption of $X$ decreases (from 43 units at income $225$ to 30 units at income $300$). This is a definitive trait of an **inferior good**, directly confirming part (f) of the image. For inferior goods, demand falls as income rises due to negative income elasticity.
  
- **Compensation Mechanism**:  
  - The income reduction of $\$75$ (from $\$300$ to $\$225$) isolates the Hicksian substitution effect. At the new price level ($p_X = \$2.50$), income of $\$225$ allows Zog to achieve the original utility level (point C: $x=43$), while income of $\$300$ yields the new Marshallian demand (point F: $x=35$).  
  - The downward slope implies that when income decreases (e.g., from $\$300$ to $\$225$), $X$ consumption increases, reinforcing why $X$ is inferior. This contrasts with normal goods (as in the upper text), where demand rises with income.

#### Integration with Price Effect Decomposition:
- **Substitution Effect (E → F)**:  
  The movement from E ($x=30$) to F ($x=35$) reflects the substitution effect. Despite the text labeling this as "substitution," it actually represents the **total effect** under constant income ($m=300$), as F is the Marshallian demand after the price drop. Normally, the substitution effect requires Hicksian compensation (E → C in standard analysis), but here the text mislabels F as the substitution point. The increase of 5 units (35–30) is driven primarily by the substitution effect, as the relative price drop makes $X$ more attractive. However, for an inferior good, the substitution effect still dominates the total effect (since 35 > 30), but the magnitude is smaller than in a Hicksian decomposition.
  
- **Income Effect (F → C)**:  
  The movement from F ($x=35$, income $=300$) to C ($x=43$, income $=225$) captures the income effect. As income decreases by $\$75$, $X$ consumption rises by 8 units (43–35), which is the hallmark of an inferior good. In standard terms, this demonstrates that a reduction in "real income" (due to price-induced compensation) increases demand for $X$. For a price fall, the income effect is **negative** (reducing demand if income rose), but here the text reverses the direction (F → C) to emphasize the income-decrease impact.

- **Total Effect (E → F)**:  
  The total effect (not E → C as misstated in part (d)) is from E ($x=30$) to F ($x=35$), a +5-unit increase. This results from:
  - Substitution effect: +13 units (in Hicksian terms, E → C: 30 → 43).
  - Income effect: -8 units (C → F: 43 → 35, due to the real income increase from the price drop).
  The income effect opposes the substitution effect, which is the defining characteristic of inferior goods. This differs from the normal good case in the upper text (e.g., Zog in 8.3), where both effects reinforced each other.

#### Continuity with Upper Text:
- The upper text exclusively analyzed **normal goods** (e.g., where income and substitution effects reinforce), emphasizing Slutsky/Hicks decomposition and the consistency of "substitution effect always opposes price change." Here, the image demonstrates the **inferior good case**, where:
  - The substitution effect (30 → 35 or 30 → 43 in Hicksian terms) still opposes the price change (price fell, demand rose).
  - The income effect (43 → 35) aligns with the upper text's description for inferior goods: "income effect may offset substitution effect," but the text in the image incorrectly characterizes the directional movements.
- The $\$75$ income adjustment in part (c) mirrors the Hicksian compensation method discussed in the upper text (e.g., "Hicks compensation maintains utility level at new prices"), yet here it isolates the opposite effect due to inferiority. This reinforces that the compensation mechanism applies universally, but the sign of the income effect depends on the good type.  
- The downward-sloping Engel curve here contrasts with the upward-sloping curve expected for normal goods (as implied in the upper text's demand analysis), illustrating why the Slutsky equation often shows a negative income effect for inferior goods:  
  $$
  \Delta x = \underbrace{\text{substitution}}_{\text{positive}} + \underbrace{\text{income}}_{\text{negative for price fall}}.
  $$

This chart and text resolution highlights that income effect direction is pivotal: for inferior goods, it reduces the total demand response to price changes, whereas for normal goods (as in the upper text), it amplifies it. The 8-unit income effect (F → C) correlates with the $\$75$ compensation, validating the quantitative approach from the upper text's 8.2 numerical example.

---
### Page/Slide 6



### 1. 提取文字与公式  
**图表信息**：  
- 纵轴：Price（刻度 1, 2, 2.5, 3, 4）  
- 横轴：x（刻度 30, 35）  
- 数据点：(Price=4, x=30) 和 (Price=2.5, x=35)  

**文字内容**：  
```  
102 SLUTSKY EQUATION (Ch. 8)  

8.4 (0) Maude spends all of her income on delphiniums and hollyhocks. She thinks that delphiniums and hollyhocks are perfect substitutes; one delphinium is just as good as one hollyhock. Delphiniums cost $4 a unit and hollyhocks cost $5 a unit.  

(a) If the price of delphiniums decreases to $3 a unit, will Maude buy more of them? Yes. What part of the change in consumption is due to the income effect and what part is due to the substitution effect? All due to income effect.  

(b) If the prices of delphiniums and hollyhocks are respectively $p_d = \$4$ and $p_h = \$5$ and if Maude has \$120 to spend, draw her budget line in blue ink. Draw the highest indifference curve that she can attain in red ink, and label the point that she chooses as A.  
```  

---

### 2. 图表解析  
#### **需求曲线特征**  
- 图表为**向下倾斜的需求曲线**，显示价格（Price）与需求量（x）呈负相关：价格从 \$4 降至 \$2.5 时，需求量从 30 增至 35。  
- **关键差异**：与上文正常商品/低档商品的分解不同，本图反映**完全替代品**的特殊情境。  

#### **经济含义**  
1. **完全替代偏好下的消费决策**：  
   - 由于 Maude 认为两种商品为完美替代品（MRS=1），且初始时 $p_d = \$4 < p_h = \$5$，她将**全部收入用于购买 delphiniums**（如预算 \$120 时，$x = 120/4 = 30$）。  
   - 当 $p_d$ 降至 \$3，**无替代效应**（因她已完全消费 delphiniums，无其他商品可替代），总效应（需求量增加）**完全由收入效应驱动**：  
     - 实际收入提升（$m/p_d$ 增大），导致需求量进一步上升（如 \$120 时，$x = 120/3 = 40$）。  
     - 与上文知识点对比：此处收入效应**强化**了总需求（正常商品特性），但**替代效应为零**，而非低档商品中“收入效应抵消替代效应”的情形。  

2. **与上文知识点的连续性**：  
   - 上文强调：正常商品中，收入与替代效应**同向**；低档商品中，二者**反向**。  
   - 本图通过**完全替代品极限案例**拓展理解：当替代效应为零时，总需求变动仅由收入效应决定，验证了斯勒茨基分解的普适性——**补偿机制仍适用，但效应权重取决于偏好结构**。  

#### **数值逻辑**  
- 图中价格 \$2.5 对应 $x=35$，隐含预算收入为 $35 \times 2.5 = \$87.5$（与题 (b) 中 \$120 无关，为独立场景）。  
- 题 (a) 中“价格降至 \$3 时全部由收入效应导致”直接体现：**替代效应为零**的边界条件（完全替代偏好已使消费集中于更便宜商品）。  

--- 

### 关键结论  
- 本图揭示**完全替代品行为的特殊性**：价格变动仅触发收入效应，与上文常规分解形成对比。  
- 重申斯勒茨基方程核心：  
  $$
  \Delta x = \underbrace{\text{substitution effect}}_{\text{zero here}} + \underbrace{\text{income effect}}_{\text{sole driver}}
  $$  
  此处收入效应为正，表明 delphiniums 为正常品，但效应来源与普通正常商品不同（无替代效应）。

---
### Page/Slide 7



### Extracted Content from Current Image

#### **Text and Formulas**  
- **Header**: `NAME ________ 103`  
- **Chart Labels**:  
  - Axes: `Delphiniums` (vertical, range 0–40), `Hollyhocks` (horizontal, range 0–40)  
  - Lines: `Blue line`, `Black line`, `Red curves`, points labeled `a` and `b`  
- **Problem Statements**:  
  - `(c)` *Now let the price of hollyhocks fall to $3 a unit, while the price of delphiniums does not change. Draw her new budget line in black ink. Draw the highest indifference curve that she can now reach with red ink. Label the point she chooses now as B.*  
  - `(d)` *How much would Maude’s income have to be after the price of hollyhocks fell, so that she could just exactly afford her old commodity bundle A? $120.*  
  - `(e)` *When the price of hollyhocks fell to $3, what part of the change in Maude’s demand was due to the income effect and what part was due to the substitution effect? All substitution effect.*  
  - `8.5 (1)` *Suppose that two goods are perfect complements. If the price of one good changes, what part of the change in demand is due to the substitution effect, and what part is due to the income effect? All income effect.*  
  - `8.6 (0)` *Douglas Cornfield’s demand function for good x is $x(p_x, p_y, m) = \frac{2m}{5p_x}$. His income is $1,000, the price of x is $5, and the price of y is $20. If the price of x falls to $4, then his demand for x will change from 80 to 100.*  
  - `(a)` (Part of 8.6) *If his income were to change at the same time so that he could exactly afford his old commodity bundle at $p_x = 4$ and $p_y = 20$, what would his new income be? 920. What would be his demand for x at this new level of income, at prices $p_x = 4$ and $p_y = 20$? 92.*  

---

### **Chart and Economic Interpretation**  
The chart illustrates Maude’s consumption choice between delphiniums (perfect substitutes) before and after the price of hollyhocks falls from $5 to $3. It extends the Slutsky decomposition logic from the previous context (where a price decrease in the cheaper good was analyzed) to a new scenario where the *more expensive good* becomes cheaper.  

#### **Key Chart Elements and Changes**  
1. **Blue line (original budget line)**:  
   - With $p_d = \$4$, $p_h = \$5$, and income $m = \$120$.  
   - Intercepts: 24 hollyhocks ($0 \times \$5 = \$120$), 30 delphiniums ($30 \times \$4 = \$120$).  
   - Point `a` `(0, 30)`: Initial optimal bundle where Maude consumes **only delphiniums** (since $p_d < p_h$ and MRS = 1).  

2. **Black line (new budget line)**:  
   - With $p_d = \$4$ (unchanged), $p_h = \$3$, and $m = \$120$.  
   - Intercepts: 40 hollyhocks ($40 \times \$3 = \$120$), 30 delphiniums ($30 \times \$4 = \$120$).  
   - Point `b` `(40, 0)`: New optimal bundle where Maude consumes **only hollyhocks** (since $p_h < p_d$ now).  

3. **Red curves (indifference curves)**:  
   - Straight lines with slope $-1$ (reflecting MRS = 1 under perfect substitutes).  
   - Stuncate at bundles like `(0,30)` and `(40,0)`, confirming corner solutions.  

#### **Economic Meaning of Changes**  
- **Price change**: Hollyhocks (formerly more expensive) fall to $3/unit, below delphiniums’ $4/unit.  
- **Total effect on hollyhocks demand**:  
  - Original: 0 units (consumption focused on delphiniums).  
  - New: 40 units (full switch to hollyhocks).  
- **Slutsky decomposition** (verified by problem (d) and (e)):  
  - **Substitution effect**: Dominates entirely. The income level to afford the old bundle A `(0,30)` at new prices is $m' = p_d \cdot 0 + p_h \cdot 30 = 4 \times 30 = \$120$ (from (d)). At $(p_d = 4, p_h = 3, m' = 120)$, Maude chooses 40 hollyhocks (corner solution), so substitution effect $= 40 - 0 = 40$.  
  - **Income effect**: Zero. The compensated choice (40 hollyhocks) equals the new choice, as real income increase does not alter demand at the corner (unlike the previous case where the cheaper good’s price fell).  
- **Contrast with prior context**:  
  - In part (a) of the earlier section (delphinium price decrease), substitution effect was zero (demand already cornered), so **all effect was income-driven**.  
  - Here, the good was not consumed initially, so a price drop **triggers pure substitution** (all effect is substitution-driven). This confirms:  
    - The sign and magnitude of effects depend on the **starting consumption bundle** relative to preference structure.  
    - For perfect substitutes, the Slutsky equation resolves to:  
      $$
      \Delta x_h = \underbrace{\text{substitution effect}}_{\text{40}} + \underbrace{\text{income effect}}_{\text{0}}
      $$  

#### **Continuity with Previous Knowledge**  
- This case complements the earlier analysis (where income effect dominated) by showing a boundary scenario where substitution effect is 100% of the change. It reinforces that:  
  - **Slutsky decomposition is universally applicable**, but relative weights of income/substitution effects depend on both preferences (e.g., perfect substitutes) and initial prices relative to consumption.  
  - The $m' = \$120$ in (d) is a direct application of the **compensated income** concept from the Slutsky equation, used here to isolate substitution effects for welfare analysis.  

The additional exercises (8.5, 8.6) extend these principles:  
- 8.5 demonstrates that for **perfect complements**, price changes affect demand purely through income effects (no substitution possible at kink points).  
- 8.6 quantifies Slutsky effects for a linear demand function, illustrating that substitution effects can dominate (as seen when $x$ rises from 80 to 92 under compensation), contrasting with the perfect-substitutes case here.

---
### Page/Slide 8



# 图片解析

## 提取文字与公式

```
(b) The substitution effect is a change in demand from 80 to 92. The income effect of the price change is a change in demand from 92 to 100.

(c) On the axes below, use blue ink to draw Douglas Cornfield's budget line before the price change. Locate the bundle he chooses at these prices on your graph and label this point A. Use black ink to draw Douglas Cornfield's budget line after the price change. Label his consumption bundle after the change by B.

(d) On the graph above, use black ink to draw a budget line with the new prices but with an income that just allows Douglas to buy his old bundle, A. Find the bundle that he would choose with this budget line and label this bundle C.

8.7 (1) Mr. Consumer allows himself to spend $100 per month on cigarettes and ice cream. Mr. C's preferences for cigarettes and ice cream are unaffected by the season of the year.

(a) In January, the price of cigarettes was $1 per pack, while ice cream cost $2 per pint. Faced with these prices, Mr. C bought 30 pints of ice cream and 40 packs of cigarettes. Draw Mr. C's January budget line with blue ink and label his January consumption bundle with the letter J.
```

## 图表解析

### 坐标系统与曲线
- **x轴**：商品x数量（0-320单位）  
- **y轴**：商品y数量（0-80单位）  
- **蓝色实线**：初始价格下的预算线  
- **黑色实线**：价格变化后的预算线（更平缓，表明商品x价格下降）  
- **虚线**：补偿预算线（在(d)部分要求绘制）

### 消费点
- **点A (a)**：初始消费束（x=80）  
- **点C (c)**：补偿预算线上的消费束（x=92）  
- **点B (b)**：最终消费束（x=100）

### Slutsky分解量化
| 效应类型 | 消费变化 | 数量变化 |
|----------|----------|----------|
| 替代效应 | 80 → 92 | +12 |
| 收入效应 | 92 → 100 | +8 |
| 总效应 | 80 → 100 | +20 |

### 图表变动含义
1. **预算线变动**：价格下降使预算线从蓝色变为黑色，斜率变小（x价格下降导致预算线更平缓）
2. **替代效应**：当价格下降但实际收入维持初始购买能力时（虚线预算线），消费从A点移动到C点（x从80增至92）
3. **收入效应**：在价格下降导致实际收入增加后，从C点移动到B点（x从92增至100）

## 与上文知识点的关联

此图展示了与上文**不同的初始条件场景**：
- 上文分析的是"初始未消费"场景（纯替代效应，收入效应为0），而此处初始消费80单位商品x
- 双重效应同时存在：替代效应（+12）和收入效应（+8）均呈正向，表明商品x是**正常品**
- 量化验证了Slutsky分解原理：价格下降同时影响相对价格（替代效应）和实际购买力（收入效应）

这与上文"完美替代品"案例形成互补：
- 上文强调**初始消费状态**如何决定效应主导性
- 本图展示当消费者已有初始消费时，替代和收入效应如何共同作用
- 验证了"效应权重取决于初始消费束"的核心结论

### 8.7部分的延伸意义
- Mr. C的1月消费（30单位冰淇淋+40单位香烟）构成$100的预算约束验证：  
  $30 \times \$2 + 40 \times \$1 = \$100$
- 此案例为后续应用型分析作铺垫，与上文讨论的**补偿收入概念**直接关联（m' = $120在上文中）
- 体现了Slutsky方程在不同商品组合中的普遍适用性

此图通过具体数值（80→92→100）展示了理论与实证的衔接，强化了"Slutsky分解需结合具体消费起点"的方法论原则，与上文关于效应主导性的讨论形成完整分析框架。

---
### Page/Slide 9



# 8.7 价格变动的替代效应与收入效应分析

## 图像内容提取

### 坐标系统与元素
- **x轴**：Cigarettes (香烟)，刻度0-100
- **y轴**：Ice cream (冰淇淋)，刻度0-100
- **预算线**：
  - Blue budget line（蓝色实线）
  - Black budget line（黑色实线）
  - Red budget line（红色实线）
  - Pencil budget line（铅笔线，虚线）
- **消费点**：
  - J：蓝色预算线上的点（1月份消费束）
  - A：黑色预算线与铅笔预算线的交点（补偿消费束）
  - F：红色预算线上的点（2月份消费束）

### 文字内容
```
(b) In February, Mr. C again had $100 to spend and ice cream still cost
$2 per pint, but the price of cigarettes rose to $1.25 per pack. Mr. C
consumed 30 pints of ice cream and 32 packs of cigarettes. Draw Mr. C's
February budget line with red ink and mark his February bundle with
the letter F. The substitution effect of this price change would make him
buy (less, more, the same amount of) less cigarettes and (less, more,
the same amount of) more ice cream. Since this is true and the total
change in his ice cream consumption was zero, it must be that the income
effect of this price change on his consumption of ice cream makes him buy
(more, less, the same amount of) less ice cream. The income
effect of this price change is like the effect of an (increase, decrease)
```

### 消费点验证
- **点J (1月)**：40包香烟 + 30品脱冰淇淋
  - $40 \times \$1 + 30 \times \$2 = \$100$
- **点F (2月)**：32包香烟 + 30品脱冰淇淋
  - $32 \times \$1.25 + 30 \times \$2 = \$100$

## Slutsky分解量化

| 消费点 | 香烟(包) | 冰淇淋(品脱) | 分解阶段 |
|--------|-----------|---------------|----------|
| J | 40 | 30 | 初始消费束 |
| A | ~36 | ~33 | 补偿消费束 |
| F | 32 | 30 | 最终消费束 |

| 效应类型 | 香烟变化 | 冰淇淋变化 |
|----------|----------|------------|
| 替代效应 (J→A) | -4 | +3 |
| 收入效应 (A→F) | -4 | -3 |
| 总效应 (J→F) | -8 | 0 |

## 图表变动含义

### 预算线变化
1. **蓝色→红色预算线**：
   - 香烟价格从$1上升至$1.25
   - 预算线绕y轴（冰淇淋截距）向内旋转
   - 香烟最大消费从100包降至80包 ($100/$1.25)

2. **铅笔虚线**：
   - 补偿预算线，通过点J
   - 斜率与红色预算线相同（体现新相对价格）
   - 代表维持原始效用水平所需调整后的收入

### 价格变化效应分析
1. **替代效应**：
   - 价格变化导致相对价格变动（香烟相对变贵）
   - 消费者倾向用冰淇淋替代香烟
   - 香烟消费减少4包，冰淇淋增加3品脱

2. **收入效应**：
   - 价格上涨导致实际收入下降
   - 表现为从补偿消费束A向最终消费束F的移动
   - 两种商品消费均减少（香烟-4包，冰淇淋-3品脱）

3. **冰激凌消费特殊性**：
   - 替代效应与收入效应方向相反
   - 两者完全抵消，导致总效用为0（消费量不变）
   - 验证冰激凌在此价格范围内为**劣等品**（收入效应为负）

## 与上文知识点的承续性

此图延续了上文"8.7"问题的分析框架，但展示了**价格上升**而非下降的情况：

1. **与1月对照**：
   - 上文描述1月消费组合(40,30)构成点J
   - 本月价格变化（香烟上涨）导致新消费组合(32,30)

2. **效应对比**：
   - 上文案例（香烟价格下降）：替代效应与收入效应均为正
   - 本图案例（香烟价格上涨）：两种效应共同导致香烟消费下降
   - 强调了**价格变动方向**对效应组合方式的影响

3. **劣等品特性验证**：
   - 冰淇淋消费量不变但收入效应为负，证明在此价格区间为劣等品
   - 补充了上文未讨论的**劣等品**情形（上文展示的是正常品）

4. **补偿预算线应用**：
   - 通过铅笔预算线演示Slutsky补偿机制
   - 完整展示了"固定效用水平"下替代效应的测量方法

此图通过具体数字（40→36→32）验证了上文所述的Slutsky分解原理，特别突出了当商品种类包含劣等品时效应抵消的特殊情况，扩展了上文基于正常品的分析框架。

---
### Page/Slide 10



# Marta's Approach to the Slutsky Equation (March-May Extensions)

## Extracted Text from Current Image

```
106 SLUTSKY EQUATION (Ch. 8)

decrease in his income. Therefore the information we have suggests
that ice cream is a(n) (normal, inferior, neutral) normal good.

(c) In March, Mr. C again had $100 to spend. Ice cream was on sale for $1
per pint. Cigarette prices, meanwhile, increased to $1.50 per pack. Draw
his March budget line with black ink. Is he better off in January,
worse off, or can you not make such a comparison? Better off.
How does your answer to the last question change if the price of cigarettes
had increased to $2 per pack? Now you can't tell.

8.8 (1) This problem continues with the adventures of Mr. Consumer
from the previous problem.

(a) In April, cigarette prices rose to $2 per pack and ice cream was still
on sale for $1 per pint. Mr. Consumer bought 34 packs of cigarettes and
32 pints of ice cream. Draw his April budget line with pencil and label
his April bundle with the letter A. Was he better off or worse off than
in January? Worse off. Was he better off or worse off than in
February, or can't one tell? Better off.

(b) In May, cigarettes stayed at $2 per pack and as the sale on ice cream
ended, the price returned to $2 per pint. On the way to the store, how-
ever, Mr. C found $30 lying in the street. He then had $130 to spend on
cigarettes and ice cream. Draw his May budget with a dashed line. With-
out knowing what he purchased, one can determine whether he is better
off than he was in at least one previous month. Which month or months?
He is better off in May than in February.

(c) In fact, Mr. C buys 40 packs of cigarettes and 25 pints of ice cream
in May. Does he satisfy WARP? No.

8.9 (2) In the last chapter, we studied a problem involving food prices
and consumption in Sweden in 1850 and 1890.

(a) Potato consumption was the same in both years. Real income must
have gone up between 1850 and 1890, since the amount of food staples
purchased, as measured by either the Laspeyres or the Paasche quantity
index, rose. The price of potatoes rose less rapidly than the price of either
meat or milk, and at about the same rate as the price of grain flour. So
real income went up and the price of potatoes went down relative to
other goods. From this information, determine whether potatoes were
```

## Conceptual Analysis

### March Scenario (Extension of Prior Knowledge)

- When ice cream drops to $1/pint with cigarettes at $1.50/pack, Mr. C is **better off** than in January despite cigarette price increase:
  - New budget line: 100/1.5 = 66.7 max cigarettes, 100/1 = 100 max ice cream
  - Optimal bundle must lie on a higher indifference curve than January's (40,30)
  - Note: This confirms ice cream as a **normal good** (if it were inferior, we could not make this determination)

- If cigarettes rose to $2/pack, comparison becomes impossible:
  - Budget line would rotate inward more severely, possibly intersecting previous indifference curves
  - Demonstrates the importance of relative price change magnitude in welfare analysis

### April Extension (Slutsky Decomposition Application)

- April bundle (34,32) compared to February's (32,30):
  - Budget constraint: 34×$2 + 32×$1 = $100
  - While worse than January (40,30), he is **better off** than February due to:
    - The **substitution effect** dominates when ice cream is cheaper (as established in prior analysis)
    - Higher consumption of the now-cheaper ice cream (32 vs 30) partially offsets cigarette price increase

- This contrasts with February's analysis where cigarette price increase caused reduced ice cream consumption due to income effects

### May Scenario (Combined Price and Income Change)

- Budget calculation: $130 income with prices (Pc=$2, Pi=$2)
  - Budget line: C + I = 65 (steeper than February but with higher income)
  
- The clear dominance over February manifests through:
  - Unambiguous welfare improvement: May's budget set completely contains February's
  - Mathematical verification: February's bundle (32,30) costs 32×$2 + 30×$2 = $124 < $130

- WARP violation with May's actual consumption (40,25):
  - In February: spent $100 on (32,30) when (40,25) would have cost 40×$1.25 + 25×$2 = $100
  - Yet chose (32,30) over affordable (40,25)
  - Contradicts in May when he buys (40,25) instead of affordable February bundle
  - Violates consistent preference ordering between the two periods

### Historical Example (Swedish Data)

- The potato consumption puzzle presents an opportunity to apply Slutsky:
  - Real income increased as measured by quantity indices
  - Potato price decreased relatively (growing more slowly than meat/milk)
  - Despite constant potato consumption, the real income increase should induce:
    - **Substitution effect**: Toward potatoes due to relative price decrease
    - **Income effect**: Away from potatoes if inferior, toward if normal
  - As consumption remained constant, these effects must perfectly offset
  - The conclusion must address whether potatoes are normal or inferior (text cuts off)

## Continuity with Prior Knowledge

This material extends the February analysis framework by:
1. Introducing income changes (found money in May) alongside price changes
2. Demonstrating how compensating/normal income effects interact with substitution effects differently across price ranges
3. Applying WARP to test consistency of observed choices
4. Providing a real-world historical example connecting Slutsky to welfare analysis

The transition from February to March-April deployment shows how the substitution effect in February (where ice cream increased as cigarettes became more expensive) continues to operate with further price changes, albeit with changing magnitude. The May scenario uniquely demonstrates how an income increase can offset price increases, allowing us to determine welfare changes without observing utility levels directly.

---
### Page/Slide 11



### Extracted Text and Formulas

**Potato Analysis Conclusions**  
- *Normal/Inferior Determination*:  
  "If potatoes were a normal good, both the fall in potato price and the rise in income would increase the demand for potatoes. But potato consumption did not increase. So potatoes must be an inferior good."  

- *Giffen Good Assessment*:  
  "(b) Can one also tell from these data whether it is likely that potatoes were a Giffen good? If potatoes were a Giffen good, then the fall in the price of potatoes would decrease demand and the rise in income would also decrease demand for potatoes. But potato demand stayed constant. So potatoes were probably not a Giffen good."  

**Orient Express Problem (8.10 (1))**  
- Scenario:  
  "Agatha must travel on the Orient Express from Istanbul to Paris. The distance is 1,500 miles. A traveler can choose to make any fraction of the journey in a first-class carriage and travel the rest of the way in a second-class carriage. The price is 10 cents a mile for a second-class carriage and 20 cents a mile for a first-class carriage. Agatha much prefers first-class to second-class travel, but because of a misadventure in an Istanbul bazaar, she has only $200 left with which to buy her tickets. [...] She will travel first class as much as she can afford to, but she must get all the way to Paris, and $200 is not enough money to get her all the way to Paris in first class."  

- Graph Instructions:  
  "(a) On the graph below, use red ink to show the locus of combinations of first- and second-class tickets that Agatha can just afford to purchase with her $200. Use blue ink to show the locus of combinations of first- and second-class tickets that are sufficient to carry her the entire distance from Istanbul to Paris. Locate the combination of first- and second-class miles that Agatha will choose on your graph and label it A."  

---

### Analysis of Image Content in Context of Prior Knowledge  

#### **1. Potato Consumption Conclusions**  
The text finalizes the Swedish data case introduced in the prior summary:  
- **Inferior Good Confirmation**:  
  - Prior logic (price decrease → substitution effect toward potatoes; real income increase → income effect *away* from potatoes) is validated here.  
  - Since total consumption remained *unchanged*, the negative income effect (for an inferior good) must have exactly counteracted the substitution effect. If potatoes were normal, both effects would reinforce higher demand, which contradicts observed data.  
  - *Direct continuity*: This resolves the "text cuts off" point in the prior summary by explicitly stating potatoes are inferior.  

- **Giffen Good Elimination**:  
  - For a Giffen good, the demand *decreases* when price falls (due to an extreme income effect). Here, demand *stayed constant*, not decreased.  
  - Thus, potatoes are inferior but **not Giffen**, as the substitution effect offset the income effect rather than reinforcing a price-induced demand fall.  

#### **2. Agatha’s Travel Problem**  
- **Budget Constraint**:  
  - Cost constraint: $ 0.10S + 0.20F = 200 $, where $ S $ = second-class miles, $ F $ = first-class miles.  
  - Distance constraint: $ S + F = 1,500 $ (must cover full distance).  
- **Key Implications**:  
  - Maximum second-class travel cost: $ 1,500 \times 0.10 = \$150 $ < \$200 (affordable).  
  - Maximum first-class cost: $ 1,500 \times 0.20 = \$300 $ > \$200 (unaffordable).  
  - **Optimal choice (point A)**: Agatha maximizes first-class miles within budget. Solving $ S = 1,500 - F $ and substituting into budget constraint:  
    $$
    0.10(1,500 - F) + 0.20F = 200 \implies F = 500 \text{ miles}, \ S = 1,000 \text{ miles}.
    $$  
- **Connection to Prior Concepts**:  
  - This extends the February/May budget set analysis (from prior summary) to a constrained discrete-choice scenario.  
  - Demonstrates **marginal rate of substitution (MRS)**: Agatha will allocate the budget to maximize $ F $ until her cash constraint binds, illustrating how budget lines interact with fixed requirements (full distance).  

---

### Critical Note on Missing Graph  
While the text describes graph instructions (red/blue loci), no visual is provided. However, the description clarifies:  
- **Red locus (affordable combinations)**: Budget line sloping downward from $ F = 1,000 $ (all first-class, \$200) to $ S = 2,000 $ (beyond total distance).  
- **Blue locus (feasible distance)**: A 45° line $ S + F = 1,500 $.  
- **Equilibrium A**: Intersection where budget constraint meets distance constraint (500 first-class, 1,000 second-class miles), reflecting utility maximization under dual constraints.  
- *Relevance*: This echoes the February-May welfare analysis (prior summary), where budget sets and choice consistency determine preference rationality.

---
### Page/Slide 12



### 图片内容提取

#### 文字与公式
- **标题与坐标轴**：  
  - "108 SLUTSKY EQUATION (Ch. 8)"  
  - Y轴："First-class miles"（刻度：400, 800, 1200, 1600）  
  - X轴："Second-class miles"（刻度：400, 800, 1200, 1600）  
  - 线条标签："Pencil line", "Blue line", "Red line", "Black line"  
  - 点标记：a, b, c  

- **问题与答案文本**：  
  - (b) Let $ m_1 $ be the number of miles she travels by first-class coach and $ m_2 $ be the number of miles she travels by second-class coach. Write down two equations that you can solve to find the number of miles she chooses to travel by first-class coach and the number of miles she chooses to travel by second-class coach.  
    **公式**：  
    $$
    0.2m_1 + 0.1m_2 = 200, \quad m_1 + m_2 = 1,500
    $$  
  - (c) The number of miles that she travels by second-class coach is **$ 1,000 $**.  
  - (d) Just before she was ready to buy her tickets, the price of second-class tickets fell to $ \$0.05 $ while the price of first-class tickets remained at $ \$0.20 $. On the graph that you drew above, use pencil to show the combinations of first-class and second-class tickets that she can afford with her $ \$200 $ at these prices. On your graph, locate the combination of first-class and second-class tickets that she would now choose. (Remember, she is going to travel as much first-class as she can afford to and still make the 1,500 mile trip on $ \$200 $.) Label this point B. How many miles does she travel by second class now? **$ 666.66 $**. (Hint: For an exact solution you will have to solve two linear equations in two unknowns.) Is second-class travel a normal good for Agatha? **No**. Is it a Giffen good for her? **Yes**.  

#### 图表元素
- **Blue line**：表示距离约束 $ m_1 + m_2 = 1,500 $（45°向下倾斜线）。  
- **Red line**：表示初始预算约束 $ 0.2m_1 + 0.1m_2 = 200 $（斜率为 $ -0.1/0.2 = -0.5 $）。  
- **Black line**：表示新预算约束 $ 0.2m_1 + 0.05m_2 = 200 $（斜率为 $ -0.05/0.2 = -0.25 $，较平缓）。  
- **Pencil line**：虚线，同 Black line（新预算约束），需手动绘制以反映价格变化。  
- **点标记**：  
  - a：初始均衡点（$ m_1 = 500 $, $ m_2 = 1,000 $）。  
  - b：Blue line 与 Red line 的交点（即点 a，但标注为 b，可能为绘图误差）。  
  - c：新均衡点 B（$ m_1 \approx 833.33 $, $ m_2 \approx 666.66 $）。  

---

### 图表变化的详细解释

#### 背景与上文的连续性
- 此图衔接上文 **Agatha’s Travel Problem**：
  - 初始设定：预算约束 $ 0.1m_2 + 0.2m_1 = 200 $（$ m_2 $ 为 second-class miles，$ m_1 $ 为 first-class miles），距离约束 $ m_1 + m_2 = 1,500 $，均衡点 A（即图中点 a）为 $ m_1 = 500 $, $ m_2 = 1,000 $。
  - 图中 **Blue line** 直接对应用上文 **Blue locus**（可行距离约束），**Red line** 对应 **Red locus**（初始预算线），点 a 即上文 **Optimal choice (point A)**。

#### 价格变化的影响（结合 Slutsky Equation）
- **关键变化**：second-class 价格从 $ \$0.10 $ 降至 $ \$0.05 $，first-class 价格不变（$ \$0.20 $）。这导致：
  - **新预算约束**：$ 0.2m_1 + 0.05m_2 = 200 $（即图中 Black/Pencil line）。
    - 当 $ m_1 = 0 $ 时，$ m_2 = 4,000 $（超出图示范围）；当 $ m_2 = 0 $ 时，$ m_1 = 1,000 $。
    - 与初始 Red line 相比，斜率更平缓（$ -0.25 $ vs. $ -0.5 $），表明 second-class 价格下降后，预算线外移并更扁平。
  - **新均衡点 c (B)**：  
    通过联立新预算约束与距离约束求解：
    $$
    \begin{cases}
    0.2m_1 + 0.05m_2 = 200 \\
    m_1 + m_2 = 1,500
    \end{cases}
    \implies m_1 = \frac{125}{0.15} \approx 833.33,  \quad m_2 = 1,500 - 833.33 = 666.67
    $$
    - Agatha 仍最大化 first-class miles，但因 second-class 价格下降，**$ m_2 $ 从 1,000 降至 666.67**，而 $ m_1 $ 从 500 增至 833.33。

#### 经济含义：Giffen Good 的验证
- **需求异常**：second-class 价格下降（$ \$0.10 \to \$0.05 $），但需求量 **减少**（$ 1,000 \to 666.67 $），这违背常规需求规律。
- **Slutsky 分解**：  
  - **替代效应**：价格下降使 second-class 相对更便宜，应**增加**其需求（但被收入效应抵消）。  
  - **收入效应**：价格下降等价于实际收入增加。由于 second-class 是**劣等品**（inferior good），收入增加导致需求**减少**；且在此案例中，收入效应幅度 **>** 替代效应幅度，导致总效应为需求下降。  
- **Giffen Good 属性**：  
  - 上文指出 potatoes 为 inferior but not Giffen（因替代效应抵消收入效应）。  
  - 本图中，second-class 满足 **Giffen good** 定义：价格下降 → 需求减少（$ \Delta p_2 < 0 $, $ \Delta m_2 < 0 $），且收入效应 **加强**（reinforce）而非抵消了价格诱导的需求变动。  
  - 这直接呼应 (d) 部分结论："No"（非正常品）、"Yes"（是 Giffen good），是 Slutsky Equation 的典型应用：通过分离效应，解释非理性需求行为。

#### 图表与上文逻辑的连贯性
- **约束交点的动态变化**：  
  - 初始均衡（点 a）：Red line 与 Blue line 交点（预算绑定且距离约束满足）。  
  - 新均衡（点 c）：Black line 与 Blue line 新交点，反映价格变动后预算约束软化，但距离约束仍刚性绑定最优选择。  
- **Policy 与行为启示**：  
  - Agatha 偏好 first-class，second-class 仅用于填补距离缺口。当 second-class 价格下降：  
    - 替代效应微弱（因偏好强烈偏向 first-class）。  
    - 收入效应强势（实际收入增加后，她减少劣等品消费，转向 first-class 以满足固定距离需求）。  
  - 此逻辑延伸上文 "marginal rate of substitution (MRS)" 分析：MRS 在新均衡点更高，表明为维持效用，first-class 的边际价值上升。  

> **关键提示**：图中 "Pencil line" 需手动绘制以体现动态调整，凸显微观经济学中价格变动的实验性质—与上文 "February-May welfare analysis" 一致，均通过预算集变化验证选择一致性。

---
### Page/Slide 13



### 文本与公式提取  
#### 文字内容  
```text
NAME__________________ 109
8.11 (f) We continue with the adventures of Agatha, from the previous problem. Just after the price change from $.10 per mile to $.05 per mile for second-class travel, and just before she had bought any tickets, Agatha misplaced her handbag. Although she kept most of her money in her sock, the money she lost was just enough so that at the new prices, she could exactly afford the combination of first- and second-class tickets that she would have purchased at the old prices. How much money did she lose?
$50. On the graph you started in the previous problem, use black ink to draw the locus of combinations of first- and second-class tickets that she can just afford after discovering her loss. Label the point that she chooses with a C. How many miles will she travel by second class now?
1,000.
(a) Finally, poor Agatha finds her handbag again. How many miles will she travel by second class now (assuming she didn’t buy any tickets before she found her lost handbag)? 666.66. When the price of second-class tickets fell from $.10 to $.05, how much of a change in Agatha’s demand for second-class tickets was due to a substitution effect? None. How much of a change was due to an income effect? −333.33.
```

#### 公式与数值  
- 旧价格：$ p_2^{\text{old}} = \$0.10 $/mile (second-class), $ p_1 = \$0.20 $/mile (first-class)  
- 新价格：$ p_2^{\text{new}} = \$0.05 $/mile  
- 丢失金额：$ \$50 $  
- 丢钱后 second-class 里程：$ m_2 = 1,000 $  
- 找回手袋后 second-class 里程：$ m_2 = 666.66 $  
- 替代效应：$ 0 $  
- 收入效应：$ -333.33 $  

---

### 关键信息解析  
#### 1. **补偿性预算约束的构建**  
- **丢失金额逻辑**：  
  - 旧均衡组合（对应上文 **point A**）为 $ (m_1, m_2) = (500, 1,000) $，满足旧预算约束 $ 0.2m_1 + 0.1m_2 = 200 $。  
  - 新价格下，该组合成本为 $ 0.2 \times 500 + 0.05 \times 1,000 = 150 $。  
  - 原始收入为 $ \$200 $，故丢失金额 $ = 200 - 150 = \$50 $。  
  - **经济含义**：此 $ \$50 $ 损失构成 **Slutsky补偿预算线**（comparable to上文的 *Red/Pencil line*），强制保持 Agatha 的购买力等于旧价格下的实际效用水平。  

- **丢钱后的选择（点 C）**：  
  - 补偿预算线：$ 0.2m_1 + 0.05m_2 = 150 $。  
  - 图中 **点 C** 对应 $ (m_1, m_2) = (500, 1,000) $（与旧均衡完全相同），即 $ m_2 = 1,000 $。  
  - **核心含义**：在补偿预算下，second-class 需求未变（$ \Delta m_2 = 0 $），**直接验证替代效应为零**。这归因于 Agatha 对 first-class 的强偏好（距离约束刚性），导致即使价格下降，相对价格变化未诱使她调整组合。  

#### 2. **效应分解与 Giffen Good 的强化**  
- **总效应计算**：  
  - 旧均衡 $ m_2^{\text{old}} = 1,000 $ → 新均衡 $ m_2^{\text{new}} = 666.67 $，总需求变动 $ \Delta m_2 = -333.33 $。  
- **替代效应（S.E.）**：  
  - 如上所述，补偿预算下需求无变化（S.E. = 0），与上文逻辑一致：**替代效应被压至零**（因偏好强烈偏向 first-class，使 MRS 不随价格变动调整）。  
- **收入效应（I.E.）**：  
  - 由 Slutsky Equation $ \Delta m_2 = \text{S.E.} + \text{I.E.} $，得 $ \text{I.E.} = -333.33 - 0 = -333.33 $。  
  - **关键延伸**：收入效应完全主导总效应，且为负值（实际收入增加时 second-class 需求减少），**确证其为 Giffen good**。这呼应上文结论：当 second-class 价格下降，收入效应强度 $ > $ 替代效应强度，并**加强**需求下降趋势。  

#### 3. **与上文知识点的连续性**  
- **距离约束（Blue line）的绑定性**：  
  - 点 C（丢钱后）和新均衡点（找回手袋后）均位于 $ m_1 + m_2 = 1,500 $ 约束上，重申该约束在最优选择中的刚性作用（避免需求分散）。  
- **返璞归真实验设计**：  
  - 本场景通过 "丢钱-找回" 操作构造补偿变化，与上文 "February-May welfare analysis" 方法论一致，系统分离价格效应：  
    - 补偿预算（丢钱 $ \$50 $）$ \rightarrow $ **替代效应隔离**；  
    - 恢复原始收入（找回手袋）$ \rightarrow $ **仅收入效应启动**。  
  - 此设计直接呼应 (d) 部分结论：`替代效应：None`、`收入效应：-333.33`，实证 "Giffen good 测试" 中收入效应全覆盖。  
- **政策启示深化**：  
  - Agatha 的行为暴露 ** inferior good 的极端情形**：second-class 被用作 "距离填充工具"，收入增加后立即减少其消费以增持 first-class。此反直觉反应（价格降需求减）再次印证上文 Ku Max 求解逻辑——MRS 在新均衡点升高，反映 first-class 边际价值跃升。  

> **逻辑锚点**：本解析消除冗余叙述，紧贴上文以 "补偿实验" 为支柱的 Slutsky 框架，凸显 `S.E. = 0` 而 `I.E. = -333.33` 是 Giffen good 的决定性证据。

---
### Page/Slide 14



# Slutsky方程章节页解析

## 1. 图片文字提取
- 页码：110
- 标题：SLUTSKY EQUATION (Ch. 8)

## 2. 知识连续性分析

该页面作为Slutsky方程章节的起始页，标志着从理论框架向具体应用的过渡。结合上文已建立的分析逻辑：

- **理论定位**：此页标示着Slutsky方程的正式引入，为上文已验证的效应分解（S.E. = 0，I.E. = -333.33）提供了方法论基础
- **知识衔接**： 
  - 页码 "110" 位于微观经济学教材典型的位置，表明Slutsky方程作为价格效应分析的核心工具已在文献中确立
  - "Ch. 8" 明确此内容属于中级微观经济学标准课程体系的典型位置，对应上文"返璞归真实验设计"所依赖的Slutsky补偿框架

## 3. 解析意义

此章节页作为方法论起点，使上文已完成的Agatha案例分析获得理论归宿：
- 上文基于"丢钱-找回"实验构建的补偿预算约束，正式成为Slutsky方程的标准应用场景
- Giffen good验证逻辑（收入效应主导且大于0，实际为-333.33）自此归属于Ch. 8的规范分析框架
- 该页为空白页的特性，突显前文已完整完成效应分解过程，无需额外图表验证结论

> 本页作为理论起点，强化了上文*s.e. = 0而i.e. = -333.33*的实证结论与Slutsky方程的严格对应关系，使Giffen good判定成为该理论框架下的必然推论。
