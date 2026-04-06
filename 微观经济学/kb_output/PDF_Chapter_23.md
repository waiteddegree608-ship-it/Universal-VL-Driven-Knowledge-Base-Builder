# PDF_Chapter_23

### Page/Slide 1



### 1. 文字与公式提取  

#### 章节标题与引言  
- **Chapter 23**  
- **Industry Supply**  

- **Introduction**  
  - 行业供给计算方法：将各企业供给量相加（注意是数量而非价格）。  
  - 行业供给曲线可能出现拐点：当市场价格低至某企业供给量降为零时。  
  - 本章后三题将供给-需求分析用于非法经济活动问题。  

#### 23.0 Warm Up Exercise（核心逻辑与示例）  
- **核心逻辑**：市场供给函数由企业供给函数加总而成，可能存在拐点（因不同价格区间企业供给状态不同）。  
- **示例**：若企业供给函数 $ s_1(p) = p $、$ s_2(p) = p - 2 $，则市场供给函数为：  
  $$
  S(p) = 
  \begin{cases} 
  p & \text{for } p \leq 2, \\
  2p - 2 & \text{for } p > 2.
  \end{cases}
  $$  
  （$ p < 2 $ 时仅企业1供给；$ p > 2 $ 时两家企业均供给。）  

- **练习题公式**  
  (a) 企业供给：$ s_1(p) = p $, $ s_2(p) = 2p $, $ s_3(p) = 3p $；市场供给：$ S(p) = 6p $.  
  (b) 企业供给：$ s_1(p) = 2p $, $ s_2(p) = p - 1 $；市场供给：  
  $$
  S(p) = 
  \begin{cases} 
  2p & \text{for } p \leq 1, \\
  3p - 1 & \text{for } p > 1.
  \end{cases}
  $$  
  (c) 200家企业 $ s_1(p) = 2p - 8 $、100家企业 $ s_2(p) = p - 3 $；市场供给：  
  $$
  S(p) = 
  \begin{cases} 
  0 & \text{for } p < 3, \\
  100p - 300 & \text{for } 3 \leq p \leq 4, \\
  500p - 1,900 & \text{for } p > 4.
  \end{cases}
  $$  
  (d) 企业供给：$ s_1(p) = 3p - 12 $, $ s_2(p) = 2p - 8 $, $ s_3(p) = p - 4 $；市场供给：  
  $$
  S(p) = 6p - 24 \quad \text{for } p > 4.
  $$  

#### 23.1 (1) 问题背景  
- Al Deardwarf 的表亲 Zwerg 制造石膏花园小矮人，生产需模具（成本 $1,000、寿命1年）、石膏和劳动力。  


### 2. 图表与变化含义说明  
当前图片**无图表**，仅含文字与公式。所有供给函数均体现“分段加总”逻辑：  
- 低价格区间：部分企业因成本门槛退出（供给量为0）；  
- 价格超过临界值后：新企业进入，供给曲线斜率变化（即拐点）。  
例如 (c) 中 $ p < 3 $ 时无企业供给；$ 3 \leq p \leq 4 $ 时仅 $ s_2(p) $ 有效（100家企业）；$ p > 4 $ 时两组企业均供给，市场供给斜率骤增（$ 500p - 1,900 $）。

---
### Page/Slide 2



### 1. 文字与公式提取  

#### 章节与背景描述  
- **页码与标题**：282 INDUSTRY SUPPLY (Ch. 23)  
- **生产技术参数**：  
  - 模具成本：\$1,000（寿命1年，无残值）  
  - 模具年产量：500 个/模具  
  - 单位可变成本：每个小矮人需 \$7（石膏和劳动力）  
  - 短期模具数量固定，新模具需提前1年订购（仅1月1日下单，次年1月1日交付）  
  - 假设：模具寿命内生产的所有小矮人于12月31日售出，劳动力与材料费用年末支付  

- **市场与长期均衡条件**：  
  - 行业需求函数：$ D(p) = 60,000 - 5,000p $（$ D(p) $ 为年销量，$ p $ 为价格）  
  - 价格与技术长期稳定，行业处于长期均衡  
  - 资本成本：利息率 10%  

#### 问题与解答  
(a) 银行投资 \$1,000 一年后本息和：**\$1,100**  
　　模具投资需满足：年收入超额成本部分 ≥ \$1,100（因模具期末无残值）  

(b) 单模具短期边际成本（≤500单位）：**\$7**  
　　平均可变成本（≤500单位）：**\$7**  
　　是否可短期生产超过 500 单位：**No**（模具产能上限）  

(c) 单模具生产决策阈值：  
　　- 价格 **> \$7** 时生产 500 单位  
　　- 价格 **< \$7** 时停产（产量为 0）  

---

### 2. 逻辑关联与行业供给分析  
当前案例直接应用**上文"分段供给曲线"逻辑**：  
- **临界价格 \$7 的意义**：  
  企业短期供给存在**价格下限**（等于边际成本），对应上文提及的"拐点"。当市场价格 $ p < \$7 $ 时，企业供给量为 0；$ p > \$7 $ 时，单企业供给量跃升至产能上限 500。此阈值构成行业供给曲线的**分段节点**。  

- **行业供给曲线形态**：  
  若行业含 $ n $ 个同质企业（单模具产能 500），则市场供给函数需分段：  
  $$
  S(p) = 
  \begin{cases} 
  0 & \text{if } p < 7, \\
  500n & \text{if } p \geq 7.
  \end{cases}
  $$  
  此结构与上文练习题 (c) 逻辑一致——**产能约束与成本门槛共同决定供给曲线的离散跳跃**，但此处因企业同质，供给曲线在 $ p=7 $ 处呈现垂直段（完全弹性）。  

- **长期均衡条件延伸**：  
  上文提及"行业供给拐点可能因企业退出产生"，而本题隐含**长期均衡要求价格覆盖总成本**（含资本机会成本）。由 (a) 可知，模具投资需产生 \$1,100 年收益，对应有效产能的盈亏平衡价格需满足：  
  $$
  500p = 500 \times 7 + 1,100 \quad \Rightarrow \quad p = 9.2
  $$  
  但当前短期决策仅关注可变成本（\$7），体现**短期与长期供给曲线的根本差异**。

---
### Page/Slide 3



### 1. 文字与公式提取  

#### 完整文字与数据  
- **上下文补充**：  
  "lars. You would be indifferent between producing any number of gnomes between 0 and 500 if the price of gnomes is 7 dollars."  

- **问题 (d)**：  
  > "If you could sell as many gnomes as you liked for \$10 each and none at a higher price, what rate of return would you make on your \$1,000 by investing in a gnome mold? **50%**. Is this higher than the return from putting your money in the bank? **Yes**. What is the lowest price for gnomes at which investing in a gnome mold gives the same rate of return as you get from the bank? **\$9.20**. Could the long-run equilibrium price be lower than this? **No**."  

- **问题 (e)**：  
  > "At the price you found in the last section, how many gnomes would be demanded each year? **14,000**. How many molds would be purchased each year? **28**. Is this a long-run equilibrium price? **Yes**."  

- **23.2 (1) 问题描述**：  
  > "We continue our study of the garden-gnome industry. Suppose that initially everything was as described in the previous problem. To the complete surprise of everyone in the industry, on January 1, 1993, the invention of a new kind of plaster was announced. This new plaster made it possible to produce garden gnomes using the same molds, but it reduced the cost of the plaster and labor needed to produce a gnome from \$7 to \$5 per gnome. Assume that consumers’ demand function for gnomes in 1993 was not changed by this news. The announcement came early enough in the day for everybody to change his order for gnome molds to be delivered on January 1, 1994, but of course, the number of molds available to be used in 1993 is already determined from orders made one year ago. The manufacturer of garden gnome molds contracted to sell them for \$1,000 a year ago, so it can’t change the price it charges on delivery."  

- **问题 (a)**：  
  > "In 1993, what will be the equilibrium total output of garden gnomes? **14,000**. What will be the equilibrium price of garden gnomes? **\$9.20**. Cousin Zwerg bought a gnome mold that was delivered on January 1, 1993, and, as had been agreed, he paid \$1,000 for it on that day. On January 1, 1994, when he sold the gnomes he had made during the year and when he paid the workers and the suppliers of plaster, he received a net cash flow of **\$2,100**. Did he make more than a 10% rate of return on his investment in the gnome mold? **Yes**. What rate of return did he make? **110%**."  

#### 隐含公式  
- 问题 (d) 中盈亏平衡价格计算：  
  $$
  500p = 500 \times 7 + 1,100 \quad \Rightarrow \quad p = 9.2
  $$  
- 问题 (a) 中投资回报率计算：  
  $$
  \text{Return Rate} = \frac{2,100}{1,000} \times 100\% = 210\% \quad \text{(gross return)} \quad \text{but net return } = 110\% \text{ after capital opportunity cost is considered.}
  $$  
  *注：净回报率 110% 隐含扣除 10% 资本机会成本（即 \$1,000 本金 + 10% 机会成本 = \$1,100），因此 \$2,100 cash flow 对应净收益 \$1,100，回报率 $ \frac{1,100}{1,000} = 110\% $。*  

---

### 2. 逻辑关联与行业调整解析  
本部分直接延伸【上文知识点总结】中的**短期供给刚性**和**长期均衡路径**逻辑，重点分析成本冲击下的分段调整机制。无图表，但需结合文本解释关键经济含义：  

#### (1) 价格阈值 (\$9.20) 与长期均衡条件  
- **延续上文供给曲线逻辑**：  
  上文强调价格阈值（如 \$7）是短期供给的拐点（$ p < 7 $ 时生产为 0），而此处 \$9.20 是**长期均衡价格**，由总成本约束决定：模具投资 \$1,000 需覆盖一年可变成本（500 个 × \$7）和资本机会成本（10% × \$1,000 = \$110），即 $ 500p = 3,500 + 1,100 $。这体现上文“长期均衡要求价格覆盖总成本”的核心原则。  
- **行业供给的离散性**：  
  问题 (e) 中 14,000 需求量对应 28 个模具（$ 14,000 / 500 $），说明行业供给在 $ p \geq 9.20 $ 时呈垂直跳跃（非平滑曲线），因企业同质且产能固定（每个模具 500 个）。这与上文练习题 (c) 中“$ p > 4 $ 时斜率骤增”机理一致：**需求冲击仅改变模具数量，而不改变单个企业供给函数形态**。  

#### (2) 1993 年成本冲击 (\$7 → \$5) 的短期影响  
- **短期刚性的微观基础**：  
  上文背景提及“模具订单需提前 1 年确定”，此处新成本 \$5 仅影响 1994 年订单，但 1993 年模具数量已锁定（由 1992 年订单决定）。因此：  
  - 短期供给曲线保持不变（仍由 28 个模具决定，$ S(p) = 14,000 $ for $ p \geq 7 $）。  
  - 均衡价格维持 \$9.20（需求函数未变：$ D(p) = 60,000 - 5,000p $，代入 $ p = 9.20 $ 得 $ D(9.20) = 14,000 $）。  
  *这印证上文“短期模具数量固定”假设，凸显**供给滞后导致短期调整无效**。*  
- **超额利润的成因**：  
  问题 (a) 中 Zwerg 的 110% 净回报源于：  
  - 新可变成本 \$5 → 年现金流入 $ 500 \times 9.20 = 4,600 $，  
  - 实际可变成本 $ 500 \times 5 = 2,500 $，  
  - 净收益 $ 4,600 - 2,500 = 2,100 $（但已扣除劳动力和材料支付）。  
  此时隐性经济利润 $ 2,100 - 1,100 = 1,000 $ 超越资本机会成本，直接验证上文“长期均衡价格 \$9.20 会消失于供给增加”的动态机制。  

#### (3) 长期调整路径预示  
- **价格门槛的演变**：  
  上文认为“拐点因企业退出产生”，而本冲击后，1994 年新模具订单将基于成本 \$5 重新校准盈亏平衡价格：  
  $$
  500p' = 500 \times 5 + 1,100 \quad \Rightarrow \quad p' = 7.2
  $$  
  长期均衡价格降至 \$7.20，行业供给曲线将整体左移（相同价格下模具需求增加）。  
- **制度约束的关键作用**：  
  本问题升级上文“分段供给”逻辑：模具订单的**1 年滞后期**使成本冲击仅引发一次性超额利润（1993 年），而非价格即刻下降。这说明，**当行业存在强资本约束时，长期均衡需经历“短期刚性 → 超额利润 → 新投资进入”的阶段路径**，而非自动调整。

---
### Page/Slide 4



### 提取当前图片内容

#### 文字  
284 INDUSTRY SUPPLY (Ch. 23)  
(b) Zwerg’s neighbor, Munchkin, also makes garden gnomes, and he has a gnome mold that is to be delivered on January 1, 1993. On this day, Zwerg, who is looking for a way to invest some more money, is considering buying Munchkin’s new mold from Munchkin and installing it in his own plant. If Munchkin keeps his mold, he will get a net cash flow of $2,100 in one year. If the interest rate that Munchkin faces, both for borrowing and lending is 10%, then should he be willing to sell his mold for $1,000? No. What is the lowest price that he would be willing to sell it for? $1,909. If the best rate of return that Zwerg can make on alternative investments of additional funds is 10%, what is the most that Zwerg would be willing to pay for Munchkin’s new mold? $1,909.  
(c) What do you think will happen to the number of garden gnomes ordered for delivery on January 1, 1994? Will it be larger, smaller, or the same as the number ordered the previous year? Larger. After the passage of sufficient time, the industry will reach a new long-run equilibrium. What will be the new equilibrium price of gnomes? $7.20.  
23.3 (1) On January 1, 1993, there were no changes in technology or demand functions from that in our original description of the industry, but the government astonished the garden gnome industry by introducing a tax on the production of garden gnomes. For every garden gnome produced, the manufacturer must pay a $1 tax. The announcement came early enough in the day so that there was time for gnome producers to change their orders of gnome molds for 1994. Of course the gnome molds to be used in 1993 had been already ordered a year ago. Gnome makers had signed contracts promising to pay $1,000 for each gnome mold that they ordered, and they couldn’t back out of these promises.  
(a) Recalling from previous problems the number of gnome molds ordered for delivery on January 1, 1993, we see that if gnome makers produce up to capacity in 1993, they will produce 14,000 gnomes. Given the demand function, we see that the market price would then have to be $9.20.  
(b) If you have a garden gnome mold, the marginal cost of producing a garden gnome, including the tax, is $8. Therefore all gnome molds (will, will not) will be used up to capacity in 1993.

#### 公式  
- $2,100 现金流折现：$\text{PV} = \frac{2,100}{1 + 0.10} = 1,909$  
- 新长期均衡价格：$p' = 7.20$  
- 1993年市场均衡价格：$p = 9.20$  
- 税收后边际成本：$\text{Marginal Cost} = 8$  

---

### 结合上文解析  
当前内容直接延伸【上文知识点总结】中的**资本机会成本**和**短期供给刚性**逻辑，通过税收冲击案例验证长期均衡调整路径：  

#### 1. **$1,909 的经济含义**  
- 该价格是 $2,100 现金流在 10% 机会成本下的现值计算，呼应上文 *投资回报率计算*：  
  $ \text{PV} = \frac{2,100}{1.10} = 1,909 $  
  隐含扣除资本机会成本（即 \$1,000 本金的 10% 机会成本），验证了上文“净回报率 110% 需考虑机会成本”的原则。Munchkin 拒绝 \$1,000 卖价，因其低于现值，符合上文“净收益 \$1,100 驱动投资决策”的逻辑。  

#### 2. **税收冲击对均衡的分段影响**  
- **短期（1993 年）供给刚性**：  
  - 模具数量已锁定（28 个模具对应 14,000 gnomes），延续上文 *成本冲击短期分析*：  
    - 税收使边际成本升至 \$8（\text{原 } \$7 + \$1 \text{ 税}），但供给曲线未移动（因 1993 年模具订单固定）。  
    - 需求函数 $D(p) = 60,000 - 5,000p$ 与上文一致，代入 $S(p) = 14,000$ 仍得均衡价格 \$9.20。  
  - (b) 中“模具会满负荷生产”的结论，直接源于上文 *短期供给逻辑*：当价格 \$9.20 > 边际成本 \$8 时，企业无动力减少产量，体现 **供给滞后导致调整仅能通过需求响应**。  

- **长期（1994 年及以后）均衡重构**：  
  - 新长期均衡价格 \$7.20 的推导与上文 *成本冲击案例* 完全同构：  
    $$
    500p' = 500 \times (\text{新可变成本}) + 1,100
    $$  
    税收使可变成本升至 \$6（原 \$5 + \$1 税），故：  
    $$
    p' = \frac{500 \times 6 + 1,100}{500} = 7.20
    $$  
  - (c) 中“1994 年订购量更大”的预测，验证上文 *行业调整路径*：短期超额利润（\$9.20 - \$8 = \$1.20/单位）刺激新模具投资，推动供给增加直至价格降至 \$7.20，实现长期均衡。  

#### 3. **关键延续点**  
- 与上文 *1993 年成本冲击* 机理一致：税收作为外生成本冲击，仅能通过 **“短期刚性 → 价格不变 → 超额利润 → 新投资进入”** 路径调整，再次证明 **行业资本约束（1 年模具滞后期）是长期均衡非瞬时实现的核心原因**。  
- \$7.20 价格阈值的形成，强化上文 *长期均衡条件*：价格必须覆盖可变成本（含税收）和资本机会成本（\$1,100），体现“总成本决定均衡”的根本原则。

---
### Page/Slide 5



### 提取文字与公式  
**文字内容**：  
- (c) In 1993, what will be the total output of garden gnomes?  
  **14,000.** What will be the price of garden gnomes? **$9.20.**  
  What rate of return will Deardwarf’s cousin Zwerg make on his investment in a garden gnome mold that he ordered a year ago and paid $1,000 for at that time? **−40%.**  
- (d) Remember that Zwerg’s neighbor, Munchkin, also has a gnome mold that is to be delivered on January 1, 1993. Knowing about the tax makes Munchkin’s mold a less attractive investment than it was without the tax, but still Zwerg would buy it if he can get it cheap enough so that he makes a 10% rate of return on his investment. How much should he be willing to pay for Munchkin’s new mold? **$545.45.**  
- (e) What do you think will happen to the number of gnome molds ordered for delivery on January 1, 1994? Will it be larger, smaller, or the same as the number ordered the previous year? **Smaller.**  
- (f) The tax on garden gnomes was left in place for many years, and nobody expected any further changes in the tax or in demand or supply conditions. After the passage of sufficient time, the industry reached a new long-run equilibrium. What was the new equilibrium price of gnomes? **$10.20.**  
- (g) In the short run, who would end up paying the tax on garden gnomes, the producers or the consumers? **Producers.** In the long run, did the price of gnomes go up by more, less, or the same amount as the tax per gnome? **Same amount.**  
- (h) Suppose that early in the morning of January 1, 1993, the government had announced that there would be a $1 tax on garden gnomes, but that the tax would not go into effect until January 1, 1994. Would the producers of garden gnomes necessarily be worse off than if there were no tax? Why or why not? **No. The producers would anticipate the tax increase and restrict supply, thereby raising prices.**  

**隐含公式**：  
- (d) 中 $545.45 的计算：  
  \[
  P = \frac{500 \times (9.20 - 8.00)}{1 + 0.10} = \frac{500 \times 1.20}{1.10} = \frac{600}{1.10} = 545.45
  \]  
  （其中 $500$ 为每套模具年产量，$9.20 - 8.00$ 为单位利润，$10\%$ 为机会成本率）  
- (f) 与 (g) 中长期价格关系：  
  \[
  p_{\text{new}} = p_{\text{original}} + \text{tax} = 9.20 + 1.00 = 10.20
  \]  
  （$p_{\text{original}}$ 为税收前长期均衡价格，由 (c) 短期均衡价格 $9.20$ 外推）  

---

### 结合上文解析  
当前内容深化上文 **资本价值重估** 与 **预期驱动调整** 逻辑，重点揭示税收作为**持续性冲击**如何重塑行业动态路径。以下结合关键点展开：  

#### 1. **短期静态效应：资本价值崩溃与信号作用**  
   - (c) 中 $-40\%$ 回报率是上文“资本机会成本”原则的**负向印证**：  
     - 支付 $1,000$ 模具成本，1993 年现金流仅 $600$（$500$ 单位 × $1.20$ 利润），直接暴露税收对资本效率的侵蚀。  
     - 与上文 Munchkin 案例对比：上文正回报（$110\%$）吸引投资，此处负回报（$-40\%$）则**强化 sunk cost 逻辑**——短期生产仍按 $p > \text{marginal cost}$ 维持（$9.20 > 8.00$），但新资本决策已转向规避。  
   - **延续点**：重申“投资决策依赖现金流现值”准则，但突出税收导致的 **资本贬值速度加快**（从上文 \$1,909 现值降至 (d) 中 \$545.45）。  

#### 2. **新资本定价：机会成本的显性化**  
   - (d) 中 $545.45$ 直接延用上文 PV 计算框架：  
     \[
     \text{PV} = \frac{\text{年现金流}}{1 + r} = \frac{600}{1.10}
     \]  
     - 与上文 $\frac{2,100}{1.10}$ 形式一致，但现金流从 \$2,100 降至 \$600，反映税收使**每单位资本贡献下降**。  
     - **关键差异**：上文案例中资本价值仍高于投资成本（\$1,909 > \$1,000），催生扩张；此处 \$545.45 < \$1,000，释放**行业收缩信号**。  
   - **连续性**：验证“理性投资者按机会成本定价”原则，但税收将上文的**超额利润引致进入**逆转为**亏损驱动退出**。  

#### 3. **行业调整路径：从负回报到长期均衡的派生逻辑**  
   - (e) 与 (f) 揭示调整方向反转的根本原因：  
     - (e) 订购量 **Smaller** 源于 (c) 中负回报——预期 1994 年现金流不变（税收持续），新投资经济利润为负，故**无动机进入**（上文“超额利润引致订购增加”需利润 > 0 的前提）。  
     - (f) $10.20$ 新均衡价是税收**长期传递效率 **(100%) 的体现：  
       \[
       p_{\text{new}} = p_{\text{original}} + \text{tax} = 9.20 + 1.00
       \]  
       与上文 $7.20$ 案例对比：上文 $p' = 7.20$ 源于**一次性成本冲击**（含税收但资本成本不变），此处因税收**永久嵌入可变成本**，长期供给曲线平行上移，价格阶梯式上涨。  
   - **延伸上文**：强化“调整路径由冲击性质决定”结论——**持续性税收直接重定义长期均衡门槛**，而非仅触发短期价格波动。  

#### 4. **税负归宿：刚性约束与理性预期的交互**  
   - (g) 分段机制呼应上文**供给刚性**核心：  
     - 短期生产者承担税负：模具订单锁定（1993 年商品供给量 $14,000$ 不可调），需求曲线约束下价格无法覆盖全税，挤压利润空间。  
     - 长期价格上升等于税额：完全竞争假设下，长期供给弹性趋近无穷，**税收不改变资本投资门槛**，仅传递至价格。  
   - **知识延伸**：结合上文“资本约束导致调整滞后”，(g) 明确短期承担主体，但 (h) 进一步揭示**预期可弱化滞后性**。  

#### 5. **预期机制：对行业调整时滞的突破**  
   - (h) 中“ producers would anticipate... restrict supply” 重构调整路径：  
     - 提前宣布税收使生产者**将未来税负内生化**——1993 年主动减产抬高价格，规避 (c) 中 $-40\%$ 损失。  
     - **核心延续**：与上文“信息完整时调整提前启动”一致，但更突出 **资本决策前瞻性可绕过物理刚性**（如模具滞后期）。  
   - **深化结论**：税收作为外生变量，其影响程度取决于**预期形成时间**，印证上文“资本调整非瞬时源于信息不对称”推论的动态扩展。  

#### 关键延续总结  
- **资本价值**仍是连接短期与长期的枢纽：(d) 价格 \$545.45 为资本重估标尺，(e) 订购减少是价值崩溃的直接响应。  
- **税收性质**决定调整方向：一次性冲击（上文）激化竞争，持续性冲击（当前）系统性抬升均衡价格，验证“长期均衡定义依赖外部条件稳定性”原则。  
- **预期逻辑闭环**：(h) 证实行业可依托前瞻决策**压缩上文所述的时间滞后**，但未能消除资本约束本身，凸显微观主体理性与结构性刚性的张力。

---
### Page/Slide 6



# 当前图片内容解析

## 1. 提取文字与公式

### 文字内容
```
286 INDUSTRY SUPPLY (Ch. 23)
(i) Is it reasonable to suppose that the government could introduce "sur-
prise" taxes without making firms suspicious that there would be similar
"surprises" in the future? Suppose that the introduction of the tax in Jan-
uary 1993 makes gnome makers suspicious that there will be more taxes
introduced in later years. Will this affect equilibrium prices and supplies?
How? If a surprise tax makes gnome makers 
expect similar "surprises" in future, it
will take a higher current price to get
them to enter the industry. This will raise
the price paid by consumers.

23.4 (0) Consider a competitive industry with a large number of firms,
all of which have identical cost functions c(y) = y² + 1 for y > 0 and
c(0) = 0. Suppose that initially the demand curve for this industry is
given by D(p) = 52 − p. (The output of a firm does not have to be an
integer number, but the number of firms does have to be an integer.)

(a) What is the supply curve of an individual firm? S(p) = p/2. If
there are n firms in the industry, what will be the industry supply curve?
Y = np/2.

(b) What is the smallest price at which the product can be sold? p* =
2.

(c) What will be the equilibrium number of firms in the industry? (Hint:
Take a guess at what the industry price will be and see if it works.)
Guess at p* = 2. This gives D(p) = 52 − 2 =
n2/2, which says n* = 50.

(d) What will be the equilibrium price? p* = 2. What will be the
equilibrium output of each firm? y* = 1.

(e) What will be the equilibrium output of the industry? Y* = 50.
```

### 公式提取
- 个体企业成本函数：`c(y) = y² + 1`（当 y > 0）且 `c(0) = 0`
- 市场需求函数：`D(p) = 52 − p`
- 个体企业供给曲线：`S(p) = p/2`
- 行业供给曲线：`Y = np/2`
- 均衡最小价格：`p* = 2`
- 每个企业均衡产出：`y* = 1`
- 行业均衡产出：`Y* = 50`

## 2. 与上文知识点的连续性分析

### 基准均衡状态的意义
- 本题展示的完全竞争市场**无税收基准状态**，为理解《上文》中税收冲击提供参照系：
  - 长期均衡价格恰好等于最小平均成本点 `p* = 2`，验证"长期均衡需价格覆盖所有成本"原则
  - 每个企业产出 `y* = 1` 对应成本曲线上最低点，体现**规模经济临界点**
  - **关键衔接**：此基准状态与《上文》Munchkin案例中的"税前正回报"一致，构成**投资决策的起点参照**

### "Surprise taxes"段落的递进逻辑
- 段落揭示：若税后预期被破坏，企业将对**未来不确定性**要求风险溢价：
  ```
  If a surprise tax makes gnome makers expect similar "surprises" in future, 
  it will take a higher current price to get them to enter the industry.
  ```
  - **与上文关键点呼应**：这直接强化了《上文》"预期机制"部分中"资本决策前瞻性"结论
  - **新增洞见**：政府信用（fiscal credibility）成为隐性制度成本——不确定性将**提前抬升行业进入门槛**，使价格在税前即已上涨
  - **动态延伸**：对比《上文》(h)部分关于预期弱化滞后的描述，此处指出**政策不连贯性本身即可成为新的市场扭曲源**

### 数学模型的深层含义
1. **成本结构对税收传导的预示作用**：
   - 二次成本函数 `c(y) = y² + 1` 使边际成本线性递增（MC = 2y），预示长期供给曲线斜率为正
   - 与《上文》中"税收长期传递效率100%"形成对比：若行业具有向上倾斜的长期供给曲线（非常规完全竞争），税收传递率将**低于100%**，这为扩展税收归宿理论埋下伏笔

2. **整数约束的现实意义**：
   - 题目注明"企业数量必须为整数"，具象化《上文》"物理刚性"本质：
     - 即使达到 `n* = 50` 的理论均衡，实际市场只能存在49或51家企业，造成**持续性的微小超额利润/亏损**
     - 这解释了为何《上文》(e)中"订单量Smaller"后市场仍需动态调整

3. **最小价格的经济学本质**：
   - `p* = 2` 源于 `min AVC` 与 `min AC` 重合点
   - 与《上文》"短期维持生产条件（p > marginal cost）"形成反差：在无税收基准中，长期均衡已要求价格覆盖所有成本

## 3. 知识连续性定位
- 本图提供**分析税收效应的基础参照系**，使《上文》中"税收导致资本贬值加速"的结论更具说服力：
  - 当前 `p* = 2` 的零经济利润状态，正是《上文》(c)中"年现金流仅600"税后状态的反向参照
  - 行业供给曲线 `Y = np/2` 的线性结构，恰为理解《上文》(f)中"长期供给曲线平行上移"提供微观基础
- 对"Surprise taxes"的讨论直接延伸《上文》预期机制，论证：**制度不确定性会内生化为资产定价因素**，使税负前置影响市场均衡——这比《上文》(h)仅讨论物理滞后更有政策深度

---
### Page/Slide 7



# 完全竞争市场动态调整机制解析

## 1. 文字与公式提取

### 需求冲击情景分析
- **(f) 需求曲线移动**：`D(p) = 52.5 - p`  
  *调整机制*：  
  - 供给需求方程：`52.5 - p = 51p/2`  
  - 均衡价格：`p* = 105/53 < 2`  
  - 结论：新企业进入会导致亏损，均衡企业数量保持 **50家**

- **(g) 均衡计算**：  
  - 均衡价格：`52.5 - p = 50p/2 → p* = 2.02`  
  - 企业产出：`y* = 1.01`  
  - 企业利润：`≈ 0.02`

- **(h) 进一步需求移动**：`D(p) = 53 - p`  
  - 均衡企业数量：**51家**  
  - 均衡价格：**2**

- **(i) 均衡状态**：  
  - 企业产出：`y = 1`  
  - 企业利润：**Zero**

### 出租车市场案例 (23.5 (3))
- **已知条件**：  
  - 边际成本：`$5`（恒定）  
  - 单车容量：`20 trips/day`  
  - 需求函数：`D(p) = 1,200 - 20p`  
- **(a) 均衡计算**：  
  - 均衡价格：`5`（等于边际成本）  
  - 均衡需求量：`1,100 rides/day`  
  - 出租车数量：`55`

## 2. 动态调整机制解析

### 需求冲击的阶梯式响应
| 需求曲线 | 企业数量 | 价格 | 企业产出 | 经济利润 | 市场机制 |
|----------|----------|------|----------|----------|----------|
| `D(p)=52-p` | 50 | 2 | 1 | 0 | 基准均衡（上文已述） |
| `D(p)=52.5-p` | 50 | 2.02 | 1.01 | ≈0.02 | **短期调整**：价格微升维持50家企业 |
| `D(p)=53-p` | 51 | 2 | 1 | 0 | **长期调整**：新企业进入恢复零利润 |

- **关键动态逻辑**：  
  - 需求微增(`+0.5`)未触发新企业进入：当尝试新增第51家企业时，`p*<2`导致负利润（成本曲线约束）  
  - 需求持续增长(`+1`)：完全达到新均衡阈值，企业数量整数约束被突破（51家可维持`p*=2`）  
  - **与上文整数约束呼应**：验证了"实际市场仅能存在离散企业数"的物理刚性，解释为何需求需超过临界点(`ΔD=1`)才能触发结构变化

### 利润波动的经济含义
- **微利润(0.02)的动态意义**：  
  - 企业产出`y*=1.01`略超基准规模（上文`y*=1`），反映企业短期应对需求的边际调整能力  
  - 该利润成为新企业进入的**动态信号**：在无摩擦市场中，此微利将在下一期吸引新企业，直至利润归零  
  - **对比上文税收影响**：此内生利润波动与"Surprise taxes"外生冲击形成对照，前者是市场自我校准机制，后者破坏价格信号系统

### 出租车市场案例的理论验证
- **边际成本定价的核心性**：  
  - 恒定边际成本(`$5`)直接决定均衡价格——强化上文"长期价格=最小平均成本"原则  
  - 需求量`D(5)=1,100`与单辆车产能`20`，推导出出租车数量`55`，体现**行业供给的离散性约束**  
- **与基准模型的深层比较**：  
  | 特征 | 企业模型(上文) | 出租车模型 |  
  |------|----------------|------------|  
  | 成本性质 | 递增边际成本 | 恒定边际成本 |  
  | 产出弹性 | 企业可调产出规模 | 固定产能约束 |  
  | 调整层级 | 先价格后企业数 | 直接通过市场容量变化 |  
  - 验证上文理论：当边际成本恒定时，价格立即调整；成本递增时需经历"价格-数量"双重调整

## 3. 知识体系的递进关系
- **需求冲击如何强化上文核心结论**：  
  - 基准状态(`D=52-p`)中`p*=2`是长期均衡的"临界平面"  
  - 需求微增(`+0.5`)证明该平面具有**向下刚性**（价格可上探但难低于2）  
  - 需求足增(`+1`)触发的跳跃式调整，揭示**离散企业数量**如何造成非连续市场反应  
- **对政策启示的延伸**：  
  - 税收分析中"预期机制"（上文）在此处显化为**进入决策的阈值条件**：新企业只在`p*≥2`且利润≥0时进入  
  - 出租车案例证明：当政策扭曲市场信号（如发放有限牌照），将导致`55 vs 实际数量`的偏离，直接生成**制度性租金**——与"Surprise taxes"引发的风险溢价形成双重扭曲机制

---
### Page/Slide 8



### 提取内容  
#### 文字与公式  
- **(b)** In 1990 the city council of Ham Harbor created a taxicab licensing board and issued a license to each of the existing cabs. The board stated that it would continue to adjust the taxicab fares so that the demand for rides equals the supply of rides, but no new licenses will be issued in the future. In 1995 costs had not changed, but the demand curve for taxicab rides had become $ D(p) = 1,220 - 20p $. What was the equilibrium price of a ride in 1995? **$6**.  
- **(c)** What was the profit per ride in 1995, neglecting any costs associated with acquiring a taxicab license? **$1**. What was the profit per taxicab license per day? **20**. If the taxi operated every day, what was the profit per taxicab license per year? **$7,300**.  
- **(d)** If the interest rate was 10% and costs, demand, and the number of licenses were expected to remain constant forever, what would be the market price of a taxicab license? **$73,000**.  
- **(e)** Suppose that the commission decided in 1995 to issue enough new licenses to reduce the taxicab price per ride to $5. How many more licenses would this take? **1**.  
- **(f)** Assuming that demand in Ham Harbor is not going to grow any more, how much would a taxicab license be worth at this new fare? **Nothing**.  
- **(g)** How much money would each current taxicab owner be willing to pay to prevent any new licenses from being issued? **$73,000 each**. What is the total amount that all taxicab owners together would be willing to pay to prevent any new licences from ever being issued? **$4,015,000**. The total amount that consumers would be willing to pay to have another taxicab license issued would be **more than** this amount.  
- **23.6 (2)** (部分截断): In this problem, we will determine the equilibrium pattern of agricultural land use... The price of wheat at the market is $10 a bushel, cost to grow is $5 a bushel, transport cost 10 cents per mile.  

#### 核心公式  
$$ D(p) = 1,220 - 20p $$  

---

### 变化含义解析（基于上文知识体系）  
当前图片描述了**制度性供给约束**下的动态调整，完美验证上文"离散企业数量"与"需求冲击阶梯响应"的核心逻辑，具体解析如下：  

#### 1. **需求微增下的短期价格调整（对应 (b)-(c)）**  
- **变化机制**：  
  上文基准案例需求 $ D(p) = 1,200 - 20p $（均衡 $ p^*=5 $，$ N=55 $）。  
  本例需求移至 $ D(p) = 1,220 - 20p $（截距 $+20$），但**制度约束（无新许可）** 使企业数量 $ N $ 固定为 55。  
  → 供给量维持 $ 55 \times 20 = 1,100 $ rides/day，需求冲击通过**价格上行**吸收（$ p^*=6 $ 而非 5）。  
- **经济含义**：  
  - $ p^*=6 $ 导致 **正经济利润**（$ \$6 - \$5 = \$1 $/ride），与上文"需求微增 $+0.5$ 时利润 $\approx 0.02$" 逻辑一致：  
    > *需求未达 $ N $ 调整阈值时，市场仅靠价格调整，利润成为企业进入的**内生信号**（但因许可管制，此信号无法触发新进入）*。  
  - 离散约束凸显：即使利润为正（$ \$1/ride $），企业数量仍无法连续调整，印证上文"实际市场仅存离散企业数"的**物理刚性**。  

#### 2. **制度租金与长期均衡恢复（对应 (d)-(f)）**  
- **许可证价值形成**：  
  - (d) 中 $ \$73,000 $ 是许可证的**贴现制度租金**（$ \$7,300 \text{/year} / 10\% $），直接源于 (c) 的正利润。  
  - 呼应上文出租车案例：当 $ N $ 固定，需求增加会**创造制度性稀缺**，使许可持有者获得租金（对比上文"Surprise taxes"引致的扭曲，此处为**管制直接生成的租金**）。  
- **均衡恢复过程**：  
  - (e) 需 **1 新许可** 使 $ p^*=5 $：需求量 $ D(5)=1,120 $ 需 $ 1,120/20=56 $ 辆车，验证上文"需求持续增长需突破 $ N $ 临界点才能触发数量调整"。  
  - (f) $ p=5 $ 时许可价值归 **0**，强化上文 **"长期均衡要求 $ p = \text{边际成本} $"** 原则（利润归零）。  
  - 关键启示：制度管制（无新许可）延缓了市场向零利润均衡收敛，但一旦许可数量调整，**离散约束被克服**，价格立即回归成本线。  

#### 3. **寻租与社会福利损失（对应 (g)）**  
- **业主行为**：  
  单个业主愿付 $ \$73,000 $（等于许可证现值）阻挡新进入，总支付 $ \$4,015,000 $（$ 55 \times 73,000 $）。  
  - 这是上文"动态进入阈值"的延伸：**业主通过寻租维持制度租金**，将上文"企业进入的利润动机"转化为**垄断租金保护行为**。  
- **消费者视角**：  
  消费者愿付"more than" $ \$4,015,000 $，揭示 **需求侧效率损失**：  
  - 新许可释放消费者剩余 $ \Delta CS = \frac{1}{2} \times (6-5) \times (1,120-1,100) = \$10 $/day/许可，年化超 $ \$3,650 $，远大于生产者损失。  
  - 与上文"税收扭曲"对比：此处低效源于**供给端行政约束**（而非价格管制），导致 **"价格信号失效"** 和 **"社会总剩余损失"**。  

#### 知识连续性总结  
- **延续上文逻辑链**：  
  | 情境                | 上文 (企业模型)         | 本例 (出租车许可)        |  
  |---------------------|------------------------|-------------------------|  
  | **约束类型**        | 企业数量离散性         | 行政许可刚性            |  
  | **短期调整**        | 价格微升吸收需求冲击   | 政府调价维持供需平衡    |  
  | **利润动态**        | 微利 $\approx 0.02$    | 制度租金 $\$1$/ride    |  
  | **长期恢复**        | $ N $ 跳跃至 51 家     | 新许可使 $ N $ 增 1 辆 |  
- **深化核心结论**：  
  - 本例实证了上文"需求需超过临界点才能触发结构变化"——许可数量调整仅在 $ p=5 $ 时发生，对应上文 $ D(p)=53-p $ 需 $ \Delta D=1 $ 才突破 $ N=50 $ 阈值。  
  - 制度租金 ($ \$73,000 $) 量化了**离散约束的经济价值**，为上文"整数约束"提供现实尺度，揭示市场失灵本质：**当企业进入机制被行政替代，价格调整功能受损，租金取代利润成为核心均衡变量**。

---
### Page/Slide 9



### Extracted Content from Current Image

#### Text and Formulas
- **(a)** Profit per bushel formula:  
  \( \text{Profit per bushel} = 5 - 0.10t \)
- **(b)** Land rent formula:  
  \( \text{Rent} = 5,000 - 100t \)
- **(c)** Zero land value distance:  
  \( 50 \text{ miles} \)
- **23.7 (1)** Firm supply functions:  
  \( S_1(p) = p \), \( S_2(p) = p - 5 \), \( S_3(p) = 2p \)
- **23.7 (a)** Demand \( D(p) = 15 \) results:  
  - Market price: \( 5 \)  
  - Total output: \( 15 \)  
  - Firm 1 output: \( 5 \)  
  - Firm 2 output: \( 0 \)  
  - Firm 3 output: \( 10 \)
- **23.8 (0)** Individual firm supply:  
  \( S_i(p) = p/2 \)

#### Chart Description (23.7)
- **Vertical axis:** Price (ranging 0–20)  
- **Horizontal axis:** Quantity (ranging 0–40)  
- **Plotted curves:**  
  - \( S_2 \): Starts at (0, 5), linear with slope 1  
  - \( S_1 \): Origin-intercept, linear with slope 1  
  - \( S_3 \): Steeper linear curve through origin with slope 0.5 (i.e., \( q = 2p \))  
  - **Industry supply:** Piecewise linear curve with a kink at price \( p = 5 \), quantity \( Q = 15 \)

---

### Chart Analysis: Integration with Previous Concepts
The chart visually demonstrates **how discrete firm configurations and fixed entry constraints create non-linear supply behavior**, directly extending the discrete-adjustment framework from the prior discussion. Key insights:

#### **1. Piecewise Supply and Entry Thresholds (Kink at p=5)**  
- The industry supply kink at \( p = 5 \) corresponds to **Firm 2’s entry threshold** (\( S_2(p) \) activates only at \( p \geq 5 \)). Below \( p = 5 \), industry supply is solely from Firms 1 and 3 (\( S_{\text{ind}} = 3p \)), mirroring the prior case where demand shocks are absorbed by **price-only adjustments** without firm entry (e.g., taxi demand <1,120 rides/day holds \( N=55 \) fixed).  
- At \( D(p)=15 \), the market clears at \( p=5 \) with Firm 2 inactive—**no new firm enters despite demand growth**, reinforcing the principle that **sub-threshold demand changes do not trigger structural adjustments** (as in the taxi example where demand +0.5 only generated \( \approx \$0.02 \) profit per ride).  

#### **2. Discrete Jumps in Market Equilibrium**  
- The chart formalizes the **"critical point" for discrete regime shifts**: A marginal demand increase (e.g., \( D(p)=15.1 \)) would initially force a price rise (as \( p \) jumps above 5 to maintain equilibrium), but only when demand crosses the threshold for Firm 2’s entry (\( p \geq 5 \)) does total capacity expand. This aligns with the taxi case where **demand must hit 1,120 rides** to justify the single-license increase (from \( N=55 \) to 56).  
- Crucially, the **magnitude of the kink** (e.g., S_2’s supply slope) quantifies how the cost structure of *marginal entrants* shapes market response—paralleling the taxi permit value (\$73,000) that arises when administrative constraints bind at the entry threshold.  

#### **3. Implications for Supply Elasticity and Adjustment Lags**  
- The industry supply curve’s low elasticity in segments (e.g., near \( p=5 \)) reflects **short-run inflexibility** when firms are fixed. This mirrors the taxi scenario where price adjusts to \( p^*=6 \) (vs. 5) but cannot elicit entry due to license caps.  
- Section 23.8 (implied by \( S_i(p) = p/2 \)) extends this: With identical firms, supply curves for \( N=1,2,3,4 \) show that **increasing \( N \) reduces slope** (e.g., \( N=4 \) gives \( S_{\text{ind}} = 2p \), higher elasticity). However, transitions between integer \( N \) remain discontinuous—validating the prior claim that **"actual markets only exist at discrete enterprise counts"**. A demand shock small enough to avoid crossing the next \( N \)-threshold (e.g., \( N=3 \) to 4) will only push prices up, just as taxi permits fix \( p > \text{MC} \) until the license queue clears.  

#### **4. Contrast with Long-Run Zero-Profit Restoration**  
- Here, no firm earns positive profits at equilibrium (e.g., Firm 2 produces zero at \( p=5 \), implying its marginal cost equals price). This contrasts with the taxi case but confirms that **price must equal marginal cost for zero profit *if entry is unblocked***—when the chart’s threshold is crossed (e.g., \( p > 5 \)), Firm 2 enters and drives price back to its cost level (as in taxi part (f) where \( p=5 \) nullifies permit value). The absence of rent in this agricultural model highlights that **discrete constraints alone do not create economic rents; administrative barriers (e.g., taxi licenses) are required**—a key distinction from the prior regulatory context.  

This chart operationalizes the core insight: **Discrete firm structures convert continuous demand changes into stepwise supply responses**, with price adjusting first until the "entry \( N \)-threshold" is breached. It quantifies the **inflexibility wedge** that separates short-run price-only equilibria from long-run structural adjustments, directly linking to the earlier analysis of institutional barriers slowing zero-profit restoration.

---
### Page/Slide 10



### 图表与文本提取  
**图表元素**  
- **坐标轴**：纵轴为 *Price*（0–20），横轴为 *Quantity*（0–40）  
- **供给曲线**：$ S_1, S_2, S_3, S_4 $，均从原点出发的直线，斜率递减（$ S_1 $ 最陡峭，$ S_4 $ 最平缓）  
- **关键标注**：  
  - (a) *Demand* $ D(p) = 3.5 $（垂直线） → 均衡：$ p = \$3.50 $, $ Q = 3.5 $, **2家企业**  
  - (b) *Demand* $ D(p) = 8 - p $ → 均衡：$ p = \$3.20 $, $ Q = 4.8 $, **3家企业**  

---

### 图表解析  
#### **1. 离散企业数量与供给曲线形态**  
- **$ S_N $ 曲线含义**：$ S_N $ 表示 $ N $ 家企业时的行业供给曲线（基于上文 $ S_{\text{ind}} = N \cdot (p/2) $ 的推导）。  
  - **斜率递减**：$ N $ 增加时，供给曲线更平缓（如 $ S_4 $ 比 $ S_1 $ 弹性更高），印证“**增加企业数量降低供给曲线斜率**”的结论。  
  - **分段连续性**：$ S_1 \to S_2 \to S_3 \to S_4 $ 之间无平滑过渡，体现“**实际市场仅存在于离散企业数量点**”的核心逻辑。  

#### **2. 需求冲击与均衡调整**  
- **需求 $ D(p) = 3.5 $（问题 (a)）**：  
  - 垂直需求线与 $ S_2 $ 相交于 $ (3.5, 3.5) $，说明当需求固定时，**企业数量固定为 2**，价格直接反映短期供给约束（类似出租车牌照限制下 $ p > \text{MC} $）。  
  - **隐含阈值**：若需求略低于 3.5，价格会降至 $ S_1 $ 区间，但企业数量仍为 1（需求不足触发 $ N=2 $）。  

- **需求 $ D(p) = 8 - p $（问题 (b)）**：  
  - 线性需求与 $ S_3 $ 相交于 $ (4.8, 3.2) $，表明**需求扩张使 $ N $ 从 2 跳至 3**，验证“需求冲击必须跨越 $ N $-阈值才能触发企业进入”。  
  - **价格-数量动态**：价格（\$3.20）低于 (a) 中的 \$3.50，体现供给弹性随 $ N $ 增加而提升（$ S_3 $ 比 $ S_2 $ 更平缓）。  

#### **3. 与上文知识的衔接**  
- **短期不灵活性**：小幅度需求变动（如 $ D(p)=3.5 $）仅改变价格，企业数量保持 2，直接呼应“**离散约束将连续需求转化为阶梯式供给响应**”。  
- **进入阈值机制**：当需求从 3.5 增至 4.8（问题 (b)），价格从 \$3.50 降至 \$3.20，但企业数从 2 增至 3，说明 **“价格下调诱使新企业进入”**，与上文“价格调整先于结构变化”一致。  
- **对比长期自由进入**：问题 23.9 提及自由进入（$ p = \min \text{AC} $），但图表中 (a)(b) 场景仍受离散约束，凸显 **行政壁垒（如牌照）与完全竞争的分野**——此处无许可限制，但企业数量仍因短期固定而无法即时调整。  

---

### 关键结论  
图表定量验证了**离散企业结构对市场弹性的影响**：  
- **供给曲线的阶梯性**：$ S_1 $–$ S_4 $ 映射短期间断调整过程，需求冲击需突破 $ N $-阈值（如 $ Q > 3.5 $）才能驱动企业数量跃迁。  
- **价格机制的双重角色**：既需平衡当前供给（短期），又需触发结构变化（长期进入），但后者依赖需求强度跨越临界点。  
- **政策含义**：若市场存在人工约束（如出租车牌照），价格将长期高于边际成本，而此图中无此类约束，故均衡价格趋近于企业成本临界值（\$3），形成自然调整机制。

---
### Page/Slide 11



### 文字与公式提取  
**图表元素**  
- **坐标轴**：纵轴 *Price*（0–20），横轴 *Quantity*（0–40）  
- **曲线标注**：  
  - 原始成本曲线：`Blue mc`（蓝色边际成本）、`Blue ac`（蓝色平均成本）  
  - 单位税 `t` 下新曲线：`Red mc`（红色边际成本，上移 `t`）、`Red ac`（红色平均成本）  
  - 固定税 `l` 下新曲线：`Black ac`（黑色平均成本，上移）  
  - 关键价格点：`P`（原均衡价格）、`P+t`（单位税后价格）、`P+l`（固定税后价格）  

**文本内容**  
- **(b)** Suppose the government imposes a tax, `t`, on every unit of output sold by the industry. Use red ink to draw the new conditions on the above graph. After the industry has adjusted to the imposition of the tax, the competitive model would predict the following: the market price would **increase** by amount `t`, there would be **fewer** firms operating in the industry, and the output level for each firm operating in the industry would **Stay the same**.  
- **(c)** What if the government imposes a tax, `l`, on every **firm** in the industry. Draw the new cost conditions on the above graph using black ink. After the industry has adjusted to the imposition of the tax the competitive model would predict the following: the market price would **increase**, there would be **fewer** firms operating in the industry, and the output level for each firm operating in the industry would **increase**.  
- **23.10 (0)** In many communities, a restaurant that sells alcoholic beverages is required to have a license. Suppose that the number of licenses is limited and that they may be easily transferred to other restaurant owners. Suppose that the conditions of this industry closely approximate perfect competition. If the average restaurant’s revenue is $100,000 a year, and if a liquor license can be leased for a year for $85,000 from an existing restaurant, what is the average variable cost in the industry?  
  **$15,000.**  

---

### 图表解析  
#### **1. 单位税（`t`）冲击：供给刚性与结构调整**  
- **短期价格调整**：  
  边际成本曲线 `Blue mc` 上移 `t` 至 `Red mc`，导致短期均衡价格从 `P` 跳至 `P+t`（与上文 **inflexibility wedge** 一致）。价格立即上升 `t`，但企业数量**未变**（填空显示 "Stay the same"），体现 **短期供给刚性**——企业无法即时调整数量，仅通过价格传递部分冲击。  
- **长期结构变化**：  
  `Red ac` 引发企业亏损，触发**进入阈值（`N`-threshold）** 被突破：部分企业退出，行业供给收缩（曲线整体左移）。长期均衡时，**企业数量减少**（"fewer firms"），但每个企业产量维持不变（因边际成本未变，最优产出点不变）。这验证了上文 **"price-only equilibria" 向 "long-run structural adjustments" 的过渡**：价格调整是长期结构变化的先决条件，但企业退出仅发生在需求冲击（此处由税收引起）跨越阈值后。  

#### **2. 固定税（`l`）冲击：固定成本对进入阈值的影响**  
- **成本曲线变化**：  
  固定税使平均成本上移至 `Black ac`（`Blue ac` 上移），但边际成本 `Blue mc` **不变**，故短期 **每个企业产量不变**。  
- **长期调整机制**：  
  固定成本增加抬高了 **零利润门槛**（`min AC` 上升），导致：  
  - 市场价格上升（填空 "increase"），但**增幅小于单位税**（因无直接边际影响）。  
  - **企业数量减少**（"fewer firms"），体现 **"entry `N`-threshold" 被上移**：新企业需克服更高固定成本，进入门槛提高。  
  - 每个企业产量**增加**（"increase"），因行业供给收缩，留存企业需扩大产出以逼近新均衡，呼应上文 **"institutional barriers slowing zero-profit restoration"**（此处固定税为人为壁垒）。  

#### **3. 与牌照制度（23.10）及上文知识的衔接**  
- **牌照作为隐性固定税**：  
  23.10 中许可费 `$85,000` 等价于固定税 `l`，**许可租赁市场使牌照成本内生化**。零利润条件隐含：  
  \[
  \text{Revenue} = \text{Total Cost} \implies 100,000 = \text{AVC} \cdot Q + 85,000 \quad \text{（但 \$15,000 为总可变成本，非平均）}
  \]  
  牌照稀缺性创造 **类似行政壁垒的 `N`-threshold**，减缓了企业进入：需求未超阈值时，价格上升（直接反映牌照稀缺），而非企业数量调整。  
- **核心机制统一性**：  
  - 单位税与固定税均**扩大上文定义的 "inflexibility wedge"**：短期价格调整幅度不同（单位税完全转嫁，固定税部分转嫁），但长期均通过**企业数量离散调整**恢复零利润。  
  - **行业供给弹性差异**：单位税（`t`）降低短期供给弹性（`Red mc` 更陡），而固定税（`l`）通过提高进入门槛压制长期弹性，印证上文 **"离散企业数量导致阶梯式市场响应"**。  
- **政策启示延伸**：  
  23.10 中许可制度暴露 **"价格高于边际成本" 的根源**（牌照成本），而图表中无许可时（`t`/`l` 税）的价格调整更贴近自然阈值。这凸显 **行政壁垒 vs. 经济性税负**：前者长期扭曲价格，后者仅触发内生阈值跨越。  

---

### 关键结论  
- **税收类型决定调整路径**：  
  - 单位税 `t` 驱动**价格主导的短期均衡**，企业数量滞后调整。  
  - 固定税 `l` 直接重构**进入阈值**，强化长期结构刚性，与牌照制度同源。  
- **与上文深化衔接**：  
  双重税负场景定量验证 **"inflexibility wedge" 的核心作用**——企业数量调整仅在冲击越过 `N`-threshold 后启动，而价格始终承担短期缓存作用。牌照案例（23.10）更揭示 **制度性壁垒如何人为放大楔子**，使市场长期偏离完全竞争均衡。  
- **现实映射**：  
  交通管制（如车牌拍卖）或行业准入中，固定成本壁垒会**延长零利润恢复过程**，导致价格持续高于边际成本，而本图税收机制提供其内生化调整的对比参照。

---
### Page/Slide 12



### 解析：非法鸟类走私市场的微观经济学机制  
基于上文知识点总结（供给刚性、固定税冲击、牌照制度衔接），对当前图片（教科书第292页，问题23.11(2)）进行解析。本部分聚焦文字/公式提取及机制阐释，避免重复上文已有结论，但强化知识连续性。

---

#### **1. 文字与公式提取**  
##### **问题背景**  
> In order to protect the wild populations of cockatoos, the Australian authorities have outlawed the export of these large parrots. An illegal market in cockatoos has developed. The cost of capturing an Australian cockatoo and shipping him to the United States is about $40 per bird. Smuggled parrots are drugged and shipped in suitcases. This is extremely traumatic for the birds and about 50% of the cockatoos shipped die in transit. Each smuggled cockatoo has a 10% chance of being discovered, in which case the bird is confiscated and a fine of $500 is charged. Confiscated cockatoos that are alive are returned to the wild. Confiscated cockatoos that are found dead are donated to university cafeterias.

##### **子问题与解答**  
- **(a)** The probability that a smuggled parrot will reach the buyer alive and unconfiscated is `.45`. Therefore when the price of smuggled parrots is `p`, what is the expected gross revenue to a parrot-smuggler from shipping a parrot? `.45p`.  
- **(b)** What is the expected cost, including expected fines and the cost of capturing and shipping, per parrot? `$.10 × 500 + 40 = $90`.  
- **(c)** The supply schedule for smuggled parrots will be a horizontal line at the market price `$200`. (Hint: At what price does a parrot-smuggler just break even?)  
- **(d)** The demand function for smuggled cockatoos in the United States is `D(p) = 7,200 − 20p` per year. How many smuggled cockatoos will be sold in the United States per year at the equilibrium price? `3,200`. How many cockatoos must be caught in Australia in order that this number of live birds reaches U.S. buyers? `3,200 / .45 = 7,111`.  
- **(e)** Suppose that instead of returning live confiscated cockatoos to the wild, the customs authorities sold them in the American market. The profits from smuggling a cockatoo do not change from this policy change. Since the supply curve is horizontal, it must be that the equilibrium price of smuggled cockatoos will have to be the same as the equilibrium price when the confiscated cockatoos were returned to nature. How many live cockatoos will be sold in the United States in equilibrium? `3,200`. How many cockatoos will be permanently removed from the Australian wild? `6,400`.

##### **脚注**  
> * The story behind this problem is based on actual fact, but the numbers we use are just made up for illustration. It would be very interesting to have some good estimates of the actual demand functions and cost functions.

---

#### **2. 机制解析与上文知识衔接**  
##### **核心机制：隐性固定成本设定零利润阈值**  
- **概率性罚款的预期成本等价于固定税**  
  子问题(b)中，预期成本公式 `$.10 × 500 + 40 = $90` 体现了 **预期固定成本结构**：  
  - 捕获/运输成本 `$40` 可视为 **不变边际成本**（MC 不变，因每单位成本恒定），呼应上文“固定税（`l`）冲击”中边际成本不变的特征。  
  - 预期罚款 `$50`（= 0.1 × $500）构成 **风险溢价**，本质是 **隐性固定税**（`l`），直接抬高 **零利润门槛**（`min AC` 上移）。  
  - 此设定与上文牌照制度（23.10）一致：许可费 `$85,000` 作为固定税，使零利润条件从 `Revenue = AVC · Q` 拓展到 `Revenue = AVC · Q + l`。此处 `l` 隐式内化为 `$90`，可通过子问题(c)验证：  
    \[
    \text{Expected Revenue} = \text{Expected Cost} \implies .45p = 90 \implies p = 200
    \]  
    破碎均衡价格 `$200` 是 **“entry `N`-threshold” 的边界值**——价格低于此，走私者退出；高于此，新参与者涌入。  

- **水平供应曲线的长期含义**  
  子问题(c)指出供应曲线为水平线 `$200`，直接源于 **零利润条件下的完全弹性供给**：  
  - 与上文“短期供给刚性”对比：在合法市场（如牌照制度），离散企业数量导致阶梯式调整（短期无退出，价格完全吸收冲击）。但非法走私市场 **进入门槛低**（无行政壁垒），企业数量可连续调整，使长期供给弹性趋近无穷大，**无短期刚性**。  
  - 然而，其内核与固定税冲击一致：隐性固定成本（风险成本）**人为抬高阈值**，但市场能快速通过数量调整恢复零利润。这验证了上文结论——“**政策冲击是否触发阈值跨越取决于壁垒性质**”：牌照制度强化壁垒致调整迟滞，而走私市场壁垒弱（仅成本性），故立即达长期均衡。  

##### **需求冲击下的结构调整路径**  
- **需求固定下的阈值锁定效应**  
  子问题(d)引入需求函数 `D(p) = 7,200 − 20p`：  
  - 均衡产量 `3,200` 由需求决定（`D(200) = 7,200 - 20 \times 200 = 3,200`），而 **总捕获量 `7,111` 体现机构低效**：  
    \[
    \text{Total caught} = \frac{\text{Desired live arrivals}}{\text{Success probability}} = \frac{3,200}{.45} = 7,111
    \]  
    其中 `0.45` 是活体无没收概率，源于50%死亡率+10%没收率的双重损耗。此损耗类似 **“非经济性壁垒”**，使实际 **离散调整成本内部化**——为满足3,200单位需求，需7,111单位投入，印证上文“**inflexibility wedge**”在非法市场的变形。  

- **政策外生冲击的阈值不变性**  
  子问题(e)中政策变化（没收活鸟出售 vs. 放生）：  
  - 走私利润不变 → 破碎均衡价 `$200` 不变（因预期成本未变），直接呼应上文“**价格仅当冲击跨越阈值时才启动调整**”。此处没收政策未改变走私者成本结构，故价格无需重新调整，验证 **价格在阈值内的缓存作用**。  
  - 永久移除量从 `7,111` 降至 `6,400`（`3,200 / 0.5 = 6,400`），因政策消除没收损耗（仅死亡率50%影响），反映 **制度调整对阈值的压缩效应**：  
    - 当壁垒降低（如许可证制度简化），`N`-threshold 下移，恢复零利润速度加快。  
    - 这与上文“**行政壁垒 vs. 经济性税负**”结论一致：牌照制度（23.10）人为放大楔子，而走私案例中政策优化直接收窄 wedge。  

##### **与上文关键结论的强化衔接**  
| 上文知识点                | 本图片适用性                                                                 |
|---------------------------|----------------------------------------------------------------------------|
| **固定税抬高零利润门槛**  | 预期罚款 `$50` 作为隐性固定税，使 break-even price 从基础成本 `$40` 升至 `$200`。 |
| **离散数量导致阶梯响应**  | 非法市场因低壁垒，调整连续；但捕获-死亡-没收损耗创造 “隐性离散”，需 `7,111` 捕获满足 `3,200` 需求，量化 wedge 大小。 |
| **价格缓存作用**          | 政策变化(e)中，走私价格稳定在 `$200`，因冲击未达阈值；数量变化由需求驱动，而非价格主导，验证“**price-only equilibria**”的先决性。 |

> **关键延伸**：本题揭示 **“机构壁垒强度决定调整路径”** ——牌照制度（23.10）通过许可费将隐性固定税**外显化**，导致价格长期偏离边际成本；而走私市场的隐性成本虽设阈值，但低进入壁垒使价格快速收敛。二者共同说明：**经济性壁垒（如税收）触发内生调整，行政壁垒则扭曲市场机制**。

---
### Page/Slide 13



### 当前图片内容提取  
#### 文字与公式  
- **(f) 部分**：  
  > Suppose that the trade in cockatoos is legalized. Suppose that it costs about $40 to capture and ship a cockatoo to the United States in a comfortable cage and that the number of deaths in transit by this method is negligible. What would be the equilibrium price of cockatoos in the United States? `$40`. How many cockatoos would be sold in the United States? `6,400`. How many cockatoos would have to be caught in Australia for the U.S. market? `6,400`.  

- **23.12 (0) 部分**：  
  > The horn of the rhinoceros is prized in Japan and China for its alleged aphrodisiac properties. This has proved to be most unfortunate for the rhinoceroses of East Africa. Although it is illegal to kill rhinoceroses in the game parks of Kenya, the rhinoceros population of these parks has been almost totally depleted by poachers. The price of rhinoceros horns in recent years has risen so high that a poacher can earn half a year’s wages by simply killing one rhinoceros. Such high rewards for poaching have made laws against poaching almost impossible to enforce in East Africa. There are also large game parks with rhinoceros populations in South Africa. Game wardens there were able to prevent poaching almost completely and the rhinoceros population of South Africa has prospered. In a recent program from the television series *Nova*, a South African game warden explained that some rhinoceroses even have to be “harvested” in order to prevent overpopulation of rhinoceroses. “What then,” asked the interviewer, “do you do with the horns from the animals that are harvested or that die of natural causes?” The South African game warden proudly explained that since international trade in rhinoceros horns was illegal, South Africa did not contribute to international crime by selling these horns. Instead the horns were either destroyed or stored in a warehouse.  

- **(a) 部分**：  
  > Suppose that all of the rhinoceros horns produced in South Africa are destroyed. Label the axes below and draw world supply and demand curves for rhinoceros horns with blue ink. Label the equilibrium price and quantity.  

*注：图片中无显式公式或图表；(a) 部分要求绘制供需曲线，但实际图表未在当前图片中呈现。*  

---

### 基于上文知识点的详细解析  
#### 合法化对市场均衡的重构（对应 (f) 部分）  
- **价格机制的阈值解耦**：  
  上文指出，非法走私市场的均衡价格 `$200$` 源于隐性固定税（风险成本），构成 **`$N$-threshold` 边界值**（低于此价，参与者退出；高于此价，新参与者涌入）。当前图片合法化情景中，价格降至 `$40$`，直接验证了 **“行政壁垒消除后，阈值被重置”** 的核心结论：  
  - 非法状态下，`$50$` 的预期罚款作为隐性固定税，将 break-even price 从基础成本 `$40$` 推高至 `$200$`（因成功概率 `$0.45$`，故 `$0.45p = 90 \implies p = 200$`）。  
  - 合法化后，风险成本完全消失，**价格回归边际成本**（`$40$`），边际成本定价成为新均衡。这直接印证上文 **“政策移除壁垒使 `N`-threshold 下移至零”** 的推论：行政壁垒（非法贸易状态）是推高阈值的主因，而非经济性税负。  

- **需求与结构调整的连续性**：  
  - 销售量从非法状态的 `$3,200$`（上文子问题(d)中 `$D(200) = 7,200 - 20 \times 200 = 3,200$`）增至合法状态的 `$6,400$`，由需求函数 `$D(p) = 7,200 - 20p$` 决定（`$D(40) = 7,200 - 20 \times 40 = 6,400$`）。这体现 **“需求驱动数量调整”** 而非价格主导，强化上文 **“price-only equilibria 仅在阈值内有效”** 的逻辑——当冲击（合法化）跨阈值跃迁，价格一次性调整至新均衡，后续变动由需求弹性传导。  
  - 捕获量与销售量相等（`$6,400$`），因无死亡/没收损耗。与上文非法案例对比（需 `$7,111$` 捕获量满足 `$3,200$` 需求），凸显 **“inflexibility wedge 由制度壁垒创造”**：非法市场中，`$45\%$` 成功概率将损耗内部化为隐性离散调整成本；合法化后，wedge 消失，市场实现帕累托改进。  

#### 机构壁垒对供给效率的扭曲（对应 23.12 (0) 和 (a) 部分）  
- **南非案例的楔子（wedge）内化**：  
  - 上文强调 **“行政壁垒扭曲市场机制”**（如牌照制度外显化固定税）。当前图片中，南非合法管理但销毁犀牛角的行为，相当于 **人造行政壁垒**：  
    - 销毁产出使潜在供应（生育过剩的犀牛角）无法进入市场，即便无物理损耗（需求端存在，东亚消费者愿支付溢价），有效供应仍被人为压缩。  
    - 这与上文走私案例一脉相承：非法贸易的钞票被没收（`(e)` 部分）或合法化前的隐性成本，均体现 **“制度设计将外生冲击转化为内生 wedge”**——在此，国际非法贸易禁令使南非的储备无法变现，相当于施加隐性固定成本。  
  - 世界供需曲线需标签化（`(a)` 部分要求），但基于知识连续性：  
    - **纵轴（价格）**：反映需求端支付意愿（东亚市场价格已受盗猎推高）。  
    - **横轴（数量）**：南非销毁使世界供应曲线 **左移**（合法产能失效），但需求曲线不变（东亚需求刚性）。  
    - **均衡变动**：若南非角原可供应，销毁将导致均衡 **价格上升、数量下降**；这验证上文 **“壁垒强度决定调整路径”** ——南非的“主动销毁”强化 wedge，而东非盗猎屡禁不止则因无有效壁垒（类似走私市场），但供给无法制度化。  

- **与上文核心结论的衔接**：  
  | 上文关键结论               | 本图片适用性                                                                 |
  |----------------------------|-----------------------------------------------------------------------------|
  | **行政壁垒 vs. 经济性税负** | 南非销毁角属 **行政壁垒**（国际非法禁令），人为降低有效供给；合法化鸟类案例移除壁垒，证明“经济性冲击可内生调整，行政壁垒则制造刚性”。 |
  | **阈值的动态性**           | 当销毁政策移除（未提及），南非角可交易时，`$N$-threshold` 将下移，价格收敛至边际价值；但当前销毁维持高阈值，呼应上文“价格仅当冲击跨越阈值时调整”（阈值内价格缓存失效）。 |
  | **wedge 的测量**           | 鸟类合法化案例量化 wedge 消失（捕获量 = 销售量）；犀牛角中，销毁比率即 wedge 大小（潜在可交易量 vs. 实际供应量），延续上文“损耗 → 量化离散调整成本”的逻辑链。 |  

> **关键延伸**：合法化（(f) 部分）通过移除行政壁垒，实现 **“零利润边界回归边际成本”**；而南非（23.12 部分）以销毁规避非法责任，却延续了 **“制度性 wedge 的低效”**。两者共同强化：**经济效率取决于壁垒性质**——可规避的行政壁垒（如禁令）扭曲最甚，而风险性成本（如走私损耗）可通过市场弹性消化。

---
### Page/Slide 14



### 提取内容  
#### 文字与公式  
- **图表标签**：  
  - 纵轴：`Price`  
  - 横轴：`Quantity`  
  - 曲线：`S (Blue)`, `S (Red)`, `D (Blue)`  
  - 价格点：`P_a`, `P_b`  
  - 数量点：`Q_a`, `Q_b`  
- **问题文本**：  
  > (b) If South Africa were to sell its rhinoceros horns on the world market, which of the curves in your diagram would shift and in what direction? **Supply curve to the right.** Use red ink to illustrate the shifted curve or curves. If South Africa were to do this, would world consumption of rhinoceros horns be increased or decreased? **Increased.** Would the world price of rhinoceros horns be increased or decreased? **Decreased.** Would the amount of rhinoceros poaching be increased or decreased? **Decreased.**  
- **其他文本（非图表直接相关）**：  
  > 23.13 (1) The sale of rhinoceros horns is not prohibited because of concern about the wicked pleasures of aphrodisiac imbibers, but because the supply activity is bad for rhinoceroses. [...] Suppose that there is a constant marginal cost of $5 per ounce for growing marijuana and delivering it to buyers. But whenever the marijuana authorities find marijuana growing or in the hands of dealers, they seize the marijuana and fine the supplier. Suppose that the probability  

#### 图表结构  
- **原均衡**：供给曲线 `S (Blue)` 与需求曲线 `D (Blue)` 交于 `(Q_a, P_a)`。  
- **新均衡**：供给曲线右移至 `S (Red)`，与 `D (Blue)` 交于 `(Q_b, P_b)`，其中 `Q_b > Q_a` 且 `P_b < P_a`。  

---

### 图表解析  
#### 变化过程与含义  
当前图表展示了南非犀牛角**移除行政壁垒**（即停止销毁、允许合法出售）时的市场调整。结合上文知识点：  
- **供给曲线右移 (`S (Blue) → S (Red)`)**：  
  上文指出南非销毁犀牛角相当于**人为施加行政壁垒**，将潜在供应（生育过剩的犀牛角）排除在市场外，导致世界供应曲线左移（对应均衡点从 `(Q_b, P_b)` 左移至 `(Q_a, P_a)`）。此处反向操作——允许出售即**移除该壁垒**，使潜在供应进入市场，故供给曲线右移。这直接验证上文结论：**行政壁垒移除后，`N`-threshold 下移至零**，市场回归效率。  
- **均衡变动**（`P_a → P_b`, `Q_a → Q_b`）：  
  - **价格下降 (`P_a > P_b`)**：上文强调行政壁垒（如销毁）推高价格（非法/壁垒状态的 `p=200`，合法化后回归边际成本 `40`）。当南非出售犀牛角，生产端无隐性损耗，价格收敛至**边际成本定价**（上文“**价格回归边际成本**”的推论）。  
  - **数量上升 (`Q_b > Q_a`)**：销售量由需求函数 `D(p) = 7,200 - 20p` 决定（上文子问题(d)）。价格下降后，需求弹性驱动数量调整（`D(P_b) > D(P_a)`），体现 **“需求驱动数量调整”** 的连续性——冲击（壁垒移除）导致价格一次性跃迁至新均衡，后续变动由需求弹性传导。  
  - **盗猎减少**：上文量化非法市场的 `45\%` 捕获成功概率为 **“inflexibility wedge”**（损耗导致需 `7,111` 捕获量满足 `3,200` 需求）。此处供应曲线右移后，**wedge 消失**（隐性调整成本归零），盗猎动机弱化，呼应“**制度壁垒移除实现帕累托改进**”的核心逻辑。  

#### 与上文关键结论的衔接  
| 上文结论                  | 本图表验证点                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **行政壁垒 vs. 经济性税负** | 销毁属行政壁垒（国际禁令），移除后价格下降、数量上升；证明“**经济性冲击可内生调整，行政壁垒制造刚性**”（壁垒移除 vs. 持续销毁的对比）。 |
| **阈值的动态性**          | 供给右移代表冲击**跨越 `N`-threshold**，触发价格一次性调整至边际成本；若壁垒未移除（如持续销毁），阈值维持高位，价格缓存失效。 |
| **wedge 的测量**          | 销毁比率量化 wedge 大小（潜在供应 vs. 实际供应）；右移后捕获量=销售量，wedge 趋零，延续“**损耗→离散调整成本**”的逻辑链。 |  

> **政策启示**：南非的案例与上文鸟类合法化（(f) 部分）一致，说明**移除制度性壁垒**（而非仅调整经济性税负）是解决供给扭曲的关键。行政壁垒（销毁/非法化）制造的 wedge 无法通过市场弹性消化，其消除直接驱动价格向边际成本收敛，同时抑制盗猎（负外部性）。

---
### Page/Slide 15



### 提取当前图片文字与公式  
**文字内容：**  
- that marijuana is seized is .3 and that the fine if you are caught is $10 per ounce.  
- (a) If the “street price” is $p per ounce, what is the expected revenue net of fines to a dealer from selling an ounce of marijuana? .7p − 3. What then would be the equilibrium price of marijuana? $11.4.  
- (b) Suppose that the demand function for marijuana has the equation Q = A − Bp. If all confiscated marijuana is destroyed, what will be the equilibrium consumption of marijuana? A − 11.4B. Suppose that confiscated marijuana is not destroyed but sold on the open market. What will be the equilibrium consumption of marijuana? A − 11.4B.  
- (c) The price of marijuana will (increase, decrease, stay the same) Stay the same.  
- (d) If there were increasing rather than constant marginal cost in marijuana production, do you think that consumption would be greater if confiscated marijuana were sold than if it were destroyed? Explain. Consumption will increase because the supply curve will shift to the right, lowering the price.  

**公式：**  
- Expected revenue net of fines: \(0.7p - 3\)  
- Equilibrium price: \(\$11.4\)  
- Demand function: \(Q = A - Bp\)  
- Equilibrium consumption (for both destruction and sale of confiscated goods): \(A - 11.4B\)  

---

### 结合上文的知识点解析  
当前图片分析大麻市场中**没收政策的变化**（销毁 vs. 公开出售没收品），与上文犀牛角案例共享核心逻辑：**行政壁垒（如销毁）制造市场扭曲，但扭曲是否发生取决于成本结构**。以下结合上文知识点连续展开：  

#### 1. **行政壁垒的界定与成本结构依赖性**  
- 上文将南非销毁犀牛角定义为**行政壁垒**（人为排除潜在供应），导致供给曲线左移（如图表中 \(S_{\text{(Blue)}} \to S_{\text{(Red)}}\) 的反向操作）。  
- 在当前图片中：  
  - **销毁没收大麻等同于行政壁垒**：它强制移除潜在供应，但 (b) 部分显示，在**常数边际成本**下，销毁与否对均衡消费无影响（消费均为 \(A - 11.4B\)）。  
  - **关键原因**：上文强调“经济性冲击可内生调整，行政壁垒制造刚性”，但此处扭曲**仅在边际成本非弹性时显现**。常数 MC 下，供给完全弹性（供给曲线水平），行政壁垒不影响价格（仍由 \(0.7p - 3 = \text{MC}\) 决定），消费仅由需求函数 \(Q = A - Bp\) 导出，故剥离了壁垒的变形效应。  
  - 对比上文犀牛角案例：犀牛角隐含的“捕获损耗”使供应具有**离散调整成本**（类似上文 \(N\)-threshold），但大麻 (b) 部分因常数 MC 剥离了此效应，说明**行政壁垒的扭曲需依赖供给弹性**——若供给完全弹性（常数 MC），壁垒仅改变总产量（如销毁时需更高生产以满足消费），不影响均衡价格和消费量。  

#### 2. **政策变动的经济含义：壁垒移除的效果**  
- 上文结论：**屏障移除触发价格向边际成本收敛**（犀牛角案例中从 \(p=200\) 降至 \(40\)），且盗猎减少。  
- 在当前图片 (d) 部分：  
  - 若 **边际成本递增**，出售没收品（移除行政壁垒）将**使供给曲线右移**，价格下降，消费上升。  
  - **机制解释**：销毁时，没收率 (\(\theta = 0.3\)) 直接抑制有效供应（市场供给为 \((1-\theta)S(p)\)）；出售时，没收既不影响总供应（所有生产品流入市场），也弱化了经销商的预期损失（商品未销毁，但罚款仍存在）。在递增 MC 下，供给曲线向上倾斜，供应扩张导致**价格二次下降**，消费从 \(A - 11.4B\) 增加（例如至 \(A - Bp_{\text{new}}\)，其中 \(p_{\text{new}} < 11.4\)）。  
  - 衔接上文逻辑：此过程复现了犀牛角“壁垒移除后供给曲线右移 (\(S_{\text{(Blue)}} \to S_{\text{(Red)}}\))”的机制，直接验证“**行政壁垒移除实现帕累托改进**”的推论——价格下降减少需求缺口，同时抑制非法供应动机（因无隐性损耗，捕获量需求降低）。  

#### 3. **关键差异：常数 MC vs. 非弹性供给的政策启示**  
| 上文说理点               | 当前图片 (b)/(d) 验证                                                                 |  
|--------------------------|-------------------------------------------------------------------------------------|  
| **行政壁垒制造刚性**     | 常数 MC 下壁垒无影响（(b) 消费不变），但递增 MC 下壁垒引发扭曲（(d) 消费差异）；证明**刚性源于供给弹性不足**（如犀牛角繁殖周期的隐性成本）。 |  
| **wedge 的动态性**       | 销毁率量化 wedge 大小：在递增 MC 案例中，销毁导致 \(\text{捕获量} > \text{销售量}\)（如上文 \(7,111 > 3,200\)），出售后 wedge 趋零；衔接“**损耗→离散调整成本**”的因果链。 |  
| **政策有效性边界**       | 锁定常数 MC 时，仅调整经济惩罚（如罚款）即可内化风险（(a) 中 \(0.7p - 3 = \text{MC}\)）；但非弹性供给下，**必须移除行政壁垒**（如 (d) 出售没收品）才能释放效率。 |  

> **核心连续性**：当前图片强化了上文核心结论——**行政壁垒的消除（而非仅惩罚）是解决市场扭曲的关键**。在递增 MC 下，出售没收大麻等同于犀牛角合法化，直接推动价格收敛至边际成本，同时降低非法活动的“inflexibility wedge”。这解释了为何现实中“销毁禁令”（如部分国家大麻政策）常加剧黑市，而允许没收品流通（如南非犀牛角合法化）为帕累托改进。

---
### Page/Slide 16



### 当前图片解析（基于上文知识点连续展开）

#### 1. 提取图片文字  
- **文字内容**：`296 INDUSTRY SUPPLY (Ch. 23)`  
- **公式/图表**：无  

#### 2. 与上文的连续性衔接  
当前图片为教材章节标题页，表明后续内容属于**行业供给理论**（第23章），直接对应上文核心分析框架：  
- **行政壁垒与供给曲线移动**：上文通过犀牛角销毁、大麻没收案例，论证了行政壁垒（如销毁政策）对供给曲线的刚性扭曲。该章节标题提示，此类分析基于行业供给模型的结构特性——**供给曲线形状（弹性）决定政策有效性**。  
- **成本结构的关键作用**：  
  - 常数边际成本（水平供给曲线）：行政壁垒仅影响总产量（如销毁需额外生产补偿），但不改变均衡价格与消费量（如上文图片(b)部分）。  
  - 递增边际成本（上倾供给曲线）：行政壁垒导致价格-消费量扭曲（如上文图片(d)部分），移除壁垒后供给曲线右移，价格收敛至边际成本，验证帕累托改进。  
- **政策边界清晰化**：该章节内容隐含行业供给理论对“行政壁垒”的界定标准——**仅当供给存在调整成本（如离散生产、繁殖周期）时，销毁等行政强制才会制造刚性wedge**，呼应上文结论“壁垒的扭曲效应依赖成本结构”。  

> **核心衔接**：本章节（Ch. 23）为上文案例提供理论基础。无需重复销毁/出售机制，但需指出：当前标题页所指的“INDUSTRY SUPPLY”模型，是理解**行政壁垒为何在常数MC下无效、在递增MC下导致扭曲**的底层逻辑支撑。
