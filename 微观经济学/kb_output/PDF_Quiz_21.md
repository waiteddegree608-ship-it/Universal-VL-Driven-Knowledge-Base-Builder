# PDF_Quiz_21

### Page/Slide 1



### 图片内容提取与解析

#### 1. 文字与公式提取  
**标题与标识**  
- Quiz 21  
- NAME__________________  
- Cost Curves  

**问题 21.1**  
- 文本内容：  
  "In Problem 21.2, if Mr. Dent Carr’s total costs are $4s^2 + 75s + 60$, then if he repairs 15 cars, his average variable costs will be"  
- 选项：  
  (a) 135.  
  (b) 139.  
  (c) 195.  
  (d) 270.  
  (e) 97.50.  
- **公式**：  
  $TC = 4s^2 + 75s + 60$（*总成本函数，其中 $s$ 为修车数量*）  

**问题 21.2**  
- 文本内容：  
  "In Problem 21.3, Rex Carr could pay \$10 for a shovel that lasts one year and pay \$5 a car to his brother Scoop to bury the cars, or he could buy a low-quality car smasher that costs \$200 a year to own and that smashes cars at a marginal cost of \$1 per car. If it is also possible for Rex to buy a high-quality hydraulic car smasher that cost \$300 per year to own and if with this smasher he could dispose of cars at a cost of \$0.80 per car, it would be worthwhile for him to buy this high-quality smasher if"  
- 选项：  
  (a) he plans to dispose of at least 500 cars per year.  
  (b) he plans to dispose of no more than 250 cars per year.  
  (c) he plans to dispose of at least 510 cars per year.  
  (d) he plans to dispose of no more than 500 cars per year.  
  (e) he plans to dispose of at least 250 cars per year.  

**问题 21.3**  
- 文本内容：  
  "Mary Magnolia in Problem 21.4 has variable costs equal to $y^2 / F$ where $y$ is the number of bouquets she sells per month and where $F$ is the number of square feet of space in her shop. If Mary has signed a lease for a shop with 1,600 square feet and if she is not able to get out of the lease or to expand her store in the short run, and if the price of a bouquet is \$3 per unit, how many bouquets per month should she sell in the short run?"  
- 选项：  
  (a) 1,600  
- **公式**：  
  $VC = \frac{y^2}{F}$（*可变成本函数，其中 $y$ 为月销量，$F$ 为店铺面积*）  

---

#### 2. 无图表，仅基于问题内容补充关键经济逻辑  
当前图片不含图表，但问题嵌套前序问题（如 "Problem 21.2"、"Problem 21.3"），需基于**成本曲线核心逻辑**补充分析：  
- **问题 21.1 关键解析**：  
  - 总成本 $TC = 4s^2 + 75s + 60$ 中，固定成本 $FC = 60$（常数项），可变成本 $VC = 4s^2 + 75s$。  
  - 平均可变成本 $AVC = \frac{VC}{s} = 4s + 75$。  
  - 代入 $s = 15$：$AVC = 4 \times 15 + 75 = 135$，答案为 **(a)**。  
  - *注：选项 (e) 97.50 为 $ATC$ 混淆（$ATC = \frac{TC}{s}$ 含固定成本），此处需严格区分 AVC 仅含可变部分。*  

- **问题 21.2 关键解析**：  
  - 目标：比较高质粉碎机与低质粉碎机的总成本，求高质更优的临界产量。  
    - 低质粉碎机总成本：$TC_{\text{low}} = 200 + 1 \cdot q$（$q$ 为处置车数）  
    - 高质粉碎机总成本：$TC_{\text{high}} = 300 + 0.8 \cdot q$  
  - 令 $TC_{\text{high}} < TC_{\text{low}}$：  
    $$
    300 + 0.8q < 200 + q \implies 100 < 0.2q \implies q > 500
    $$  
  - $q = 500$ 时成本相等（$TC_{\text{low}} = TC_{\text{high}} = 700$），经济含义为 **"至少处置 500 辆车"** 时高质更优（含相等边界，因 $q > 500$ 严格成立），答案为 **(a)**。  
  - *注：选项 (c) 510 无依据，临界点严格为 500；其他选项数量级偏差源于未解方程。*  

- **问题 21.3 关键解析**：  
  - 短期 $F = 1600$ 固定，因此 $VC = \frac{y^2}{1600}$。  
  - 边际成本 $MC = \frac{d(VC)}{dy} = \frac{2y}{F} = \frac{y}{800}$。  
  - 利润最大化条件：$MC = P$（$P = 3$），解得 $y = 2400$。  
  - *注：图片仅显示选项 (a)，但 2400 未列出；实际应计算至 $MC=P$，而非误用 $F$ 值（如误选 $y=F=1600$ 会导致 $MC=2 < P$，非最优）*。  
  - 实际问题隐含前提：若履约约定，但利润最大化仍由边际原则主导。  

---

#### 3. 知识连续性说明  
- 上文知识点总结缺失，故结合成本曲线核心框架分析：  
  - **21.1 验证 $AVC$ 与 $TC$ 分解**：强化固定成本（FC）与可变成本（VC）的分离逻辑。  
  - **21.2 体现规模经济**：设备选择取决于产量对总成本的影响，凸显长期决策中固定成本分摊效应。  
  - **21.3 明确短期约束**：产能（$F$）固定时，产量决策依据 $MC=P$，与固定成本无关（呼应成本曲线中 $FC$ 不影响短期供给决策）。  
- 问题序列隐含**微观成本理论递进**：从成本函数定义 → 产能选择优化 → 短期利润最大化，形成完整逻辑链。

---
### Page/Slide 2



### 1. 文字与公式提取  
#### 问题 21.4  
- **生产函数**：$ Q = 0.1 J^{1/2} L^{3/4} $  
  - $ J $：旧笑话数量（固定为 900，单价 \$6）  
  - $ L $：漫画家工时（单价 \$5）  
- **目标**：计算生产 $ Q = 24 $ 本漫画书的总成本  
- **选项**：  
  (a) 5,480 (b) 2,740 (c) 8,220 (d) 5,504 (e) 1,370  

#### 问题 21.5  
- **生产函数**：$ Q = 0.1 J^{1/2} L^{3/4} $  
- **给定价格**：  
  - 旧笑话成本 \$2/单位（$ w_J = 2 $）  
  - 漫画家工资 \$18/小时（$ w_L = 18 $）  
- **目标**：成本最小化时最优投入比例 $ J/L $  
- **选项**：  
  (a) 9 (b) 12 (c) 3 (d) $ 2/3 $ (e) 6  

---

### 2. 问题解析  
#### **问题 21.4：短期固定投入下的总成本计算**  
- **关键逻辑**：  
  由于 $ J = 900 $ 是短期固定投入（类似上文 **21.3 中 $ F = 1600 $** 的约束），需通过生产函数解出所需的可变投入 $ L $，再计算总成本。  
  1. **代入生产函数**：  
     $$
     24 = 0.1 \cdot (900)^{1/2} \cdot L^{3/4} \implies 24 = 0.1 \cdot 30 \cdot L^{3/4} \implies L^{3/4} = 8
     $$  
     解得 $ L = 8^{4/3} = 16 $ 小时。  
  2. **总成本构成**：  
     - 固定投入成本：$ 900 \times 6 = 5,400 $（已支付，类似上文 **21.1 中 $ FC = 60 $**）  
     - 可变投入成本：$ 16 \times 5 = 80 $（类似上文 **21.1 中 $ VC = 4s^2 + 75s $**）  
     - **总成本**：$ 5,400 + 80 = 5,480 $ → **选项 (a)**。  
  - *注：旧笑话成本已支付，但仍计入总成本（沉没成本不影响最优决策，但会计计算需包含）。*  

#### **问题 21.5：长期成本最小化的最优投入比例**  
- **关键逻辑**：  
  长期可自由调整 $ J $ 和 $ L $，需满足 **边际技术替代率（MRTS）等于要素价格比**（类似上文 **21.2 中设备选择的总成本比较逻辑**）：  
  $$
  \text{MRTS} = \frac{MP_J}{MP_L} = \frac{w_J}{w_L}
  $$  
  1. **计算边际产量**：  
     $$
     MP_J = \frac{\partial Q}{\partial J} = 0.05 J^{-1/2} L^{3/4}, \quad MP_L = \frac{\partial Q}{\partial L} = 0.075 J^{1/2} L^{-1/4}
     $$  
  2. **推导 MRTS**：  
     $$
     \text{MRTS} = \frac{MP_J}{MP_L} = \frac{0.05}{0.075} \cdot \frac{L}{J} = \frac{2}{3} \cdot \frac{L}{J}
     $$  
  3. **代入价格比**：  
     $$
     \frac{2}{3} \cdot \frac{L}{J} = \frac{w_J}{w_L} = \frac{2}{18} = \frac{1}{9} \implies \frac{J}{L} = 6
     $$  
     → **选项 (e)**。  
  - *注：此逻辑延续上文 **21.2 的设备选择原则**（总成本最小化），但聚焦长期要素配置优化。*  

---

### 3. 知识连续性说明  
- **短期 vs 长期约束**：  
  - **21.4** 类似 **21.3**：固定要素（$ J $ 或 $ F $）决定短期供给，成本计算包含固定投入支出（即使沉没）。  
  - **21.5** 延伸 **21.2**：长期自由选择下，通过边际条件（MRTS=价格比）实现成本最小化，呼应规模经济分析。  
- **成本理论递进**：  
  从 **21.1（成本分解）→ 21.2（长期产能选择）→ 21.3（短期产量决策）→ 21.4/21.5（生产函数应用）**，完整覆盖 **成本最小化与利润最大化** 的微观决策逻辑。
