# PDF_Chapter_1

### Page/Slide 1



# 市场需求曲线解析

## 文字与数据提取
- **章节标题**：Chapter 1 The Market  
- **核心概念**：  
  - 需求曲线基于消费者保留价格构建，而非平滑曲线  
  - 保留价格定义：消费者对租用/不租用公寓完全无差异的价格点  
  - 阶梯需求特性：价格等于保留价格时存在两个需求量，形成价格均衡区间  
- **问题数据表**：  
  | Person | A | B | C | D | E | F | G | H |  
  |--------|---|---|---|---|---|---|---|---|  
  | Price  | 40 | 25 | 30 | 35 | 10 | 18 | 15 | 5 |

## 阶梯需求曲线构建逻辑
1. **保留价格排序**：  
   将价格按降序排列：**40 (A) → 35 (D) → 30 (C) → 25 (B) → 18 (F) → 15 (G) → 10 (E) → 5 (H)**

2. **需求量分段结构**：  
   | 价格区间          | 需求量 | 对应消费者       |  
   |-------------------|--------|------------------|  
   | $ p > 40 $      | 0      | -                |  
   | $ 40 \geq p > 35 $ | 1    | A                |  
   | $ 35 \geq p > 30 $ | 2    | A, D             |  
   | $ 30 \geq p > 25 $ | 3    | A, D, C          |  
   | $ 25 \geq p > 18 $ | 4    | A, D, C, B       |  
   | $ 18 \geq p > 15 $ | 5    | A, D, C, B, F    |  
   | $ 15 \geq p > 10 $ | 6    | A, D, C, B, F, G |  
   | $ 10 \geq p > 5 $  | 7    | 前7人            |  
   | $ p \leq 5 $      | 8      | 全部8人          |

3. **阶梯特性关键点**：  
   - 在**保留价格断点**（如 $ p=35 $）处，需求量存在**双值性**：  
     - 当 $ p $ 略高于 35 → 需求量=1（仅A保留租用）  
     - 当 $ p $ 略低于 35 → 需求量=2（A、D均租用）  
     - 精确等于 35 时 → 需求量可为1或2（D无差异）  
   - 这直接验证上文"阶梯状需求曲线存在供需相等的价格范围"的结论

## 与知识点的逻辑衔接
- **保留价格作为决策临界点**：数据表中每个价格值对应上文定义的消费者决策边界，例如B在 $ p=25 $ 时无差异  
- **阶梯宽度决定均衡区间**：若供给量为3，根据上文将推导均衡价格在 $ (25,30] $ 区间（最高价30，最低价25）  
- **阶梯高度与需求弹性**：垂直跳跃高度恒为1单位（每人最多租1套），体现完全价格刚性需求特征  

> 注：当前图片仅包含需求曲线构建的前置条件，后续需结合供给曲线才能确定具体均衡价格区间。阶梯结构为理解离散需求下的市场均衡提供了不可简化的微观基础。

---
### Page/Slide 2



### 当前图片内容提取与解析

#### 1. 图片文字与数据提取
- **页眉**：  
  `2 THE MARKET (Ch. 1)`
- **图表坐标轴**：  
  - 纵轴：`Price`（刻度：0, 10, 20, 30, 40, 50, 60）  
  - 横轴：`Apartments`（刻度：0, 1, 2, 3, 4, 5, 6, 7, 8）  
- **问题与答案文本**：  
  > (b) Suppose the supply of apartments is fixed at 5 units. In this case there is a whole range of prices that will be equilibrium prices. What is the highest price that would make the demand for apartments equal to 5 units? **$18**.  
  > (c) What is the lowest price that would make the market demand equal to 5 units? **$15**.  
  > (d) With a supply of 4 apartments, which of the people A–H end up getting apartments? **A, B, C, D**.  
  > (e) What if the supply of apartments increases to 6 units. What is the range of equilibrium prices? **$10 to $15**.  
  > 1.2 (3) Suppose that there are originally 5 units in the market and that 1 of them is turned into a condominium.  
  >    (a) Suppose that person A decides to buy the condominium. What will be the highest price at which the demand for apartments will equal the supply of apartments? What will be the lowest price? Enter your answers in column A, in the table. Then calculate the equilibrium prices of apartments if B, C, …, decide to buy the condominium.  

*注：图片中无公式，仅含离散价格数值和文字描述。*

---

#### 2. 图表与问题解析
##### 阶梯需求曲线的图像验证与含义
当前图片中的阶梯需求曲线直接映射了上文知识点总结中的**保留价格排序**和**需求量分段结构**。图表以横轴公寓数量（0–8）和纵轴价格（0–60）展示需求曲线，其阶梯转折点严格对应上文表中的保留价格降序排列：  
- **转折点序列**：  
  | Apartments | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  
  |------------|---|---|---|---|---|---|---|---|  
  | Price      | 40 (A) | 35 (D) | 30 (C) | 25 (B) | 18 (F) | 15 (G) | 10 (E) | 5 (H) |  

**阶梯变化的核心含义**：  
- **非平滑性与断点跳跃**：每个阶梯垂直下降点（如价格从40降至35）对应消费者保留价格（上文定义：消费者租用/不租用无差异的价格）。例如：  
  - 在公寓数量=1 → 2 时，价格从40跳至35，反映**D的保留价格=35**。当价格等于35时，D处于无差异状态（需求量可能为1或2），这直接验证上文“阶梯状需求曲线存在供需相等的价格范围”的结论。  
  - 所有垂直跳跃高度恒为1单位，体现**完全价格刚性需求特征**（每人最多租1套）。  
- **阶梯宽度决定均衡区间**：  
  - 图表中每段水平阶梯代表一个**价格区间**，其宽度（如价格18到15之间约3单位）对应需求量的稳定区间（如需求=5时价格在(15, 18]）。  
  - 例如，需求=5的阶梯位于公寓数量5处，价格范围从18（上边界）降至15（下边界），**而非单一点价格**。这强化了上文“阶梯结构为离散需求下市场均衡提供微观基础”的观点。

##### 问题逻辑与均衡价格推导
图片中的问题基于需求曲线求解供给-需求均衡，其答案直接依赖上文的阶梯结构：  
- **(b) 供给=5时，需求=5的最高价格=$18**  
  当价格=18（F的保留价格），F会租用公寓（因价格≤保留价格），**需求正好为5**（A, D, C, B, F）。若价格>18，F退出市场，需求降至4。此结果印证上文表格中“$18 \geq p > 15$ 时需求=5”的区间上界。  

- **(c) 需求=5的最低价格=$15**  
  逻辑上，需求=5要求 $p > 15$（因 $p=15$ 时G租用，需求增至6）。但图片答案标注$15，反映了**阶梯断点的离散处理**：上文指出精确等于保留价格（如15）时，需求量存在双值性（G无差异），因此最低有效价格常被简化为断点值$15，实际操作中代表略高于15的临界。  

- **(d) 供给=4时，入住者为A, B, C, D**  
  直接应用**保留价格排序**：择取最高保留价格的前4人（A:40, D:35, C:30, B:25），与上文需求量分段表中需求=4的区间（$25 \geq p > 18$）完全一致。  

- **(e) 供给=6时，均衡价格范围=$10 to $15**  
  对应需求量=6的阶梯（上文表格：$15 \geq p > 10$）。  
  - **上边界$15**：当 $p=15$，G租用，需求=6。  
  - **下边界$10**：当 $p>10$ 且 $p \leq 15$，需求保持6；若 $p=10$，E租用，需求增至7。  
  此范围验证了上文“阶梯宽度决定均衡区间”的论断——供给量变动时，均衡价格范围由相邻保留价格间隙决定。

##### 1.2(3)问题的延伸意义
- **市场结构变化影响**：当1单位转为公寓时，需求曲线需重构（如A购买后，需求减少1单位）。这体现了上文未明确的**动态均衡特性**：均衡价格区间随供给/需求成员变动而平移（例如，A退出后，需求=4的新均衡区间上移至(25,30]）。  
- **政策启示**：此设置揭示**稀缺资源再分配**（如转为公寓）如何压缩需求曲线，导致价格区间上移，为理解市场扰动提供微观基础。

> **知识连续性说明**：本部分不重复上文已详述的保留价格定义或阶梯构建逻辑，而是聚焦图片对**离散需求均衡的量化应用**——通过具体供给值推导价格区间，凸显阶梯曲线在政策分析中的实操价值。后续问题（如1.2(3)）进一步深化需求侧变动的影响，衔接至市场动态调整的分析框架。

---
### Page/Slide 3



#### 1. 文字与数值提取  
**表1：个人价格参数**  
| Person | A | B | C | D | E | F | G | H |  
|--------|---|---|---|---|---|---|---|---|  
| High price | 18 | 18 | 18 | 18 | 25 | 25 | 25 | 25 |  
| Low price | 15 | 15 | 15 | 15 | 18 | 15 | 18 | 18 |  

**问题与答案**  
- *(b) Suppose that there were two people at each reservation price and 10 apartments. What is the highest price at which demand equals supply?*  
  **Answer: 18**  
- *18. Suppose that one of the apartments was turned into a condominium. Is that price still an equilibrium price?*  
  **Answer: Yes**  
- **1.3 (2) Monopolist scenario**  
  - *(a) Monopolist revenue table*  
    | Number | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  
    |--------|---|---|---|---|---|---|---|---|  
    | Price  | 40 | 35 | 30 | 25 | 18 | 15 | 10 | 5 |  
    | Revenue| 40 | 70 | 90 | 100| 90 | 90 | 70 | 40 |  
  - *(b) Which of the people A–F would get apartments?*  
    **Answer: A, B, C, D**  
  - *(c) If the monopolist were required to rent exactly 5 apartments, what price would he charge to maximize revenue?*  
    **Answer: $18**  
  - *(d) Who would get apartments?*  
    **Answer: A, B, C, D, F**  
  - *(e) If the landlord could charge each individual a different price, what is the maximum revenue for 5 apartments?*  
    **Answer: $148**  
  - *(f) If 5 apartments were rented, which individuals would get them?*  
    **Answer: A, B, C, D, F**  
- **1.4 (2) Rent control scenario**  
  *Suppose 5 apartments, rent-control max rent $9, and A,B,C,D,E get apartments while F,G,H are frozen out.*  

---

#### 2. 表格解析与知识连续性  
##### 2.1 需求曲线数据表（1.3(a)）的微观基础  
- **保留价格映射**：  
  该表直接延续上文知识点总结中的**阶梯需求曲线结构**，其中 `Price` 列严格对应上文保留价格降序序列：`A(40) > D(35) > C(30) > B(25) > F(18) > G(15) > E(10) > H(5)`。每增加1单位公寓数量，价格阶梯垂直下降点由新消费者的保留价格决定（如需求量从4→5时，价格从25降至18，由F的保留价格触发）。  

- **阶梯宽度与收入最大化**：  
  - `Revenue` 列印证上文“**阶梯宽度决定均衡区间**”的核心论断：  
    - 需求量为4时，价格区间为 `(25, 30]`（上文知识点总结），垄断者设定 `p = 25`（下边界）卖出4套，收入 `4 × 25 = 100` 达峰值（对比 `p > 25` 时需求量≤3，收入<100）。  
    - 需求量为5时，价格区间为 `(15, 18]`，设定 `p = 18`（上边界）收入 `5 × 18 = 90`；若 `p ≤ 15` 需求量增至6，但收入降至 `6 × 15 = 90`，**阶梯的离散性导致收入峰值出现在非端点**（`q=4` 收入100 > `q=5/6` 收入90）。  
  - 此表量化了上文所述“**阶梯结构为离散需求下市场均衡提供微观基础**”，揭示垄断者通过**精准对齐保留价格断点**（而非连续曲线顶点）实现收入最大化。  

##### 2.2 个人价格参数表（表1）的市场机制含义  
- **保留价格双值性的政策应用**：  
  - `High price` 和 `Low price` 定义消费者在不同政策下的**有效支付意愿区间**：  
    - 例如，E 的 `High price=25` 与 `Low price=18` 对应上文保留价格序列中 **B=25 和 F=18** 的阶梯间隙，体现租金管制（1.4部分）中“**冻结部分消费者**”后剩余需求的压缩效应。  
    - 当租控上限 $9 时（1.4问题），E 虽保留价格25>9，但因 `Low price=18 > 9`，其需求被抑制（间接验证上文“价格等于保留价格时需求量双值性”）。  
  - 此表可视为上文“**阶梯宽度决定均衡区间**”向**混合需求政策**的延伸：`High`/`Low` 差距反映供应刚性下消费者的福利弹性（如G的 `High=25` 与 `Low=18` 差距大，表明对供给变动敏感）。  

##### 2.3 问题逻辑与阶梯曲线的动态演化  
- **1.3(c)-(d)：数量管制的均衡推导**  
  - 限定需求量=5时，垄断者选择 `p = 18`（F的保留价格），对应上文需求量=5的阶梯上界（`$18 \geq p > 15$`）。  
    - **机制**：`p = 18` 使F无差异（租或不租），需求量稳定为5（A,D,C,B,F）；若 `p > 18`，F退出需求量降至4，收入下降至70（见1.3(a)表）。  
  - 此结果强化上文“**阶梯断点的离散处理**”——精确等于保留价格时，需求量双值性被政策约束（法律要求租5套）化解为**可操作的均衡点**。  

- **1.3(e)-(f)：完全价格歧视的微观验证**  
  - 差异定价下，5套最大收入 $148 = 40(A) + 35(D) + 30(C) + 25(B) + 18(F)$，严格遵循上文**保留价格降序原则**：  
    - 取前5高保留价格（A,D,C,B,F），其和 $40+35+30+25+18=148$。  
  - 此计算直接依赖阶梯曲线的**分段可加性**，证明离散需求下完全价格歧视收入高于统一定价（$148 > $90，1.3(c)）。  

- **1.4(2)：租控政策的阶梯压缩**  
  - 租控价 $9$ 低于所有保留价格下限（`Low price ≥15`），导致：  
    - A-E 以 $9$ 租得房（因 `High price ≥18 >9`），反映**需求端僵化**：消费者无选择弹性（上文“ Prices rigid”）。  
    - F-G-H 被冻结（`F Low price=15 >9` 但未达标），**原阶梯需求曲线从8人削至5人**，均衡区间上移（对比上文需求=5时价格在 `(15,18]`，现强制压至 $9$）。  

> **知识连续性说明**：本解析聚焦图片中**离散需求在垄断/政策冲击下的实操验证**——  
> - 1.3(a) 表量化上文所述需求阶梯的收入效应，揭示垄断均衡高度依赖断点跳跃；  
> - 表1 拓展阶梯概念至混合价格政策，凸显上文“资源再分配压缩需求曲线”的动态性；  
> - 1.4问题显式演示上文“阶梯宽度决定均衡”的脆弱性，政策干预将连续区间退化为单一价格。  
> 后续问题（如1.3(e)）深化差异定价对阶梯结构的解构，衔接至市场效率分析框架。

---
### Page/Slide 4



### 3. 当前图片解析

#### 3.1 文字与公式提取
- **所有文字内容**:
  ```
  4  THE MARKET (Ch. 1)

  (a) If subletting is legal—or, at least, practiced—who will sublet to whom in equilibrium? (Assume that people who sublet can evade the city rent-control restrictions.) E, who is willing to pay only $10 for an apartment would sublet to F, who is willing to pay $18.

  (b) What will be the maximum amount that can be charged for the sublet payment? $18.

  (c) If you have rent control with unlimited subletting allowed, which of the consumers described above will end up in the 5 apartments? A, B, C, D, F.

  (d) How does this compare to the market outcome? It’s the same.

  1.5 (2) In the text we argued that a tax on landlords would not get passed along to the renters. What would happen if instead the tax was imposed on renters?

  (a) To answer this question, consider the group of people in Problem 1.1. What is the maximum that they would be willing to pay to the landlord if they each had to pay a $5 tax on apartments to the city? Fill in the box below with these reservation prices.

  (b) Using this information determine the maximum equilibrium price if there are 5 apartments to be rented. $13.

  (c) Of course, the total price a renter pays consists of his or her rent plus the tax. This amount is $18.

  (d) How does this compare to what happens if the tax is levied on the landlords? It’s the same.
  ```

- **表格内容**:
  | Person     | A   | B   | C   | D   | E   | F   | G   | H   |
  |------------|-----|-----|-----|-----|-----|-----|-----|-----|
  | Reservation Price | 35  | 20  | 25  | 30  | 5   | 13  | 10  | 0   |

- **公式/关键数值**:
  - Sublet payment max: `$18`
  - Equilibrium outcome with rent control: `A, B, C, D, F`
  - Max equilibrium rent for 5 apartments: `$13`
  - Total renter payment (rent + tax): `$18`

#### 3.2 图表分析与知识连续性
当前图片包含一个**离散需求保留价格表**（1.5(2)(a)部分），补充了上文“阶梯需求结构”的实证基础。表格展示了8位消费者的 reservation price，排序后序列为：  
**35(A) > 30(D) > 25(C) > 20(B) > 13(F) > 10(G) > 5(E) > 0(H)**。  

- **阶梯结构的动态含义**：  
  - 此表直接体现上文“**阶梯宽度决定均衡区间**”的核心论断。需求量 $q=5$ 时，价格阶梯的垂直下降点由第5高的保留价格触发（F的 `$13`），形成价格区间 `(10, 13]`。  
    - 若 $p > 13$（如 $p=14$），F退出需求，$q=4$（A,B,C,D），收入下降。  
    - 若 $p \leq 10$（如 $p=10$），G进入需求，$q=6$，但均衡收入峰值仍出现在 $q=5$ 时（见下文税收分析）。  
  - 这与上文知识点总结中“**阶梯的离散性导致收入峰值出现在非端点**”一致：$q=5$ 时收入 `$5 \times 13 = 65$` 高于 $q=6$ 时（`$6 \times 10 = 60$`），验证垄断均衡高度依赖断点跳跃。

- **税收政策对阶梯需求的冲击**（衔接上文“混合需求政策”逻辑）：  
  - 1.5(2) 部分通过 `$5` 税收实验，量化说明**税收归宿与法定征收对象无关**：  
    - 税前：$q=5$ 的均衡租价 `$13$` 由F的保留价格决定，与上文 `F(18)` 序列逻辑同构（保留价格触发送阶下降）。  
    - 税后：  
      - 租客实际支付总成本 = 租价 + 税收 = `$13 + 5 = $18$`（1.5(2)(c)）。  
      - 若税收改向房东征收，均衡结果相同（1.5(2)(d)），因固定供应（5套公寓）下，阶梯需求曲线的**价格弹性趋近于零**，税收完全转嫁给租客，总支付维持 `$18$`。  
    - **关键衔接**：此结论实证上文“**资源再分配压缩需求曲线的动态性**”——税收作为外部冲击，未改变阶梯底部（H的`$0$`），但将价格阶梯内移，均衡租价 (`$13$`) 与税前原始阶梯顶点 (`$13$`) 重合，印证“政策干预将连续区间退化为单一价格”。

- **与知识连续性的强化**：  
  - 此表格是上文“个人价格参数表（表1）”的延伸，通过新保留价格序列（如 `F(13)` 代替上文的 `F(18)`）证明：**阶梯曲线的分段可加性** universally 适用于不同政策场景。  
  - 1.5(2) 与 1.3(c) 租控问题逻辑一致：  
    - 无限转租（1.3(c)）使租控妥协于市场结果（`A,B,C,D,F` 获得公寓）；  
    - 税收中性（1.5(2)）同样体现“**离散需求下，制度安排仅调整均衡表达式，不改变效率损失本质**”。  
  - **知识演进**：上文强调租控凸显“阶梯宽度脆弱性”，此例则揭示税收归宿的**阶梯惯性**——政策冲击后，均衡始终锚定保留价格断点（如F的`$13$`），为后续市场效率分析提供微观实证。
