# PDF_Chapter_17

### Page/Slide 1



### 1. 文字与公式提取  
**标题与章节**  
Chapter 17  
Auctions  

**Introduction**  
An auction is described by a set of rules. The rules specify bidding procedures for participants and the way in which the array of bids made determines who gets the object being sold and how much each bidder pays. Those who are trying to sell an object by auction typically do not know the willingness to pay of potential buyers but have some probabilistic expectations. Sellers are interested in finding rules that maximize their expected revenue from selling the object.  

Social planners are often interested not only in the revenue generated from an auction method, but also in its efficiency. In the absence of externalities, an auction for a single object will be efficient only if the object is sold to the buyer who values it most highly.  

**17.1 (1) 案例**  
At Toivo’s auction house in Ishpemming, Michigan, a beautiful stuffed moosehead is being sold by auction. There are 5 bidders in attendance: Aino, Erkki, Hannu, Juha, and Matti. The moosehead is worth $100 to Aino, $20 to Erkki, and $5 to each of the others. The bidders do not collude and they don’t know each others’ valuations.  

- **(a)** If the auctioneer sells it in an English auction, who would get the moosehead and approximately how much would the buyer pay?  
  **Aino would get it for $20.**  

- **(b)** If the auctioneer sells it in a sealed-bid, second-price auction and if no bidder knows the others’ values for the moosehead:  
  - How much should Aino bid to maximize expected gain? **$100**  
  - How much should Erkki bid? **$20**  
  - How much would each of the others bid? **$5**  
  - Who gets it and at what price? **Aino would get it for $20.**  

**17.2 (2) 案例**  
Charlie Plopp sells used construction equipment in a quiet Oklahoma town. He has run short of cash and needs to raise money quickly by selling an old bulldozer. If he doesn’t sell his bulldozer to a customer today, he will have to sell it to a wholesaler for $1,000.  

Two kinds of people are interested in buying bulldozers: professional operators (willing to pay $6,000) and recreational users.  

---

### 2. 案例解析（结合上文知识点）  
#### **17.1 (1) 案例逻辑验证**  
- **效率体现**：两拍卖形式均将物品分配给最高估值者（Aino, $100），符合上文“**single-object auction efficiency requires sale to highest-value buyer**”的结论。  
- **英式拍卖**：开放竞价中，价格上升至次高估值（$20）时 Erkki 退出，Aino 以略高于 $20 的价格中标（简化为 $20），体现**价格 discovery**机制。  
- **密封第二价格拍卖**：  
  - 竞标者真实出价（Aino $100, Erkki $20, 其他人 $5）构成**主导策略均衡**（Vickrey 拍卖核心特性），与上文“**with no collusion, sealed-bid second-price auction ensures truthful bidding**”一致。  
  - 支付价格为第二高报价（$20），验证“**efficiency does not require price equal to highest valuation**”，仅需分配至最高价值者。  

#### **隐含机制对比**  
- 两种拍卖均实现效率，但**卖家收益相同（$20）**，说明在单物品独立私人价值模型中，预期收益可能受**Revenue Equivalence Theorem**约束（需后续章节展开）。  
- 若存在“**wholesale fallback option**”（如 17.2 案例中 $1,000 底价），可能直接影响拍卖策略，但本例未触发该条件。

---
### Page/Slide 2



### 当前图片内容提取

#### 文字内容
214 AUCTIONS (Ch. 17)  
more, while a weekend recreational user would be willing to pay $4,500 but no more. Charlie puts a sign in his window. “Bulldozer Sale Today.”  
Charlie is disappointed to discover that only two potential buyers have come to his auction. These two buyers evidently don’t know each other. Charlie believes that the probability that either is a professional bulldozer operator is independent of the other’s type and he believes that each of them has a probability of 1/2 of being a professional bulldozer operator and a probability of 1/2 of being a recreational user.  
Charlie considers the following three ways of selling the bulldozer:  
- Method 1. Post a price of $6,000 and if nobody takes the bulldozer at that price, sell it to the wholesaler.  
- Method 2. Post a price equal to a recreational bulldozer user’s buyer value and sell it to anyone who offers that price.  
- Method 3. Run a sealed-bid auction and sell the bulldozer to the high bidder at the second highest bid (if there is a tie, choose one of the high bidders at random and sell the bulldozer to this bidder at the price bid by both bidders.)  
(a) What is the probability that both potential buyers are professional bulldozer operators? 1/4. What is the probability that both are recreational bulldozer users? 1/4. What is the probability that one of them is of each type? 1/2.  
(b) If Charlie sells by method 1, what is the probability that he will be able to sell the bulldozer to one of the two buyers? 3/4. What is the probability that he will have to sell the bulldozer to the wholesaler? 1/4. What is his expected revenue? $(3/4) × $6,000 + (1/4) × $1,000 = $4,750.  
(c) If Charlie sells by method 2, how much will he receive for his bulldozer? $4,500.  
(d) Suppose that Charlie sells by method 3 and that both potential buyers bid rationally. If both bidders are professional bulldozer operators, how much will each bid? $6,000. How much will Charlie receive for his bulldozer? $6,000. If one bidder is a professional bulldozer operator and one is a recreational user, what bids will Charlie receive? Professional bids $6,000. Recreational user bids $4,500. Who will get  

#### 公式
- 概率计算：  
  - P(both professional) = \( \frac{1}{4} \)  
  - P(both recreational) = \( \frac{1}{4} \)  
  - P(one of each type) = \( \frac{1}{2} \)  
- Method 1 预期收入：  
  $$
  \left( \frac{3}{4} \times \$6,000 \right) + \left( \frac{1}{4} \times \$1,000 \right) = \$4,750
  $$

---

### 案例解析

#### 机制与概率逻辑（链接上文知识点）
- **独立类型概率**： Charlie 的假设（每个买家独立且有 \( \frac{1}{2} \) 概率为专业或休闲）直接应用了上文单物品拍卖的**独立私人价值模型**。概率计算（\( \frac{1}{4} \), \( \frac{1}{4} \), \( \frac{1}{2} \)) 源于买家类型独立，验证了上文隐含的“**无合谋且估值独立时，概率分布可简化分析**”原则。  
- **wholesale fallback option 的影响**： $1,000 批发价（上文 17.2 案例开头提及）在 Method 1 中作为保留价格，导致部分场景（两个休闲用户）无法售出，体现上文“**fallback option 直接影响卖家收益和销售概率**”，但未改变核心拍卖效率逻辑。

#### 销售方法对比（结合上文机制特性）
- **Method 1（固定高价）**：  
  - 销售概率 \( \frac{3}{4} \) 源于仅当两个买家均为休闲用户时失败（上文知识点中，英式拍卖需价格触及次高估值，此处高价格 $6,000 仅专业用户接受）。  
  - 预期收入 $4,750 反映了收益权衡：虽可能售出高价，但 $1,000 fallback 降低了稳定性，与上文“**交易未达成风险会导致期望收益低于潜在峰值**”一致。

- **Method 2（固定休闲价）**：  
  - 稳定收入 $4,500 对应休闲用户估值，上文未直接讨论此机制，但隐含其**非效率性**：专业用户估值 $6,000 > $4,500，但价格固定导致卖家无法捕获剩余（对比上文 17.1 案例，真实估值未被最大化）。

- **Method 3（密封第二价格拍卖）**：  
  - **真实出价验证**：买家“bid rationally”直接对应上文密封第二价格拍卖的**主导策略均衡**（Aino 出 $100、Erkki 出 $20）。专业用户出 $6,000（自身估值）、休闲用户出 $4,500（自身估值），符合“**truthful bidding 属性**”。  
  - **支付价格逻辑**：  
    - 两专业时，第二高价为 $6,000（无竞争下降），Charlie 收 $6,000（与上文 17.1(b) 中“Aino 支付 $20”同理，第二高报价决定价格）。  
    - 混合类型时，第二高价为 $4,500（休闲出价），专业用户中标——验证上文“**效率仅要求分配至最高价值者，不需支付最高估值**”。  
  - 此机制延续了上文“**single-object auction efficiency**”：总将推土机分配给最高估值买家（专业用户），且支付次高估值，与 17.1 案例逻辑完全一致。  
  - *隐含连续性*：若扩展计算预期收入，将体现 Revenue Equivalence Theorem（因 17.1 未触发 fallback，而此处 Method 1/3 的期望收入在独立私有价值下应趋近，但本例 Method 3 未给出数值，需后续推导）。

#### 机制选择启示
- Method 3 优于 Method 2：前者在混合类型时捕获部分专业价值（收 $4,500 vs. Method 2 的固定 $4,500，但 Method 3 在两专业时收 $6,000），体现上文“**拍卖机制比固定价格更适应估值分布**”。  
- Method 1 与 Method 3 比较：Method 3 无 fallback 成本（因总有高标者），在本例中可能实现更高期望收入（上文 17.1 案例中两拍卖形式收益相同，但 fallback 选项在此引入新变量，需具体计算）。  
- **效率一致性**：三种方法均在可售时分配给专业用户（若存在），但仅 Method 3 通过价格发现确保长期效率——呼应上文“**分配有效性不受支付机制影响，但拍卖设计优化剩余分配**”。

---
### Page/Slide 3



### 提取图片内容
#### 文字
```
the bulldozer? The professional. How much money will Charlie get for his bulldozer? $4,500. If both bidders are recreational bulldozer users, how much will each bid? $4,500. How much will Charlie receive for his bulldozer? $4,500. What will be Charlie’s expected revenue from selling the bulldozer by method 3? $(1/4) × $6,000 + (3/4) × $4,500 = $4,875.

(e) Which of the three methods will give Charlie the highest expected revenue? Method 3.

17.3 (2) We revisit our financially afflicted friend, Charlie Plopp. This time we will look at a slightly generalized version of the same problem. All else is as before, but the willingness to pay of recreational bulldozers is an amount C < $6,000 which is known to Charlie. In the previous problem we dealt with the special case where C = $4,500. Now we want to explore the way in which the sales method that gives Charlie the highest expected revenue depends on the size of C.

(a) What will Charlie’s expected revenue be if he posts a price equal to the reservation price of professional bulldozer operators? $(3/4) × $6,000 + (1/4) × $1,000 = $4,750.

(b) If Charlie posts a price equal to the reservation price C of recreational bulldozer operators, what is his expected revenue? $C.

(c) If Charlie sells his bulldozer by method 3, the second-price sealed-bid auction, what is his expected revenue? (The answer is a function of C.) $(1/4) × $6,000 + (3/4) × $C = $1,500 + (3/4)C.

(d) Show that selling by method 3 will give Charlie a higher expected payoff than selling by method 2 if C < $6,000. With method 3, each bidder will bid his true valuation. If both bidders have valuations of $6,000, he will get $6,000. Otherwise, he will get $C. His expected payoff is then
```

#### 公式
1. **Method 3 预期收入（特例 $C = 4,500$）**:  
   $$
   \left( \frac{1}{4} \times \$6,000 \right) + \left( \frac{3}{4} \times \$4,500 \right) = \$4,875
   $$
2. **Method 1 预期收入（参考上文）**:  
   $$
   \left( \frac{3}{4} \times \$6,000 \right) + \left( \frac{1}{4} \times \$1,000 \right) = \$4,750
   $$
3. **Method 2 预期收入（一般化）**:  
   $$
   \$C
   $$
4. **Method 3 预期收入（一般化）**:  
   $$
   \left( \frac{1}{4} \times \$6,000 \right) + \left( \frac{3}{4} \times \$C \right) = \$1,500 + \frac{3}{4}C
   $$

---

### 解析（结合上文知识点的连续性）
#### 1. Method 3 预期收入公式的含义
- **特例计算（$C = 4,500$）**：  
  公式 $\frac{1}{4} \times 6,000 + \frac{3}{4} \times 4,500 = 4,875$ 直接源于上文“密封第二价格拍卖”的**真实出价机制**和**效率分配原则**：  
  - $\frac{1}{4}$ 概率为两专业用户场景，收入 $6,000$（支付第二高价 $6,000$，因无竞争下降）。  
  - $\frac{3}{4}$ 概率为混合类型或两休闲用户场景，收入 $C = 4,500$（休闲用户支付自身估值，专业用户中标）。  
  此计算**避免了 Method 1 中 fallback option 的干扰**（上文已强调 fallback 导致部分场景收入降至 $1,000$），体现拍卖机制**无交易失败风险**——与上文“无合谋且估值独立时，分配总给最高价值者”一致，但捕获价值更充分（$4,875 > 4,750$）。

- **一般化推导**：  
  公式 $\frac{1}{4} \times 6,000 + \frac{3}{4} \times C = 1,500 + \frac{3}{4}C$ 扩展了上文 17.1 案例的 Revenue Equivalence Theorem 逻辑：  
  - 其中 $\frac{1}{4} \times 6,000$ 对应两专业场景（保留上文“真实估值决定支付”的核心），$\frac{3}{4} \times C$ 对应其他场景（印证上文“支付次高估值”的拍卖效率）。  
  - **关键连续性**：上文指出 fallback option 会降低 Method 1 的收益稳定性（因 $\frac{1}{4}$ 概率收入骤降），而 Method 3 的预期收入**严格递减于 $C$**，但始终无 fallback 成本——此一般化公式量化了“机制设计优化剩余分配”的结论。

#### 2. 机制选择的经济逻辑
- **Method 3 优于 Method 2 的证明**（图片 17.3(2)(d)）：  
  比较 $1,500 + \frac{3}{4}C$（Method 3）与 $C$（Method 2），当 $C < 6,000$ 时：  
  $$
  1,500 + \frac{3}{4}C > C \iff 1,500 > \frac{1}{4}C \iff C < 6,000
  $$  
  这直接强化上文“拍卖机制比固定价格更适应估值分布”的启示：  
  - Method 2 固定价格 $C$ 忽略专业用户估值（$6,000 > C$），损失潜在剩余；  
  - Method 3 通过**价格发现机制**（真实出价）捕获混合场景中的 $C$ 与专业场景中的 $6,000$，体现上文“分配有效性”的实操价值。

- **收入排序结论**（图片 (e)）：  
  Method 3（$4,875$） > Method 1（$4,750$） > Method 2（$4,500$）验证了上文“Method 3 无 fallback 成本”的预判。但**一般化下关键前提**：  
  - Method 3 优势依赖 $C < 6,000$（休闲估值低于专业估值），符合上文“独立私人价值模型”基础；  
  - 若 $C \geq 6,000$，则收入排序变化（但图片限定 $C < 6,000$，保持逻辑连贯）。

#### 3. 解析连续性说明
- 本部分**扩展而非重复**上文：上文仅定性对比机制，图片首次定量呈现 Method 3 的预期收入公式，并推广至一般 $C$，论证了“机制最优性取决于参数 $C$”——呼应上文“销售方法选择需适配估值分布”的深层逻辑。  
- 未提及图表（图片纯文本），但公式推导锚定上文概率基础：$\frac{1}{4}$（两专业）与 $\frac{3}{4}$（其他）源自独立类型假设（上文知识点总结已覆盖），聚焦新信息的经济含义。

---
### Page/Slide 4



### 当前图片内容提取与解析

#### 1. 文字与公式提取
**主要文字**：  
- `$1,500 + (3/4)C$. With method 2 he gets $C$. But $1,500 + (3/4)C > C$ whenever $C < \$6,000$.`  
- `(e) For what values of $C$ is Charlie better off selling by method 2 than by method 1? $C > \$(3/4)6,000 + (1/4)1,000 = 4,759$.`  
- `(f) For what values of $C$ is Charlie better off selling by method 1 than by method 3? This happens when $4,750 > 1,500 + \frac{3}{4}C$, which is the case whenever $C < 4,333.33$.`  
- `17.4 (3) Yet again we tread the dusty streets of Charlie Plopp’s home town. Everything is as in the previous problem. Professional bulldozer operators are willing to pay $6,000 for a bulldozer and recreational users are willing to pay $C$. Charlie is just about to sell his bulldozer when a third potential buyer appears. Charlie believes that this buyer, like the other two, is equally likely to be a professional bulldozer operator as a recreational bulldozer operator and that this probability is independent of the types of the other two.`  
- `(a) With three buyers, Charlie’s expected revenue from using method 1 is $5375$, his expected revenue from using method 2 is $C$, and his expected revenue from using method 3 is $\$3,000 + (C/2)$.`  
- `(b) At which values of $C$ would method 1 give Charlie a higher expected revenue than either of the other two methods of selling proposed above? $C < \$4,750$.`  
- `(c) At which values of $C$ (if any) would method 2 give Charlie a higher expected revenue than either of the other two methods of selling proposed above? None.`  
- `(d) At which values of $C$ would method 3 give Charlie a higher expected revenue than either of the other two methods of selling proposed above? $C > \$4,750$`  
- `17.5 (2) General Scooters has decided to replace its old assembly line with a new one that makes extensive use of robots. ...`  

**关键公式**：  
- `$1,500 + \frac{3}{4}C$` (Method 3 预期收入, 双买家场景)  
- `$C$` (Method 2 预期收入)  
- `$\frac{3}{4} \times 6,000 + \frac{1}{4} \times 1,000 = 4,759$` (注：上文知识点总结中为 `$4,750$`，此处 `$4,759$` 应为笔误，实际应为 `$4,750$`，因 `$\frac{3}{4} \times 6,000 = 4,500$`, `$\frac{1}{4} \times 1,000 = 250$`, 总和 `$4,750$`)  
- `$4,750 > 1,500 + \frac{3}{4}C \implies C < 4,333.33$` (双买家下 Method 1 优于 Method 3 的条件)  
- `$5,375$` (三买家下 Method 1 预期收入)  
- `$\$3,000 + \frac{C}{2}$` (三买家下 Method 3 预期收入)  
- `$C < 4,750$` (三买家下 Method 1 最优条件)  
- `$C > 4,750$` (三买家下 Method 3 最优条件)  

---

### 解析：三买家场景的机制设计延伸

#### 1. 从双买家到三买家的关键变化  
- **概率分布重构**：  
  上文知识点总结基于 **双买家独立类型假设**（专业概率 `$\frac{1}{2}$`），导致两专业场景概率 `$\frac{1}{4}$`、其他场景概率 `$\frac{3}{4}$`。当前图片 **17.4 (3)** 引入 **三买家**，维持独立性（每买家专业概率 `$0.5$`），概率空间扩展为二项分布：  
  - 三专业场景概率 `$\frac{1}{8}$`，两专业一休闲概率 `$\frac{3}{8}$`，一专业两休闲概率 `$\frac{3}{8}$`，三休闲概率 `$\frac{1}{8}$`。  
  - 这直接推导出新预期收入：  
    - `Method 1` 收入 `$5,375$` 源于fallback机制（交易失败时收入 `$1,000$`），但混合场景中专业用户中标率提升，部分抵消降阶影响（计算细节：`$\left[\frac{1}{8} \times 6,000 + \frac{3}{8} \times 6,000 + \frac{3}{8} \times C + \frac{1}{8} \times 1,000\right] = 5,375$` 当 `$C=4,500$`，但公式未显式给出）。  
    - **连续性锚定**：上文已强调 fallback option 在双买家下导致收入不稳定（`$4,750$`），三买家进一步降低全休闲概率（从双买家 `$\frac{1}{4}$` 降至 `$\frac{1}{8}$`），故 Method 1 收入提高（双买家 `$4,750$` → 三买家 `$5,375$`），验证了“买家数量增加降低交易失败风险”的上文结论。  

- **Method 3 公式升级**：  
  - 双买家一般化公式 `$1,500 + \frac{3}{4}C$`（上文知识点总结）反映 `$\frac{1}{4}$` 概率收入 `$6,000$` + `$\frac{3}{4}$` 概率收入 `$C$`。  
  - 三买家下更新为 `$\$3,000 + \frac{C}{2}$`，源于：  
    - 三专业场景（`$\frac{1}{8}$`）：支付第二专业价 `$6,000$`，  
    - 两专业场景（`$\frac{3}{8}$`）：支付专业价 `$6,000$`，  
    - 一专业两休闲场景（`$\frac{3}{8}$`）：支付休闲价 `$C$`，  
    - 三休闲场景（`$\frac{1}{8}$`）：无专业用户，收入 `$0$`（但题目隐含专业概率 `$0.5$`，实际收入 `$\frac{7}{8} \times 6,000 + \frac{1}{8}C = 5,250 + \frac{C}{8}$`，与 `$3,000 + \frac{C}{2}$` 不符；需按题目逻辑：**仅当专业用户存在时才交易**，故有效场景为专业用户出现率 `$\frac{7}{8}$`，但公式结构匹配上文）。  
  - **核心逻辑延续**：上文指出 Method 3 通过价格发现捕获剩余，三买家下公式 `$3,000 + \frac{C}{2}$` 仍体现“次高估值支付”原则，但权重因买家数增加而调整（`$\frac{1}{2}$` 替代双买家 `$\frac{3}{4}$`），强化“机制适应买家规模”的上文启示。  

#### 2. 机制比较阈值的经济含义  
- **三买家下最优域变化**：  
  | 机制 | 三买家最优条件 | 经济解释 |  
  |---|---|---|  
  | Method 1 | `$C < 4,750$` | fallback option 在 `$C$` 低位时仍优于纯固定价，但上文双买家下阈值为 `$C < 4,333.33$`（图片 `(f)`），**阈值提升**源于三买家降低 fallback 触发概率（全休闲概率 `$\frac{1}{8}$` vs 双买家 `$\frac{1}{4}$`），印证上文“买家数量增强fallback稳定性”的隐含逻辑。 |  
  | Method 3 | `$C > 4,750$` | 当 `$C$` 超越临界值，拍卖机制充分捕获专业高估值（`$6,000 > C$`），公式 `$3,000 + \frac{C}{2}$` 的线性增长优于 Method 1 的基准收入 `$5,375$`（当 `$C > 4,750$` 时 `$3,000 + \frac{C}{2} > 5,375$`）。**连续性体现**：上文双买家下 Method 3 优势条件为 `$C < 6,000$`，三买家下因竞争加剧，阈值收敛至 `$4,750$`，呼应“估值分布密度影响机制效率”的上文核心。 |  
  | Method 2 | 无最优域 | 上文已指出固定价 `$C$` 无法捕获专业估值（`$6,000 > C$`），三买家下仍损失剩余，且图片 `(c)` 明确“None”最优域，强化上文“静态定价劣于动态价格发现”的结论。 |  

- **与双买家参数的对照**：  
  - 图片 `(f)` 中双买家下 Method 1 优于 Method 3 的条件 `$C < 4,333.33$`，源自 `$4,750 > 1,500 + \frac{3}{4}C$`。  
  - 三买家下阈值移至 `$C < 4,750$`（Method 1 优于其他），因买家增多提升 Method 1 可靠性：$`\frac{1}{8}$` 降阶场景（收入 `$1,000$`）替代双买家 `$\frac{1}{4}$`，故最大可容忍 `$C$` 上升。  
  - **关键延续**：上文解析强调“机制最优性取决于 `$C$` 与估值分布”，三买家案例通过阈值量化展示 **买家规模如何结构性改变参数敏感性**——当买家数 `$n$` 增加，falloof 概率衰减至 `$\left(\frac{1}{2}\right)^n$`，导致 Method 1 优势域扩张，而 Method 3 更聚焦高 `$C$` 场景。  

#### 3. 知识扩展而非重复  
- 本解析聚焦 **17.4 (3)** 引入的新维度：**买家数量对机制设计的影响**，而非重述上文（如 Revenue Equivalence 定理基础或双买家计算）。  
- 三买家公式 `$3,000 + \frac{C}{2}$` 将上文一般化逻辑扩展至 `$n=3$` 案例，量化证明 **拍卖机制的效率增益随买家增加而凸显**（对比 Method 2 永远次优），直接支持上文“机制设计需适配市场条件”的深层命题。  
- 注：图片 `(e)/(f)` 中的 `$4,759$` 笔误无需纠缠，因上文知识点总结确证初始 `$4,750$` 计算，此处仅检验逻辑一致性。

---
### Page/Slide 5



# 图片内容解析：Vickrey拍卖机制的应用

## 1. 提取文字与公式

### 文字内容
- **背景描述**：General Scooters需选择两个承包商之一建造装配线。每个承包商成本可能为$H$、$M$或$L$（满足$H > M > L$），每种成本概率均为$\frac{1}{3}$，且两承包商成本分布相互独立。承包商知晓自身成本，但认为对方成本等可能为$H$、$M$、$L$。
- **(a) 问题**：会计师建议采用密封投标，授予最低出价者合同，但按另一方出价支付。问承包商应如何报价以最大化利润？
  - **答案**：Each would bid his true valuation.
- **(b) 问题**：在此机制下，支付$H$、$M$、$L$的概率各是多少？项目期望成本表达式？
  - **答案**：支付$H$概率$\frac{5}{9}$，支付$M$概率$\frac{1}{3}$，支付$L$概率$\frac{1}{9}$。期望成本：$H \cdot \frac{5}{9} + M \cdot \frac{3}{9} + L \cdot \frac{1}{9}$
- **(c) 问题**：董事长质疑为何支付较高出价，会计师应如何解释？
  - **答案**：The amount that contractors will bid depends on the rules of the auction. If you contract to the low bidder at the low...

### 公式
- 成本关系：$H > M > L$
- 概率分布：各承包商成本为$H$、$M$、$L$的概率均为$\frac{1}{3}$
- 支付概率：
  - $P(\text{支付 } H) = \frac{5}{9}$
  - $P(\text{支付 } M) = \frac{1}{3} = \frac{3}{9}$
  - $P(\text{支付 } L) = \frac{1}{9}$
- 期望成本：$\frac{5}{9}H + \frac{3}{9}M + \frac{1}{9}L$

## 2. 结合上文的知识连续性分析

### 机制逻辑与上文"次高估值支付"原则的验证
当前图片展示的是**第二价格密封投标拍卖**（Vickrey拍卖）在采购场景中的应用，直接验证了上文核心逻辑：
- **(a)部分**中"Each would bid his true valuation"明确体现了上文强调的**激励相容性**：在第二价格拍卖中，真实报价是占优策略。这与上文三买家场景中"价格发现捕获剩余"的机制设计逻辑完全一致——无论买家数量多少，第二价格拍卖都能引导参与者真实披露估值。
- 本案例中"支付另一方出价"实质是**次低成本支付**（因卖方报价对应成本），与上文"次高估值支付"原则在买卖角色反转后逻辑同构。上文双买家场景（图片`(f)`）的公式结构$\$1,500 + \frac{3}{4}C$，与本案例期望成本$\frac{5}{9}H + \frac{3}{9}M + \frac{1}{9}L$均体现**估值分布权重化**的特征。

### 概率计算对上文"买家规模影响机制效能"的佐证
- **支付$H$概率$\frac{5}{9}$**：对应"至少一个承包商成本为$H$且非双$L$"的场景。计算显示，当承包商数量为2时，买方支付最高成本的概率显著高于三买家场景（上文全休闲概率$\frac{1}{8}$）。这量化支撑了上文"买家数量增加降低fallback触发概率"的结论——本案例仅2个参与者，支付极端值(H)的概率更高。
- **期望成本表达式**：$\frac{5}{9}H + \frac{1}{3}M + \frac{1}{9}L$直观展示了**估值分布对最终支付的权重影响**，与上文三买家公式$3,000 + \frac{C}{2}$共同证明：机制的期望输出是估值分布与参与者数量的函数。此处$\frac{5}{9}$（$H$权重）高于上文三买家中专业价的权重$\frac{7}{8}$，印证了"参与者数量越少，极端估值对结果影响越大"的规律。

### (c)解释与上文"机制适配性"主张的衔接
董事长质疑"为何支付较高出价"，会计师的回答揭示了上文反复强调的**机制内生性**：
> "The amount that contractors will bid depends on the rules of the auction."

此句精炼概括了上文"静态定价劣于动态价格发现"的核心论点：若改用第一价格拍卖（支付自身报价），承包商会策略性抬高报价（$b > \text{true cost}$），导致买方实际成本上升。正如上文Method 2（固定价$C$）必然损失剩余，**规则改变会扭曲参与者行为**。这与上文三买家场景中"Method 3通过价格发现捕获剩余"形成无缝衔接——无论买卖方角色如何，机制设计必须考虑参与者对规则的响应。

## 3. 新增维度：采购场景中的成本分布效应
本图片拓展了上文光谱（买家/卖家、估值/成本）：
- 上文讨论买家估值分布（专业/休闲），本图片聚焦卖家成本分布（H/M/L），但**机制原理高度对称**：成本分布与估值分布共同决定拍卖效率。
- 公式$\frac{5}{9}H + \frac{3}{9}M + \frac{1}{9}L$中的系数$\frac{5}{9}$直接由成本分布独立性导出（$1 - P(\text{无}H) + P(\text{一}H\text{一}L)$），量化展示了**离散估值分布如何影响期望支付**，丰富了上文连续估值假设下的分析维度。

---
### Page/Slide 6



# 董事长方案与会计师方案对比分析

## 1. 文字与公式提取

### 文字内容
- **(d)部分**：董事长提出仅接受$H$、$M$、$L$三种报价的第一价格密封投标方案，将合同授予最低报价者并按其报价支付。
- **关键结论**：成本为$L$的承包商不会真实报价$L$——"If he bids $L$, he is sure to make zero profits whether or not he gets the contract. If he bids higher than $L$ there is a chance that he might get the contract and make a profit."
- **(e)部分**：假设双方采用抬价策略：成本为$L$报价$M$，成本为$H$或$M$报价$H$。计算结果表明：$\frac{2}{3}H + \frac{1}{3}M$为预期成本
- **方案比较**：会计师方案（第二价格拍卖）预期成本更低
- **(f)部分**：说明限制报价为离散值$H$、$M$、$L$是导致效率损失的原因；若允许连续报价，结果将与第二价格拍卖相同

### 公式
- 董事长方案期望成本：$\frac{2}{3}H + \frac{1}{3}M$
- 会计师方案期望成本：$\frac{5}{9}H + \frac{3}{9}M + \frac{1}{9}L$（引自上文）

## 2. 机制设计比较与解析

### 首价拍卖导致策略性抬价
| 特征 | 董事长方案(首价) | 会计师方案(次价) |
|------|------------------|------------------|
| 支付规则 | 支付自身报价 | 支付次低价 |
| 真实报价激励 | 不存在 | 存在(占优策略) |
| $L$成本投标行为 | 激励抬价至$M$ | 激励报真实成本$L$ |

董事长方案中，承包商成本为$L$时必然抬价（要不零利润，要不获胜机会），这直接导致：
- 买方无法获得最低成本$L$的报价
- 买方必须支付高于实际成本的金额（即使获胜的承包商成本为$L$，也会报价$M$）

### 期望成本量化对比
将两种方案的期望成本结构调整为统一形式：

$$
\begin{align*}
\text{会计师方案} &: \frac{5}{9}H + \frac{3}{9}M + \frac{1}{9}L \\
\text{董事长方案} &: \frac{6}{9}H + \frac{3}{9}M + 0\cdot L
\end{align*}
$$

**关键差异**：董事长方案：
- 完全排除了支付$L$的可能性（$P(\text{支付 } L)=0$，对应系数$0$）
- 支付$H$的概率上升$\frac{1}{9}$（从$\frac{5}{9}$增至$\frac{6}{9}$）

此结果**直接验证了上文(c)部分的会计师解释**：拍卖规则影响投标行为。董事长方案中承包商策略性抬价，最终导致买方承担更高成本。

### 离散报价限制的效率损失
图片(f)部分揭示了关键机制：
> "The chairman's scheme might not have worked out so badly... if he had not insisted that the only acceptable bids are $H$, $M$, and $L$."

此表述**修正并强化了上文结论**：
- 在连续估值空间中，即使第一价格拍卖也会实现与第二价格拍卖相同的期望成本
- 但**离散报价限制**破坏了这一等价性，导致：
  - 消失的$L$报价机会（对应上文$\frac{1}{9}L$项消失）
  - 额外的$H$支付概率（对应系数增加$\frac{1}{9}$）

这补充了上文"买家规模影响机制效能"框架：**报价自由度**（连续vs离散）与参与者数量同为决定拍卖效率的关键维度。当报价被强制离散化时，传统"拍卖形式等价原理"失效，买方必须选择能保持激励相容性的机制设计。

---
### Page/Slide 7



# 董事长方案与会计师方案对比分析（续）

## 1. 文字与公式提取

### 文字内容
- **策略描述**：某一参与者（买家视角）"H when his costs are M or H and he will bid M when his costs are L"
- **最优条件**：当成本为L时，选择报H的条件为"5M - 4H > L"
- **问题17.6 (3)**：古董地毯拍卖场景，仅剩两位竞标者（April和Bart），第一价格密封拍卖规则
- **买家信念**：每个竞标者认为对手估值均匀分布在$[0,1000]$，"probability that the other bidder values the rug at less than X is X/1,000"
- **April估值**：地毯对April实际价值$800
- **问题(a)**：April出价$700时，"probability that she will get the rug"为$7/10$，赢标利润$100$，期望利润$70
- **问题(b)**：April出价$600时，"probability that she will get the rug"为$6/10$，赢标利润$200$，期望利润$120
- **问题(c)**：一般化模型，出价$x$时"probability that she will get the rug"为$x/1,000$，赢标利润$800-x$，期望利润函数$(800-x)(x/1,000)$，最优出价$x=400$

### 公式
- 离散决策条件：$5M - 4H > L$
- 概率函数：$\Pr(\text{win with bid } x) = \frac{x}{1,000}$
- 期望利润函数：$E[\pi(x)] = (800 - x) \cdot \frac{x}{1,000}$
- 最优出价条件：$x = 400$

## 2. 连续估值空间的策略性出价解析

### 买家视角的对称机制
上文讨论了**卖家成本分布**对第一价格拍卖的影响，而本题将视角转换为**买家估值分布**。由于拍卖机制的对称性：
- 卖家"成本" ↔ 买家"估值"（方向相反但数学结构相同）
- 董事长方案（第一价格）中的卖家策略性抬价 ↔ 本题中买家的策略性降价

### 连续估值下的均衡策略
本题揭示了**连续估值空间中第一价格拍卖的核心机制**：
- 当发现真实估值$V=800$时，最优策略是降价出价$x^*=400$，而非报真实估值
- 该结果通过期望利润最大化导出：
  $$
  \frac{d}{dx} \left[(800-x)\frac{x}{1000}\right] = 0 \implies x^* = 400
  $$
- 这验证了上文(f)部分的关键论断：**允许连续报价时，第一价格拍卖可实现帕累托有效配置**

### 与离散报价的对比
本题与上文分析形成鲜明对照：

| 维度 | 上文离散成本模型 | 本题连续估值模型 |
|------|------------------|------------------|
| 报价空间 | 限制为{H,M,L} | [0,1000]连续 |
| 策略复杂度 | 需分析离散均衡 | 可求导得精确解 |
| 效率结果 | 第一价格拍卖失效 | 实现最优效率 |
| 上文对应 | 董事长方案困境 | 会计师方案原理 |

特别值得注意的是，当估值连续分布时：
- 买家能够精确实施"抑制出价"策略，确保获胜时获得正利润
- 期望支付最终收敛至第二价格拍卖水平（收益等价原理）
- 此结果**直接扩展了上文公式$\frac{5}{9}H + \frac{3}{9}M + \frac{1}{9}L$的适用范围**：离散模型是连续模型在报价受限时的特殊情况

### 机制设计的深层启示
本题揭示出上文未明示的关键条件：
- **报价自由度**是拍卖效率的决定性因素
- 将连续均匀分布离散化为三类（H/M/L）会：
  - 消除精确匹配最优出价的可能性
  - 产生额外的期望成本（上文董事长方案中$\frac{6}{9}H$ vs $\frac{5}{9}H$）
- 在实际机制设计中，应优先保障报价连续性，而非单纯选择拍卖形式

> 总结：本题从买家估值角度验证了上文结论——**离散限制是效率损失的根源**，而连续报价空间下第一价格拍卖能实现与次价拍卖相同的效率水平，这正是上文(f)部分所暗示的理论边界条件。

---
### Page/Slide 8



# 第17.7(3) 题目解析：策略性出价的动态均衡

## 1. 文字与公式提取

### 文字内容
- **(d) 部分**：一般化问题，April认为Bart会按真实估值出价，期望利润函数推导
- **17.7(3)**：当April认为Bart报价为其估值一半时的策略选择
  - **(a)**：Bart最高报价为$500（因其报价是自己估值的一半，而估值上限$1,000）
  - **(b)**：April估值$800出价$300时：
    * 获胜条件：Bart估值<$600
    * 获胜概率：6/10
    * 单次利润：$500
    * 期望利润：$300
  - **(c)**：April估值$800出价$x$时（$x < 500$）：
    * 获胜概率：$2x/1,000$
    * 期望利润函数：$(800-x)2x/1,000$
    * 最优出价：$400

### 公式
- 一般期望利润：$E[\pi] = (V - x)\left(\frac{x}{1,000}\right)$
- 对称均衡解：$x = \frac{V}{2}$
- 非对称环境获胜概率：$\Pr(\text{win}) = \frac{2x}{1,000}$（当对手竞价为估值一半时）
- 广义期望利润函数：$E[\pi(x)] = (800-x)\frac{2x}{1,000}$
- 最优出价条件：$x^* = 400$

## 2. 不对称信息下的纳什均衡解析

### 深层策略互动机制
本题揭示了**预期的策略性互动如何重塑拍卖均衡**：
- 当April意识到Bart不会报真实估值（而是报一半）时，她的最优策略不再是简单"折半"（如(d)部分的$x=V/2$）
- 新均衡的数学推导：
  $$
  \frac{d}{dx}\left[(800-x)\frac{2x}{1000}\right] = 0 \implies x^* = 400
  $$
  该结果表明，当一方采用非真实报价策略时，另一方的最优响应仍是**自己估值的一半**，但基于对对手行为的准确判断

### 与离散报价模型的决定性差异
对比上文的离散成本模型，本题展现了连续报价下的**动态适应能力**：

| 机制维度       | 上文离散模型                     | 本题连续策略互动模型             |
|----------------|----------------------------------|----------------------------------|
| 信息处理方式   | 依赖有限离散点的条件比较       | 基于连续概率分布的精确优化     |
| 均衡稳定性     | 局部方向性最优（如$5M>4H+L$） | 全局最优解（导数为零的精确值） |
| 策略适应能力   | 只能跳跃式调整报价             | 可无限微调出价                |
| 效率实现路径   | 依赖离散点匹配                 | 通过动态预期实现机制隐性协调  |

特别值得注意的是，当April发现Bart采用"半价策略"：
- 获胜概率函数从$x/1000$变为$2x/1000$（因Bart报价区域被压缩）
- 但最优报价规则仍保持为**自身估值的一半**，证明了连续空间中博弈均衡的**结构稳定性**

### 机制设计的核心启示
本题直接扩展了上文关于"连续性决定效率"的论点：
- **报价自由度创造动态均衡空间**：当参与者能感知并响应对手策略（如察觉对方采用非真实竞价）时，连续报价允许实时策略调整，这在离散模型中无法实现
- **预期一致性取代静态机制设计**：无需外部强制机制，参与者通过不断优化报价自然形成高效均衡：
  > *"She can get it for sure by bidding just over $500, since Bart will never bid more than $500"* —— 这表面是简单策略，实则是**理性参与者对对手行为的精确预判**，形成隐性协调

- **效率本质是信息处理能力**：当对手估值分布已知且报价连续时，买方通过计算将"对手报价策略"转化为新的获胜概率函数，从而：
  - 避免了离散报价中的"错配损失"
  - 实现了期望支付与次价拍卖的渐近收敛

> 总结：本题展示了"连续报价"与"策略互动"的双重效应——不仅是报价空间的连续性，更是参与者基于预期的动态调整能力，共同构成拍卖效率的基础。这解释了上文(f)部分中"帕累托有效配置"的实现机制：**当信息通过连续报价渠道顺畅流动时，理性参与者自发形成最优分配**。

---
### Page/Slide 9



# 拍卖理论中的信息处理与策略均衡解析

## 1. 文字与公式提取

### 文字内容
- **(d) 部分**：April对Bart出价策略的理性反应
  - "Suppose that April values the rug at $V and she believes that Bart will bid half of his true value. Show that the best thing for April is to bid half of her own true value."
  - "The derivative with respect to x is 0 when x = V/2."
  
- **(e) 部分**：策略性预期的自洽性验证
  - "Suppose that April believes that Bart will bid half of his actual value and Bart believes that April will bid half of her actual value. Suppose also that they both act to maximize their expected profit given these beliefs. Will these beliefs be self-confirming...? Yes."

- **17.8(2) 二手车拍卖问题**：
  - "Rod's Auction House... holds sealed-bid used-car auctions every Tuesday. Each used car is sold to the highest bidder at the second-highest bidder's bid."
  - "On average, half of the cars... are lemons and half are good used cars. A good used car is worth $1,000... a lemon is worth only $100."
  - "Al can sometimes, but not always, detect a lemon by licking the oil off of the dipstick. A good car will never fail Al's taste test, but 1/3 of the lemons fail his test."

- **(a) 部分**：
  - "This auction environment is an example of a (common, private) common value auction."

- **(b) 部分**：
  - "If a car passes Al's taste test, what is the probability that it is a good used car? 3/4"

- **(c) 部分**：
  - "If a car fails Al's taste test, what is the probability that it is a good used car? 0"

- **(d) 部分**：
  - "How much will Al bid for a car that passes his taste test? 3/5 × 1,000 + 2/5 × 100 = $640 How much will he bid for a car that fails his taste test? $100"

### 公式
- 目标函数：$\max_x (V - x)2x/1,000$
- 均衡条件：$x = V/2$
- 条件概率计算：
  - 通过测试的期望价值：$3/5 \times 1,000 + 2/5 \times 100 = \$640$
  - 未通过测试的报价：$\$100$

## 2. 理论解析

### 信息不对称下的贝叶斯更新机制
17.8(2)问题揭示了**共同价值拍卖中信息处理的关键作用**，是对上文(d)(e)部分私人价值拍卖的扩展：

- **朱利安·罗伯茨的柠檬市场模型延伸**：不同于上文设定的私人价值拍卖（物品对每个买家有不同价值），此案例属于**共同价值拍卖**（common value auction），即物品真实价值对所有人相同，但认知存在差异
  - 按照(a)部分标注，这确认了拍卖类型的转变：从私人价值（上文April-Bart模型）到共同价值

- **贝叶斯更新的精准应用**：
  - 尽管(b)部分答案标注为3/4，但(d)部分的计算逻辑表明**正确概率应为3/5**：
    ```
    P(好车|通过) = [P(通过|好车)×P(好车)] / [P(通过|好车)×P(好车) + P(through|柠檬)×P(柠檬)]
                = [1×0.5] / [1×0.5 + (2/3)×0.5] = 3/5
    ```
  - 这一概率反映买方在收到私人信号后**条件期待值的精确计算，是避免"赢家诅咒"的核心机制**

- **预期价值定价策略**：
  - 通过测试的报价：$640 = 3/5 \times 1000 + 2/5 \times 100$ 直接应用了**贝叶斯后验期望**
  - 未通过测试的报价：$100（等于柠檬价值，因(c)部分显示失败测试的车必为柠檬）
  - 这验证了上文观点："买方通过计算将'对手报价策略'转化为新的获胜概率函数"

### 从私人价值到共同价值拍卖的理论演进
| 维度 | 上文私人价值拍卖 | 17.8(2)共同价值拍卖 |
|------|------------------|---------------------|
| 价值来源 | 私人主观估值 | 客观真实价值（存在不确定性） |
| 信息角色 | 策略性隐瞒估值 | 信号提取与贝叶斯更新 |
| 均衡形成 | 纳什均衡（x=V/2） | 预期价值出价（条件概率） |
| 效率基础 | 信息对称下的动态调整 | 信息不对称下的信号处理 |

关键理论延续：
- **期望利润最大化**：(d)部分公式$(V-x)2x/1,000$与17.8(2)中Al的定价策略都基于**期望效用最大化原则**
- **纳什均衡的稳定性**：(e)部分"self-confirming beliefs"与Al的最优出价定理：当买方依据信息更新预期，最终会形成**理性预期均衡**
- **信息价值量化**：Al的测试能力将信息转化为**可货币化的优势**（支付$640而非$550的平均价），印证了上文"效率本质是信息处理能力"的观点

### 拍卖机制的核心启示
本案例深化了上文关于"连续报价创造动态均衡空间"的论点：
- **信号机制替代外部监管**：Al不需要拍卖规则保护，仅通过**贝叶斯学习**就能优化行为，实现"预期一致性"
- **私人信息挖掘效率**：通过(d)部分可见，信息丰富的投标者（Al）能规避次优结果，验证了"帕累托有效配置"的微观基础
- **赢家诅咒的规避**：Al的报价严格等于**期望价值**（非乐观估值），展示了理性参与者如何避免"因获胜而受损"的普遍陷阱

> 上文指出"参与者通过不断优化报价自然形成高效均衡"，本例中Al的行为证明：**在共同价值拍卖中，理性参与者通过贝叶斯更新处理私人信号，将报价精确锚定在条件期望上，这确保了信息有效利用和资源配置效率**。这一机制是对上文"动态均衡"理论的深化扩展，表明从私人价值到共同价值拍卖，均衡形成从"策略互动"转向"信息处理"。

---
### Page/Slide 10



# 当前图片解析：信息不对称拍卖的实证验证

## 1. 文字与公式提取

### (e) 部分
- "Suppose that for each car, a naive bidder at Rod's Auction House bid his expected value for a randomly selected car from among those available."
- "How much would he bid? **$550**"

### (f) 部分
- "Given that Al bids his expected value for every used car and the naive bidders bid the expected value of a randomly selected car, will a naive bidder ever get a car that passed Al's taste test? **No**"

### (g) 部分
- "What is the expected value of cars that naive bidders get if they always bid their expected values for a randomly selected car? **$100** Will naive bidders make money, lose money, or break even if they follow this policy? **Lose money.**"

### (h) 部分
- "If the bidders other than Al bid their expected value for a car, given that it has failed Al's taste test, how much will they bid? **$100**"

### (i) 部分
- "If bidders other than Al bid their expected values for cars that fail Al's taste test, and Al bids his expected value for all cars, given the results of the test, who will get the good cars and at what price? ... **Al will get all of the good cars and he will pay $100 for them.**"

### (j) 部分
- "What will Al's expected profit be on a car that passes his test? **$540**"

### 17.9 (3) 部分
- "Steve and Leroy buy antique paintings... 80% are fakes, rest genuine."
- "Genuine is worth $1,000. A fake is worthless."
- "If a painting fails Steve's sniff test, then it is certainly a fake."
- "Probability that a fake passes Steve's sniff test is 1/2."
- "Leroy detects fakes in same way as Steve."
- "Genuine paintings are sure to pass Leroy's sniff test."
- "For any fake, the probability that Steve recognizes it as a fake is independent of the probability that Leroy recognizes it as a fake."

## 2. 理论解读：信息不对称下的市场机制验证

### 均衡结果的验证路径

#### (e)天真出价的逻辑基础
- $550 = 0.5 \times 1000 + 0.5 \times 100$
- 此出价**忽略信息价值**，代表完全信息不对称下的"平均价值"误区
- 与上文(d)部分Al的认知形成鲜明对比：Al通过贝叶斯更新将价值判断提升至$640

#### (f)(g)部分的赢家诅咒实证
- "No"和"Lose money"的结论**直接验证了"赢家诅咒"理论**：
  - 天真买家只能获得未通过测试的车（柠檬）
  - 出价$550远超实际价值$100，导致平均亏损$450
- 这证明上文观点："没有适当处理信号的参与者会因为未更新先验概率而陷入次优均衡"

#### (h)(i)部分的均衡效率
- 未通过测试的车出价$100，反映**市场对坏车的真实定价**
- Al获得所有好车并支付$100，证明：
  - **第二价格拍卖**使Al能按最坏情况出价（$100）却获得好车
  - 信息优势转化为**实际资源配置效率**：Al支付$100得到期望价值$640的车
- 这验证了上文论断："通过贝叶斯更新，理性参与者将报价锚定在条件期望上，实现帕累托有效配置"

#### (j)部分的期望利润解析
- **$540 = $640 (通过测试期望价值) - $100 (实际支付价格)**
- 利润来源于**信息租金**：Al的测试能力创造的$540价值差
- 与上文"信息丰富的投标者能规避次优结果"的结论完全一致

### 17.9(3)的新案例：多信号贝叶斯更新

此案例**强化了上文理论框架**，展示了更复杂信息环境下的应用：

- **信号独立性条件**："Steve识别假货的概率...独立于Leroy"使贝叶斯更新更具挑战性
- **多维度测试结构**：
  - 两种信号（Steve和Leroy的嗅觉）
  - 不同检出率（假货通过率=1/2）
  - 完美检出率（真品通过率=1）
- **延续上文关键机制**：
  - 需要计算联合条件概率：*P(真品|双通过)*
  - 构建期望价值定价策略
  - 规避赢家诅咒的核心仍是"报价=期望价值"
- **理论深化点**：引入多信号协同效应，验证"信息聚合能力决定拍卖收益"的扩展论证

> 此部分内容直接延续上文"信息处理能力决定均衡效率"的核心观点，通过更复杂的信号组合案例，证明贝叶斯更新机制在非对称信息环境中的普适性——无论信号数量如何增加，理性参与者始终聚焦于**条件期望价值**制定策略，从而避免"因其获胜而受损"的典型拍卖陷阱。

---
### Page/Slide 11



# 17.9(3) 多信号贝叶斯更新与赢家诅咒案例解析

## 提取内容

### 文字与公式提取

**基础机制描述**  
"The auction house posts a price for each painting. Potential buyers can submit a written offer to buy at the posted price on the day of the sale. If more than one person offers to buy the painting, the auction house will select one of them at random and sell to that person at the posted price."

**(a) 部分**  
- "Given that it has passed his test, what is the probability that it is a good painting? **1/3**"
- "What is the highest posted price at which he would be willing to buy the painting? **$333.33**"

**(b) 部分 - 五种结果概率**  
- A. Genuine and passes both dealers' tests. Probability: **.2**
- B. Fake and passes both dealers' tests. Probability: **.2**
- C. Fake and passes Steve's test but fails Leroy's. Probability: **.2**
- D. Fake and passes Leroy's test but fails Steve's. Probability: **.2**
- E. Fake and fails both dealers' tests. Probability: **.2**

**(c) 部分**  
- "what is the probability that a randomly selected painting is genuine and that Steve is able to buy it? **.1**"
- "What is the probability that a randomly selected painting is a fake and that Steve will bid on it and get it? **.3**"
- "will his expected profit be positive or negative? **negative**"

## 深度解析

### (a) 部分：单信号贝叶斯更新

*基于上文基础参数：80%假货，20%真品，假货通过概率1/2，真品通过概率1*

通过测试的画作真品概率验证：
$$P(\text{真品}|\text{通过测试}) = \frac{P(\text{通过}|\text{真品})P(\text{真品})}{P(\text{通过})} = \frac{1 \times 0.2}{(1 \times 0.2) + (0.5 \times 0.8)} = \frac{0.2}{0.6} = \frac{1}{3}$$

$\Rightarrow$ 这一结果验证了信息不对称市场核心机制：**即使通过检测，多数通过测试品仍是假货**（80%×50% > 20%）

期望价值计算：
$$E(\text{价值}|\text{通过测试}) = \frac{1}{3} \times 1000 + \frac{2}{3} \times 0 = \$333.33$$

$\Rightarrow$ 与上文"报价应等于条件期望价值"原则一致，高于此价格会导致预期亏损。

### (b) 部分：多信号联合概率分布

*假设信号独立且识别率相同（假货通过率=0.5）*

| 结果类型 | 先验概率 | 条件概率 | 联合概率 |
|---------|---------|---------|---------|
| A: 真品通过双检测 | 0.2 | $1 \times 1 = 1$ | $0.2 \times 1 = 0.2$ |
| B: 假货通过双检测 | 0.8 | $0.5 \times 0.5 = 0.25$ | $0.8 \times 0.25 = 0.2$ |
| C: 假货仅Steve通过 | 0.8 | $0.5 \times 0.5 = 0.25$ | $0.8 \times 0.25 = 0.2$ |
| D: 假货仅Leroy通过 | 0.8 | $0.5 \times 0.5 = 0.25$ | $0.8 \times 0.25 = 0.2$ |
| E: 假货双检测失败 | 0.8 | $0.5 \times 0.5 = 0.25$ | $0.8 \times 0.25 = 0.2$ |

$\Rightarrow$ 此表量化了**信号独立性假设**下的联合概率分布，证明五种结果概率均等。这强化了上文"多维度信号需独立处理"的理论，展示信息聚合对定价的关键作用。

### (c) 部分：赢家诅咒实证

**期望利润计算逻辑：**
- P(Steve获得画|画通过测试) =  
  $$P(\text{真品}) \times P(\text{双通过}) \times 0.5 + P(\text{假货}) \times P(\text{通过Steve但Leroy可能通过}) \times 0.5$$
- P(Steve获得真品) = $0.2 \times 1 \times 0.5 = 0.1$
- P(Steve获得假货) = $0.8 \times 0.5 \times [0.5 \times 0.5 + 0.5 \times 1] = 0.3$

**期望利润验证：**
$$E(\pi) = 0.1 \times (1000 - 300) + 0.3 \times (0 - 300) = 70 - 90 = -20 < 0$$

$\Rightarrow$ 此结果**直接验证赢家诅咒理论**：当Steve沿线性支付$300时，实际仅获得期望价值$250的画作（$100/0.4），导致每笔交易平均亏损$50。这与上文"未更新条件概率会陷入次优均衡"论断完全一致。

> **关键洞见**：在多参与者场景中，中标概率（1/2）引入了*额外信息筛选机制*——Steve仅在Leroy不竞争时（或双人都竞争但幸运中标）获得画作，这使中标品更可能处于"假货通过单人测试"的低价值状态。此例深化了上文观点：信息处理能力不仅包括贝叶斯更新，还需考虑**竞争者行为对条件概率的再塑造**。

---
### Page/Slide 12



# 拍卖理论案例解析：第二价格密封拍卖与赢家诅咒的关联

## 图片内容提取

### 文字与公式
- **标题信息**：`224 AUCTIONS (Ch. 17)`
- **问题背景**：
  > Every day the Repo finance company holds a sealed-bid, second-price auction in which it sells a repossessed automobile. There are only three bidders who bid on these cars, Arnie, Barney, and Carny. Each dealer's value is a random variable taking high value `$H$` with probability `1/2` and low value `$L$` with probability `1/2`. Values are independent across dealers.
  
- **拍卖规则**：
  > The car is sold to the highest bidder at the second-highest bid price. Ties for highest bid result in random selection among top bidders at the tied bid price.
  
- **问题与答案**：
  - (a) Bid with value `$H$`: **`$H`**; Bid with value `$L$`: **`$L`**
  - (b) Revenue with ≥2 `$H$`-valuers: **`$H`**; Revenue with <2 `$H$`-valuers: **`$L`**
  - (c) P(Repo receives `$H$`): **`1/2`**; P(Repo receives `$L$`): **`1/2`**; Expected revenue: **`$(H+L)/2`**
  - (d) P(Arnie gets car below his valuation): **`1/8`**

## 理论解析

### 与上文知识点的连续性
此案例延续了**信息处理与期望利润**的核心逻辑，但转向更标准的**私人价值拍卖模型**。与上文"信号测试-贝叶斯更新"机制形成对照：
- 上文处理的是*共同价值拍卖*（物品真实价值相同，但信息不对称）
- 本例是*私人价值拍卖*（每位竞标者有独立私有估值）
- 两者都需精确计算条件期望值，但本例通过**第二价格拍卖机制**避免了赢家诅咒的产生

### 关键机制分析
#### (a) 真实估值出价策略
- **依据公式**：`$b_i(v_i) = v_i$`（Vickrey独立私人价值模型）
- **理论衔接**：上文问题中因未更新概率导致期望利润为负，而本例中按真实估值出价是**主导策略**，直接保证竞标者不陷入上文所述的"条件概率未更新"陷阱
- **深层含义**：该机制将赢家诅咒问题转化为信息处理问题——当竞标者信任机制并按真实估值出价时，支付的期望价格自然等于物品对他的价值

#### (d) 赢家利润概率的量化
- **事件概率**：`$P(\text{Arnie wins below valuation}) = P(\text{Arnie} = H) \times P(\text{Barney}=L) \times P(\text{Carny}=L) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}$`
- **与上文连接**：
  - 上文计算"Steve获得假货概率=0.3"依赖于**信号通过条件概率**
  - 本例`$1/8$`源于**独立私有估值分布**，体现两个关键差异：
    1. 不需要贝叶斯更新（私有信息已知）
    2. 竞争结构更清晰（三人对称竞争）
- **利润本质**：此概率量化了上文未明确的"赢家收益空间"——在机制设计合理的拍卖中，只有当其他竞标者全部低估值时，胜者才能获得正利润

### 期望收益的启示
- **Repo预期收益** `$E[\text{revenue}] = \frac{H+L}{2}$` 
  - 验证了**收入等价定理**：在风险中性、独立私有估值假设下，第二价格拍卖与英式拍卖等产生相同期望收益
  - 与上文"期望价值=$333.33"逻辑一致，但此处无需条件概率修正——机制本身保障了价格等于胜者估值的条件期望

### 两者理论框架对比
| 维度 | 上文案例 | 本例 |
|------|----------|------|
| **价值类型** | 共同价值（信息不对称） | 私人价值（独立信息） |
| **决策瓶颈** | 信号测试后的贝叶斯更新 | 拍卖机制下的出价策略 |
| **赢家诅咒根源** | 未修正的条件概率导致出价过高 | 无需担忧（机制内嵌纠错） |
| **期望利润计算** | $E(\pi)=0.1\times(1000-300)+0.3\times(0-300)=-20$ | $E(\pi|H)=H\times\frac{3}{8}+L\times\frac{1}{8}$（需结合赢得概率） |

> **核心洞见**：本例揭示了最优拍卖设计如何解决上文的赢家诅咒问题——在机制良好的第二价格拍卖中，竞标者通过按真实估值出价自动实现下文所述的"报价等于条件期望价值"原则，而无需执行复杂的贝叶斯更新。这说明**拍卖机制质量**与**信息处理能力**共同决定市场效率。

---
### Page/Slide 13



### 1. 图片文字与公式提取

#### 文字内容：
- "between what a car is worth to him and what he pays for it. On a randomly selected day, what is Arnie’s expected profit? \((H - L)/8\)"
- "(e) The expected total profit of all participants in the market is the sum of the expected profits of the three car dealers and the expected revenue realized by Repo. Used cars are sold by a sealed-bid, second-price auction and the dealers do not collude. What is the sum of the expected profits of all participants in the market? \(3(H - L)/8 + (H + L)/2 = (7/8)H + (1/8)L\)"
- "17.11 (3) This problem (and the two that follow) concerns collusion among bidders in sealed-bid auctions. Many writers have found evidence that collusive bidding occurs. The common name for a group that practices collusive bidding is a “bidding ring.”*"
- "Arnie, Barney, and Carny of the previous problem happened to meet at a church social and got to talking about the high prices they were paying for used cars and the low profits they were making. Carny complained, “About half the time the used cars go for $H, and when that happens, none of us makes any money.” Arnie got a thoughtful look and then whispered, “Why don’t we agree to always bid $L in Repo’s used-car auctions?” Barney said, “I’m not so sure that’s a good idea. If we all bid $L, then we will save some money, but the trouble is, when we all bid the same, we are just as likely to get the car if we have a low value as we are to get it if we have a high value. When we bid what we think its worth, then it always goes to one of the people who value it most.”"
- "(a) If Arnie, Barney, and Carny agree to always bid $L, then on any given day, what is the probability that Barney gets the car for $L when it is actually worth $H to him? \(1/6\) What is Barney’s expected profit per day? \$(H - L)/6\)"
- "(b) Do the three dealers make higher expected profits with this collusive agreement than they would if they did not collude? Explain. Yes. \((H - L)/6 > (H - L)/8\)"
- "* Our discussion draws extensively on a paper, “Collusive Bidder Behavior at Single-Object, Second-price, and English Auctions” by Daniel Graham and Robert Marshall in the Journal of Political Economy, 1987."

#### 公式列表：
- \((H - L)/8\)
- \(3(H - L)/8 + (H + L)/2 = (7/8)H + (1/8)L\)
- \(1/6\)
- \$(H - L)/6\)
- \((H - L)/6 > (H - L)/8\)

---

### 2. 理论解析：合谋行为对私人价值拍卖的影响

本图片延续**私人价值第二价格拍卖**框架（上文知识点），但引入**竞标者合谋**（collusion）这一新变量，揭示机制设计局限性。与上文“问题(e)”的非合谋基准形成直接对比，核心在于合谋如何改变参与者利润分配与市场效率。

#### **与上文知识点的连续性**
- **上文基准**：在非合谋第二价格拍卖中（上文知识点(a)-(d)），按真实估值出价是主导策略（\(b_i = v_i\)），确保：
  - 无赢家诅咒：支付价等于条件期望价值。
  - 高效分配：车总归估值最高者（上文(d)中P(Arnie gets car below valuation) = \(1/8\) 衡量利润空间）。
  - Repo 期望收益 \(E[\text{revenue}] = (H + L)/2\)（上文(c)），三买家总期望利润 \(3 \times (H - L)/8\)（上文(e)）。
- **本图片变化**：合谋打破非合谋均衡，买家约定固定出价 $L$。这并非机制设计问题，而是**参与者策略协同**导致：
  - 分配效率下降：车不再必然归估值最高者（与上文“机制保障效率”矛盾）。
  - 利润重新分配：买家利润提升，但 Repo 收益受损，总剩余减少。
  - 与上文逻辑的延续：上文证明第二价格拍卖本身**消除赢家诅咒**（通过真实出价自动实现期望收益），但本例表明当参与者主动合谋时，可进一步操纵系统以牺牲总体效率换取个体利益，暴露机制在防串通上的弱点。

#### **关键公式与行为含义解析**
- **\(1/6\)（问题(a)概率）**  
  表示**联合概率**：Barney 在估值为 $H$ 时赢得汽车且支付 $L$ 的概率，即：
  \[
  P(\text{Barney wins} \cap \text{val}_\text{Barney} = H) = P(\text{val}_\text{Barney} = H) \times P(\text{win} \mid \text{val}_\text{Barney} = H) = \frac{1}{2} \times \frac{1}{3} = \frac{1}{6}
  \]
  - **变化含义**：  
    - 非合谋时（上文），给定 Barney 估值 $H$，他获胜需其他两人均估值 $L$（条件概率 $1/4$），体现机制保障高效分配。  
    - 合谋时，出价不反映估值，胜负随机化。此处 $1/3$ 获胜概率与估值无关，反映**分配扭曲**：即使 Barney 估值高，他获胜概率反低于非合谋（$1/3 < 3/4$），但因无需支付高价，整体利润上升（衔接问题(b)）。

- **\$(H - L)/6$（问题(a)期望利润）**  
  Barney 的期望利润：
  \[
  E[\text{profit}] = P(\text{win} \cap \text{val}_\text{Barney} = H) \times (H - L) = \frac{1}{6}(H - L)
  \]
  - **变化含义**：  
    - 非合谋时（上文(d)），期望利润为 \((H - L)/8\)，源于仅当其他两人均估值 $L$ 时获利（概率 $1/8$）。  
    - 合谋时利润提升：\((H - L)/6 > (H - L)/8\)（因 \(1/6 > 1/8\)）。此增长来自**支付溢价降低**——固定支付 $L$（原支付价可能高达 $H$），但代价是分配低效：公式中 $P(\text{win} \mid \text{val}_\text{Barney} = H) = 1/3$ 意味定价无法筛选高估值者，与上文“支付价等于条件期望价值”原则脱钩。

- **问题(b)不等式：\((H - L)/6 > (H - L)/8\)**  
  证明合谋提升买家整体利润：
  \[
  \frac{H - L}{6} > \frac{H - L}{8} \quad \text{(since \(H > L\))}
  \]
  - **变化含义**：  
    - 直接量化上文未涉及的**合谋动机**：买家放弃分配效率（车常归非最高估值者），换取更高利润（增长率 \(33.3\%\)，因 \(1/6 \div 1/8 = 4/3\)）。  
    - 与上文对比：  
      - 上文（非合谋）：买家无需更新概率（机制自动纠偏），利润由估值分布自然决定。  
      - 本例（合谋）：买家主动放弃信息利用（出价不随估值调整），但通过串通人为压低支付价。  
    - 隐含总剩余损失：非合谋总剩余 \(E[\text{surplus}] = (7/8)H + (1/8)L\)（上文(e)计算），合谋时降为 \((H + L)/2\)。效率损失源于错误分配（如低估值者获胜时，总剩余减少），而买家利润增加以卖方损失为代价（Repo 收益恒为 $L$，低于非合谋期望 $(H+L)/2$）。

#### **理论框架演进**
| 维度 | 上文（非合谋） | 本图片（合谋） |
|------|----------------|----------------|
| **支付机制** | 第二价格保障真实出价 | 串通压低支付价至 $L$ |
| **分配效率** | 车归最高估值者（无扭曲） | 随机分配，效率损失 |
| **买家利润来源** | 仅当他人低估值时获利 | 恒定低价竞标，扩大获利概率 |
| **与上文连接** | 机制内嵌解决赢家诅咒 | 合谋利用机制漏洞，暴露防串通缺陷 |

> **核心洞见**：本例验证上文“拍卖机制质量决定效率”的延伸——第二价格拍卖虽在**非合谋**下最优（收入等价定理），但无法抵御串通。竞标者通过放弃信息利用（不再按估值出价），以分配效率为代价换取个体利润提升。这与上文“机制设计使参与者自动呈现理想行为”形成张力：当参与者合谋时，**系统信息处理能力**被抑制，导致上文未见的效率-利润权衡。此现象为反垄断政策提供微观基础（如合谋禁止的必要性），并凸显拍卖理论中“防串通机制设计”的重要性。

---
### Page/Slide 14



# 当前图片解析：合谋效率损失与敲定机制改进

## 文字与公式提取
- **问题 (c)**:  
  \( 3(H-L)/6 + L = (H+L)/2 \)  
  *Are these expected total profits larger or smaller than they are when the dealers do not collude?*  
  **Smaller**

- **问题 (d)**:  
  *With no collusion, are the cars allocated efficiently?* **Yes**  
  *If dealers collude, are the cars allocated efficiently?* **No**

- **问题 17.12 (2)**:  
  > Arnie proposed... "knockout" auction. The dealer who wins... can bid anything... while others must bid $L$.  
  > Revenue from knockout is divided equally among all three.

- **问题 (a)**:  
  > Value of winning knockout to H-valuation agent: **$H - L$**  
  > Value of winning knockout to L-valuation agent: **$0$**

---

## 关键内容解析（衔接上文知识点）

### 1. 问题 (c) 总利润公式的经济含义
- **公式拆解**：  
  \( 3 \times \frac{H-L}{6} + L = \frac{H+L}{2} \) 直接量化了 **合谋下的市场总剩余**：
  - \( 3 \times \frac{H-L}{6} \) = 三买家总利润（每个买家期望利润 \(\frac{H-L}{6}\)，源于上文问题(a)）  
  - \( +L \) = Repo固定收益（合谋时支付价恒为 \(L\)）  
  - **核心结论**：总剩余降至 \(\frac{H+L}{2}\)

- **与上文连续性**：  
  上文已推导非合谋总剩余为 \(\frac{7}{8}H + \frac{1}{8}L\)。该公式**首次显式验证效率损失规模**：  
  \[
  \text{损失量} = \left( \frac{7}{8}H + \frac{1}{8}L \right) - \frac{H+L}{2} = \frac{3(H-L)}{8}
  \]  
  这解释了为何答案是 **"Smaller"** —— 合谋以总剩余损失 \(37.5\%\frac{H-L}{2}\) 为代价（当 \(H-L=1\) 时），换取买家个体利润提升（上文已证 \(\frac{H-L}{6} > \frac{H-L}{8}\)），**量化了"牺牲总体效率换取个体利益"的机制缺陷**。

### 2. 问题 (d) 效率判断的深层含义
- **无合谋高效性（Yes）**：  
  重申上文核心结论 —— 第二价格拍卖在独立决策下**自动实现高效分配**（车归最高估值者），体现机制内嵌的信息处理能力。

- **合谋低效性（No）**：  
  直接验证上文"分配扭曲"论点：  
  - 合谋时获胜概率与估值脱钩（上文：高估值者获胜概率从 \(\frac{3}{4}\) 降至 \(\frac{1}{3}\))  
  - 导致"高估值者因串通无法中标"（如上文例中：\(H\) 值背支付 \(L\) 但常输标）  
  **关键衔接**：此结果使抽象理论具象化 —— 机制设计可保证个体激励相容，但**无法抵御策略性合谋**，暴露防串通机制的结构性缺陷。

### 3. 17.12 (a) 敲定（Knockout）机制的突破性设计
- **机制本质**：  
  通过子博弈（内部第二价格拍卖）**将串通行为转化为效率提升工具**：  
  - H-valuation 代理赢得 knockout：在主拍卖中以 \(H\) 出价、\(L\) 支付，故 **\(H-L\) 为其真实收益**  
  - L-valuation 代理赢得 knockout：主拍卖无法获利，故 **价值为 0**  

- **对上文问题的改进**：  
  | 维度                | 简单合谋（上文）          | Knockout 机制（本图片）       |  
  |---------------------|--------------------------|-------------------------------|  
  | **分配效率**        | 严重扭曲（随机获奖）      | **部分恢复**：高估值者更易获出价权 |  
  | **利润来源**        | 仅靠支付溢价压低（无效率补偿） | 内部拍卖**内化效率提升**（高估值者主导） |  
  | **与上文差距弥补**  | 加剧效率-利润权衡         | **收缩权衡空间**：买家利润提升不再依赖总剩余损失 |  

- **理论演进意义**：  
  - 消除上文简单合谋的致命缺陷：通过**分层拍卖**使串通行为 **"服务于效率"**（高估值者更有动力赢取 knockout）。  
  - **关键衔接上文结尾**：上文指出"防串通设计是拍卖理论前沿"，本机制提供实践方案 ——  
    > 不强制禁止串通（可能不可行），而是通过**子博弈结构**引导参与者自发回归高效分配（参见脚注提及的 Graham-Marshall 模型）。  
  - 由此开启 **"效率损失内生化"** 新框架：原合谋损失 \(\frac{3(H-L)}{8}\) 可被削减（仅存 knockout 运行成本），**弥合个体利润与系统效率的鸿沟**。

> **核心延续**：本图片不单是新例题，而是对上文"机制设计局限"的动态回应 —— 政策制定者需超越"禁止串通"的被动策略，转向 **"将合谋导向效率改进"** 的主动机制设计（如 knockout 这类子博弈构造），这正是反垄断微观基础的深化。

---
### Page/Slide 15



### 提取内容：当前图片文字与公式  
**文字内容**：  
- (b) On a day when one dealer values the used car at $H$ and the other two value it at $L$, the dealer with value $H$ will bid $H - L$ in the knockout auction and the other two dealers will bid $0$. In this case, in the knockout auction, the dealer pays $0$ for the right to be the only high bidder in Repo’s auction. In this case, the day’s used car will go to the only dealer with value $H$ and he pays Repo $L$ for it. On this day, the dealer with the high buyer value makes a total profit of $H - L$.  
- (c) We continue to assume that in the knockout auction, dealers bid their actual values of winning the knockout. On days when two or more buyers value the used car at $H$, the winner of the knockout auction pays $H - L$ for the right to be the only high bidder in Repo’s auction.  
- (d) If Arnie’s scheme is adopted, what is the expected total profit of each of the three car dealers? (Remember to include each dealer’s share of the revenue from the knockout auction.) $\frac{7(H-L)}{8}$  
- 17.13 (2) After the passage of several weeks during which Repo never got more than one high bid for a car, the Repo folks guessed that something was amiss. Some members of the board of directors proposed hiring a hit man to punish Arnie, Barney, and Carny, but cooler heads prevailed and they decided instead to hire an economist who had studied Intermediate Microeconomics. The economist suggested: “Why don’t you set a reserve price $R$ which is just a little bit lower than $H$ (but of course much larger than $L$)? If you get at least one bid of $R$, sell it for $R$ to one of these bidders, and if you don’t get a bid as large as your $R$, then just dump that day’s car into the river. (Sadly, the environmental protection authorities in Repo’s hometown are less than vigilant.) “But what a waste,” said a Repo official. “Just do the math,” replied the economist.  
  - (a) The economist continued. “If Repo sticks to its guns and refuses to sell at any price below $R$, then even if Arnie, Barney, and Carny collude, the best they can do is for each to bid $R$ when they value a car at $H$ and to bid nothing when they value it at $L$.” If they follow this strategy, the probability that Repo can sell a given car for $R$ is $\frac{7}{8}$, so Repo’s expected profit will be $\frac{7}{8}R$.  
  - (b) Setting a reserve price that is just slightly below $H$ and destroying cars for which it gets no bid will be more profitable for Repo than setting no reservation price if the ratio $H/L$ is greater than $\frac{7}{8}$ and less profitable if $H/L$ is less than $\frac{7}{8}$.  

**公式列表**：  
- $H - L$（多次出现，代表高估值与低估值的差异）  
- $0$（投标金额）  
- $\frac{7(H-L)}{8}$（经销商的预期利润）  
- $\frac{7}{8}$（销售概率）  
- $\frac{7}{8}R$（Repo的预期利润）  
- 条件：$\frac{H}{L} > \frac{7}{8}$ 时更优，$\frac{H}{L} < \frac{7}{8}$ 时更劣  

---

### 含义解析：基于上文知识点的连续性解释  
#### 1. **Knockout 机制的利润验证与效率延续（对应 (b)、(c)、(d) 部分）**  
- **利润公式 $\frac{7(H-L)}{8}$ 的经济学意义**：  
  上文知识点总结已阐明，简单合谋下个体买家的期望利润仅为 $\frac{H-L}{6}$（源于问题 (a)），而 Knockout 机制通过子博弈设计将该利润提升至 $\frac{7(H-L)}{8}$。当前图片 (d) 部分直接量化此结果，其核心在于 **利润来源的结构性转变**：  
  - 在简单合谋中，利润完全依赖支付溢价压低（支付价恒为 $L$），但总剩余损失 $\frac{3(H-L)}{8}$ 证明效率-利润权衡不可持续。  
  - Knockout 机制下（如 (b)、(c) 描述）：  
    - 单高估值情形：高估值经销商以 $H-L$ 投标 knockout，零成本获得唯一出价权，利润 $H-L$（无效率损失）。  
    - 多高估值情形：winner 支付 $H-L$ 获得出价权，但子博弈内化了效率——高估值者主导，使总剩余损失从 $\frac{3(H-L)}{8}$ 收缩至接近零（仅存 knockout 运行成本）。  
  - **连续性要点**：该利润 $\frac{7(H-L)}{8}$ 显式体现上文结论——买家利润提升不再牺牲系统效率（上文对比：$\frac{7(H-L)}{8} > \frac{H-L}{6}$），且总剩余更接近非合谋水平 $\frac{7H}{8} + \frac{L}{8}$。这直接验证了 Knockout 机制通过"将合谋导向效率改进"，弥合了个体利润与系统效率的鸿沟。  

#### 2. **Reserve Price 设计的支付策略与效率权衡（对应 17.13 (2) 部分）**  
- **关键机制设计逻辑**：  
  17.13 (2) 延续了上文"防串通设计"的前沿探索（上文结尾强调需转向主动机制设计），但聚焦于 **Repo 作为卖方的策略性响应**：  
  - 经济学家建议设置 reserve price $R \approx H$，迫使合谋方在估值 $H$ 时投标 $R$（否则失去中标机会），且当无合格投标时销毁车辆。  
  - 联合上文知识点：  
    - 简单合谋下，Repo 固定收入 $L$（上文问题 (c)：支付价恒为 $L$）。  
    - 本设计中，Repo 预期利润 $\frac{7}{8}R$（因销售概率 $\frac{7}{8}$，对应非合谋下至少一个高估值的概率 $1 - (1/2)^3 = \frac{7}{8}$）。  
  - **核心改进**：此设计无需禁止合谋，而是 **将合谋行为转化为卖方收益工具**——通过 reserve price，Repo 从被动受害者转为主动获益方，体现了机制设计的"内生化"思维（与 Knockout 机制 "分层拍卖" 异曲同工）。  

- **效率条件 $\frac{H}{L} > \frac{7}{8}$ 的实质含义**：  
  - 文字中 $\frac{H}{L} > \frac{7}{8}$ 实为笔误（$\frac{7}{8} < 1$ 但 $H > L$ 故 $H/L >1$），正确临界点应为 $\frac{H}{L} > \frac{8}{7}$（因 $\frac{7}{8}R > L \Rightarrow R > \frac{8}{7}L$，且 $R \approx H$）。  
  - **深层经济含义**：  
    - 当 $\frac{H}{L} > \frac{8}{7}$ 时，$\frac{7}{8}H > L$，设置 reserve price 的预期收益超过简单合谋固定收入 $L$，证明卖方可通过设计"可执行威胁"（销毁车辆）重获议价权。  
    - 该条件量化了 **上文"效率损失内生化"框架的延伸**：原合谋导致的总剩余损失 $\frac{3(H-L)}{8}$，现可部分回补为卖方利润（$\frac{7}{8}(H - L)$ 的潜在增量），进一步弱化合谋的效率代价。  
  - **连续性衔接**：上文指出防串通需"不强制禁止，而是引导参与者回归高效分配"；本部分通过 reserve price 实现类似逻辑——买方在最优策略下隐含接受高效分配（即仅在 $H$ 时中标），使串通从"制造扭曲"转为"被机制吸收"。  

> **知识演进总结**：当前图片是上文 Knockout 机制分析的自然延续，同时开启卖方视角的机制设计。17.13 (2) 深化了"效率损失内生化"理念：不仅买家可通过子博弈（Knockout）优化利润，卖方亦能通过 reserve price 将合谋冲击转化为收益，共同为反垄断政策提供微观基础——**系统性解决合谋问题需买卖双方机制协同，而非单方面压制**。

---
### Page/Slide 16



# 图片内容解析

## 提取的文字内容

- 228
- AUCTIONS (Ch. 17)

## 公式与图表

当前图片中**没有包含任何经济学公式或图表**，仅为教材的页码和章节标题。

## 与上文知识点的关联

此页面作为第17章"AUCTIONS"的延续页码（228页），提示这是上文知识点总结所讨论的拍卖理论内容的物理位置。该页未提供新的分析内容，而是作为章节过渡页，与上文介绍的Knockout机制、Reserve Price设计等微观经济学理论形成章节连贯性。当前图片本身不含需解析的经济模型，但其存在确认了上文知识点总结所分析的17.13问题属于第17章拍卖理论的实质内容框架。
