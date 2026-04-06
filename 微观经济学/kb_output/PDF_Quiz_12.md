# PDF_Quiz_12

### Page/Slide 1



## 1. 提取文字与公式  

### 文字内容  
- **Quiz 12**  
- **Uncertainty**  
- 12.1 问题描述及选项：  
  > Billy has a von Neumann-Morgenstern utility function $ U(c) = c^{1/2} $. Income: \$25 million (no injury), \$10,000 (injury). Probability of injury: 0.1, no injury: 0.9.  
  > Options:  
  > (a) 4,510  
  > (b) between 24 million and 25 million dollars  
  > (c) 100,000  
  > (d) 9,020  
  > (e) 18,040  

- 12.2 问题描述及选项：  
  > $ p c_f^{1/2} + (1-p) c_{nf}^{1/2} $, $ p = 1/15 $ (flood probability). Factory value: \$600,000 (no flood), 0 (flood). Insurance: pay \$ $ \frac{3x}{17} $, receive \$ $ x $ after flood.  
  > Options:  
  > (a) no insurance...  
  > (b) wealth after flood = $ \frac{1}{9} $ no-flood wealth  
  > (c) equal wealth in both states  
  > (d) wealth after flood = $ \frac{1}{4} $ no-flood wealth  
  > (e) wealth after flood = $ \frac{1}{7} $ no-flood wealth  

- 12.3 问题描述：  
  > Sally's utility: $ p u(c_1) + (1-p) u(c_2) $, where $ u(x) = 2x $ if $ x < 4,000 $, $ u(x) = 8,000 + x $ if $ x \geq 4,000 $.  

---

## 2. 核心解析  

### 12.1 风险厌恶下的期望效用计算  
- **公式** $ U(c) = c^{1/2} $ 表明个体为**风险厌恶型**（凹效用函数）。  
- **关键计算**：  
  $$
  \text{Expected Utility} = 0.9 \cdot \sqrt{25,000,000} + 0.1 \cdot \sqrt{10,000} = 0.9 \cdot 5,000 + 0.1 \cdot 100 = 4,510
  $$  
  对应选项 **(a)**，验证了风险厌恶个体的期望效用低于确定性等价收入（如选项 (b) 的区间范围）。  

---

### 12.2 保险市场的最优购买条件  
- **公式** $ p c_f^{1/2} + (1-p) c_{nf}^{1/2} $ 体现**状态依存财富**的期望效用。  
- **保险定价分析**：  
  - 保费成本：$ \frac{3x}{17} \approx 0.176x $  
  - 公平保费应满足：保费 = 期望赔付 $ \Rightarrow p x = \frac{1}{15}x \approx 0.067x $  
  - 实际保费 **0.176x > 0.067x**，即保险成本超过损失概率。  
- **决策逻辑**：选项 **(a)** 正确，因保险价格**不利**（unfair insurance），最优选择为零保险。  

---

### 12.3 分段效用函数的期望效用决策  
- **公式** $ u(x) $ 为**分段线性函数**，在 $ x = 4,000 $ 处存在边际效用突变：  
  - $ x < 4,000 $：$ u'(x) = 2 $（高边际效用）  
  - $ x \geq 4,000 $：$ u'(x) = 1 $（低边际效用）  
- **经济含义**：个体在低财富区间风险厌恶程度更高，决策需分段计算期望效用，体现**非恒定风险偏好**对选择的影响。

---
### Page/Slide 2



### 1. 提取文字与公式  

#### 文字内容  
- **12.3 选项**:  
  > (a) Sally will be risk averse if her income is less than 4,000 but risk loving if her income is more than 4,000.  
  > (b) Sally will be risk neutral if her income is less than 4,000 and risk averse if her income is more than 4,000.  
  > (c) For bets that involve no chance of her wealth exceeding 4,000, Sally will take any bet that has a positive expected net payoff.  
  > (d) Sally will never take a bet if there is a chance that it leaves her with wealth less than 8,000.  
  > (e) None of the above are true.  

- **12.4 问题描述及选项**:  
  > Martin’s expected utility function is $ p c_1^{1/2} + (1-p)c_2^{1/2} $. Wilbur can choose between a sure payment of \$Z or a lottery (\$2,500 with probability 0.40, \$900 with probability 0.60).  
  > Options:  
  > (a) $ Z > 1,444 $ and the lottery if $ Z < 1,444 $  
  > (b) $ Z > 1,972 $ and the lottery if $ Z < 1,972 $  
  > (c) $ Z > 900 $ and the lottery if $ Z < 900 $  
  > (d) $ Z > 1,172 $ and the lottery if $ Z < 1,172 $  
  > (e) $ Z > 1,540 $ and the lottery if $ Z < 1,540 $  

- **12.5 问题描述及选项**:  
  > Clancy has \$4,800. Sullivan tickets cost \$6 (pay \$10 if win), Flanagan tickets cost \$4 (pay \$10 if win). Both fighters have 1/2 winning probability. Clancy maximizes $ E[\ln(\text{wealth})] $.  
  > Options:  
  > (a) Don’t gamble at all  
  > (b) Buy 400 Sullivan and 600 Flanagan tickets  
  > (c) Buy equal numbers of both tickets  
  > (d) Buy 200 Sullivan and 300 Flanagan tickets  
  > (e) Buy 200 Sullivan and 600 Flanagan tickets  

---

### 2. 结合上文的知识连续性解析  

#### 12.3 题目解析  
- **核心逻辑**：上文指出Sally的效用函数为**分段线性**（$ u'(x) = 2 $ for $ x < 4,000 $, $ u'(x) = 1 $ for $ x \geq 4,000 $），其**全局风险厌恶**源于函数凹性（斜率递减），但**局部风险态度**取决于财富区间：  
  - 当赌局**不跨越 $ x = 4,000 $** 时（如选项 (c) 的条件），效用函数在区间内是线性的 → **风险中性**，会接受任何期望净支付为正的赌局。  
  - 选项 (a)/(b) 错误：效用函数在任一区间内均为线性，**无风险偏好切换**；全局凹性导致整体风险厌恶，但局部无风险厌恶/喜好。  
  - 选项 (d) 错误：无依据表明 \$8,000 是财富阈值。  
  **结论**：**(c) 正确**，体现分段线性函数下**局部风险中性**的特性（上文12.3知识点延伸）。  

---

#### 12.4 题目解析  
- **公式关联**：与上文12.1一致，效用函数 $ U(c) = c^{1/2} $ 为**风险厌恶型**（凹函数），需计算**确定性等价收入**：  
  $$
  \text{Lottery Utility} = 0.4 \cdot \sqrt{2,500} + 0.6 \cdot \sqrt{900} = 0.4 \cdot 50 + 0.6 \cdot 30 = 38
  $$  
  $$
  \text{Certainty Equivalent: } \sqrt{Z} = 38 \Rightarrow Z = 38^2 = 1,444
  $$  
- **决策逻辑**：  
  - 若 $ Z > 1,444 $，$ \sqrt{Z} > 38 $ → 选择确定支付（选项 (a)）。  
  - 与上文12.1对比：本题直接应用**期望效用等价条件**，验证风险厌恶下确定性等价低于期望值（期望财富 $ = 0.4 \cdot 2,500 + 0.6 \cdot 900 = 1,540 $，但确定性等价仅 \$1,444）。  

---

#### 12.5 题目解析  
- **效用函数特性**：$ E[\ln(\text{wealth})] $ 对应**对数效用**（比上文 $ c^{1/2} $ 更强的风险厌恶），需优化投资组合：  
  - 设购买 $ s $ 张Sullivan票、$ f $ 张Flanagan票，支出约束：$ 6s + 4f \leq 4,800 $.  
  - 两种状态下的财富：  
    - Sullivan wins: $ W_1 = 4,800 - 6s - 4f + 10s = 4,800 + 4s - 4f $  
    - Flanagan wins: $ W_2 = 4,800 - 6s - 4f + 10f = 4,800 - 6s + 6f $  
  - 目标函数：$ 0.5 \ln(W_1) + 0.5 \ln(W_2) \to \max $.  

- **优化逻辑**：  
  - 对数效用下最优解需满足 **$ W_1 = W_2 $**（风险厌恶者的完全保险条件，同上文12.2的公平保险逻辑）。  
  - 令 $ 4,800 + 4s - 4f = 4,800 - 6s + 6f \Rightarrow 10s = 10f \Rightarrow s = f $.  
  - 预算约束：$ 6s + 4s \leq 4,800 \Rightarrow s \leq 480 $ → 选项 (c) **"Buy equal numbers"** 符合最优条件。  
  - **排除其他选项**：  
    - (a) 未利用可能的正期望收益（赌局期望净利润为正）；  
    - (b)/(d)/(e) 不满足 $ s = f $，导致状态间财富不等，违反效用最大化必要条件。
