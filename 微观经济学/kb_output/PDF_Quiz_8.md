# PDF_Quiz_8

### Page/Slide 1



# Quiz 8: Slutsky Equation 问题解析

## 1. 提取文字与公式

### 文字内容
- **标题**：Quiz 8、Slutsky Equation
- **问题 8.1**：Charlie 的效用函数基于 $x_A x_B$。苹果原价 \$1/单位，香蕉原价 \$2/单位，日收入 \$40。当苹果价格上涨至 \$1.25，香蕉价格降至 \$1.25 时，为负担原消费束，Charlie 每日需收入：  
  (a) \$37.50.  
  (b) \$76.  
  (c) \$18.75.  
  (d) \$56.25.  
  (e) \$150.  
- **问题 8.2**：同效用函数，苹果原价 \$1，香蕉原价 \$2，收入 \$40。苹果价格涨至 8（单位：美元），香蕉价格不变。替代效应对苹果消费的减少量为：  
  (a) 17.50 个苹果  
  (b) 7 个苹果  
  (c) 8.75 个苹果  
  (d) 13.75 个苹果  
  (e) 无正确选项  
- **问题 8.3**：Colin 的需求函数为 $q = .02m - 2p$（$m$ 为收入，$p$ 为价格），初始收入 \$6,000，初始价格 \$30/瓶，价格涨至 \$40。价格变化的替代效应：  
  (a) 需求减少 20  
  (b) 需求增加 20  

### 公式总结
| 问题 | 关键公式 |
|------|----------|
| 8.1 & 8.2 | 效用函数： $ U = x_A x_B $ |
| 8.3 | 需求函数： $ q = 0.02m - 2p $ |

---

## 2. 问题解析（基于 Slutsky 方程知识点）

### 问题 8.1：补偿收入计算
- **核心机制**：当价格变动后，Slutsky 补偿收入 $m'$ 满足 $m' = p'_A x_A^* + p'_B x_B^*$，确保**原消费束 $(x_A^*, x_B^*)$** 在新价格下仍可被负担。
- **关键逻辑**：  
  1. 原价格下最优消费束：由效用最大化解得 $x_A^* = 20$，$x_B^* = 10$（通过 $ \text{MRS} = p_A/p_B $ 与预算约束联立）。  
  2. 新价格 $p'_A = 1.25$、$p'_B = 1.25$ 下，所需补偿收入：  
     $$
     m' = (1.25 \times 20) + (1.25 \times 10) = 37.5
     $$
  3. **含义**：此计算直接体现 Slutsky 方程中**补偿变化**的定义——消除收入效应，仅隔离价格变动对消费的影响。

---

### 问题 8.2：替代效应量化
- **核心机制**：替代效应是**保持效用不变**（通过补偿收入），价格变动导致的消费变化，即 $ \Delta x_A^{\text{sub}} = x_A(p', m') - x_A(p, m) $。
- **关键逻辑**：  
  1. 原消费束 $x_A^* = 20$（同 8.1）。  
  2. 苹果价格从 $p_A = 1$ 涨至 $p'_A = 8$，香蕉价格 $p_B = 2$ 不变，需计算补偿收入 $m'$：  
     $$
     m' = (8 \times 20) + (2 \times 10) = 180
     $$
  3. 补偿收入下，新最优消费束满足：  
     $$
     x_A(p', m') = \frac{m'}{2p'_A} = \frac{180}{16} = 11.25 \quad \text{(由柯布-道格拉斯需求函数推导)}
     $$
  4. 替代效应：  
     $$
     \Delta x_A^{\text{sub}} = 11.25 - 20 = -8.75
     $$
  5. **含义**：替代效应为负（-8.75），体现价格上升与消费反向变动的基本规律，且全程不涉及真实收入变化。

---

### 问题 8.3：需求函数中的替代效应
- **核心机制**：对线性需求函数 $q = a m - b p$，替代效应需通过**补偿收入法**计算：先求补偿收入 $m' = m + q^* \Delta p$，再代入需求函数。
- **关键逻辑**：  
  1. 初始点：$m = 6000$, $p = 30$  
     $$
     q^* = 0.02 \times 6000 - 2 \times 30 = 60
     $$
  2. 价格变动：$\Delta p = 10$（从 30→40），补偿收入需满足：  
     $$
     \Delta m = q^* \Delta p = 60 \times 10 = 600 \implies m' = 6000 + 600 = 6600
     $$
  3. 补偿后在新价格下需求：  
     $$
     q' = 0.02 \times 6600 - 2 \times 40 = 52
     $$
  4. 替代效应：  
     $$
     \Delta q^{\text{sub}} = 52 - 60 = -8
     $$
  5. **选项矛盾**：计算结果为 **-8**（需求减少 8），但题目选项仅给出 ±20。结合上文理论，**实际正确答案为 "none"（若参照 8.2 的选项结构）**。选项错误可能源于参数表述歧义（如 $m$ 未按单位标准化），但**方法论上仍严格遵循 Slutsky 补偿逻辑**。  
  6. **含义**：线性需求函数下，替代效应 = $\left( \frac{\partial q}{\partial p} + q \frac{\partial q}{\partial m} \right) \Delta p$，体现价格变动中纯替代作用的量化路径。

---
### Page/Slide 2



### 提取当前图片中的所有文字和公式  
当前图片中仅包含文字内容，无公式或图表。文字内容为以下多选题：  

**(c) reduced his demand by 8.**  
**(d) reduced his demand by 32.**  
**(e) reduced his demand by 18.**  

**8.4** Goods 1 and 2 are perfect complements and a consumer always consumes them in the ratio of 2 units of Good 2 per unit of Good 1. If a consumer has income 120 and if the price of good 2 changes from 3 to 4, while the price of good 1 stays at 1, then the income effect of the price change  
**(a)** is 4 times as strong as the substitution effect.  
**(b)** does not change demand for good 1.  
**(c)** accounts for the entire change in demand.  
**(d)** is exactly twice as strong as the substitution effect.  
**(e)** is 3 times as strong as the substitution effect.  

**8.5** Suppose that Agatha in Problem 8.10 had $570 to spend on tickets for her trip. She needs to travel a total of 1,500 miles. Suppose that the price of first-class tickets is $0.50 per mile and the price of second-class tickets is $0.30 per mile. How many miles will she travel by second class?  
**(a)** 900  
**(b)** 1,050  
**(c)** 450  
**(d)** 1,000  
**(e)** 300  

**8.6** In Problem 8.4, Maude thinks delphiniums and hollyhocks are perfect substitutes, one for one. If delphiniums currently cost $5 per unit and hollyhocks cost $6 per unit, and if the price of delphiniums rises to $9 per unit,  
**(a)** the income effect of the change in demand for delphiniums will be bigger than the substitution effect.  
**(b)** there will be no change in the demand for hollyhocks.  
**(c)** the entire change in demand for delphiniums will be due to the substitution effect.  
**(d)** the fraction 1/4 of the change will be due to the income effect.  
**(e)** the fraction 3/4 of the change will be due to the income effect.  

---

### 问题解析（基于 Slusky 方程知识点）  
结合上文知识点总结中 **Slutsky 方程的核心机制**（替代效应通过补偿收入隔离，收入效应为总效应减替代效应），对当前问题做针对性解析：替代效应仅反映价格变动对消费的纯替代作用，而收入效应源于实际购买力变化。完全互补品和完全替代品是极端案例，需特殊分析。  

#### 问题 8.4：完全互补品的收入效应  
- **关键逻辑**：  
  **完全互补品的消费比例固定（2:1）**，导致消费者无法通过调整组合替代价格变化，因此 **替代效应为零**。  
  - 补偿收入计算（基于上文 Slusky 补偿机制）：  
    - 原最优消费束：设商品1消费量为 $q$，则商品2为 $2q$。  
      预算约束：$1 \cdot q + 3 \cdot 2q = 120 \implies 7q = 120 \implies q \approx 17.14$。  
    - 价格变动后（$p_2 = 4$），补偿收入 $m'$ 需维持原消费束：  
      $m' = 1 \cdot q + 4 \cdot 2q = 1 \cdot 17.14 + 8 \cdot 17.14 = 154.26$。  
    - **替代效应**：在补偿收入 $m'$ 下，新价格下的最优消费束仍为 $q$（比例固定），故 $\Delta q^{\text{sub}} = 0$。  
  - **收入效应**：总效应为实际收入变动导致的需求变化。  
    - 实际价格变动后：预算约束 $q + 8q = 120 \implies 9q = 120 \implies q \approx 13.33$。  
    - 总效应：$13.33 - 17.14 = -3.81$。  
    - 由于替代效应为 0，**收入效应 = 总效应**，即全部需求变化均来自收入效应。  
  - **答案解析**：选项 (c) 正确。这与上文 **问题 8.1–8.3 强调的 Slusky 方程逻辑一致**：当替代效应消失时，收入效应完全主导需求变动（与上文线性需求函数的量化路径形成对比）。  

#### 问题 8.5：无效应评估的纯预算约束问题  
- **关键逻辑**：  
  此问题未涉及价格变动，仅需预算约束和总量约束求解，**不适用 Slusky 方程**（因无价格效应分析）。  
  - 设第二类里程为 $y$，则第一类里程 $x = 1500 - y$。  
  - 预算约束：$0.50x + 0.30y = 570$。  
    代入得：$0.50(1500 - y) + 0.30y = 570 \implies 750 - 0.2y = 570 \implies y = 900$。  
  - **与上文关联**：若将价格变动引入（如提高第二类单价），则需用上文 **问题 8.3 的补偿收入法** 计算替代效应（例如求 $\Delta m = y \Delta p$ 后代入需求函数），但本题仅考察基础优化。  
  - **答案解析**：选项 (a) 正确，但核心是区分 **效应分析场景**（本题无价格变动，不需分解效应）。  

#### 问题 8.6：完全替代品的分解效应  
- **关键逻辑**：  
  **完全替代品（1:1）** 的效用函数为 $U = x + y$，**替代效应主导需求变动**，收入效应影响弱。  
  - 初始状态：$p_D = 5 < p_H = 6$，消费者仅消费 delphiniums（$q_D = m/5$）。  
  - 价格变动后：$p_D = 9 > p_H = 6$，消费者仅消费 hollyhocks。  
  - **替代效应**（补偿收入法）：  
    - 维持原效用的补偿收入 $m'$ 满足：  
      原效用 $U = q_D = m/5$，新价格下最小成本 $m' = U \cdot \min(p_D', p_H) = U \cdot 6$。  
      故补偿后需求：$q_D' = 0$（因 $p_D' > p_H$）。  
    - 替代效应：$q_D' - q_D^* = 0 - (m/5) < 0$（完全转向 hollyhocks）。  
  - **收入效应**：  
    - 总效应：需求从 $m/5$ 降至 0。  
    - 由于替代效应已完全解释需求归零，**收入效应可忽略**（仅影响绝对量，不改变消费结构）。  
  - **答案解析**：选项 (c) 正确。这与上文 **问题 8.2 的替代效应量化逻辑一致**（价格变动后需求突变，但补偿收入下分离出纯替代效应；此处因完全替代，替代效应占 100%）。  

---  
**知识连续性说明**：  
- 问题 8.4 和 8.6 延伸了上文 **Slutsky 方程在极端偏好下的应用**：完全互补品（替代效应=0）与完全替代品（收入效应≈0）分别对应效应分解的两个边界，与上文 **8.3 的线性需求函数（替代效应/收入效应均非零）形成互补案例**。  
- 问题 8.5 作为基础求解，提示：**效应分析的前提是价格变动**——若无价格变化，仅需优化框架（非 Slusky 方程适用范围），这与上文强调的“**只有价格变动才会分解出替代/收入效应**”逻辑一致。
