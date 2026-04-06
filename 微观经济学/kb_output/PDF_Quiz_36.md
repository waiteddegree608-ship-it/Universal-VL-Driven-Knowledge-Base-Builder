# PDF_Quiz_36

### Page/Slide 1



### 1. Extracted Text and Formulas  

#### **Quiz 36.1**  
- **Setup**:  
  - Low-productivity workers: marginal product = $10$  
  - High-productivity workers: marginal product = $16$  
  - Cost of microeconomics course:  
    - High-productivity: equivalent to wage cut of $4$  
    - Low-productivity: equivalent to wage cut of $7$  

- **Options**:  
  - (a) Separating equilibrium: High take course (paid $16$), low do not (paid $10$).  
  - (b) No separating/pooling equilibrium.  
  - (c) No separating equilibrium; pooling equilibrium at wage $13$.  
  - (d) Separating equilibrium: High take course (paid $20$), low do not (paid $10$).  
  - (e) Separating equilibrium: High take course (paid $16$), low paid $13$.  

#### **Quiz 36.2**  
- **Setup**:  
  - Klutzes: productivity = $\$1,000$; cost of 1 hour of lectures = $\$200$  
  - Kandos: productivity = $\$5,000$; cost of 1 hour of lectures = $\$100$  
  - Separating equilibrium condition: Attending $H$ hours → paid $\$5,000$; not attending → paid $\$1,000$.  

- **Options**:  
  - (a) $H < 40$ and $H > 20$  
  - (b) $H < 80$ and $H > 20$  
  - (c) All positive $H$  
  - (d) Only as $H \to \infty$  

---

### 2. Conceptual Analysis  

#### **Quiz 36.1: Signaling and Separating Equilibrium**  
- **Key Mechanism**: The course acts as a **signal** of productivity. A separating equilibrium exists if:  
  1. High-productivity workers **prefer** taking the course (net utility > not taking).  
  2. Low-productivity workers **prefer not** to take it (net utility < not taking).  

- **Critical Inequality**:  
  - For high-productivity workers:  
    $$
    \text{Wage with course} - 4 > 10 \quad \text{(reservation wage)}
    $$  
    If paid $16$, net utility = $16 - 4 = 12 > 10$ → incentivized to take.  
  - For low-productivity workers:  
    $$
    \text{Wage with course} - 7 < 10
    $$  
    If paid $16$, net utility = $16 - 7 = 9 < 10$ → disincentivized to mimic.  

- **Option (a) Validity**:  
  - High workers choose the course (net utility $12 > 10$).  
  - Low workers avoid it (net utility $9 < 10$).  
  - **Result**: Self-selection is sustainable → separating equilibrium.  

- **Why Other Options Fail**:  
  - (d): Wage $20$ for high workers is unnecessary (overpayment breaks equilibrium efficiency).  
  - (c) Pooling equilibrium at $13$ would fail if high workers can signal for higher wages.  

#### **Quiz 36.2: Signaling with Heterogeneous Costs**  
- **Incentive Compatibility Conditions**:  
  - **Kandos (high-productivity)** must prefer taking $H$ hours:  
    $$
    5000 - 100H > 1000 \implies H < 40
    $$  
  - **Klutzes (low-productivity)** must prefer not taking:  
    $$
    1000 > 5000 - 200H \implies H > 20
    $$  

- **Solving for $H$**:  
  - $20 < H < 40$ ensures both conditions hold.  
  - **Option (a)** directly satisfies this range.  

- **Why Other Options Fail**:  
  - (b): $H < 80$ is irrelevant (cost for Klutzes is driven by $200H$).  
  - (c)/(d): Universal/an infinite $H$ would eliminate separation (Klutzes might mimic if $H$ is too small/large).  

---

### 3. Key Microeconomic Principles  
- **Signaling**: Costly actions (e.g., education) reveal private productivity information when costs differ by type.  
- **Separating Equilibrium**: Sustained when signal costs are **proportionally lower** for high types (here, $4/16 < 7/10$ for Quiz 36.1; $100/5000 < 200/1000$ for Quiz 36.2).  
- **Pooling Equilibrium**: Only viable if signal costs prevent credible separation (not the case here).

---
### Page/Slide 2



# 当前图片解析

## 文字与公式提取

- **问题 36.3**（Rustbucket, Michigan 二手车市场）:  
  "In Rustbucket, Michigan, there are 200 used cars for sale. Half of them are good, and half of them are lemons. Owners of lemons are willing to sell them for $300. Owners of good used cars are willing to sell them for prices above $1,100 but will keep them if the price is lower than $1,100. There is a large number of potential buyers who are willing to pay $400 for a lemon and $2,100 for a good car. Buyers can’t tell good cars from bad, but original owners know."  
  - 选项:  
    (a) There will be an equilibrium in which all used cars sell for $1,250.  
    (b) The only equilibrium is one in which all used cars on the market are lemons and they sell for 400.  
    (c) There will be an equilibrium in which lemons sell for 300 and good used cars sell for 1,100.  
    (d) There will be an equilibrium in which all used cars sell for 700.  
    (e) There will be an equilibrium in which lemons sell for 400 and good used cars sell for 2,100.  

- **问题 36.4**（Burnt Clutch, Pa. 二手车评估信号）:  
  "Suppose that in Burnt Clutch, Pa., the quality distribution of the 1000 used cars on the market is such that the number of used cars of value less than V is V/2. Original owners must sell their used cars. Original owners know what their cars are worth, but buyers can’t determine a car’s quality until they buy it. An owner can either take his car to an appraiser and pay the appraiser $100 to appraise the car (accurately and credibly), or he can sell the car unappraised. In equilibrium, car owners will have their cars appraised if and only if their value is at least"  
  - 选项:  
    (a) $100.  
    (b) $500.  
    (c) $300.  
    (d) $200.  
    (e) $400.  

- **隐含公式**:  
  - 问题 36.3:  
    - 柠檬保留价: $ \leq 300 $  
    - 好车保留价: $ > 1,100 $  
    - 买家估值: 柠檬 $ 400 $，好车 $ 2,100 $  
    - 期望价值: $ 0.5 \times 400 + 0.5 \times 2,100 = 1,250 $  
  - 问题 36.4:  
    - 质量分布: $ \text{number of cars with value} < V = \frac{V}{2} $（隐含均匀分布于 $[0,2000]$）  
    - 均衡条件: $ P = E[v \mid v \leq k] $ 且 $ k = P + 100 $，解得 $ P = 100 $, $ k = 200 $  

## 经济学解析  

### 针对问题 36.3  
- **与上文知识点的联系**: 本题是 **逆向选择（Adverse Selection）** 的典型案例，属于 Akerlof 柠檬市场模型。与上文 Quiz 36.1 的池化均衡分析一致：当买家无法区分质量时，市场可能达成池化均衡（pooling equilibrium）或崩溃为柠檬市场。上文强调，池化均衡仅在无法通过信号实现分离时成立（如信号成本过高或不可信），但此处无信号机制，故仅能依赖匿名交易。  
- **均衡分析**:  
  - 买家期望价值 $1,250$ 高于好车保留价 $1,100$，因此好车主愿意以 $1,250$ 出售（$1,250 > 1,100$），形成可行池化均衡（选项 a）。  
  - 选项 b（仅柠檬市场）理论上成立，但非唯一均衡，因选项 a 同样满足条件：上文指出池化均衡需满足高类型参与（high-type participation），此处好车主因保留价低于 $1,250$ 而参与，与上文 "reservation wage" 逻辑一致。  
  - 选项 c、d、e 不可持续：买家无法区分质量，故无法实现价格分离；若价格低于 $1,100$（如选项 d 的 $700$），好车主退出，但买家只愿付柠檬价值 $400$，导致矛盾。  

### 针对问题 36.4  
- **与上文知识点的联系**: 本题直接应用 **信号传递理论（Signaling）**，类似于上文 Quiz 36.2 的成本异质性设计。评估费 $100$ 构成可信信号：高价值车主因信号成本比例更低（上文 "proportionally lower" 原则），更愿支付成本分离自身类型；评估后买家可支付真实价值，解决信息不对称。  
- **均衡推导关键**:  
  - 定义 $k = P + 100$ 为选择评估的临界价值（$v > k$ 时车主偏好评估，因 $v - 100 > P$）。  
  - 未评估车的期望价值 $P = E[v \mid v \leq k] = k/2$（由均匀分布推导，$k \in [0,2000]$）。  
  - 代入 $k = P + 100$ 解得 $P = 100$，$k = 200$。  
  - **临界价值 $200$ 意义**:  
    - 当 $v > 200$，评估净收益 $v - 100 > 100 = P$，符合上文 "incentive compatibility" 条件（如 Quiz 36.2 中 $H > 20$ 等约束）。  
    - 价值 $200$ 处无差异，与上文 Quiz 36.1 的 "reservation wage" 逻辑一致（$12 > 10$ 产生激励）。  
- **选项选择依据**:  
  - 选项 (d) $200$ 正确，因车主仅在 $v \geq 200$ 时选择评估，符合分离均衡条件。  
  - 其他选项失效：如 (a) $100$ 下，若临界值过低，低值车主可能模仿（与上文 Quiz 36.1 de-mimicking 条件矛盾）；(b) $500$ 等过高值则过高估计成本比例，违反信号传递效率原则。  

### 总结启示  
- 36.3 体现无信号时池化均衡的脆弱性，印证上文 "pooling equilibrium only viable if signal costs prevent credible separation"；36.4 则验证信号机制如何通过 **异质时间成本（heterogeneous costs）** 实现分离均衡，直接呼应上文 "separating equilibrium sustained when signal costs are proportionally lower for high types" 的核心结论。  
- 两例共同说明：信息不对称下，市场效率取决于信号是否可行且激励相容——与教育信号案例（Quiz 36.1）本质一致，仅应用场景（二手车 vs 劳动力）不同。
