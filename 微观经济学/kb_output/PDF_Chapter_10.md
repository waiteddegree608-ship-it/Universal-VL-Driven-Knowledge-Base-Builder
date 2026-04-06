# PDF_Chapter_10

### Page/Slide 1



# 跨期选择理论详解

## 文字与公式提取

### 章节与标题
- Chapter 10
- Intertemporal Choice

### 主要内容
- **理论基础**：消费者储蓄理论，关注时间维度上的消费选择
- **核心方法**：将不同时期的消费视为不同商品
  - 时期1消费设为计价物(numeraire)
  - 时期2消费的"价格"为 $1/(1+r)$，$r$ 为利率
- **收入处理**：两时期无通胀情况下的总收入表示

### 关键公式
1. 跨期预算约束方程：
   $$c_1 + \frac{c_2}{1+r} = m_1 + \frac{m_2}{1+r}$$

2. 无通胀例子：
   - 效用函数：$U(c_1,c_2) = c_1c_2$
   - 利率：10%
   - 时期1收入：100
   - 时期2收入：121
   - 预算约束：$c_1 + \frac{c_2}{1.1} = 100 + \frac{121}{1.1} = 210$
   - 价格比率：$1+r = 1.1$
   - 边际替代率条件：$\frac{MU_1}{MU_2} = 1.1$
   - 边际效用计算：$MU_1 = c_2$，$MU_2 = c_1$
   - 消费选择关系：$\frac{c_2}{c_1} = 1.1$
   - 最优解：$c_1 = 105$，$c_2 = 115.50$

## 理论解析

### 跨期预算约束的本质
将跨期预算约束 $c_1 + \frac{c_2}{1+r} = m_1 + \frac{m_2}{1+r}$ 映射为标准静态预算约束：
- "商品1"（时期1消费）价格 = 1
- "商品2"（时期2消费）价格 = $\frac{1}{1+r}$
- "总收入" = $m_1 + \frac{m_2}{1+r}$

这一转换使跨期选择问题等价于标准消费者选择问题，可直接应用边际替代率等于价格比率的优化条件。

### 时间偏好与利率关系
- 时期2消费的折现价格 $\frac{1}{1+r}$ 反映了时间偏好
- 利率 $r$ 决定了现在消费与未来消费的交换比率
- 价格比率 $1+r$ 表明为获得1单位未来消费需要放弃的现期消费量

### 例子分析
1. **预算约束计算**：
   - 时期1消费能力：100 + 未来收入折现 = $100 + 121/1.1 = 210$
   - 表明消费者通过借贷可将两期资源集中使用

2. **优化决策**：
   - 从 $\frac{c_2}{c_1} = 1.1$ 和预算约束同时求解
   - 消费者选择现期消费超过收入(105 > 100)，表明此时是借款人
   - 借款额5需在时期2偿还5.5(5×1.1)，剩余121 - 5.5 = 115.5用于消费

3. **经济行为解释**：
   - 借贷行为源于时间偏好与市场利率的关系
   - 当边际替代率等于市场交换比率时达到最优
   - 消费平滑化是跨期选择的核心动机

## 理论拓展

- **储蓄与借贷决策**：储蓄 = $m_1 - c_1$，正值表示储蓄，负值表示借贷
- **利率变动影响**：改变预算线斜率，影响消费在两期的分配
- **通胀因素**：后续内容将探讨通胀对名义利率和实际消费决策的影响

此模型将时间维度纳入消费者选择框架，将跨期决策简化为两商品选择问题，为分析生命周期消费、储蓄行为奠定了基础。

---
### Page/Slide 2



## 跨期选择理论解析：通胀影响与应用问题

### 1. 当前图片文字与公式提取

**文字内容：**  
> ssumer behavior. The key to understanding the effects of inflation is to see what happens to the budget constraint.  
> **Example:** Suppose that in the previous example, there happened to be an inflation rate of 6%, and suppose that the price of period-1 goods is 1. Then if you save $1 in period 1 and get it back with 10% interest, you will get back $1.10 in period 2. But because of the inflation, goods in period 2 cost 1.06 dollars per unit. Therefore the amount of period-1 consumption that you have to give up to get a unit of period-2 consumption is $1.06/1.10 = .964$ units of period-2 consumption. If the consumer’s money income in each period is unchanged, then his budget equation is $c_1 + .964c_2 = 210$. This budget constraint is the same as the budget constraint would be if there were no inflation and the interest rate were $r$, where $.964 = 1/(1+r)$. The value of $r$ that solves this equation is known as the **real rate of interest**. In this case the real rate of interest is about $.038$. When the interest rate and inflation rate are both small, the real rate of interest is closely approximated by the difference between the **nominal interest rate**, (10% in this case) and the inflation rate (6% in this case), that is, $.038 \sim .10 - .06$. As you will see, this is not such a good approximation if inflation rates and interest rates are large.  
> **10.1 (0)** Peregrine Pickle consumes $(c_1, c_2)$ and earns $(m_1, m_2)$ in periods 1 and 2 respectively. Suppose the interest rate is $r$.  
> $(a)$ Write down Peregrine’s intertemporal budget constraint in present value terms. $c_1 + \frac{c_2}{(1+r)} = m_1 + \frac{m_2}{(1+r)}$.  
> $(b)$ If Peregrine does not consume anything in period 1, what is the most he can consume in period 2? $m_1(1+r) + m_2$. This is the (future value, present value) of his endowment. **Future value**.  
> $(c)$ If Peregrine does not consume anything in period 2, what is the most he can consume in period 1? $m_1 + \frac{m_2}{(1+r)}$. This is the (future value, present value) of his endowment. **Present value**. What is the slope of Peregrine’s budget line? $-(1+r)$.  
> **10.2 (0)** Molly has a Cobb-Douglas utility function $U(c_1,c_2) = c_1^a c_2^{1-a}$, where $0 < a < 1$ and where $c_1$ and $c_2$ are her consumptions in periods 1 and 2 respectively. We saw earlier that if utility has the form $u(x_1,x_2) = x_1^a x_2^{1-a}$ and the budget constraint is of the “standard” form $p_1x_1 + p_2x_2 = m$, then the demand functions for the goods are $x_1 = am/p_1$ and $x_2 = (1-a)m/p_2$.

**公式列表：**  
- 通胀调整后预算约束： $c_1 + .964c_2 = 210$  
- 实际利率定义： $.964 = \frac{1}{(1+r)}$  
- 现值预算约束（问题10.1a）： $c_1 + \frac{c_2}{(1+r)} = m_1 + \frac{m_2}{(1+r)}$  
- 未来值表示（问题10.1b）： $m_1(1+r) + m_2$  
- 现值表示（问题10.1c）： $m_1 + \frac{m_2}{(1+r)}$  
- 预算线斜率（问题10.1c）： $-(1+r)$  
- Cobb-Douglas效用函数（问题10.2）： $U(c_1,c_2) = c_1^a c_2^{1-a}$  
- 需求函数： $x_1 = \frac{a m}{p_1}, \quad x_2 = \frac{(1-a) m}{p_2}$  

---

### 2. 结合上文的新增内容解析

#### 通胀对跨期预算约束的影响（延伸上文"通胀因素"部分）
- **名义利率与实际利率的区分**：  
  上文知识点指出通胀将影响名义利率对消费决策的作用，此处例证了具体机制。当名义利率 $r_{\text{nominal}} = 10\%$ 且通胀率 $\pi = 6\%$ 时：
  - 物价变动使时期2商品实际购买力下降（价格由 $1$ 升至 $1.06$），导致未来消费的**相对价格**从 $\frac{1}{1+r_{\text{nominal}}}$ 变为 $\frac{1+\pi}{1+r_{\text{nominal}}}$（即 $0.964$）。  
  - 消费者为获得1单位时期2消费，需牺牲 $0.964$ 单位时期1消费（原无通胀时为 $1/1.10 \approx 0.909$），表明通胀降低了未来消费的吸引力。  
  - **实际利率 $r_{\text{real}}$ 的推导**：由 $\frac{1}{1+r_{\text{real}}} = \frac{1+\pi}{1+r_{\text{nominal}}}$ 解得 $r_{\text{real}} \approx 3.8\%$。上文提及通胀是"后续探讨"，此处明确其核心逻辑——预算约束的**有效价格**需用实际利率重标定，而非直接使用名义利率。

- **近似规则的适用性**：  
  $r_{\text{real}} \approx r_{\text{nominal}} - \pi$（即 $0.10 - 0.06 = 0.04$）仅在低通胀/低利率时成立（实际值 $0.038$）。上文强调通胀对"名义利率和实际消费决策"的影响，此例揭示：当通胀率高时，该近似失效（例如 $30\%$ 通胀时，$r_{\text{real}} = \frac{1.10}{1.30} - 1 \approx -15.4\% \neq 10\% - 30\% = -20\%$），导致消费分配扭曲。

#### 跨期预算表示的多样化（衔接上文"预算约束方程"）
- **现值 vs. 未来值表述**（问题10.1）：  
  - 上文已定义标准预算约束 $c_1 + \frac{c_2}{1+r} = m_1 + \frac{m_2}{1+r}$，此处补充其经济含义：  
    - **现值形式**（a部分）：等式两侧均以时期1货币计量，体现"资源总现值"守恒。  
    - **未来值形式**（b部分）：当 $c_1=0$ 时，$m_1(1+r) + m_2$ 表示将全部收入投资至时期2的**终值**，即预算约束的横截距。  
    - **预算线斜率**（c部分）：$-(1+r)$ 直接反映市场交换比率（为获取1单位时期2消费需放弃 $1+r$ 单位时期1消费），与上文"价格比率 $1+r$"的结论一致。  
  - **关键连续性**：上文将时期2消费价格定义为 $\frac{1}{1+r}$，此处斜率 $-(1+r)$ 验证了价格比率的倒数关系，强化了"跨期选择等同于两商品静态选择"的核心逻辑。

#### Cobb-Douglas效用的应用拓展（衔接上文"例子分析"）
- 问题10.2 将上文无通胀案例中的 $U(c_1,c_2)=c_1 c_2$（即 $a=0.5$ 的特例）推广至一般形式 $U = c_1^a c_2^{1-a}$。  
  - 结合上文的边际替代率条件 $\frac{MU_1}{MU_2} = 1+r$，此处给出需求函数解：  
    $$
    c_1 = a \left( m_1 + \frac{m_2}{1+r} \right), \quad c_2 = (1-a)(1+r) \left( m_1 + \frac{m_2}{1+r} \right)
    $$  
  - **延续性体现**：上文计算得 $c_1=105, c_2=115.50$（当 $a=0.5, m_1=100, m_2=121, r=0.1$），代入此公式亦得相同结果，验证了理论普适性。  
  - 此处未引入通胀，但为后续章节（如通胀下效用最大化）埋下伏笔，呼应上文"通胀因素"的预告。

---
### Page/Slide 3



# 问题 10.2 详细解析

## 1. 文字与公式提取

### (a) 部分
- **文字**：Suppose that Molly's income is $m_1$ in period 1 and $m_2$ in period 2. Write down her budget constraint in terms of present values.
- **公式**：$c_1 + \frac{c_2}{(1+r)} = m_1 + \frac{m_2}{(1+r)}$

### (b) 部分
- **文字**：We want to compare this budget constraint to one of the standard form. In terms of Molly's budget constraint...
- **公式**：
  - $p_1 = 1$
  - $p_2 = \frac{1}{(1+r)}$
  - $m = m_1 + \frac{m_2}{(1+r)}$

### (c) 部分
- **文字**：If $a = .2$, solve for Molly's demand functions for consumption in each period as a function of $m_1$, $m_2$, and $r$.
- **公式**：
  - 时期1需求：$c_1 = 0.2m_1 + 0.2\frac{m_2}{(1+r)}$
  - 时期2需求：$c_2 = 0.8(1+r)m_1 + 0.8m_2$

### (d) 部分
- **文字**：An increase in the interest rate will decrease her period-1 consumption. It will increase her period-2 consumption and increase her savings in period 1.

### 10.3 问题
- **文字**：Nickleby has an income of $2,000 this year, and he expects an income of $1,100 next year. He can borrow and lend money at an interest rate of 10%. Consumption goods cost $1 per unit this year and there is no inflation.

## 2. 知识点解析与连续性

### (a) 部分解析
- 预算约束的**现值形式**直接对应上文知识点中的"现值表示"。
- 与上文建立的空间关系不同，这里明确显示消费者通过市场交易，将时期1和时期2的消费统一在现值框架下进行权衡。
- 等式左侧是消费的现值总和，右侧是收入的现值总和，反映跨期资源约束的核心逻辑。

### (b) 部分解析
- **价格定义的延续性**：
  - $p_1 = 1$ 确认了时期1消费的基准价格
  - $p_2 = \frac{1}{(1+r)}$ 验证了上文"时期2消费相对价格"的定义，体现了时间价值
- **预算总额 $m$** 与上文"资源总现值"概念完整对应，明确将跨期决策转化为标准静态选择模型：
  $$
  p_1c_1 + p_2c_2 = m
  $$
- 这一标准形式使跨期选择问题能直接应用消费者理论的基本工具，强化了"时间选择等同于商品选择"的微观经济学核心思想。

### (c) 部分解析
- **Cobb-Douglas需求函数的具体化**：
  - 当 $a=0.2$ 时，需求函数直接体现了上文知识点中的通用形式
  - 将通用公式 $c_1 = a(m_1 + \frac{m_2}{(1+r)})$ 和 $c_2 = (1-a)(1+r)(m_1 + \frac{m_2}{(1+r)})$ 展开为图片中的具体表达式
- **需求分解**：
  - $c_1$ 表达式显示当前消费既依赖当期收入 $m_1$，也依赖未来收入现值 $\frac{m_2}{(1+r)}$
  - $c_2$ 表达式中 $(1+r)m_1$ 项表明当期储蓄的未来价值，$m_2$ 项表示预期未来收入
- **参数含义**：$a=0.2$ 表示Molly将20%的资源分配给当期消费，80%分配给未来消费，反映其时间偏好。

### (d) 部分解析
- **利率变化的替代效应**：
  - 利率上升，时期2消费相对价格下降 $(p_2 = \frac{1}{1+r})$，产生替代效应使当期消费减少
  - 与上文"通胀对跨期决策"部分逻辑一致：实际利率变化会改变消费的时间配置
- **储蓄决策机制**：
  - 时期1储蓄 = $m_1 - c_1$
  - 从需求函数可见，利率 $r$ 增加会降低 $c_1$ 部分项中的 $\frac{m_2}{(1+r)}$ 和 $c_2$ 中的 $(1+r)m_1$ 项
  - 当 $a<0.5$ 时（此处 $a=0.2$），利率上升对储蓄的正向影响更显著
- **与上文的衔接**：此处分析为上文"通胀对跨期预算约束的影响"提供了具体机制——利率变动通过改变价格比率影响消费分配，而通胀会进一步扭曲这一机制。

## 3. 与后续问题的关联
- 10.3问题中Nickleby的案例 (无通胀、10%利率) 为应用上述理论提供了实证场景
- 需注意此案例与(c)部分相比：
  - 不同 $a$ 值：需确定Nickleby的偏好参数
  - 有具体数值而非参数化表达
  - 可直接计算消费与储蓄的具体值
- 这种由一般化参数向具体案例的过渡，体现了微观经济学从理论到应用的逻辑链条。

---
### Page/Slide 4



### 提取图片中的文字与公式

#### 文字内容
- 页眉：`134 INTERTEMPORAL CHOICE (Ch. 10)`
- 图表标题：  
  - 纵轴：`Consumption next year in 1,000s`  
  - 横轴：`Consumption this year in 1,000s`  
- 图例标注：  
  - `Red line`  
  - `Blue line`  
  - `Squiggly line`  
  - 点 `a` 和 `e`  
- 问题 (a)：  
  - `What is the present value of Nickleby’s endowment? $3,000.`  
  - `What is the future value of his endowment? $3,300.`  
  - `With blue ink, show the combinations of consumption this year and consumption next year that he can afford. Label Nickleby’s endowment with the letter E.`  
- 问题 (b)：  
  - `Suppose that Nickleby has the utility function \( U(C_1, C_2) = C_1 C_2 \). Write an expression for Nickleby’s marginal rate of substitution between consumption this year and consumption next year. (Your answer will be a function of the variables \( C_1, C_2 \).)`  
  - `MRS = -C_2 / C_1`  
- 问题 (c)：  
  - `What is the slope of Nickleby’s budget line? -1.1.`  
  - `Write an equation that states that the slope of Nickleby’s indifference curve is equal to the slope of his budget line when the interest rate is 10%. 1.1 = C_2 / C_1.`  
  - `Also write down Nickleby’s budget equation. \( C_1 + C_2 / 1.1 = 3,000 \).`  
- 问题 (d)：  
  - `Solve these two equations. Nickleby will consume 1,500 units in period 1 and 1,650 units in period 2. Label this point A on your diagram.`

#### 公式内容
- 边际替代率：  
  \[
  \text{MRS} = -\frac{C_2}{C_1}
  \]
- 预算线斜率：  
  \[
  \text{slope} = -1.1
  \]
- 均衡条件：  
  \[
  1.1 = \frac{C_2}{C_1}
  \]
- 预算方程：  
  \[
  C_1 + \frac{C_2}{1.1} = 3,000
  \]

---

### 图表解析与知识连续性

#### 图表元素的核心含义
本图表是上文知识点中 **10.3 问题** 的具象化延伸（上文定义：\( m_1 = 2000 \), \( m_2 = 1100 \), \( r = 0.1 \), 无通胀），将跨期决策转化为几何表示。关键点如下：

- **坐标轴单位**：  
  - 横轴 `Consumption this year in 1,000s` 表示本期消费 \( C_1 \)（单位：千美元），刻度 `1` 对应 $1,000。  
  - 纵轴 `Consumption next year in 1,000s` 表示下期消费 \( C_2 \)（单位：千美元），刻度 `1` 对应 $1,000。  
  - **连续性说明**：延续上文 (b) 部分的价格定义（\( p_1 = 1 \), \( p_2 = 1/(1+r) \)），此处价格比 \( p_1/p_2 = 1.1 \) 直接决定预算线斜率。

- **预算线（Blue line）**：  
  - 由预算方程 \( C_1 + \frac{C_2}{1.1} = 3,000 \) 确定，斜率 \( -1.1 = -(1+r) \)，与上文 (b) 部分一致。  
  - 端点含义：  
    - 当 \( C_2 = 0 \) 时，\( C_1 = 3,000 \)（全部收入现值用于本期消费）；  
    - 当 \( C_1 = 0 \) 时，\( C_2 = 3,300 \)（全部收入储蓄至下期，现值 $3,000 × 1.1 = $3,300，匹配问题 (a) 中未来价值）。  
  - **连续性说明**：验证了上文“跨期资源约束的现值形式”，强化了“时间选择等同于商品选择”的核心思想（上文 2. 知识点解析）。

- **禀赋点（Label E，图中标注为 `e`）**：  
  - 位置：\( (C_1, C_2) = (2, 1.1) \)（即 \( m_1 = 2,000 \), \( m_2 = 1,100 \)）。  
  - **连续性说明**：直接对应上文 10.3 问题设定，代表无借贷时的收入分配。若 \( C_1 < m_1 \)（如最优解 \( C_1 = 1.5 < 2 \)），则本期有储蓄，延续上文 (d) 部分“储蓄 = \( m_1 - c_1 \)”的逻辑。

- **最优消费点（图中标注为 `a`）**：  
  - 位置：\( (C_1, C_2) = (1.5, 1.65) \)（即 1,500 和 1,650 单位）。  
  - 由均衡条件 \( \frac{C_2}{C_1} = 1.1 \) 和预算方程推导得出，与上文 (c) 部分 Cobb-Douglas 需求函数逻辑一致：  
    - Nickleby 的效用 \( U = C_1 C_2 \) 是 \( a = 0.5 \) 的特例（对比上文 Molly 的 \( a = 0.2 \)），故 \( C_1 = 0.5 \times 3,000 = 1,500 \), \( C_2 = 0.5 \times 3,300 = 1,650 \)。  
  - **连续性说明**：体现了“时间偏好参数化分配资源”的原理（上文 (c) 解析），且计算过程验证了上文 (b) 部分“预算总额 \( m \) 作为标准静态选择模型输入”的设定。

- **无差异曲线（Squiggly line）**：  
  - 在点 `a` 处与预算线相切，斜率为 \( -\text{MRS} = -C_2/C_1 \)。  
  - **均衡含义**：切点满足 \( | \text{MRS} | = 1 + r \)（上文 2.3 节），此处 \( C_2 / C_1 = 1.1 = 1 + r \)，符合效用最大化一阶条件。  
  - **连续性说明**：曲线形状（凸性）隐含递减边际替代率，与上文跨期选择理论一致，但无通胀下价格稳定，未引入扭曲。

- **Red line 的无关性**：  
  - 问题文本未提及，图中存在但无定义。结合上文知识点，**无利率或收入变化场景**，故 `Red line` 可能用于拓展问题（如利率变动的假设分析），但当前图表中不具经济含义。上文 (d) 部分讨论利率上升的影响（减少 \( c_1 \)、增加 \( c_2 \) 和储蓄），但本图表仅展示基准均衡，不涉及动态变化。

#### 深层含义总结
- 图表**固化上文理论逻辑**：预算线位置由收入现值（$3,000）决定，斜率由利率（10%）定义，印证上文 (a) 部分“跨期资源约束的现值表示”。  
- **实证衔接**：将上文 (c) 部分参数化需求（\( a = 0.2 \)）转化为具体数值案例（\( a = 0.5 \)），体现微观经济学“从理论到应用”的推演链条（上文 3. 与后续问题的关联）。  
- **关键缺失**：未展示利率变化（上文 (d) 部分），故无法直接解析“变化”，但点 `a` 和 `e` 的位移隐含储蓄行为（\( m_1 - C_1 = 500 \)，即本期储蓄 500 美元），可延拓至利率变动分析。

---
### Page/Slide 5



### 当前图片解析

#### 1. 提取当前图片中的所有文字、公式
**文字内容：**
```
(e) Will he borrow or save in the first period? Save. How much?  
500.  

(f) On your graph use red ink to show what Nickleby’s budget line would be if the interest rate rose to 20%. Knowing that Nickleby chose the point A at a 10% interest rate, even without knowing his utility function, you can determine that his new choice cannot be on certain parts of his new budget line. Draw a squiggly mark over the part of his new budget line where that choice can not be. (Hint: Close your eyes and think of WARP.)  

(g) Solve for Nickleby’s optimal choice when the interest rate is 20%.  
Nickleby will consume 1,458.3 units in period 1 and 1,750 units in period 2.  

(h) Will he borrow or save in the first period? Save. How much?  
541.7.  

10.4 (0) Decide whether each of the following statements is true or false. Then explain why your answer is correct, based on the Slutsky decomposition into income and substitution effects.  
(a) “If both current and future consumption are normal goods, an increase in the interest rate will necessarily make a saver save more.” False. Substitution effect makes him consume less in period 1 and save more. For a saver, income effect works in opposite direction. Either effect could dominate.  
(b) “If both current and future consumption are normal goods, an increase in the interest rate will necessarily make a saver choose more consumption in the second period.” True. The income and substitution effects both lead to more consumption in the second period.  

10.5 (1) Laertes has an endowment of $20 each period. He can borrow money at an interest rate of 200%, and he can lend money at a rate of 0%. (Note: If the interest rate is 0%, for every dollar that you save, you get back $1 in the next period. If the interest rate is 200%, then for every dollar you borrow, you have to pay back $3 in the next period.)
```

**公式及数值：**
- 部分 (g)：最优消费点公式推导基于跨期预算约束和效用最大化。
  - 期 1 消费：\( C_1 = 1,458.3 \)（单位：美元），对应图中刻度 \( C_1 = 1.4583 \)（千美元）。
  - 期 2 消费：\( C_2 = 1,750 \)（单位：美元），对应图中刻度 \( C_2 = 1.75 \)（千美元）。
- 部分 (h)：储蓄计算公式（基于禀赋点）：
  - 储蓄 \( = m_1 - C_1 = 2,000 - 1,458.3 = 541.7 \) 美元。
- 部分 (g) 和 (h) 的数值验证：
  - 新利率 \( r = 20\% \)，预算现值 \( m = m_1 + \frac{m_2}{1+r} = 2,000 + \frac{1,100}{1.2} \approx 2,916.67 \) 美元。
  - 消费函数：\( U = C_1 C_2 \)（\( a = 0.5 \)），故 \( C_1 = 0.5 \times m = 0.5 \times 2,916.67 = 1,458.3 \)，\( C_2 = 0.5 \times m \times (1+r) = 0.5 \times 2,916.67 \times 1.2 = 1,750 \).

---

#### 2. 图表变化含义解释（基于上文知识点总结）
当前图片虽无显式图表，但部分 (f) 描述了 **利率上升至 20% 时预算线的变化**，需结合上文知识点总结中的图表结构进行解读。上文已定义：
- 横轴 \( C_1 \)（期 1 消费，单位：千美元），纵轴 \( C_2 \)（期 2 消费，单位：千美元）。
- 基准预算线（蓝色）：斜率 \( -(1+r) = -1.1 \)（对应 \( r = 10\% \))，预算方程 \( C_1 + \frac{C_2}{1.1} = 3.0 \)（现值 3,000 美元）。
- 禀赋点 \( E \)：固定于 \( (C_1, C_2) = (2.0, 1.1) \)（即 \( m_1 = 2,000 \), \( m_2 = 1,100 \) 单位）。

##### 利率上升至 20% 时的预算线变化（红线）
- **斜率变化**：  
  新预算线斜率 \( = -(1 + r_{\text{new}}) = -1.2 \)（因 \( r = 20\% \))，比基准斜率 \( -1.1 \) 更陡峭。这直接体现 **时间价格比** \( p_1 / p_2 = 1 + r \) 的上升，强化了“跨期选择中未来消费相对成本降低”的核心机制（上文 2. 知识点解析）。
  
- **现值与端点变化**：  
  - 预算现值 \( m \) 从基准 \( 3.0 \)（千美元）降至 \( m = m_1 + \frac{m_2}{1 + r} = 2.0 + \frac{1.1}{1.2} \approx 2.9167 \)（千美元）。
  - 端点：
    - 当 \( C_2 = 0 \)，\( C_1 = m \approx 2.9167 \)（千美元）→ 基准为 3.0，**下降**（因 \( m_2 \) 现值随 \( r \) 上升而减少）。
    - 当 \( C_1 = 0 \)，\( C_2 = m \times (1 + r) \approx 2.9167 \times 1.2 = 3.5 \)（千美元）→ 基准为 3.3，**上升**（储蓄收益更高）。
  - **含义**：收入现值微降（上文未涵盖），但未来消费潜力扩大，凸显利率变化对 **跨期资源分配** 的杠杆效应（衔接上文 2.3 节 MRS 条件）。

- **旋转特性**：  
  新预算线围绕禀赋点 \( E = (2.0, 1.1) \) **顺时针旋转**：
  - 当 \( C_1 < m_1 \)（储蓄区，如期 1 消费低于 2,000 美元）：新预算线在基准线上方（例：\( C_1 = 1.5 \) 时，新 \( C_2^{\max} = 1.7 \) vs 基准 \( 1.65 \))，代表储蓄回报提升。
  - 当 \( C_1 > m_1 \)（借款区）：新预算线在基准线下方（例：\( C_1 = 2.5 \) 时，新 \( C_2^{\max} = 0.5 \) vs 基准 \( 0.55 \))，借贷成本更高。
  - **经济含义**：此旋转是 **斯勒茨基分解** 的基础（衔接上文 10.4 部分）。作为净储蓄者（基准 \( C_1 = 1.5 < 2.0 \))，替代效应（未来消费相对便宜）和收入效应（整体福利微降）共同作用，但替代效应通常主导（部分 (g) 和 (h) 显示 \( C_1 \) 减少、储蓄增加）。

##### WARP 对新选择的约束（部分 (f) 解析）
- **关键机制**：  
  基准选择点 \( a = (1.5, 1.65) \) 在新预算集内部（因 \( 1.5 + \frac{1.65}{1.2} = 2.875 < 2.9167 \))。由 **弱公理显示性偏好（WARP）**：
  - 旧预算集可行但未选的点，不得成为新选择（因显示偏好传递）。
  - 新预算线上，部分区域在旧预算集可行：当 \( C_1 \geq m_1 = 2.0 \)（千美元），即借款区（例：\( C_1 = 2.5 \)，新 \( C_2 = 0.5 \)，满足旧约束 \( 2.5 + \frac{0.5}{1.1} \approx 2.955 \leq 3 \))。
- **不可选择区域**：  
  需在 **红线上 \( C_1 \geq 2.0 \) 的部分** 标记“squiggly mark”（波浪线），因为：
  - 此区域在旧预算下可行但未选（基准选 \( C_1 = 1.5 < 2.0 \))。
  - 若新选择落在此处，违反 WARP（因旧选择点 \( a \) 显示偏好于这些点）。
  - **上文延续**：上文指出 Red line “无利率变化场景”，但此处用于 **利率变动拓展分析**（上文（d）部分隐含），凸显图表对“动态均衡”的支撑作用（连接上文 3. 与后续问题的关联）。

##### 与上文计算结果的呼应
- **最优点变动**（部分 (g) 和 (h)）：
  - 期 1 消费从 \( 1,500 \) → \( 1,458.3 \) 美元（下降），期 2 消费从 \( 1,650 \) → \( 1,750 \) 美元（上升）。
  - 储蓄从 \( 500 \) → \( 541.7 \) 美元，增幅 \( 8.34\% \)。
  - **含义**：验证替代效应主导（上文 10.4(a) 结论），未来消费增加是收入与替代效应同向作用的结果（上文 10.4(b) 正确）。
- **深层关联**：  
  数值结果固化“参数化需求函数”逻辑（上文（c）部分）：利率上升时，\( C_1 = a \cdot m \) 的减小源于 \( m \) 微降和偏好权重不变（\( a = 0.5 \))，体现微观经济学“理论→应用”的连续性（上文 3. 总结）。

> **注**：当前图表无通胀或收入变动，故 **Red line 仅反映利率冲击**。上文缺失的利率变化分析（上文（d）部分）在此补全，且部分 (f) 的 WARP 约束强化了“基于数据推断行为”的实证方法（避免重复上文废话，但延续理论脉络）。

---
### Page/Slide 6



### 当前图片内容提取与解析

#### 1. 文字与公式提取
- **页码与章节**：136, INTERTEMPORAL CHOICE (Ch. 10)
- **问题 (a)**：  
  > Use blue ink to illustrate his budget set in the graph below. (Hint: The boundary of the budget set is not a single straight line.)
- **图表参数**：
  - 横轴 $ C_1 $：范围 0–40
  - 纵轴 $ C_2 $：范围 0–40
  - 标注线：
    - Blue line（蓝色线）
    - Red line（红色线）
    - Black line（黑色线）
- **问题 (b)**：  
  > Laertes could invest in a project that would leave him with $ m_1 = 30 $ and $ m_2 = 15 $. Besides investing in the project, he can still borrow at 200% interest or lend at 0% interest. Use red ink to draw the new budget set in the graph above. Would Laertes be better off or worse off by investing in this project given his possibilities for borrowing or lending? Or can’t one tell without knowing something about his preferences? Explain.  
  > **Better off. If he invests in the project, he can borrow or lend to get any bundle he could afford without investing.**
- **问题 (c)**：  
  > Consider an alternative project that would leave Laertes with the endowment $ m_1 = 15 $, $ m_2 = 30 $. Again suppose he can borrow and lend as above. But if he chooses this project, he can’t do the first project. Use pencil or black ink to draw the budget set available to Laertes if he chooses this project. Is Laertes better off or worse off by choosing this project than if he didn’t choose either project? Or can’t one tell without knowing more about his preferences? Explain.  
  > **Can’t tell. He can afford some things he couldn’t afford originally. But some things he could afford before, he can’t afford if he invests in this project.**
- **附加内容**：  
  > 10.6 (0) The table below reports the inflation rate and the annual rate of return on treasury bills in several countries for the years 1984 and 1985.

#### 2. 图表分析（结合上文知识点总结）
当前图表展示跨期预算集在投资冲击下的变化，与上文**利率变化场景形成互补**：上文（知识点总结）聚焦利率参数变化导致的预算线旋转，本图聚焦投资项目引发的禀赋点离散移动。关键点如下：

##### **预算集结构与旋转特性**
- **非直线边界成因**：  
  图中预算线转折源于借贷利率非对称（borrow at 200% ⇒ $1 + r_b = 3$; lend at 0% ⇒ $1 + r_l = 1$），这与上文**利率变化分析的延伸**一致：
  - 当 $C_1 \leq m_1$（储蓄区），预算线斜率为 $-(1 + r_l) = -1$（对应 Blue/Black/Red line 左段）。
  - 当 $C_1 > m_1$（借款区），预算线斜率为 $-(1 + r_b) = -3$（对应各线右段）。  
  **衔接上文**：这强化了上文 2.3 节“跨期资源分配”的核心机制——利率差异直接塑造预算集形状，为斯勒茨基分解（替代/收入效应）提供几何基础。

- **各线经济含义**：
  | 线色 | 对应场景 | 禀赋点 | 几何特征 | 与上文知识点关联 |
  |------|----------|--------|----------|------------------|
  | Blue line | 基准预算集 | 隐含初始 $m_1, m_2$ | 拐点位于初始禀赋（图中约 $C_1=20$） | 类比上文基准 $E=(2.0,1.1)$，但此处因借贷利率非对称，拐点更陡峭 |
  | **Red line** | 项目 1 后 ($m_1=30, m_2=15$) | $(30, 15)$ | 完全覆盖 Blue line 区域 | 对应上文 **WARP 约束分析**：</br>- 新预算集包含原集 ⇒ 严格更好（无需偏好）</br>- 印证上文部分 (f) "新选择不可落于原可行区" 的逻辑 |
  | Black line | 项目 2 后 ($m_1=15, m_2=30$) | $(15, 30)$ | 部分重叠 Blue line，但互有不可达区域 | 延续上文 **"无偏好信息难判" 原则**：</br>- 与 Blue line 交叉 ⇒ 无法确定福利变化（呼应上文部分 (g) 对偏好权重的依赖） |

##### **关键变化含义**
- **Red line 作为 WARP 的实证验证**：  
  - 上文知识点总结指出 Red line 用于标记利率变化下的不可选区域（如 $C_1 \geq m_1$ 的借款区）。本图将 **WARP 从参数变化拓展至离散投资冲击**：
    - 项目 1 使新预算集（Red line）完全包含原集 ⇒ 若投资，消费者能达成原集所有选择，严格更好（答案已确认）。
    - 这直接体现 **WARP 的弱公理本质**：原预算可行点未被选则新集仍可行，但新集因扩展而严格支配旧集（对比上文部分 (f) 中利率上升时基准点 $a$ 落入新集内部的约束）。
  - **深层连续性**：上文通过利率参数化推导动态，本图用离散项目验证 **预算集包含关系是福利判定的核心**（衔接上文 3. 与后续问题的关联）。

- **Black line 与偏好敏感性**：  
  - 新预算集（Black line）与 Blue line 交叉，导致：
    - $C_1$ 较低时（未来高消费区），Black line 扩展可行集（$m_2=30$ 提升 $C_2$ 潜力）。
    - $C_1$ 较高时（当前高消费区），Black line 收缩可行集（$m_1=15 < $ 原 $m_1$）。  
  - **呼应上文斯勒茨基分析**：  
    - 类似上文利率上升时的 "储蓄区 vs 借款区" 分化（$C_1 < m_1$ 时新线在上方，$C_1 > m_1$ 时在下方）。
    - 本图中项目 2 使禀赋点右移至 $(15,30)$，效果等价于 **隐性收入效应扭转载体**（上文部分 (h) 储蓄增 8.34% 的根因），但因无偏好信息，净效用增减未知。

##### **结论方向**
本图以项目投资为载体，将上文 **利率参数变化** 拓展至 **禀赋点离散变动**，印证微观核心原理：
- 预算集几何形状（旋转/平移/包含）直接决定福利比较可能性。
- **WARP 的普适性**：无论利率连续变化（上文）或项目离散选择（本图），可行集关系是偏好推断基石。
- **与上文闭环**：数值计算（如上文 $C_1$ 从 1.5→1.458.3）转为图像逻辑，体现理论从参数化需求到图形化验证的连续性。

---
### Page/Slide 7



### 当前图片内容提取与解析

#### 1. 文字与公式提取
**标题**  
Inflation Rate and Interest Rate for Selected Countries  

**表格内容**  
| Country      | % Inflation Rate, 1984 | % Inflation Rate, 1985 | % Interest Rate, 1984 | % Interest Rate, 1985 |  
|--------------|------------------------|------------------------|------------------------|------------------------|  
| United States| 3.6                   | 1.9                   | 9.6                   | 7.5                   |  
| Israel       | 304.6                 | 48.1                  | 217.3                 | 210.1                 |  
| Switzerland  | 3.1                   | 0.8                   | 3.6                   | 4.1                   |  
| W. Germany   | 2.2                   | -0.2                  | 5.3                   | 4.2                   |  
| Italy        | 9.2                   | 5.8                   | 15.3                  | 13.9                  |  
| Argentina    | 90.0                  | 672.2                 | NA                    | NA                    |  
| Japan        | 0.6                   | 2.0                   | NA                    | NA                    |  

**问题与解答**  
- **(a)** In the table below, use the formula that your textbook gives for the exact real rate of interest to compute the exact real rates of interest.  
  *（公式隐含：精确实际利率 = $\frac{1 + \text{名义利率}}{1 + \text{通胀率}} - 1$）*  
- **(b)** What would the nominal rate of return on a bond in Argentina have to be to give a real rate of return of 5% in 1985? **710.8%**. What would the nominal rate of return on a bond in Japan have to be to give a real rate of return of 5% in 1985? **7.1%**.  
  *（计算公式：名义利率 = $(1 + \text{实际利率}) \times (1 + \text{通胀率}) - 1$）*  
- **(c)** Subtracting the inflation rate from the nominal rate of return gives a good approximation to the real rate for countries with a low rate of inflation. For the United States in 1984, the approximation gives you **6%** while the more exact method suggested by the text gives you **5.79%**. But for countries with very high inflation this is a poor approximation. The approximation gives you **-87.3%** for Israel in 1984, while the more exact formula gives you **-21.57%**. For Argentina in 1985, the approximation would tell us that a bond yielding a nominal rate of **677.7%** would yield a real interest rate of 5%. This contrasts with the answer **710.8%** that you found above.  

---

#### 2. 与上文知识点的关联解析
当前图片聚焦**实际利率的计算与近似**，虽无图表，但内容直接衔接上文知识点总结中关于**利率参数化对跨期决策的影响**，尤其强化了微观经济理论的核心机制：

- **实际利率作为跨期预算线的关键参数**  
  上文知识点总结（利率变化场景）强调预算线斜率由实际利率决定（如 $-(1 + r_l)$ 或 $-(1 + r_b)$）。此处精确公式 $\frac{1 + i}{1 + \pi} - 1$ 用于推导实际利率 $r$，其值直接决定跨期预算集的几何形状：  
  - 当 $r$ 已知时，预算线斜率 $-(1 + r)$ 的计算成为现实基础（例如，美国1984年精确 $r=5.79\%$，预算线斜率约为 $-1.0579$）。  
  - **知识连续性体现**：上文通过利率参数化分析预算线旋转，此处通过通胀调整将名义利率转化为实际利率，印证了 **“偏好优化依赖于实际利率而非名义利率”** 的微观原理（呼应上文2.3节跨期资源分配的起点）。

- **高通胀下近似方法的失效与微观福利判定**  
  问题(c)凸显近似法（名义利率 $-$ 通胀率）在高通胀国家（如以色列、阿根廷）的偏差：  
  - 以色列1984年近似值 $-87.3\%$ 与精确值 $-21.57\%$ 的显著差异，揭示若错误使用名义利率，可能导致预算集边界扭曲（如预算线斜率计算错误）。  
  - **与上文WARP逻辑的延伸**：上文指出预算集包含关系是福利判定的基石（如Red line完全覆盖Blue line则严格更好）。此处若因高通胀误用近似利率：  
    - 消费者可能误判跨期选择集（如阿根廷1985年实际利率5%需名义利率710.8%，而非近似的677.7%），  
    - 导致WARP检验失效（因可行集被错误定义），进而无法正确推断偏好（呼应上文Black line场景中“无偏好信息难判福利”的原则）。  

- **实证验证微观理论的普适性**  
  - 问题(b)的计算（如阿根廷名义利率710.8%）直接应用于跨期决策：若消费者面临此利率环境，其禀赋点移动（例如项目投资）需以精确实际利率校准预算集。  
  - **深层连续性**：上文通过参数化利率推导动态，此处用真实国家数据验证 **“实际利率是预算集形变的唯一驱动”**，闭合了从理论模型（上文图表）到实证（本图数据）的逻辑链——这与上文结论方向一致：福利比较必须基于精确实际利率的预算集几何分析。  

> **关键启示**：上文分析利率变化导致的预算线旋转，本图通过通胀调整将名义利率还原为实际利率，表明 **“跨期决策的微观基础必须剔除通胀噪声”**。若忽略此步骤（如误用近似法），预算集几何结构将失真，导致斯勒茨基分解或WARP应用错误。

---
### Page/Slide 8



### 提取内容  
- **标题与页码**：138 INTERTEMPORAL CHOICE (Ch. 10)  
- **表格文字**：  
  | Country      | 1984     | 1985    |  
  |--------------|----------|---------|  
  | United States| $5.7$    | $5.5$   |  
  | Israel       | $-21.57$ | $109.4$ |  
  | Switzerland  | $0.5$    | $3.33$  |  
  | W. Germany   | $3.0$    | $4.4$   |  
  | Italy        | $5.6$    | $7.6$   |  
- **问题文字**：  
  > **10.7 (0)** We return to the planet Mungo. On Mungo, macroeconomists and bankers are jolly, clever creatures, and there are two kinds of money, red money and blue money. Recall that to buy something in Mungo you have to pay for it twice, once with blue money and once with red money. Everything has a blue-money price and a red-money price, and nobody is ever allowed to trade one kind of money for the other. There is a blue-money bank where you can borrow and lend blue money at a **50%** annual interest rate. There is a red-money bank where you can borrow and lend red money at a **25%** annual interest rate.  
  >  
  > A Mungoan named Jane consumes only one commodity, ambrosia, but it must decide how to allocate its consumption between this year and next year. Jane’s income this year is **100 blue currency units** and **no red currency units**. Next year, its income will be **100 red currency units** and **no blue currency units**. The blue currency price of ambrosia is **one b.c.u. per flagon this year** and will be **two b.c.u.’s per flagon next year**. The red currency price of ambrosia is **one r.c.u. per flagon this year** and will be the same next year.  
  >  
  > **(a)** If Jane spent all of its blue income in the first period, it would be enough to pay the blue price for **100 flagons** of ambrosia. If Jane saved all of this year’s blue income at the blue-money bank, it would have **150 b.c.u.’s next year**. This would give it enough blue currency to pay the blue price for **75 flagons** of ambrosia. On the graph below, draw Jane’s blue budget line, depicting all of those combinations of current and next period’s consumption that it has enough blue income to buy.  

- **隐含公式**：  
  - 蓝货币储蓄实际回报率计算：  
    $\frac{150 \text{ b.c.u.}}{100 \text{ b.c.u.}} = 1.5$（名义回报率），结合价格变化（本年价格 1 b.c.u./flagon，次年 2 b.c.u./flagon），实际消费能力比率 = $\frac{150 / 2}{100 / 1} = 0.75$，隐含实际利率 $r = 0.75 - 1 = -25\%$。  
  - 无显式公式列表，但利率参数（50%、25%）和价格机制构成跨期预算约束基础。  

### 与上文知识点的关联解析  
上文知识点聚焦**实际利率在跨期预算约束中的核心作用**及**高通胀下近似法失效**，当前图片以实证数据和寓言模型强化这一逻辑链，保持微观理论连续性：  

- **国家实际利率数据是对上文计算框架的直接验证**  
  表格中 1984 年以色列实际利率 $-21.57\%$ 与上文知识点完全匹配，印证精确公式 $\frac{1+i}{1+\pi} - 1$ 的必要性；1985 年以色列 $109.4\%$ 的高正值进一步说明：当通胀剧烈波动（如上文阿根廷场景），近似法 $(i - \pi)$ 会系统性扭曲预算集（-Israel 1984 近似值 $-87.3\%$ 误差率达 300%）。这直接支撑上文结论——**实际利率是跨期决策的唯一有效参数**，且高通胀下必须用精确公式，否则预算线斜率 $-(1 + r)$ 会失真（例如，若误用近似值，以色列 1984 年预算线斜率可能从 $-(1 - 0.2157) \approx -0.784$ 错算为 $-(1 - 0.873) \approx -0.127$，导致消费者选择集严重变形）。  

- **Mungo 寓言模型深化预算集形变机制**  
  蓝货币系统中（储蓄利率 50%、价格从 1→2 b.c.u./flagon），Jane 的消费组合隐含实际利率 $-25\%$：  
  - 本年全额消费 → 100 flagons；  
  - 次年全额消费 → 75 flagons；  
  预算线斜率 $= -75/100 = -0.75$，对应 $-(1 + r) = -0.75$，故 $r = -25\%$。  
  这验证了上文**“预算线斜率由实际利率决定”**的核心机制：  
  - 价格通胀（100%）抵消名义利率（50%），导致负实际利率，使预算集向“牺牲当前消费”的方向偏转（类比上文高通胀国家）；  
  - 与上文 WARP 逻辑衔接：若忽略通胀（如仅用名义利率 50%），会高估次年消费能力（误算为 150 flagons 而非 75），进而扭曲可行集边界，使偏好推断失效（呼应上文“错误参数化导致福利判定错误”）。  

- **双货币系统凸显实际利率的普适性**  
  寓言中红货币（价格稳定、利率 25%）与蓝货币（价格膨胀）并行，但跨期决策仍需以 **实际相对价格** 为基准——这延续上文“名义变量需经通胀校准”的论点。例如：  
  - 红货币实际利率恒为 25%，预算线斜率 $-1.25$；  
  - 蓝货币因通胀，实际利率 $-25\%$，预算线斜率 $-0.75$；  
  两者独立构成约束，印证**“跨期福利分析依赖精确实际利率”** 的微观原理（上文关键启示）。无图表故不展开几何意义，但文字描述已清晰展示：实际利率通过 $-(1 + r)$ 量化消费跨期替代成本，与上文参数化分析（如预算线旋转）无缝衔接。  

> **逻辑闭合点**：上文通过美以数据论证精确利率计算必要性，本图以真实表格复现实证，并通过寓言模型将理论落地为操作化框架——消费者无论面对国家通胀或奇异货币系统，**预算集形变始终由实际利率驱动**，再次确证微观跨期选择的通胀不变性。

---
### Page/Slide 9



### 提取内容  
#### 文字  
- 图表标题：  
  - 纵轴：`Ambrosia next period`  
  - 横轴：`Ambrosia this period`  
- 图表下方文本：  
  > (b) If Jane planned to spend no red income in the next period and to borrow as much red currency as it can pay back with interest with next period’s red income, how much red currency could it borrow? **80**.  
  >  
  > (c) The (exact) real rate of interest on blue money is **$-25\%$**. The real rate of interest on red money is **$25\%$**.  
  >  
  > (d) On the axes below, draw Jane’s blue budget line and its red budget line. Shade in all of those combinations of current and future ambrosia consumption that Jane can afford given that it has to pay with both currencies.  

#### 公式  
- 蓝货币实际利率：$r_b = -25\%$  
- 红货币实际利率：$r_r = 25\%$  
- 预算线斜率隐含公式：  
  - 蓝预算线斜率 $= -\left(1 + r_b\right) = -(1 - 0.25) = -0.75$  
  - 红预算线斜率理论值 $= -\left(1 + r_r\right) = -(1 + 0.25) = -1.25$（需结合(d)部分绘制）  

#### 图表  
- 绘制了一条直线，连接点 $(c_0, c_1) = (100, 0)$ 和 $(0, 75)$，其中 $c_0$ 为当前消费量（横轴），$c_1$ 为下期消费量（纵轴）。  
- 网格坐标系范围：  
  - 横轴：$0$ 至 $100$（步长 $25$）  
  - 纵轴：$0$ 至 $100$（步长 $25$）  

---

### 图表变化的含义解析  
#### **1. 蓝预算线的几何意义与实际利率的映射**  
- **斜率解读**：  
  当前图表中的蓝预算线斜率为 $-0.75$，直接对应 $\left|-\left(1 + r_b\right)\right|

- **与上文通胀-利率机制的关联**：  
  上文已论证高通胀会抵消名义利率，导致实际利率为负（此处 $r_b = -25\%$）。本图表通过预算线斜率量化工了这一机制：  
  - **名义参数**：蓝货币名义储蓄回报率 $50\%$（$150/100$），但次年价格翻倍（$2 \text{ b.c.u./flagon}$），实际消费能力从 $150$ 单位货币降至 $75$ flagons。  
  - **实际约束**：放弃 $1$ 单位当前消费（$c_0$），仅能增加 $0.75$ 单位下期消费（$c_1$），反映通胀侵蚀了储蓄价值。这与上文以色列1984年案例一致——实际利率 $-21.57\%$ 使预算线斜率接近 $-0.78$（而非名义利率误导的 $-1.5$）。  
  - **关键推论**：预算线平缓化（斜率 $-0.75 > -1$）意味着 **跨期替代成本降低**，消费者无动力储蓄（上文宏观数据已警示此情形下福利损失），呼应上文“高通胀扭曲预算集，驱动当前消费倾向”的结论。  

#### **2. 与红货币系统的对比及可行集含义**  
- **红预算线的隐含作用**：  
  文本(c)明确红货币实际利率 $r_r = 25\%$（价格稳定），理论预算线斜率 $-1.25$。这代表：  
  - 放弃 $1$ 单位 $c_0$ 可换取 $1.25$ 单位 $c_1$，凸显正实际利率下的储蓄激励。  
  - 与蓝预算线（斜率 $-0.75$）形成鲜明对比，直观展示 **实际利率而非名义利率决定跨期替代弹性**（上文已通过阿根廷/以色列数据强调此点）。  
- **双货币系统的可行集逻辑（基于(d)部分）**：  
  Jane需用两种货币支付，可行消费集为两条预算线的交集：  
  - 蓝预算线边界：$c_1 = 75 - 0.75c_0$  
  - 红预算线边界：假设本年收入 $100$ red c.u.（类比蓝货币），则 $c_1 = 125 - 1.25c_0$（因 $r_r=25\%$）  
  - **可行区域特征**：阴影区将是两条预算线左侧的交集，反映消费者受双重货币约束。例如，当 $c_0=0$，蓝边界 $c_1=75$，红边界 $c_1=125$，但实际 $c_1$ 受限于 $75$（蓝货币通胀导致下期能力更低）。这强化了上文核心—— **通胀会系统性压缩未来消费能力，使实际利率成为唯一有效决策参数**（误用名义利率将高估红/蓝边界，如同上文近似法导致的 $300\%$ 误差）。  

#### **3. 对跨期选择理论的实证延伸**  
- **预算线形变与WARP验证**：  
  图表中蓝预算线的平缓形态直接源于实际利率 $-25\%$，印证上文“预算集形变由实际利率驱动”的微观机制。若忽略通胀（如仅用 $50\%$ 名义利率），会误判预算线斜率为 $-1.5$（即 $c_1 = 150 - 1.5c_0$），导致可行集虚增 $100\%$（下期消费能力误算为 $150$ flagons）。这将扭曲偏好推断（上文指出错误参数化使WARP失效），而本图表通过 $75$ vs $150$ 的实证值，实操化了“实际利率校准必要性”的理论。  
- **政策启示衔接**：  
  蓝预算线的负斜率（$-0.75$）量化了高通胀对消费的抑制——与上文以色列1985年 $109.4\%$ 正实际利率时陡峭预算线（斜率 $-2.09$）对比，揭示 **通胀波动幅度决定跨期决策扭曲程度**。这为宏观政策提供了微观基础：稳定通胀可使实际利率更接近名义值，简化消费者决策（如红货币场景）。  

> **理论延续性**：本图表将上文抽象公式（$\frac{1+i}{1+\pi} - 1$）落地为直观预算线，完整呈现“名义变量→通胀校准→实际利率→预算集形变”逻辑链。与上文数据表不同，此处通过双货币寓言模型，凸显 **任何货币系统均需以实际相对价格校准，否则福利分析必失真**，进一步巩固跨期选择理论的通胀不变性原理。

---
### Page/Slide 10



### 详细解析：跨期选择图表

#### 1. 提取图片中的所有文字与公式
- **标题与章节**：  
  `140 INTERTEMPORAL CHOICE (Ch. 10)`
  
- **图表坐标轴**：  
  - 横轴：`Ambrosia this period`（范围 0 至 100，步长 25）  
  - 纵轴：`Ambrosia next period`（范围 0 至 100，步长 25）  

- **图表元素**：  
  - 蓝色直线标注：`Blue line`  
  - 红色直线标注：`Red line`  
  - 点标记：`C`（位于图表内，初始位置约 `(25, 56.25)`）  

- **图表下方文本**：  
  - `(e) It turns out that Jane finds it optimal to operate on its blue budget line and beneath its red budget line. Find such a point on your graph and mark it with a C.`  
  - `(f) On the following graph, show what happens to Jane’s original budget set if the blue interest rate rises and the red interest rate does not change. On your graph, shade in the part of the new budget line where Jane’s new demand could possibly be. (Hint: Apply the principle of revealed preference. Think about what bundles were available but rejected when Jane chose to consume at C before the change in blue interest rates.)`  

- **隐含公式（基于上下文与图表几何）**：  
  - 蓝预算线方程：`c₁ = 75 - 0.75c₀`  
  - 红预算线方程（理论值，图中因 Y 轴上限截断）：`c₁ = 125 - 1.25c₀`  

> **注**：图中无显式公式，但预算线斜率与截距可推导为上述方程，与上文知识点一致。

---

#### 2. 图表变化的含义解析（基于上文知识点）

##### **2.1 预算线形态与实际利率的微观映射**
- **蓝预算线（浅斜率，`slope ≈ -0.75`）**：  
  - 视觉上更平缓，源于实际利率 `r_b = -25%`（上文已证，通胀抵消名义回报）。  
  - 经济含义：放弃 1 单位当前消费仅增益 0.75 单位下期消费，直观体现通胀对储蓄价值的侵蚀（例如，名义 50% 回报被价格翻倍抵消，实际消费能力从 150 降至 75）。  
  - 与上文以色列 1984 年数据呼应：真实世界中，实际利率负值使预算线斜率平缓化（斜率 `-0.75 > -1`），驱动消费者偏好当前消费，避免福利损失。

- **红预算线（陡峭斜率，`slope ≈ -1.25`）**：  
  - 视觉上更陡峭，源于实际利率 `r_r = 25%`（价格稳定）。  
  - 经济含义：放弃 1 单位当前消费可增益 1.25 单位下期消费，突出正实际利率对储蓄的激励。  
  - 对比意义：双线斜率差异（`-0.75` vs `-1.25`）直接量化 **实际利率而非名义利率决定跨期替代弹性**，实证化上文核心结论——误用名义利率（如将蓝货币误判为 `-1.5`）将虚增可行集规模。

##### **2.2 阴影区域与双货币可行集的逻辑延伸**
- **可行集特征**：  
  - 图中阴影区为两条预算线的交集（`c₁ ≤ min(75 - 0.75c₀, 125 - 1.25c₀)`），但因蓝线全程低于红线（`c₀ ∈ [0, 100)`），阴影区实际由蓝预算线界定（`c₁ ≤ 75 - 0.75c₀`）。  
  - 关键验证：当 `c₀ = 0` 时，蓝边界 `c₁ = 75` 而红边界 `c₁ = 125`，但下期消费受限于 75，印证上文“通胀系统性压缩未来消费能力”。

- **点 C 的优化选择含义**：  
  - 位置（如 `(25, 56.25)`）落于蓝预算线上（`c₁ = 75 - 0.75×25 = 56.25`），且必然在红线下方（红预算线在 `c₀=25` 时 `c₁=93.75 > 56.25`）。  
  - 行为学意义：Jane 的选择受紧约束（蓝预算线）主导，验证实际利率是唯一有效决策参数——若忽略通胀（如误用名义利率），将扭曲偏好推断（上文指出错误参数化致 WARP 失效）。

##### **2.3 对后续分析（部分 f）的铺垫**
- **利息率变化的前瞻性**：  
  - 部分 `(f)` 暗示蓝利息率上升（即 `r_b` 负值减小或转正），蓝线斜率绝对值增大（更陡峭），可行集向外扩展。  
  - 基于点 C 的**显示性偏好原理**：  
    - C 点被选时，所有曾可行但被拒绝的束（即 C 点东北方向、蓝线下方区域）为初始预算集内劣等选择。  
    - 利率上升后，新预算集包含部分原拒绝束，但仅 **新预算线中未包含初始拒绝束的区域** 可能成为新需求点（上文宏观数据佐证：实际利率波动幅度直接决定消费决策扭曲程度）。  
  - 政策启示：此机制凸显稳定通胀的重要性——若红货币系统（价格稳定）普适，实际利率近似名义值，可简化决策，呼应上文跨期选择理论的通胀不变性原理。

> **知识连续性说明**：本图表将抽象公式 `c₁ = \text{intercept} + \text{slope} \times c₀` 转化为几何形态，实操化验证“名义变量 → 通胀校准 → 实际利率 → 预算集形变”逻辑链。与上文数据表互补，突出问题本质——**任何货币系统均需以实际相对价格校准，否则福利分析失真**。

---
### Page/Slide 11



### 当前图片内容提取

#### 文字与公式
**图表标签及坐标：**
- 横轴（X轴）：`Ambrosia this period`（刻度：0, 25, 50, 75, 100）
- 纵轴（Y轴）：`Ambrosia next period`（刻度：0, 25, 50, 75, 100）
- 线条标识：
  - `Red line`（红实线）
  - `Blue line`（蓝实线）
  - `New blue line`（新蓝虚线）
  - `Shaded region`（阴影区域）
- 点标识：`c`（实心点，位于初始预算线）

**图像下方文本：**
- **10.8 (0)**  
  Mr. O. B. Kandle will only live for two periods. In the first period he will earn $50,000. In the second period he will retire and live on his savings. His utility function is \( U(c_1, c_2) = c_1 c_2 \), where \( c_1 \) is consumption in period 1 and \( c_2 \) is consumption in period 2. He can borrow and lend at the interest rate \( r = 0.10 \).  
  - (a) If the interest rate rises, will his period-1 consumption increase, decrease, or stay the same?  
    **Stay the same.** His demand for \( c_1 \) is \( 0.5(m_1 + m_2 / (1 + r)) \) and \( m_2 = 0 \).  
  - (b) Would an increase in the interest rate make him consume more or less in the second period?  
    **More.** He saves the same amount, but with higher interest rates, he gets more back next period.  
  - (c) If Mr. Kandle’s income is zero in period 1, and $55,000 in period 2, would an increase in the interest rate make him consume more, less, or the same amount in period 1?  
    **Less.**  
- **10.9 (1)**  
  Harvey Habit’s utility function is \( U(c_1, c_2) = \min\{c_1, c_2\} \), where \( c_1 \) is his consumption of bread in period 1 and \( c_2 \) is his consumption of bread in period 2. The price of bread is $1 per loaf in period 1. The interest rate is 21%. Harvey earns $2,000 in period 1 and he will earn $1,100 in period 2.

**显式公式：**
- 效用函数：\( U(c_1, c_2) = c_1 c_2 \)（10.8）、\( U(c_1, c_2) = \min\{c_1, c_2\} \)（10.9）
- 消费需求：\( c_1 = 0.5(m_1 + m_2 / (1 + r)) \)（10.8a）
- 利率参数：\( r = 0.10 \)（10.8）、\( r = 21\% \)（10.9）

---

### 图表变化的含义解析

#### **1. 预算线形态与利率变化的映射**
- **蓝实线（初始预算线）**：  
  代表初始利率 \( r = 0.10 \) 下的跨期约束。其斜率绝对值为 \( 1 + r = 1.10 \)，几何上表现为平缓程度介于上文【蓝预算线】（负实际利率）与【红预算线】（正实际利率）之间（上文斜率参考：`-0.75` 和 `-1.25`）。结合10.8(a)，此线界定可行集 \( c_2 = (1 + r)m_1 - (1 + r)c_1 \)（即 \( c_2 = 55,000 - 1.1c_1 \)），但图表单位标准化后，截距与斜率与上文公式逻辑一致。  
  - **经济含义延续性**：与上文以色列案例呼应，此处正名义利率（`r=10%`）直接反映实际利率（无通胀），避免了上文中通胀导致的预算线扭曲。点 `c` 位于其上，验证了上文“实际利率是决策核心参数”的结论。

- **新蓝虚线（利率上升后预算线）**：  
  利率上升导致斜率绝对值增大（例如至 \( 1.2 \) 或更高），几何上更陡峭。这直接量化了 `r` 增加对跨期替代的强化：放弃 1 单位本期消费可获更多下期消费，符合10.8(b)中“利率上升，下期消费增加”的机制。  
  - **与上文的逻辑衔接**：上文分析利率变化对可行集的影响（如部分 `f` 的铺垫），此处实证化——新蓝线外移但陡峭化，导致本期消费（`c₁`）在Cobb-Douglas偏好下因收入-替代效应抵消而保持不变（10.8a），呼应上文显示性偏好原理的适用场景。

#### **2. 阴影区域与显示性偏好的核心应用**
- **阴影区域的界定**：  
  图中阴影区域是新蓝虚线的特定段，其边界由点 `c` 和新预算线交点决定（需满足上文显示性偏好条件）。基于【上文知识点总结】的提示：  
  > 点 `c` 被选时，C 点东北方向的区域（即下期消费更高、本期消费更低的束）是初始预算集内被拒绝的劣等选择。  
  - **新需求可能性限制**：当货币集扩展至新蓝线，新需求点不能位于初始被拒绝区域（即不能在 `c` 点以北东方向）。因此，阴影区域仅包含新预算线上**接近或右于** `c` 的部分（几何上，`c₀` 不小于初始 `c₀`），确保不违反WARP（弱显示性偏好公理）。  
  - **为什么排除其他区域？** 若新需求点落在 `c` 点东北方向，将意味着在初始预算集存在更优束却被拒绝，与理性选择矛盾（上文已强调此为福利分析防扭曲的关键）。

- **经济行为学验证**：  
  结合10.8(a)结论（`c₁` 不变），阴影区域垂直跨度窄且水平位置稳定，直观体现Cobb-Douglas偏好下消费者对利率变动的“中性响应”。这与上文“名义利率需校准为实际利率”的论点一致——此处无通胀干扰，利率参数直接有效，故阴影区逻辑与上文推导无缝衔接。

#### **3. 与上文分析的连续性延伸**
- **可行集压缩的反向例证**：  
  上文指出通胀会系统性压缩未来消费能力（蓝线全程低于红线），而此处红实线作为参考线（斜率更陡），暗示若存在另一货币系统（如红货币），其正实际利率将扩大可行集（类似上文红预算线 `c₁ = 125 - 1.25c₀`）。但当前分析聚焦单一货币下利率变动，突出**利率波动幅度而非符号**决定消费决策扭曲程度（10.8c 中收入结构变化导致消费响应转向负向，强化上文“收入约束主导偏好推断”）。
- **政策启示延续**：  
  阴影区域的界定机制，实证化上文“稳定通胀可简化决策”的原理——在此无通胀场景中，利率变动分析直接有效；若引入通胀（如上文以色列案例），需校准实际利率以避免可行集误判，否则阴影区将错误包含被拒绝束，导致需求预测失真。

---
### Page/Slide 12



### Extracted Text and Formulas from Current Image

#### Complete Text:
- "142 INTERTEMPORAL CHOICE (Ch. 10)"
- "(a) Write Harvey’s budget constraint in terms of future value, assuming no inflation. $1.21c_1 + c_2 = 3,520$."
- "(b) How much bread does Harvey consume in the first period and how much money does he save? (The answer is not necessarily an integer.) He picks $c_1 = c_2$. Substitute into the budget to find $c_1 = 3,520 / 2.21 = 1,592.8$. He saves $2,000 - 3,520 / 2.21 = 407.2$."
- "(c) Suppose that Harvey’s money income in both periods is the same as before, the interest rate is still 21%, but there is a 10% inflation rate. Then in period 2, a loaf of bread will cost $1.10$. Write down Harvey’s budget equation for period-1 and period-2 bread, given this new information. $1.21c_1 + 1.1c_2 = 3,520$."
- "10.10 (2) In an isolated mountain village, the only crop is corn. Good harvests alternate with bad harvests. This year the harvest will be 1,000 bushels. Next year it will be 150 bushels. There is no trade with the outside world. Corn can be stored from one year to the next, but rats will eat 25% of what is stored in a year. The villagers have Cobb-Douglas utility functions, $U(c_1, c_2) = c_1 c_2$ where $c_1$ is consumption this year, and $c_2$ is consumption next year."
- "(a) Use red ink to draw a “budget line,” showing consumption possibilities for the village, with this year’s consumption on the horizontal axis and next year’s consumption on the vertical axis. Put numbers on your graph to show where the budget line hits the axes."

#### Key Formulas:
- Harvey's budget constraint (no inflation): $1.21c_1 + c_2 = 3,520$
- Harvey's consumption and savings: $c_1 = 3,520 / 2.21 = 1,592.8$, Savings $= 2,000 - 3,520 / 2.21 = 407.2$
- Harvey's budget constraint (with 10% inflation): $1.21c_1 + 1.1c_2 = 3,520$
- Village utility function: $U(c_1, c_2) = c_1 c_2$
- Village budget equation (25% storage loss): $c_2 = 900 - 0.75c_1$ (implied from the text; illustrated in the red line)

---

### Chart Analysis: Intertemporal Budget Lines in the Village Case

The chart depicts intertemporal consumption possibilities for the mountain village, mirroring the core concepts from the Harvey example but with **biological storage loss** replacing monetary interest. This directly extends the uplink knowledge: just as interest rates shape trade-offs in monetary economies (e.g., Harvey's $r = 21\%$), here the **storage loss rate** acts as a structural "interest rate" in a barter economy. The slopes of the lines quantify the intertemporal trade-off efficiency, while the intercepts reflect endowment constraints.

#### Key Elements of the Chart:
- **Axes**:
  - Horizontal: This year's consumption ($c_1$), with critical points at 1000 (this year's endowment), 1111, and 1136.
  - Vertical: Next year's consumption ($c_2$), with critical points at 150 (next year's endowment), 900, 1150, and 1250.
- **Lines**:
  - **Red line (solid)**: The binding constraint under 25% storage loss (rats eat 25% of stored corn). Hits axes at $(c_1=0, c_2=900)$ and $(c_1=1000, c_2=150)$.
  - **Black line (solid)**: Represents a scenario with **0% storage loss** (no rats). Hits axes at $(c_1=0, c_2=1150)$ and $(c_1=1111, c_2=0)$.
  - **Blue line (dashed)**: Represents a scenario with **negative storage loss** (e.g., crop growth during storage), hitting axes at $(c_1=0, c_2=1250)$ and $(c_1=1136, c_2=0)$.

#### Meaning of Chart Changes with Respect to Uplink Knowledge:
1. **Slope Changes as Analogous to Interest Rate Shifts**:
   - In the red line (25% loss), the slope is $-0.75$, derived from $c_2 = 900 - 0.75c_1$. This corresponds to an **effective interest rate $r = -0.25$** (as storing 1 bushel this year yields only 0.75 bushels next year). This flat slope mirrors the "negative actual interest rate" case in the uplink summary, where a weaker slope discourages saving due to high opportunity costs: to gain 1 unit of $c_2$, $c_1$ must decrease by $\frac{1}{0.75} \approx 1.33$ units.
   - The black line (0% loss) has a steeper slope of $-1$ (from $c_2 = 1150 - c_1$), reflecting $r = 0$. This aligns with the uplink's "positive actual interest rate" scenario (e.g., $r = 0.10$), where a steeper slope incentivizes saving: 1 unit of $c_1$ foregone directly converts to 1 unit of $c_2$.
   - The blue line (dashed) has the steepest slope ($\approx -1.10$, from $c_2 = 1250 - 1.10c_1$), implying $r > 0$ (e.g., crop bulb growth). This parallels the uplink's analysis of rising interest rates causing budget lines to steepen, amplifying intertemporal substitution (giving up $c_1$ yields more $c_2$).

   > **Continuity with uplink**: Just as the uplink showed rising monetary interest rates ($r$) steepen the budget line (e.g., from slope $-1.10$ to $-1.20$), here the *reduction in storage loss* (from 25% to 0% to negative) steepens the line. The slope's magnitude $|1 + r|$ (where $r$ is the effective interest rate) **directly maps** to intertemporal opportunity cost—no inflation adjustment needed in this barter model, simplifying the link to the uplink's interest-rate logic.

2. **Intercept Shifts and Endowment Constraints**:
   - All lines intersect at the **autarky point $(c_1=1000, c_2=150)$** (this year's full harvest, no storage). This is the anchor point equivalent to the uplink's endowment bundles (e.g., Harvey's income points).
   - Y-intercept growth (900 → 1150 → 1250) shows how reduced storage loss *expands* maximum feasible $c_2$ when $c_1 = 0$. This mimics the uplink's "inflation-adjusted budget line" in Harvey's case (e.g., 10.9(c) with 10% inflation), where income constraints shift feasible sets.
   - X-intercept growth (1000 → 1111 → 1136) reflects enhanced consumption capacity in "period 1" from stored surplus, but unlike monetary cases, **no borrowing is possible** (x-intercepts are hypothetical, as $c_1 > 1000$ is infeasible without trade).

   > **Continuity with uplink**: The uplink noted that inflation distorts budget lines by tilting them (as in Harvey's 10.9(c) where $1.21c_1 + 1.1c_2 = 3,520$), whereas here storage loss is a *structural* distortion with similar effects. The village model strips away price-level complications, highlighting how the **non-monetary wedge** (lost corn) drives the same economic intuition as nominal interest rates in monetary economies.

3. **Policy and Welfare Implications**:
   - The red line’s flat slope (25% loss) narrows the feasible set, forcing lower $c_2$ for any $c_1 < 1000$. This echoes the uplink's "negative interest rate" warning: welfare losses occur when trade-offs are distorted (e.g., the blue line feasible set dominates the red line, but rational agents on the red line cannot reach it).
   - In the Cobb-Douglas utility $U = c_1 c_2$ (uplink 10.8), optimal choices follow $c_1 = c_2$ (as Harvey’s case). For the red budget line, this pins consumption at $c_1 = 600$, $c_2 = 450$—a solvable point that would shift with line steepness, illustrating the uplink's "income-substitution effects" in physical terms.

   > **Continuity with uplink**: This operationalizes the uplink's principle that "actual interest is the decision core"—here, the effective $r = -0.25$ directly determines real choices. If loss rates were unstable (like volatile inflation in Harvey’s 10.9(c)), welfare analysis would require recalibration, but the village’s stable storage loss keeps decision rules analogous to the uplink’s $r$-based approach. Distortions like the red line’s slope also explain why the uplink emphasized shadow pricing: without correcting for loss rates (or inflation), policymakers misread "demand" (e.g., villagers "save" less due to rats, not preference).

---
### Page/Slide 13



### 当前图片内容解析

#### 1. 提取文字与公式
**问题部分文字**：  
- (b) Villagers consume **600 bushels** this year, rats eat **100 bushels**, consume **450 bushels** next year.  
- (c) After road construction: world price = $1/bushel, borrowing/lending rate = 10%. First-period consumption = **568 bushels**, second-period consumption = **624 bushels**.  
- (d) Transportation cost = $0.10/bushel (added to (c) setup), requiring black-ink budget line re-drawing.  

**表格 10.11 (0) 数据**：  
| Year | 1965 | 1970 | 1975 | 1978 | 1980 | 1985 |  
|------|------|------|------|------|------|------|  
| CPI, Start | 38.3 | 47.1 | 66.3 | 79.2 | 100.0 | 130.0 |  
| CPI, End | 39.4 | 49.2 | 69.1 | 88.1 | 110.4 | 133 |  
| % Inflation Rate | 2.9 | 4.3 | 4.2 | 11.3 | **10.4** | 2.3 |  
| Nominal Int. Rate | 4.0 | 6.4 | 5.8 | 7.2 | 11.6 | 7.5 |  
| Real Int. Rate | 1.1 | 2.1 | 1.6 | **−3.7** | **1.09** | 5.07 |  

**隐含公式**：  
- 通胀率 = $\frac{\text{CPI}_{\text{end}} - \text{CPI}_{\text{start}}}{\text{CPI}_{\text{start}}} \times 100$  
- 实际利率 $\approx \frac{1 + \text{Nominal Rate}}{1 + \text{Inflation Rate}} - 1$（如 1978 年：$\frac{1+0.072}{1+0.113} - 1 = -3.7\%$）  

**补充说明文字**：  
> (a) "Nominal interest rates were high, but so was inflation. Real interest rates were not high. (They were negative in 1978.)"  

---

#### 2. 相关变化含义解析（基于上文连续性）  
##### （1）问题 (b)-(d) 的预算线演化逻辑  
- **(b) 阶段（基础存储模型）**：  
  消费组合 $(c_1=600, c_2=450)$ 直接印证上文 **25% 存储损失率** 导致的约束：  
  $$
  c_2 = (1000 - c_1)(1 - 0.25) \implies \text{红预算线斜率} = -0.75
  $$  
  此处 $c_1 + c_2/0.75 = 1000$（类比上文 $1.21c_1 + 1.1c_2 = 3520$），**与上文知识点中 "Cobb-Douglas 效用下 $U=c_1c_2$ 最优解 $c_1=600, c_2=450$" 严格对应**，验证非货币楔子（老鼠损耗）将可行集压缩至红线下方。  

- **(c) 阶段（开放贸易）**：  
  新消费组合 $(c_1=568, c_2=624)$ 由 **蓝色预算线** 驱动：  
  $$
  c_1 + \frac{c_2}{1+r} = 1000 \quad (r=10\%) \implies \text{斜率} = -(1.1)
  $$  
  比较稳态：  
  - $c_1$ 从 600 → 568（↓5.3%），$c_2$ 从 450 → 624（↑38.7%）  
  **含义**：贸易引入正名义利率 $(r=10\%)$，替代了上文 "非货币楔子"（$r=-25\%$）。根据上文 **"income-substitution effects"**，利率上升引发跨期替代效应——村民减少当期消费以换取更高未来消费，体现 **预算线旋转拓展可行集**（蓝线完全包裹红线），直接呼应上文 "blue line feasible set dominates the red line" 的福利提升逻辑。  

- **(d) 阶段（运输成本）**：  
  $0.10/bushel 交易摩擦 = \text{等效结构扭曲}$，形成 **双向楔子**：  
  - 出村粮成本：$c_2 \text{ effective price} = 1.1(1+r)$  
  - 入村粮成本：$c_1 \text{ effective price} = 1.1$  
  **含义**：预算线折弯（kinked），类比上文 "storage loss as structural distortion"，但方向更复杂。此楔子使 **套利区间消失**（贸易无利可图当 $|c_1 - c_2|$ 过小时），还原初态稀缺性，印证上文 "distortions explain why policymakers misread demand"。  

##### （2）表格 10.11 (0) 的政策含义强化  
- **1978 年关键数据**：名义利率 7.2% → 通胀 11.3% → 实际利率 −3.7%  
  **直接支撑上文 "negative interest rate warning"**：  
  > 高名义利率投诉的误导性在于忽视通胀，**实际决策核心**（$r_{\text{real}} = -3.7\%$）表明资金负成本，与村庄模型中 $r=-0.25$ 即 $c_2$ 大幅缩水的机制一致。  
- **1980 年数据**：名义利率 11.6% → 通胀 10.4% → 实际利率 1.09%  
  **印证上文连续性**：通胀 "tilting budget lines" 的效应在此量化——实际利率 $r=1.09\%$ 使储蓄正向激励，与问题 (c) 中 $r=10\%$ 的消费平滑逻辑同源（尽管幅度不同）。  

> **核心一致性**：表格通过实证数据将村庄模型 **"non-monetary wedge" 与通胀扭曲** 统一于 **实际利率决策核心**，验证上文 "inflation distorts budget lines... same economic intuition as nominal interest rates" 的论断。

---
### Page/Slide 14



### 提取内容：当前图片文字与公式

#### 文字内容
```
144 INTERTEMPORAL CHOICE (Ch. 10)

(b) If you gave up a unit of consumption goods at the beginning of 1985
and saved your money at interest, you could use the proceeds of your
saving to buy 1.05 units of consumption goods at the beginning of
1986. If you gave up a unit of consumption goods at the beginning of
1978 and saved your money at interest, you would be able to use the
proceeds of your saving to buy .96 units of consumption goods at the
beginning of 1979.

10.12 (1) Marsha Mellow doesn’t care whether she consumes in period
1 or in period 2. Her utility function is simply \( U(c_1, c_2) = c_1 + c_2 \). Her
initial endowment is $20 in period 1 and $40 in period 2. In an antique
shop, she discovers a cookie jar that is for sale for $12 in period 1 and that
she is certain she can sell for $20 in period 2. She derives no consumption
benefits from the cookie jar, and it costs her nothing to store it for one
period.

(a) On the graph below, label her initial endowment, \( E \), and use blue ink
to draw the budget line showing combinations of period-1 and period-2
consumption that she can afford if she doesn’t buy the cookie jar. On the
same graph, label the consumption bundle, \( A \), that she would have if she
did not borrow or lend any money but bought the cookie jar in period 1,
sold it in period 2, and used the proceeds to buy period-2 consumption.
If she cannot borrow or lend, should Marsha invest in the cookie jar?
Yes.

(b) Suppose that Marsha can borrow and lend at an interest rate of 50%.
On the graph where you labelled her initial endowment, draw the budget
line showing all of the bundles she can afford if she invests in the cookie
jar and borrows or lends at the interest rate of 50%. On the same graph
use red ink to draw one or two of Marsha’s indifference curves.
```

#### 公式
- 效用函数：\( U(c_1, c_2) = c_1 + c_2 \)
- 问题 (b) 中隐含的跨期替换率：  
  - 1985→1986：\( 1.05 \) 个单位（隐含实际利率 \( +5\% \))  
  - 1978→1979：\( 0.96 \) 个单位（隐含实际利率 \( -4\% \))

#### 图表元素
- **坐标轴**：  
  - 横轴（Period-1 consumption）：范围 0–80  
  - 纵轴（Period-2 consumption）：范围 0–80  
- **线条与点**：  
  - 蓝线（Blue line）：预算线（无 cookie jar 且无借贷）  
  - 红线（Red line）：预算线（有 50% 利率市场）  
  - \( E \)：初始禀赋点（约 (20, 40)）  
  - \( A \)：投资 cookie jar 后的消费束点（约 (8, 60)）  
  - \( e \)：中间点（约 (20, 50)），可能表示 cookie jar 投资的边际效果

---

### 图表变化含义解析（基于上文连续性）

#### 1. 蓝线（无 cookie jar 且无借贷）的基准含义
- **预算线方程**：\( c_1 + c_2 = 60 \)（斜率 \( -1 \)，隐含实际利率 \( r = 0\% \))  
  - **解释**：基于上文“25% 存储损失率”的逻辑延伸，此处 **隐含无成本存储技术**。初始禀赋 \( (20, 40) \) 总现值 $60，故蓝线代表无金融市场的约束——当期与未来消费互斥，但可无损失转移资源。  
  - **对比上文**：上文 (b) 阶段红预算线（斜率 \( -0.75 \)）因“非货币楔子”（存储损失）而压缩可行集；此处蓝线斜率 \( -1 \) 表明**无扭曲**，但福利低于引入市场后（呼应上文“no distortion”基准状态）。

#### 2. 红线（50% 利率市场引入）的关键升级
- **预算线方程**：\( c_1 + \frac{c_2}{1.5} = 46.67 \)（斜率 \( -1.5 \)，隐含实际利率 \( r = 50\% \))  
  - **几何变化**：  
    - 蓝线（截距 60）被红线包裹，可行集显著扩大（红线 y 截距 ~70，x 截距 ~46.7）。  
    - **斜率深化**：从 \( -1 \)（蓝线）变为 \( -1.5 \)（红线），表示机会成本上升——放弃 1 单位当期消费，未来消费回报从 1 单位增至 1.5 单位。  
  - **经济机制**：  
    - **替代效应主导**：上文强调“利率上升引发跨期替代”，此处 \( r = 50\% > 0\% \) 强化该效应。Marsha 的线性效用 \( (U = c_1 + c_2) \) 使她**完全专业化**消费（如选择 \( (0, 70) \)），直接体现“利率正向激励储蓄”的逻辑（类比上文 1980 年实际利率 \( +1.09\% \) 的平滑机制）。  
    - **福利提升**：红线完全包含蓝线，证伪“高名义利率投诉的误导性”——关键在**实际利率**（此处 \( r_{\text{real}} = 50\% \)，远高于 cookie jar 隐含的 66.7% 机会成本，但市场仍优化资源）。

#### 3. 点 \( A \) 与 cookie jar 投资的隐性扭曲
- **点 \( A \) 意义**：\( (8, 60) \) 对应消费束（期 1 支出 $12 购 jar → \( c_1 = 8 \); 期 2 售 jar 得 $20 → \( c_2 = 60 \))。  
  - **相对于蓝线**：点 \( A \) 位于蓝线外侧（\( c_1 + c_2 = 68 > 60 \))，表明 cookie jar 提供 **9.6% 的非市场收益**（\( \frac{20}{12} - 1 \approx 66.7\% \)）——类似上文“非货币楔子”被移除的过程。  
  - **对比上文 (d) 阶段**：cookie jar 作为**单向楔子**（仅期 1 成本期 2 收益），类比上文“运输成本的双向楔子”，但此处**提升福利**（上文楔子降低福利），凸显“扭曲方向决定政策影响”：  
    > 正向投资机会（如 cookie jar）与负向摩擦（如上文存储损失）均改变预算约束，但**福利方向由楔子符号决定**。

#### 4. 与上文知识点的统一逻辑
- **实际利率决策核心**：  
  - 1978 年负利率（\( -3.7\% \)) 与 cookie jar 投资（66.7% 收益）均被**实际回报率**驱动——Marsha 拒绝 Mundell-Tobin 式误读，因她基于**净收益**决策（同上文“高名义利率投诉的误导性”）。  
- **预算线演化连续性**：  
  - 此图延续上文自 (b)→(c) 演化：  
    - 蓝线 ≈ 上文 (b) 红线（\( r \) 接近 0%，可行集窄）  
    - 红线 ≈ 上文 (c) 蓝线（\( r = 50\% \)，可行集扩展）  
  - **核心一致**：利率 \( r \) 变化时，预算线绕禀赋点 \( E \) 旋转——**斜率深化代表通胀扭曲或储蓄激励**（1980 年数据：通胀“tilting budget lines”效应此处显性化）。  

> **关键洞见**：cookie jar 作为“局部市场”，其效果受全局利率约束（\( 66.7\% \) 收益 > \( 50\% \) 市场利率）；但**引入正式市场后，其福利提升被超额覆盖**——直接呼应上文“blue line feasible set dominates the red line”的福利理论。

---
### Page/Slide 15



### 1. 提取当前图片中的文字与公式  
- **文字内容**：  
  > (c) Suppose that instead of consumption in the two periods being perfect substitutes, they are perfect complements, so that Marsha’s utility function is min{$c_1, c_2$}. If she cannot borrow or lend, should she buy the cookie jar? **No**. If she can borrow and lend at an interest rate of 50%, should she invest in the cookie jar? **Yes**. If she can borrow or lend as much at an interest rate of 100%, should she invest in the cookie jar? **No**.  

- **公式**：  
  - 效用函数：$ U = \min\{c_1, c_2\} $（完美互补品）  
  - 预算约束（隐含，基于上文逻辑）：  
    - 无借贷时：$ c_1 + c_2 \leq 60 $  
    - 利率 $ r $ 时：$ c_1 + \frac{c_2}{1+r} = \text{PV of endowment} $  

---

### 2. 结合上文的解析（无图表，聚焦逻辑连续性）  
当前图片延续上文对 **cookie jar 投资逻辑**的讨论，但将效用函数从完美替代（$ U = c_1 + c_2 $）切换为**完美互补**（$ U = \min\{c_1, c_2\} $），突出**投资决策对利率的敏感性**及**效用函数形式的关键作用**。解析如下：  

#### （1）无借贷时拒绝 cookie jar 的原因  
- 上文已证：cookie jar 需期 1 投入 \$12（得 $ c_1 = 8 $），期 2 回报 \$20（得 $ c_2 = 60 $），束为 $ (8,60) $。  
- 无借贷时，初始禀赋约束 $ c_1 + c_2 \leq 60 $（上文蓝线）。  
  - 无 jar 时：最优解 $ c_1 = c_2 = 30 $（因 $ \min\{c_1, c_2\} $），效用 $ U = 30 $。  
  - 有 jar 时：束 $ (8,60) $ 导致 $ U = \min\{8,60\} = 8 $，**显著低于 30**。  
- **上文逻辑延续**：对照上文“无借贷时 cookie jar 位于蓝线外侧”的结论（$ c_1 + c_2 = 68 > 60 $），此处**福利恶化**因互补效用要求消费均衡，而 jar 扭曲了期际分配（类似上文“非货币楔子”但方向相反）。

#### （2）利率 50% 时接受 cookie jar 的关键机制  
- 上文指出：50% 利率下市场预算线为 $ c_1 + \frac{c_2}{1.5} = 46.67 $（上文红线）。  
  - 无 jar 时：最优解 $ c_1 = c_2 = 28 $，$ U = 28 $（由 $ c_1 + c_1/1.5 = 46.67 $ 解得）。  
  - 有 jar 时：jar 的 **66.67% 隐含回报率 > 50% 市场利率**（上文明确 $ \frac{20}{12} - 1 \approx 66.7\% $），提升现值：  
    $$ \text{新预算线：} c_1 + \frac{c_2}{1.5} = (20-12) + \frac{40+20}{1.5} = 48 $$  
    最优解 $ c_1 = c_2 = 28.8 $，$ U = 28.8 > 28 $。  
- **上文逻辑延续**：呼应上文“实际利率决定投资价值”的核心（如 1980 年数据），此处 **66.7% 楔子（investing in jars）被 50% 市场利率主导**，验证“福利方向由楔子符号决定”——正向投资回报率 > 市场利率时，jar 增强可行集。

#### （3）利率 100% 时拒绝 cookie jar 的必然性  
- 市场利率 $ r = 100\% $ 时，预算线：$ c_1 + \frac{c_2}{2} = 40 $（初始禀赋现值）。  
  - 无 jar 时：$ c_1 = c_2 = 26.67 $，$ U = 26.67 $。  
  - 有 jar 时：现值 $ = 8 + \frac{60}{2} = 38 $，预算线 $ c_1 + \frac{c_2}{2} = 38 $，最优 $ c_1 = c_2 = 25.33 $，$ U = 25.33 < 26.67 $。  
- **上文逻辑延续**：当市场利率 **超过 jar 的 66.7% 回报率**（100% > 66.7%），jar 的“局部市场”效应被压制。这直接强化上文“introducing formal markets supersedes local opportunities”的洞见——**高利率市场提供更优平滑机制**（类比上文“blue line dominates red line”但方向逆转）。

#### 统一洞见  
- **决策准则**：是否投资 jar 取决于市场利率 $ r $ 与 jar 隐含回报率 $ \rho = 66.7\% $ 的大小：  
  $$ \text{若 } r < \rho \text{（如 50%）} \implies \text{Yes}; \quad \text{若 } r \geq \rho \text{（如 100%）} \implies \text{No}. $$  
- **效用函数作用**：  
  - 完美替代时（上文），$ r > 0\% $ 即触发完全专业化；  
  - 完美互补时，投资仅当 jar 提升**均衡消费水平**（$ \min\{c_1,c_2\} $）时成立。  
  二者共同印证上文核心——**实际利率是跨期决策的基石**，政策争论（如“高名义利率投诉”）需剥离通胀干扰。

---
### Page/Slide 16



### 当前图片解析

#### 1. 文字与公式提取  
- **文字内容**：  
  `146  INTERTEMPORAL CHOICE  (Ch. 10)`  
- **公式**：无。

#### 2. 图表分析  
- **无图表**，当前图片仅包含页码和章节标题，无图形或数据呈现。

#### 3. 上下文关联与知识连续性  
当前图片为页眉信息，明确标识内容属于 **跨期选择理论（Intertemporal Choice）** 第10章，页码146。这直接承接上文知识点总结中讨论的 **cookie jar 投资逻辑** 案例：  
- 上文已通过完美互补效用函数（$ U = \min\{c_1, c_2\} $）分析利率敏感性，验证了投资决策的核心准则——**jar 隐含回报率 $ \rho = 66.7\% $ 与市场利率 $ r $ 的相对大小决定福利方向**（$ r < \rho $ 时接受 jar；$ r \geq \rho $ 时拒绝）。  
- 此标题页作为理论框架的载体，强化了上文结论的适用场景：**实际利率是跨期决策的基石**，政策争议（如名义利率投诉）需剥离通胀干扰。页码146暗示该内容位于教材章节中后段，通常用于深化实证讨论（如上文 1980 年利率数据案例），突显效用函数形式对市场均衡的关键影响。  

> **注**：无新增图表或公式，故解析聚焦于标题与上文逻辑的衔接，避免重复已知结论。
