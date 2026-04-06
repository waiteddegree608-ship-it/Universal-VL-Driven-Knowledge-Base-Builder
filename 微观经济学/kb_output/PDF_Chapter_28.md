# PDF_Chapter_28

### Page/Slide 1



# 博弈论案例分析：清洁房间博弈

## 文本与公式提取

### 文本内容
- **章节标题**：Chapter 28, Game Theory
- **引入段落**：介绍三种双人博弈例子：
  - 第一个游戏有主导策略均衡
  - 第二个游戏有纯策略纳什均衡但不是主导策略均衡
  - 第三个游戏没有纯策略纳什均衡，但有混合策略均衡
- **室友例子**：Albert和Victoria作为室友，偏好干净房间但都不愿打扫
- **收益规则**：
  - 两人均打扫：每人获得5效用
  - 一人打扫一人不打扫：打扫者获0效用，不打扫者获8效用
  - 两人都不打扫：每人获1效用
- **均衡分析**：表明"Don't Clean"是双方的主导策略，形成主导策略均衡，但双方合作清洁会得到更好结果

### 收益矩阵
```
Albert \ Victoria | Clean    | Don't Clean
------------------|----------|-------------
Clean            | 5, 5     | 0, 8
Don't Clean      | 8, 0     | 1, 1
```

## 图表分析

![Clean Room-Dirty Room Payoff Matrix](https://i.imgur.com/placeholder.png)

该收益矩阵展示了双人博弈中的纯策略组合及其对应的效用结果：

1. **主导策略识别**：
   - 对Albert而言：
     - 当Victoria选择"Clean"：Don't Clean(8) > Clean(5)
     - 当Victoria选择"Don't Clean"：Don't Clean(1) > Clean(0)
     - 因此"돈't Clean"是Albert的主导策略
   - 对Victoria而言：
     - 当Albert选择"Clean"：Don't Clean(8) > Clean(5)
     - 当Albert选择"Don't Clean"：Don't Clean(1) > Clean(0)
     - 因此"돈't Clean"也是Victoria的主导策略

2. **均衡特性**：
   - (Don't Clean, Don't Clean)构成主导策略均衡，双方均获效用1
   - 尽管(1,1)是均衡结果，但(Clean,Clean)组合(5,5)对双方均更优
   - 这体现了典型的**囚徒困境**结构：个人最优选择导致集体次优结果

3. **与上文知识点关联**：
   - 该案例验证了"第一个游戏有主导策略均衡"的分类
   - 主导策略均衡一定是纳什均衡，但纳什均衡未必是主导策略均衡（后续案例将展示）
   - 揭示了非合作博弈中个体理性与集体理性的冲突

此案例表明，当个体仅追求自身利益最大化时，可能产生对所有人都不利的结果，这为理解市场失灵和集体行动问题提供了基础框架。

---
### Page/Slide 2



### 文字与公式提取

#### 文本内容
- **页码与章节**：338 GAME THEORY (Ch. 28)
- **背景描述**：  
  "concentrate his reconnaissance aircraft on the Northern or the Southern route. Once he finds the convoy, he can bomb it until its arrival in New Guinea. Kenney's staff has estimated the number of days of bombing time for each of the outcomes. The payoffs to Kenney and Imamura from each outcome are shown in the box below. The game is modeled as a 'zero-sum game.' For each outcome, Imamura's payoff is the negative of Kenney's payoff."
- **标题**：*The Battle of the Bismarck Sea*
- **均衡分析**：  
  "This game does not have a dominant strategy equilibrium, since there is no dominant strategy for Kenney. His best choice depends on what Imamura does. The only Nash equilibrium for this game is where Imamura chooses the northern route and Kenney concentrates his search on the northern route. [...] Therefore if both choose 'North,' then neither has an incentive to act differently."
- **混合策略引言**：  
  "Some two-player games do not have a 'Nash equilibrium in pure strategies.' But every two-player game of the kind we look at has a Nash equilibrium in mixed strategies. If a player is indifferent between two strategies, then he is also willing to choose randomly between them."
- **案例延伸**：  
  "Example: A soccer player has been awarded a free kick. The only player allowed to defend against his kick is the opposing team's goalie. The kicker has two possible strategies. He can try to kick the ball into the right side of the goal or he can try to kick the ball into the left side of the [...]"
- **脚注**：  
  "* This example is discussed in Luce and Raiffa's Games and Decisions, John Wiley, 1957 or Dover, 1989. We recommend this book to anyone interested in reading more about game theory."

#### 收益矩阵
```
Kenney \ Imamura | North  | South
-----------------|--------|--------
North            | 2, −2  | 2, −2
South            | 1, −1  | 3, −3
```

### 图表分析与含义解释

#### 收益矩阵的核心特性
1. **零和博弈结构**：  
   Imamura 的收益严格为 Kenney 收益的负值（如 Kenney 得 2，Imamura 得 −2）。这与上文清洁房间博弈的**非零和性质**形成对比：
   - 清洁房间博弈中，双方可通过合作实现 (5,5) 的帕累托改进（集体最优），而本案例中一方收益增加必然导致另一方损失，不存在"双赢"可能。
   - 零和特性简化了分析：Kenney 以最大化轰炸天数为目目标，Imamura 则以最小化轰炸天数（即最大化自身负收益）为目标。

2. **主导策略缺失**：  
   - Kenney 无主导策略：
     - 若 Imamura 选 North：Kenney 选 North 得 2 > South 得 1 → 偏好 North
     - 若 Imamura 选 South：Kenney 选 South 得 3 > North 得 2 → 偏好 South  
   - 此特性与上文**清洁房间博弈的核心差异**：
     - 上文案例中，"Don't Clean" 是双方主导策略，直接导向均衡（1,1）。
     - 本案例中，双方策略相互依赖，需通过纳什均衡概念求解，对应上文分类中的"第二个游戏"（有纯策略纳什均衡但非主导策略均衡）。

3. **纯策略纳什均衡验证**：  
   - 唯一均衡点为 **(North, North)**，原因：
     - 给定 Imamura 选 North：Kenney 选 North（2）优于 South（1），无偏离动机。
     - 给定 Kenney 选 North：Imamura 选 North（−2）与 South（−2）无差异，故无偏离动机（零和下收益相同）。
   - 其他组合均非均衡：
     | 组合         | Kenney 偏好改变？ | Imamura 偏好改变？ | 原因                               |
     |--------------|-------------------|-------------------|------------------------------------|
     | (North, South) | 是（选 South 得 3） | 无（−2）          | Kenney 会单方面转向 South         |
     | (South, North)| 无（1）           | 是（选 North 得 −1）| Imamura 会单方面转向 North        |
     | (South, South)| 无（3）           | 是（选 North 得 −1）| Imamura 会单方面转向 North        |
   - **历史实现**：案例中双方实际选择 (North, North)，印证均衡的现实可实现性。

4. **与上文知识点的连续性**：  
   - 本案例**直接对应上文分类的第二种双人博弈**（有纯策略纳什均衡但非主导策略均衡），需结合上文清洁房间博弈（第一种）理解：
     - 清洁房间→主导策略均衡（本质是强预测性纳什均衡），个体理性导致集体无效率（囚徒困境）。
     - 本案例→**弱预测性纳什均衡**，依赖双方对彼此理性的共同认知：Kenney 需预判 Imamura 选择 North 才决策，反之亦然。这揭示了纳什均衡的扩展适用场景。
   - 后续文本提到"混合策略均衡"（如足球点球案例），为过渡至上文提及的"第三个游戏"（无纯策略均衡但有混合策略均衡）埋下伏笔，体现博弈论分析框架的系统性。

#### 结论性含义
此博弈证明：在**非合作但非对抗性冲突**（如军事侦察）中，纳什均衡可作为稳定解存在，但依赖策略互动而非个体单边最优。其**零和特性**消除了上文清洁房间博弈中的合作改进空间，凸显博弈类型（零和 vs. 非零和）对均衡性质的关键影响。

---
### Page/Slide 3



# 足球点球博弈的混合策略均衡分析

## 1. 文字、公式与图表提取

### 文字内容
- 页码：339
- 场景描述："There is not time for the goalie to determine where the ball is going before he must commit himself by jumping either to the left or to the right side of the net. Let us suppose that if the goalie guesses correctly where the kicker is going to kick, then the goalie always stops the ball. The kicker has a very accurate shot to the right side of the net, but is not so good at shooting left. If he kicks to the right side of the net and the goalie jumps left, the kicker will always score. But the kicker kicks to the left side of the net and the goalie jumps to the right, then the kicker will score only half of the time."
- 支付规则："if the kicker makes the goal, the kicker gets a payoff of 1 and the goalie a payoff of 0 and if the kicker does not make the goal, the goalie gets a payoff of 1 and the kicker a payoff of 0."
- 核心结论："This game has no Nash equilibrium in pure strategies... What we can find is a pair of equilibrium mixed strategies."
- 模型分析："In this mixed strategy equilibrium each player's strategy is chosen at random..."

### 公式
- $ \pi_G $: 门将跳向左侧的概率
- $ 1 - \pi_G $: 门将跳向右侧的概率
- 踢右的期望收益 = $ \pi_G $
- 踢左的期望收益 = $ 0.5(1 - \pi_G) $
- 均衡方程：$ \pi_G = 0.5(1 - \pi_G) $
- 解得：$ \pi_G = 1/3 $

### 收益矩阵
```
                 Kicker
             Kick Left  Kick Right
Goalie Jump Left   1,0       0,1
      Jump Right  .5,.5      1,0
```

## 2. 图表分析与含义解释

### 收益矩阵的核心特性

#### 1. **严格无纯策略纳什均衡**
- **与上文军事博弈的对比**：
  - 军事博弈（上文）：存在纯策略纳什均衡（North, North）
  - 本案例：**所有纯策略组合均不稳定**
  - 原因分析：
    | 组合 | 偏离动机 | 偏离结果 |
    |------|----------|----------|
    | (Jump Left, Kick Left) | 门将转向Jump Right | 门将收益从0→0.5 |
    | (Jump Left, Kick Right) | 踢球者转向Kick Left | 踢球者收益从0→1 |
    | (Jump Right, Kick Left) | 门将转向Jump Left | 门将收益从0.5→0 |
    | (Jump Right, Kick Right) | 门将转向Jump Left | 门将收益从0→1 |

#### 2. **混合策略均衡的推导机制**
- **满足上文知识框架中的"第三类博弈"**：
  - 清洁房间博弈：主导策略均衡（type 1）
  - 军事博弈：纯策略纳什均衡（type 2）
  - 本案例：**唯一混合策略均衡（type 3）**

- **均衡条件**：
  - 门将最优混合概率 $ \pi_G = 1/3 $，使踢球者：
    - 踢右期望收益 = 踢左期望收益
    - $ \pi_G = 0.5(1 - \pi_G) $
  - （根据博弈对称性，踢球者均衡概率 $ \pi_K = 2/3 $，使门将跳左/跳右期望相等）

#### 3. **异质能力结构决定均衡**
- **与标准对称点球模型的本质区别**：
  | 模型特性 | 标准对称模型 | 本文模型 |
  |----------|--------------|----------|
  | 踢球能力 | 左右均衡 | 右侧能力强 |
  | 关键数据 | 无0.5收益 | 存在0.5概率收益 |
  | 均衡结果 | $ \pi_G = 0.5 $ | $ \pi_G = 1/3 $ |
  - 门将应更频繁跳向弱侧（左侧），因为踢球者在弱侧成功率较低（仅50%）
  - 这验证了"收益结构决定策略分布"的核心原理

#### 4. **与上文知识的连续性**
- **验证上文预测**：
  > "后续文本提到'混合策略均衡'（如足球点球案例），为过渡至上文提及的'第三个游戏'（无纯策略均衡但有混合策略均衡）埋下伏笔"

- **扩展纳什均衡框架**：
  - 军事博弈（上文）：纯策略均衡依赖**策略互信**
  - 本案例：混合均衡依赖**期望收益相等**，体现博弈论对**随机化行为**的解释力
  - 临界点：当一方**无严格优势策略**且**策略收益交叉依赖**时，纯策略均衡消失

### 3. 现实含义与理论价值

- **动态适应性**：混合均衡解释了真实比赛中双方的随机行为（非固定模式），避免被对手预测
- **能力差异的量化影响**：踢球者右侧准确性优势导致：
  - 门将需更少跳向强侧（$ \pi_G = 1/3 < 0.5 $）
  - 踢球者应更多使用弱侧（$ \pi_K = 2/3 > 0.5 $），体现"以弱补强"策略
- **均衡的存在性证明**：即使严格无纯策略均衡，混合策略仍保证纳什均衡的存在，完善了博弈论框架

> 此案例完美呈现了从"主导策略→纯策略均衡→混合策略均衡"的博弈论分析进阶路径，表明策略空间扩展（加入随机化）如何解决确定性策略的不稳定临界问题。

---
### Page/Slide 4



### 提取内容

#### 文字
```
the probability that the kicker does not score. If the goalie jumps left, then the kicker will not score if he kicks left and will score if he kicks right, so the expected payoff to the goalie from going left is $\pi_K$. If the goalie jumps right, then with probability $(1 - \pi_K)$, the kicker will kick right and the goalie will stop the ball. When the kicker is kicking to the undefended left side of the net, he only makes it half the time, so if the goalie jumps right, the probability that the kicker kicks left and makes the kick is only $.5\pi_K$. Therefore the expected payoff to the goalie from jumping right is $(1 - \pi_K) + .5\pi_K = 1 - .5\pi_K$. Equalizing the payoff to the goalie from jumping left or jumping right requires $\pi_K = 1 - .5\pi_K$. Solving this equation we find that in the equilibrium mixed strategy, $\pi_K = 2/3$.

28.1 (0) Perhaps you have wondered what it could mean that “the meek shall inherit the earth.” While we don’t claim this is always the case, here is an example where it is true. In a famous experiment, two psychologists* put two pigs—a little one and a big one—into a pen that had a lever at one end and a trough at the other end. When the lever was pressed, a serving of pigfeed would appear in a trough at the other end of the pen. If the little pig would press the lever, then the big pig would eat all of the pigfeed and keep the little pig from getting any. If the big pig pressed the lever, there would be time for the little pig to get some of the pigfeed before the big pig was able to run to the trough and push him away.

Let us represent this situation by a game, in which each pig has two possible strategies. One strategy is Press the Lever. The other strategy is Wait at the Trough. If both pigs wait at the trough, neither gets any feed. If both pigs press the lever, the big pig gets all of the feed and the little pig gets a poke in the ribs. If the little pig presses the lever and the big pig waits at the trough, the big pig gets all of the feed and the little pig has to watch in frustration. If the big pig presses the lever and the little pig waits at the trough, then the little pig is able to eat 2/3 of the feed before the big pig is able to push him away. The payoffs are as follows. (These numbers are just made up, but their relative sizes are consistent with the payoffs in the Baldwin-Meese experiment.)

Big Pig–Little Pig

                Big Pig
               Press  Wait
Little Pig Press -1,9   -1,10
         Wait    6,4     0,0

* Baldwin and Meese (1979), “Social Behavior in Pigs Studied by Means of Operant Conditioning,” Animal Behavior
```

#### 公式
- $\pi_K$: 踢球者踢向左侧的概率  
- 门将跳右的期望收益 = $1 - 0.5\pi_K$  
- 均衡方程：$\pi_K = 1 - 0.5\pi_K$  
- 解得：$\pi_K = 2/3$  

---

### 图表分析与含义解释

#### **Big Pig–Little Pig 收益矩阵**
|                | **Big Pig Press** | **Big Pig Wait** |
|----------------|-------------------|------------------|
| **Little Pig Press** | $-1, 9$          | $-1, 10$         |
| **Little Pig Wait**  | $6, 4$           | $0, 0$           |

##### **与上文知识点的连续性分析**
- **均衡类型对比**：  
  上文点球案例（无纯策略纳什均衡，唯一混合策略均衡）与此案例形成鲜明对比。本矩阵存在**纯策略纳什均衡（Wait, Press）**：  
  - 当 Big Pig 选择 Press 时，Little Pig 选择 Wait 可获 6（优于 Press 的 -1）；  
  - 当 Little Pig 选择 Wait 时，Big Pig 选择 Press 可获 4（优于 Wait 的 0）。  
  这验证了上文所述的博弈分类框架：  
  - ✅ **点球案例**：**第三类博弈**（无纯策略均衡，需混合策略）；  
  - ✅ **本案例**：**第二类博弈**（存在纯策略纳什均衡），体现 "纯策略均衡依赖策略互信" 的特征（上文军事博弈即如此）。

- **"meek shall inherit the earth" 的机制**：  
  - 均衡结果 (Wait, Press) 中，Little Pig 收益为 6，Big Pig 收益为 4，**弱势方（Little Pig）反获更高收益**。  
  - **关键原因**：本游戏存在**严格占优策略关系**（非对称能力结构）：  
    - Little Pig 的 Wait 对 Press 构成弱占优（Wait 时收益 ≥ Press，且在 Big Pig Press 时严格优于）；  
    - Big Pig 无占优策略，但需响应 Little Pig 的 Wait 以最大化自身收益（4 > 0）。  
  - 这与上文点球案例的**异质能力结构**逻辑一致：  
    | 案例         | 能力差异来源          | 均衡结果                          | 理论映射                 |  
    |--------------|-----------------------|-----------------------------------|--------------------------|  
    | 点球博弈     | 踢球者强侧/弱侧能力   | 门将更少跳向强侧 ($\pi_G = 1/3$) | 收益结构决定策略分布     |  
    | Big-Little Pig | 大小猪行动能力差异    | 弱势方 Wait 获更高收益          | 博弈收益不对称性导向均衡 |  

- **与混合策略框架的关联**：  
  - 本案例**无混合策略必要**（因纯策略均衡存在），但强化了上文 "临界点" 概念：  
    > 当博弈存在纯策略均衡时（策略收益无交叉依赖），混合策略均衡消失。  
  - 同时佐证上文 "均衡的存在性" 原理：  
    - 点球案例：混合策略保证均衡存在（无纯策略解时）；  
    - 本案例：纯策略均衡直接解决"随机化"需求，体现策略空间适配性。

##### **现实含义延伸**
- **动态策略选择**：Little Pig 的 Wait 策略本质是“以退为进”，利用 Big Pig 的行动能力缺陷（Big Pig Press 需时暴露机会），验证了上文“策略互信”在纯策略均衡中的核心作用。  
- **理论价值**：案例揭示博弈论对**权利不对称场景**的解释力——收益结构（如等待时的 6 vs 4）直接导向“meek 遗产”结果，补充了上文“从主导策略→纯策略→混合策略”的进阶路径。

---
### Page/Slide 5



## 提取内容：当前图片文字与公式

### 文字内容
- 顶部：`NAME _________ 341`  
- (a) Is there a dominant strategy for the little pig? **Yes, Wait.** Is there a dominant strategy for the big pig? **No.**  
- (b) Find a Nash equilibrium for this game. Does the game have more than one Nash equilibrium? **The only Nash equilibrium is where little pig waits and big pig presses.** (Incidentally, while Baldwin and Meese did not interpret this experiment as a game, the result they observed was the result that would be predicted by Nash equilibrium.)  
- (c) Which pig gets more feed in Nash equilibrium? **Little pig.**  
- **28.2 (0)** Consider the following game matrix.  
  **A Game Matrix**  
  |          | Player B Left | Player B Right |  
  |----------|---------------|----------------|  
  | Player A Top | $a, b$      | $c, d$         |  
  | Player A Bottom | $e, f$   | $g, h$         |  
  - (a) If (top, left) is a dominant strategy equilibrium, then we know that $a > e$, $b > d$, $c > g$, and $f > h$.  
  - (b) If (top, left) is a Nash equilibrium, then which of the above inequalities must be satisfied? $a > e$; $b > d$.  
  - (c) If (top, left) is a dominant strategy equilibrium must it be a Nash equilibrium? Why? **Yes. A dominant strategy equilibrium is always a Nash equilibrium.**  
- **28.3 (1)** This problem is based on an example developed by the biologist John Maynard Smith to illustrate the uses of game theory in the theory of evolution. Males of a certain species frequently come into conflict with other males over the opportunity to mate with females. If a male runs into a situation of conflict, he has two alternative “strategies.” A male  

### 公式
- 通用矩阵收益表达式：  
  - $(a, b)$, $(c, d)$, $(e, f)$, $(g, h)$  
- 主导策略均衡条件（当 (top, left) 为解）：  
  $a > e$, $b > d$, $c > g$, $f > h$  
- 纳什均衡必要条件（当 (top, left) 为解）：  
  $a > e$; $b > d$  

---

## 图表解析与含义说明

### 游戏矩阵结构
当前图片中的 **A Game Matrix** 是一个 $2 \times 2$ 双人博弈通用模型，行玩家为 **Player A**（策略：Top/Bottom），列玩家为 **Player B**（策略：Left/Right）。收益变量定义如下：
- $(a, b)$：A 选 Top、B 选 Left 时的收益  
- $(c, d)$：A 选 Top、B 选 Right 时的收益  
- $(e, f)$：A 选 Bottom、B 选 Left 时的收益  
- $(g, h)$：A 选 Bottom、B 选 Right 时的收益  

### 结合上文的知识连续性分析
#### 1. **主导策略均衡 vs. 纳什均衡的条件强化上文框架**
   - 上文已指出 **Big Pig–Little Pig 案例属于第二类博弈（存在纯策略纳什均衡）**，且 Little Pig 的 Wait 是弱占优策略（主导策略）。  
   - 本矩阵通过通用形式量化该逻辑：
     - **主导策略均衡（如 28.2a）** 要求最严格条件：$a > e$（A 的 Top 严格优于 Bottom，无论 B 选择）且 $b > d$（B 的 Left 严格优于 Right，无论 A 选择），同时需 $c > g$ 和 $f > h$ 以确保策略对全局最优。这直接映射上文 **"弱势方（Little Pig）通过弱占优策略（Wait）获取更高收益"** 的机制——Little Pig 的 Wait 等价于本矩阵中 B 的 Left（当 $b > d$ 且 $f > h$ 时成立）。
     - **纳什均衡（如 28.2b）** 仅需局部最优：$a > e$（A 无动机偏离 Top 当 B 选 Left）和 $b > d$（B 无动机偏离 Left 当 A 选 Top）。这呼应上文 **"纯策略均衡依赖策略互信"**：在 Big Pig–Little Pig 中，(Wait, Press) 成为均衡仅需 Big Pig 响应 Little Pig 的 Wait（$4 > 0$），而无需全局占优。
   - **关键验证**：28.2c 明确 **"支配策略均衡必为纳什均衡"**，补充了上文博弈分类逻辑：
     - 若存在主导策略（如 Little Pig 的 Wait），则纯策略均衡必然存在（第二类博弈）；
     - 但纯策略均衡未必需主导策略（如点球案例无主导策略，仅混合均衡）。

#### 2. **对上文案例的抽象化支撑**
   - 上文 **Big Pig–Little Pig 矩阵** 是本通用矩阵的具体实例：
     - 将 Big Pig 对应 Player A（策略：Press/Wait），Little Pig 对应 Player B（策略：Press/Wait）。
     - 均衡 (Wait, Press) 对应矩阵中的 (Bottom, Left) 位置，其中 $e = 4$（Big Pig 收益），$f = 6$（Little Pig 收益）。
     - Little Pig 的 Wait 为弱占优策略，满足 $f > b$（$6 > -1$）和 $h > d$（$0 > 10$ 不成立，故为弱占优而非严格占优），与本矩阵 $f > h$ 和 $b > d$ 条件匹配。
   - **与点球案例的对比**：
     - 点球博弈（第三类）需混合策略（$\pi_K = 2/3$）因无纯策略纳什均衡（收益无交叉依赖）；
     - 本矩阵的纯策略分析证明：**当存在主导策略时（如 Little Pig 的 Wait），混合策略需求消失**，直接佐证上文 **"均衡的存在性取决于策略空间适配性"**。

#### 3. **现实含义的递进延伸**
   - 上文 "meek shall inherit the earth" 现象（弱势方获更高收益）在此被形式化：当 $f > e$（Little Pig 收益 > Big Pig 收益），即 28.2c 的 "Little pig gets more feed"，源于收益结构不对称（如 $f = 6$, $e = 4$）。
   - 新案例（28.3）引入演化博弈，与上文 **"点球案例异质能力结构"** 逻辑一致：生物策略冲突仍由收益不对称性驱动（如互斥交配机会的收益矩阵），延续 **"博弈论解释权利不对称场景"** 的理论脉络。

---
### Page/Slide 6



### Extracted Content from Current Image

#### Text and Formulas
```
342 GAME THEORY (Ch. 28)
can play “Hawk” in which case he will fight the other male until he either
wins or is badly hurt. Or he can play “Dove,” in which case he makes
a display of bravery but retreats if his opponent starts to fight. If an
animal plays Hawk and meets another male who is playing Hawk, they
both are seriously injured in battle. If he is playing Hawk and meets an
animal who is playing Dove, the Hawk gets to mate with the female and
the Dove slinks off to calibrate contemplation. If an animal is playing Dove
and meets another Dove, they both strut around for a while. Eventually
the female either chooses one of them or gets bored and wanders off. The
expected payoffs to each of two males in a single encounter depend on
which strategy each adopts. These payoffs are depicted in the box below.

The Hawk-Dove Game

Animal B
Hawk    Dove
Animal A Hawk   −5,−5   10,0
        Dove    0,10    4,4

(a) Now while wandering through the forest, a male will encounter many
conflict situations of this type. Suppose that he cannot tell in advance
whether another animal that he meets will behave like a Hawk or like
a Dove. The payoff to adopting either strategy oneself depends on the
proportion of the other guys that is Hawks and the proportion that is
Doves. For example, suppose all of the other males in the forest act
like Doves. Any male that acted like a Hawk would find that his rival
always retreated and would therefore enjoy a payoff of 10 on every
encounter. If a male acted like a Dove when all other males acted like
Doves, he would receive an average payoff of 4.

(b) If strategies that are more profitable tend to be chosen over strategies
that are less profitable, explain why there cannot be an equilibrium in
which all males act like Doves. If you know that you
are meeting a Dove, it pays to be a Hawk.

(c) If all the other males acted like Hawks, then a male who adopted the
Hawk strategy would be sure to encounter another Hawk and would get
a payoff of −5. If instead, this male adopted the Dove strategy, he
would again be sure to encounter a Hawk, but his payoff would be 0.
```

---

### Analysis of The Hawk-Dove Game  
*(Integrated with prior universal matrix framework; avoids redundancy by focusing on new insights)*  

#### 1. **Matrix Mapping to Universal $2 \times 2$ Form**  
The payoff matrix directly instantiates the prior universal structure:  
- **Strategy correspondence**:  
  - *Top (A) ≡ Hawk*, *Bottom (A) ≡ Dove*  
  - *Left (B) ≡ Hawk*, *Right (B) ≡ Dove*  
- **Payoff assignments**:  
  |           | Hawk (Left) | Dove (Right) |
  |-----------|-------------|--------------|
  | **Hawk (Top)** | $a = -5$, $b = -5$ | $c = 10$, $d = 0$ |
  | **Dove (Bottom)** | $e = 0$, $f = 10$ | $g = 4$, $h = 4$ |  

#### 2. **Violation of Pure Strategy Equilibrium Conditions**  
- Prior framework established that pure strategy Nash equilibrium at (Top, Left) requires **$a > e$ and $b > d$**.  
  Here:  
  - $a = -5$, $e = 0$ → $-5 > 0$ **false**  
  - $b = -5$, $d = 0$ → $-5 > 0$ **false**  
  Thus, (Hawk, Hawk) cannot be a Nash equilibrium—consistent with the prior classification of games *without* pure strategy equilibria (e.g., "point shoot" example).  

- **No dominant strategies**:  
  - For Animal A:  
    - If B plays Hawk, A prefers Dove ($0 > -5$)  
    - If B plays Dove, A prefers Hawk ($10 > 4$)  
  - For Animal B: Symmetric reversal (has no consistent better response).  
  This violates the strict dominance conditions for a **dominant strategy equilibrium** (e.g., $a > e$ and $b > d$ for (Top, Left) to dominate all columns/rows).  

#### 3. **Mixed Strategy Equilibrium and Evolutionary Dynamics**  
- **Why pure strategy equilibrium fails**:  
  The illustration in part (b) confirms the core logic from prior:  
  > *"If you know that you are meeting a Dove, it pays to be a Hawk"*  
  This reflects the *local best response* principle: When $B$ plays Dove (Right), $A$'s payoff from Hawk ($c = 10$) exceeds Dove ($g = 4$), satisfying $c > g$ (from prior, $c > g$ is necessary but insufficient for dominance). However, mutual instability arises because if all adopt Dove, a deviant Hawk exploits the $10$ payoff—preventing sustainable coordination, as foreshadowed in the "point shoot" case.  

- **Evolutionary interpretation (proportions in part (a))**:  
  The dependency on strategy proportions ($\pi_{\text{Hawk}}$, $\pi_{\text{Dove}}$) extends prior mixed strategy concepts:  
  - Expected payoff for Hawk: $10(1 - \pi_{\text{Hawk}}) + (-5)\pi_{\text{Hawk}}$  
  - Expected payoff for Dove: $0(1 - \pi_{\text{Hawk}}) + 4\pi_{\text{Hawk}}$  
  Equilibrium occurs when these payoffs equalize—a direct application of the prior principle that **mixed strategies resolve pure strategy instability** (e.g., $\pi_{\text{Hawk}} = \frac{2}{3}$ as in point shoot). Part (c) examines boundary cases (all Hawks/Doves), but no pure equilibrium exists due to the asymmetric best responses.  

#### 4. **Theoretical Continuity**  
- This game exemplifies the **third type** of博弈 (games with no pure strategy Nash equilibrium) previously referenced, contrasting with Big Pig–Little Pig (second type with pure strategy equilibrium via weak dominance). The absence of a pure equilibrium here stems from the **absence of dominant strategies**, as quantified by the failure of $a > e$ and $b > d$.  
- The evolutionary angle (parts a–c) generalizes prior mixed strategy logic to **population dynamics**, showing how payoff asymmetry (e.g., $f = 10 > g = 4$) drives strategy selection—reinforcing the prior theme that "equilibrium existence depends on strategy space适配性" without repeating case-specific details.

---
### Page/Slide 7



### 当前图片解析（基于上文知识点连续性）

#### 1. 提取文字与公式  
**文字内容**：  
- (d) Explain why there could not be an equilibrium where all of the animals acted like Hawks. If everyone plays Hawk, it would be profitable to play Dove.  
- (e) Since there is not an equilibrium in which everybody chooses the same strategy, we might ask whether there might be an equilibrium in which some fraction of the males choose the Hawk strategy and the rest choose the Dove strategy. Suppose that the fraction of a large male population that chooses the Hawk strategy is $p$. Then if one acts like a Hawk, the fraction of one’s encounters in which he meets another Hawk is about $p$ and the fraction of one’s encounters in which he meets a Dove is about $1−p$. Similarly, if one acts like a Dove, the probability of meeting a Hawk is about $p$ and the probability of meeting another Dove is about $(1−p)$.  
- (f) Write an equation that states that when the proportion of the population that acts like Hawks is $p$, the payoff to Hawks is the same as the payoffs to Doves.  
- (g) Solve this equation for the value of $p$ such that at this value Hawks do exactly as well as Doves.  
- (h) On the axes below, use blue ink to graph the average payoff to the strategy Dove when the proportion of the male population who are Hawks is $p$. Use red ink to graph the average payoff to the strategy, Hawk, when the proportion of the male population who are Hawks is $p$. Label the equilibrium proportion in your diagram by $E$.  

**公式内容**：  
- 鹰的平均收益函数：$p \times (-5) + (1 - p) \times 10 = 10 - 15p$  
- 鸽子的平均收益函数：$p \times 0 + (1 - p) \times 4 = 4 - 4p$  
- 均衡方程（收益相等条件）：$4 - 4p = 10 - 15p$  
- 均衡比例解：$p = \dfrac{6}{11}$  

---

#### 2. 图表含义解析（基于(h)描述的隐含图表）  
上文已论证纯策略均衡失效（$c > g$ 导致局部最优冲突），而本图通过**平均收益函数与均衡点的动态交互**，实证了混合策略均衡的稳定性。图表以 $p$（鹰策略比例）为横轴，平均收益为纵轴，包含两条关键线：  

- **红线（鹰收益）**：$U_H(p) = 10 - 15p$  
  - *变化逻辑*：随 $p$ 增加（鹰比例上升），鹰内部冲突概率 $p$ 增大，因 $U_H(\text{Hawk vs Hawk}) = -5 < 0$，收益加速递减（斜率 $-15$ 比鸽子更陡）。当 $p=0$（全鸽）时 $U_H=10$（获取高收益 $c=10$）；$p=1$（全鹰）时 $U_H=-5$（损失）。  
  - *经济含义*：鹰策略的**规模不经济性**——比例越高，收益下降越快，印证上文“无法维持纯策略均衡”的根源。  

- **蓝线（鸽子收益）**：$U_D(p) = 4 - 4p$  
  - *变化逻辑*：随 $p$ 增加，鸽子遇鹰概率 $p$ 上升，但 $U_D(\text{Dove vs Hawk}) = 0$ 仍优于鹰内部冲突，故收益缓慢递减（斜率 $-4$）。当 $p=0$ 时 $U_D=4$（稳定收益 $g=4$）；$p=1$ 时 $U_D=0$（无损失但无收益）。  
  - *经济含义*：鸽子策略的**抗压性**——比例上升时损失小于鹰，支撑上文“混合策略解决稳定性问题”的机制。  

- **均衡点 $E$（交点）**：  
  - 位置：$p = \dfrac{6}{11}$，$U_H = U_D = \dfrac{20}{11}$。  
  - *稳定性动态*：  
    - 若 $p < \dfrac{6}{11}$：$U_H > U_D$ → 种群中鹰收益更高 → $p$ 自然上升（向 $E$ 收敛）。  
    - 若 $p > \dfrac{6}{11}$：$U_D > U_H$ → 鸽子收益更高 → $p$ 自然下降（向 $E$ 收敛）。  
  - *理论延续*：此 ESS（进化稳定策略）量化了上文 $\pi_{\text{Hawk}}$ 的均衡比例。与“point shoot”案例（比例 $\frac{2}{3}$）差异源于参数 $g$ 变化（本例中 Dove vs Dove 收益 $g=4$，而点射案例隐含不同 $g$ 值），但核心逻辑一致：**收益函数交点严格定义无占优策略博弈的混合均衡存在性**。  

> 注：图表未显式展示，但(h)中“蓝色-鸽子、红色-鹰”的线条设计直观呈现了“**收益等化驱动比例收敛**”这一上文核心结论，避免直接重复纯策略失效的论据，而聚焦动态机制验证。

---
### Page/Slide 8



### 文字与公式提取  
- **页眉文字**：`344 GAME THEORY (Ch. 28)`  
- **图表标签**：  
  - 纵轴：`Payoff`（刻度：0, 2, 4, 6, 8）  
  - 横轴：`Percentage of hawks`（刻度：0, 25, 50, 75, 100）  
  - 红线标注：`Red Line`  
  - 蓝线标注：`Blue Line`  
  - 交点标注：`e`  
- **问题及答案**：  
  > `(i) If the proportion of Hawks is slightly greater than E, which strategy does better? Dove. If the proportion of Hawks is slightly less than E, which strategy does better? Hawk. If the more profitable strategy tends to be adopted more frequently in future plays, then if the strategy proportions are out of equilibrium, will changes tend to move the proportions back toward equilibrium or further away from equilibrium? Closer.`  
- **附录内容**（与上文无关，但客观提取）：  
  - 标题：`Close Encounters of the Second Kind`  
  - 收益矩阵：  
    |               | Gabriel: Go to Party | Gabriel: Stay Home |  
    |---------------|----------------------|--------------------|  
    | **Evangelina: Go to Party** | 1000, 1000          | 0, 0               |  
    | **Evangelina: Stay Home**   | 0, 0                | 0, 0               |  

---

### 图表解析  
图表以**鹰策略比例**（横轴，$p$ 从 0% 到 100%，即 $p \in [0,1]$）为自变量，**平均收益**（纵轴）为因变量，通过两条直线直观呈现上文推导的混合策略均衡机制：  

1. **红线（Hawk 收益）**：  
   - 对应上文公式 $U_H(p) = 10 - 15p$。  
   - **关键验证**：  
     - 当 $p = 0\%$（全为 Dove），收益 $U_H = 10$（图中起点略高于 8，与上文 $c=10$ 一致）；  
     - 当 $p \approx 54.55\%$（即 $\frac{6}{11} \times 100\%$），与蓝线相交于 $e$ 点，收益 $U_H = \frac{20}{11} \approx 1.8$；  
     - 斜率 $-15$ 表明收益随 $p$ 增加**快速递减**，印证上文“鹰策略规模不经济性”。  

2. **蓝线（Dove 收益）**：  
   - 对应上文公式 $U_D(p) = 4 - 4p$。  
   - **关键验证**：  
     - 当 $p = 0\%$，收益 $U_D = 4$（图中起点略低于 4，与上文 $g=4$ 一致）；  
     - 当 $p \approx 54.55\%$，交于 $e$ 点，收益 $U_D = \frac{20}{11} \approx 1.8$；  
     - 斜率 $-4$ 表明收益随 $p$ 增加**缓慢递减**，支撑上文“鸽子策略抗压性”。  

3. **均衡点 $e$ 及动态机制**：  
   - $e$ 位置与上文解 $p = \frac{6}{11}$ 严格吻合，量化了交点处 $U_H = U_D$ 的均衡条件。  
   - 图表隐含**稳定性验证**：  
     - 若 $p > E$（横轴 $p > 54.55\%$），蓝线高于红线 → $U_D > U_H$ → 问题 (i) 的答案“Dove better”；  
     - 若 $p < E$（横轴 $p < 54.55\%$），红线高于蓝线 → $U_H > U_D$ → 问题 (i) 的答案“Hawk better”；  
     - 由此形成**负反馈调整**：策略收益优势驱动比例向 $E$ 收敛（“Closer”），实证了上文 ESS 所谓的“收益等化驱动比例收敛”。  

> **知识连续性说明**：本图表是上文 (h) 要求的直接实现，将抽象函数转化为可视化轨迹。$e$ 点作为唯一交点，避免了纯策略均衡的失效（因 $c > g$ 导致无占优策略），并为问题 (i) 提供几何依据——无需重复论述规模不经济性细节，而聚焦于**交点如何成为动态系统吸引子**，衔接上文“混合策略解决稳定性问题”的核心结论。

---
### Page/Slide 9



### 文字提取  
当前图片中的所有文字内容如下：  

- 页眉：`NAME ________  345`  
- (a) A strategy is said to be a weakly dominant strategy for a player if the payoff from using this strategy is at least as high as the payoff from using any other strategy. Is there any outcome in this game where both players are using weakly dominant strategies? **The only one is (top, left).**  
- (b) Find all of the pure-strategy Nash equilibria for this game. **There are two: (top, left) and (bottom, right).**  
- (c) Do any of the pure Nash equilibria that you found seem more reasonable than others? Why or why not? **Although (bottom, right) is a Nash equilibrium, it seems a silly one. If either player believes that there is any chance that the other will go to the party, he or she will also go.**  
- (d) Let us change the game a little bit. Evangeline and Gabriel are still desperate to find each other. But now there are two parties that they might go to. There is a little party at which they would be sure to meet if they both went there and a huge party at which they might never see each other. The expected payoff to each of them is 1,000 if they both go to the little party. Since there is only a 50-50 chance that they would find each other at the huge party, the expected payoff to each of them is only 500. If they go to different parties, the payoff to both of them is zero. The payoff matrix for this game is:  
  **More Close Encounters**  
  |                        | Gabriel: Little Party | Gabriel: Big Party |  
  |------------------------|------------------------|--------------------|  
  | **Evangeline: Little Party** | 1000, 1000             | 0, 0               |  
  | **Evangeline: Big Party**    | 0, 0                   | 500, 500           |  

---

### 图表解析  
当前图片中的图表（(d)部分的收益矩阵）是【上文知识点总结】中附录收益矩阵的动态扩展版本。结合上文知识，详细解析如下：  

#### 1. 图表变化与上文延续  
- **上文附录基础**：上文附录的收益矩阵（标题 `Close Encounters of the Second Kind`）仅含单一方协调选项，`Stay Home` 导致零收益，且仅存一个纯策略纳什均衡（双方 `Go to Party`）。  
- **当前变化**：  
  - `Stay Home` 被替换为 `Big Party`，引入第二个协调点。  
  - 双方选择 `Big Party` 时，收益由上文的 `(0,0)` 变为 `(500,500)`（源于 50-50 见面概率的期望值）。  
  - 收益结构从 **单一均衡** 演变为 **双均衡体系**：  
    - `(Little, Little)`：帕累托占优均衡（`1000,1000`），对应上文 (b) 的 `(top, left)`。  
    - `(Big, Big)`：次优均衡（`500,500`），对应上文 (b) 的 `(bottom, right)`。  

#### 2. 动态含义及知识衔接  
- **均衡多重性**：  
  上文附录因 `Stay Home` 的零收益仅产生一个纳什均衡，而当前矩阵通过保留 `Party` 选项的正收益，衍生出两个纯策略均衡。这直接呼应上文 (b) 的结论——"有且仅有两个纯策略纳什均衡"，并量化了下文 (c) 中 `(bottom, right)` 的"非理性"：尽管 `(Big, Big)` 是均衡，但 `500 < 1000` 表明其帕累托劣于 `(Little, Little)`，印证上文 (c) "if either player believes the other might go, he or she will also go" 的协调逻辑（即高期望收益驱动向 `Little Party` 的收敛）。  
- **稳定性机制强化**：  
  上文知识点总结强调 "if the more profitable strategy tends to be adopted more frequently... changes tend to move proportions back toward equilibrium"。当前矩阵中：  
  - 当群体比例偏离 `(top, left)` 时（如部分玩家误选 `Big Party`）， `(top, left)` 的更高收益（`1000 > 500`）形成 **负反馈调整**，驱动策略向帕累托占优均衡收敛。  
  - 这直接扩展了上文附录的简单协调模型，将 "单均衡稳定性" 升级为 **"多均衡中质量差异导致的自然收敛"**，无需外部干预即可解释上文 (c) 的合理均衡选择。  
- **与混合策略的隐性关联**：  
  虽无直接混合策略内容，但上文鹰-鸽图表解析中提出的 "规模不经济性"（$U_H$ 陡峭递减）与当前协调游戏形成对照：  
  - 鹰-鸽模型：高竞争比例削弱高风险策略（如 `Hawk`）。  
  - 协调模型：低匹配概率削弱次优策略（如 `Big Party`），强化优质均衡的 **抗压性**（类比上文 $U_D$ 斜率 $-4$ 的缓慢递减）。  

> **知识连续性说明**：此矩阵是上文附录 "Close Encounters" 在 **策略空间维度** 的拓展，通过增加可行均衡数量，显化了协调游戏的核心矛盾——**均衡质量差异引致的动态选择机制**。上文 (a)(b)(c) 分析直接服务于该矩阵的均衡性质验证，避免了重复上文鹰-鸽模型的细节，而聚焦于 **"从单点均衡到多点均衡的稳定性演进"**，为更复杂的混合策略均衡提供现实基础（如后续可引入随机匹配概率解决协调失败）。

---
### Page/Slide 10



### 1. 文字与公式提取  
**当前图片中的所有文字及公式：**  

- **页码与标题**：  
  `346 GAME THEORY (Ch. 28)`  

- **问题描述**：  
  `(e) Does this game have a dominant strategy equilibrium? No. What are the two Nash equilibria in pure strategies? (1) Both go to the little party. (2) Both go to the big party.`  
  `(f) One of the Nash equilibria is Pareto superior to the other. Suppose that each person thought that there was some slight chance that the other would go to the little party. Would that be enough to convince them both to attend the little party? No. Can you think of any reason why the Pareto superior equilibrium might emerge if both players understand the game matrix, if both know that the other understands it, and each knows that the other knows that he or she understands the game matrix? If both know the game matrix and each knows that the other knows it, then each may predict the other will choose the little party.`  
  `28.5 (1) This is a famous game, known to game theorists as “The Battle of the Sexes.” The story goes like this. Two people, let us call them Michelle and Roger, although they greatly enjoy each other’s company, have very different tastes in entertainment. Roger’s tastes run to ladies’ mud wrestling, while Michelle prefers Italian opera. They are planning their entertainment activities for next Saturday night. For each of them, there are two possible actions, go to the wrestling match or go to the opera. Roger would be happiest if both of them went to see mud wrestling. His second choice would be for both of them to go to the opera. Michelle would prefer if both went to the opera. Her second choice would be that they both went to see the mud wrestling. They both think that the worst outcome would be that they didn’t agree on where to go. If this happened, they would both stay home and sulk.`  

- **图表标题与矩阵**：  
  `Battle of the Sexes`  
  **Payoff Matrix**:  
  |                | Michelle: Wrestling | Michelle: Opera |  
  |----------------|---------------------|-----------------|  
  | **Roger: Wrestling** | 2, 1                | 0, 0            |  
  | **Roger: Opera**    | 0, 0                | 1, 2            |  

- **公式/关键数值**：  
  收益值：`(2, 1)`, `(0, 0)`, `(1, 2)`。  
  无显式数学公式，收益矩阵中的数字即为效用值。  

---

### 2. 图表解析  
当前图片中的 `Battle of the Sexes` 收益矩阵是【上文知识点总结】中对称协调模型的 **非对称扩展**，通过引入**偏好异质性**深化了协调游戏的动态机制。结合上文知识，解析如下：  

#### **(1) 同构性与差异点：从对称到非对称协调**  
- **上文延续**：上文知识点总结的收益矩阵（`Gabriel` vs `Evangeline`）是 **对称协调游戏**，具有：  
  - 两个纯策略纳什均衡：`(Little, Little)`（帕累托占优，收益 `1000,1000`）和 `(Big, Big)`（次优，收益 `500,500`）。  
  - 均衡质量差异驱动向 `(Little, Little)` 的自然收敛（因 `1000 > 500`）。  
- **当前变化**：  
  - 本矩阵将对称收益替换为 **非对称偏好**（`Roger` 偏好 `Wrestling`，`Michelle` 偏好 `Opera`），导致：  
    - 两个纯策略均衡：`(Wrestling, Wrestling)`（`2,1`）和 `(Opera, Opera)`（`1,2`）。  
    - **无帕累托占优均衡**：与上文不同，此处 `(Wrestling, Wrestling)` 使 `Roger` 更优但 `Michelle` 劣化，` (Opera, Opera)` 反之。二者均为帕累托有效，但互不占优（因效用无法直接比较），体现了**协调核心矛盾**——均衡选择依赖于非收益因素（如文化惯例或预沟通）。  
  - 文本 `(e)` 中 "both go to the little party/big party" 为符号化表述，对应矩阵中 `Wrestling/Opera`，但损失了上文的**收益绝对量差异**（此处无 `1000` vs `500` 的量化落差）。  

#### **(2) 均衡稳定性与知识动态的再诠释**  
- **上文衔接**：上文知识点总结强调 "高质量均衡的抗压性"，即当群体偏离 `(Little, Little)` 时，更高收益 `1000` 驱动负反馈回归。  
- **当前拓展**：  
  - 本矩阵 **消解了上文的"自然收敛"机制**：因无帕累托优越均衡，双方无法通过单纯收益比较实现协调（`2 > 1` 对 `Roger` 成立，但 `Michelle` 则相反）。文本 `(f)` 中 "Pareto superior" 的表述在严格意义上不成立，而是隐喻 **"局部偏好均衡"**（即对特定玩家占优的均衡）。  
  - 均衡选择需额外机制：  
    - 上文通过 `1000 > 500` 的效用差自动引导协调，而此处需 **共同知识**（common knowledge）如文本 `(f)` 所述："If both know the game matrix and each knows... then each may predict the other will choose the little party"。  
    - 这直接呼应上文 "stability mechanism" 的升级——从**收益差驱动的内生收敛**变为**认知共识驱动的外生协调**，印证上文知识连续性：**多重均衡的解决依赖于非收益维度**（如社会惯例）。  
  - ` (0,0) ` 项（`miscoordination`）保留上文 `Stay Home` 的功能，但效用值 `0` 强化了 **miscoordination成本均等化**，凸显协调失败的同等惩罚性。  

#### **(3) 与混合策略的隐性关联**  
- 上文通过鹰-鸽模型指出 **"规模不经济性"**（如 $U_H$ 陡峭递减）削弱高风险策略。  
- 本矩阵中：  
  - 无直接混合策略内容，但 `(0,0)` 的锯齿状分布（双侧为零）暗示 **协调脆弱性**：当一方误判另一方行动时，损失更大（对比上文鹰-鸽模型的 $U_D$ 缓慢递减）。  
  - 这预示后续可引入 **混合策略** 解决均衡选择问题（如以概率 $\sigma$ 选择偏好活动），为上文 "后续可引入随机匹配概率" 的洞见提供实证锚点。  

> **知识连续性说明**：此图矩阵是上文对称协调模型的**非对称化推演**，将 "单一质量差异均衡" 拓展至 "双质量等价均衡"。它强化了上文核心论点——**协调游戏的本质矛盾在于均衡选择机制**，而非均衡存在性。上文 (c) 中的 "rational convergence" 因收益对称性而成立，而此处需依赖认知共识，凸显了**非对称偏好下协调的复杂性**，为后续学习（如贝叶斯博弈）铺垫。

---
### Page/Slide 11



### 文本与公式提取

#### 问题部分 (Michelle & Roger)
- **(a)** Is the sum of the payoffs to Michelle and Roger constant over all outcomes? **No.** (If so, this is called a “zero-sum game.”) Otherwise it is called a “nonzero sum game.”) Does this game have a dominant strategy equilibrium? **No.**
- **(b)** Find two Nash equilibria in pure strategies for this game. **Both go to opera.** **Both go to mud wrestling.**
- **(c)** Find a Nash equilibrium in mixed strategies. **Michelle chooses opera with probability $2/3$ and wrestling with probability $1/3$. Roger chooses opera with probability $1/3$ and mud wrestling with probability $2/3$.**

#### Chicken 游戏部分
- **28.6 (1)** This is another famous two-person game, known to game theorists as “Chicken.” Two teenagers in souped-up cars drive toward each other at great speed. The first one to swerve out of the road is “chicken.” The best thing that can happen to you is that the other guy swerves and you don’t. Then you are the hero and the other guy is the chicken. If you both swerve, you are both chickens. If neither swerves, you both end up in the hospital. A payoff matrix for a chicken-type game is the following.  
  **Chicken**  
  | Joe Bob \ Leroy | Swerve | Don't Swerve |
  |----------------|--------|--------------|
  | Swerve         | $1,1$  | $1,2$        |
  | Don't Swerve   | $2,1$  | $0,0$        |
- **(a)** Does this game have a dominant strategy? **No.** What are the two Nash equilibria in pure strategies? **The two outcomes where one teenager swerves and the other does not.**

---

### 图表解析：Chicken 收益矩阵的含义

#### **与上文知识点的直接衔接**
上文知识点总结在 **(3) 与混合策略的隐性关联** 中引入鹰-鸽模型（Hawk-Dove model），强调 **"规模不经济性"** ——即高风险策略（$U_H$）的效用会随群体选择陡峭递减，从而削弱其吸引力。当前图片的 Chicken 收益矩阵是该模型的**实证化实例**，将其抽象概念转化为具体支付结构，完美印证了上文的核心洞见。

#### **矩阵变动的核心含义**
| Joe Bob \ Leroy | Swerve     | Don't Swerve |
|----------------|------------|--------------|
| Swerve         | $1,1$      | $1,2$        |
| Don't Swerve   | $2,1$      | $0,0$        |

- **纯策略均衡与规模不经济性的体现**  
  - 纯策略纳什均衡为 **(Swerve, Don't Swerve)** 和 **(Don't Swerve, Swerve)**，即 *一方合作（Swerve）、一方对抗（Don't Swerve）* 的异质结果。这反映了上文所述 **"规模不经济性"** 的动态：  
    - 当一方选择高风险策略 **Don't Swerve**（Hawk 行为）时，若对方选择 **Swerve**（Dove 行为），则自己获得高收益 $2$（"英雄"地位）；  
    - 但当双方同时选择 **Don't Swerve**（规模扩大），收益骤降至 $0$（"医院崩溃"），充分体现 $U_H$ **陡峭递减** 的特性——高风险策略的边际成本随群体规模上升而指数级恶化，导致该策略无法在正规模下维持。  
  - 此结构直接延续上文结论：Chicken 作为 Hawk-Dove 的同构模型，其均衡稳定性依赖于 **"高风险策略的内在脆弱性"**，而非对称协调模型中的收益差驱动。

- **与上文协调游戏的对比（知识连续性强化）**  
  | 特征                | 上文对称协调模型 (e.g., `Little/Big`) | 当前 Chicken 模型 (Hawk-Dove) |
  |---------------------|-------------------------------------|------------------------------|
  | **误协调成本**      | 双方行动不匹配时收益为 $0$（均等惩罚） | 双方行动匹配高风险时收益 $0$（规模性灾难） |
  | **均衡选择机制**    | 收益绝对量差异 ($1000>500$) 驱动内生收敛 | 无规模收益优势，需外生协调（如社会规范） |
  | **脆弱性根源**      | 行动错配导致损失                   | 行动匹配高风险导致损失       |
  - Chicken 的 **$(0,0)$** 项并非协调失败（如上文 `Stay Home`），而是 **规模过载的显性成本**：它强化了上文 (3) 中 "协调脆弱性" 的预判——当参与者误判对方策略（均选择高风险）时，惩罚远高于协调模型（$0$ vs. 未指定误协调值），凸显 **规模不经济性的破坏力**。  
  - 纯策略均衡 **$(1,2)$ 和 $(2,1)$** 无帕累托占优（上文知识点总结 (1) 已确立的非对称协调核心矛盾），但此处均衡性质不同：  
    - 协调游戏均衡要求 **行动一致**（e.g., both opera），  
    - Chicken 均衡要求 **行动对立**（e.g., one swerves）。  
    这印证了上文隐含的 **"多重均衡解决路径分化"**：协调依赖共同知识，而 Chicken 依赖 **风险规避机制**（高风险策略的天然不稳定性自动筛选出异质均衡）。

- **对后续学习的铺垫**  
  混合策略均衡（如 Michelle/Roger 部分的 $2/3$ 概率）在 Chicken 中可推导出相似解，它延续了上文 "后续可引入随机匹配概率" 的洞见，但机制不同：  
  - 协调游戏的混合策略用于解决 **偏好冲突**（通过概率匹配），  
  - Chicken 的混合策略（e.g., probability of Swerve）本质是 **规模经济下的风险对冲**，直接对应 $U_H$ 陡峭递减——参与者以概率 $\sigma$ 回避高风险，确保当一方过度采用 Hawk 时，另一方能通过 Dove 行为防止崩溃。  
  此逻辑为贝叶斯动态博弈提供基础：当玩家无法观测对手类型时，规模不经济性将驱动 **"声誉机制"**（e.g., 以较高概率选择 Dove 避免灾难），延续上文从纯策略到混合策略的逻辑链条。

---
### Page/Slide 12



### 提取内容  
**所有文字与表述**：  
348  GAME THEORY  (Ch. 28)  
*(b) Find a Nash equilibrium in mixed strategies for this game. Play each strategy with probability 1/2.*  
28.7 (0) I propose the following game: I flip a coin, and while it is in the air, you call either heads or tails. If you call the coin correctly, you get to keep the coin. Suppose that you know that the coin always comes up heads. What is the best strategy for you to pursue? *Always call heads.*  
(a) Suppose that the coin is unbalanced and comes up heads 80% of the time and tails 20% of the time. Now what is your best strategy? *Always call heads.*  
(b) What if the coin comes up heads 50% of the time and tails 50% of the time? What is your best strategy? *It doesn’t matter. You can call heads always, tails always, or randomize your calls.*  
(c) Now, suppose that I am able to choose the type of coin that I will toss (where a coin’s type is the probability that it comes up heads), and that you will know my choice. What type of coin should I choose to minimize my losses? *A fair coin.*  
(d) What is the Nash mixed strategy equilibrium for this game? (It may help to recognize that a lot of symmetry exists in the game.) *I choose a fair coin, and you randomize with 50% heads and 50% tails.*  
28.8 (0) Ned and Ruth love to play “Hide and Seek.” It is a simple game, but it continues to amuse. It goes like this. Ruth hides upstairs or downstairs. Ned can look upstairs or downstairs but not in both places. If he finds Ruth, Ned gets one scoop of ice cream and Ruth gets none. If he does not find Ruth, Ruth gets one scoop of ice cream and Ned gets none. Fill in the payoffs in the matrix below.  

**公式与关键表述**：  
- 混合策略均衡解：*Play each strategy with probability 1/2*（问题 (b) 提示）。  
- 纳什混合策略均衡：*I choose a fair coin, and you randomize with 50% heads and 50% tails*（问题 28.7(d)）。  
- 无显式数学公式，但隐含概率结构：公平硬币时，猜测方随机化（50% heads/tails）；硬币偏向时，纯策略占优（80% heads → always call heads）。  

---

### 解析（基于上文知识点）  
#### **混合策略均衡的微观机制强化**  
本页硬币游戏例证 **规模不经济性驱动的混合策略均衡**，直接延续上文 Chicken game 的核心逻辑：  
- **风险对冲与规模过载预防**：  
  当硬币公平（50% heads）时，猜测方通过随机化（50% heads/tails）规避 *误协调灾难*。这映射上文 Chicken 的混合策略本质——  
  - 类似鸡游戏的 $U_H$ 陡峭递减特性（双方选择 Don't Swerve 时收益骤降至 0），此处若投币方选择**不公平硬币**（如 80% heads），猜方必然固定选择 heads，导致投币方损失扩大；  
  - 投币方主动选择**公平硬币**（问题 28.7(c)），等价于上文提及的 **“风险规避机制”**：通过制造被动随机化环境，避免因策略同质化触发规模灾难（类比 Chicken 中双 Hawk 行为的 $(0,0)$）。
  
- **非对称互动中的均衡稳定性**：  
  - 该均衡依赖 **“行动对立”**（投币方不干预概率 vs. 猜测方随机响应），而非上文协调游戏的 **“行动一致”** 要求。这印证上文结论：  
    > *Chicken 均衡要求行动对立，其稳定性源于高风险策略的内在脆弱性，而非对称协调模型中的收益差驱动。*  
  - 在硬币游戏中，若猜方偏离随机化（如固定 call heads），公平硬币下收益无增益；但若投币方偏离公平硬币（如使用 80% heads），猜方会立即转向纯策略（always heads），令投币方损失最大化——**完美体现规模经济下混合策略对崩溃的阻断作用**。

#### **知识连续性与进阶铺垫**  
- **混合策略的微观基础延伸**：  
  本页是上文 Chicken 混合策略（如 Michelle/Roger 部分的 $2/3$ 概率）的**实证简化**：  
  - Chicken 中 $\sigma$（Dove 选择概率）用于对冲 $U_H$ 陡峭递减风险；此处 50% 随机化直接实现 **“规模不经济性的临界缓冲”**——既防止猜方单一策略滥用（如 always heads 使投币方偏好不平衡硬币），又约束投币方选择公平硬币以最小化损失。  
  - 服从上文框架：**混合策略在对抗性游戏中非偏好冲突解决工具，而是规模均衡的自动校准器**（投币方无法通过硬币类型施加单边优势，因猜方随机化使任何偏向无利可图）。  

- **Hide and Seek 作为 Chicken 同构模型的预演**：  
  问题 28.8 的矩阵虽未填充，但其结构隐含 **异质均衡逻辑**：  
  - Ruth 与 Ned 的隐蔽/搜索互动，本质是 Chicken 的空间化变体：双方同时选择同方向（如均选 upstairs）触发 *规模灾难*（Ned 找不到 Ruth，Ruith 获收益），而行动对立（Ned upstairs / Ruth downstairs）产生收益分化。  
  - 这强化上文对比结论：  
    > *Chicken 误协调成本源于“行动匹配高风险”，而非协调游戏的“行动错配”惩罚。*  
    后续矩阵填充将延续该逻辑，为贝叶斯动态博弈中 **“声誉机制”**（如频繁隐藏在低成本区域规避规模过载）提供微观起点。  

#### **关键洞见总结**  
本页将上文抽象理论**嵌入策略互动实操层**：  
- 硬币游戏的混合均衡证明，**规模经济脆弱性可通过外生随机化阈值（公平硬币）内生化**，无需外部规范；  
- 与 Chicken 模型一致，其均衡非帕累托优胜，但通过 **“风险成本内生扩散”**（偏向硬币导致损失扩大）确保稳定，为多参与者博弈的均衡筛选机制提供微观示范。

---
### Page/Slide 13



# 当前图片解析：Hide and Seek 博弈游戏

## 提取内容

**文字与公式：**
- 页眉：`NAME _________ 349`
- 标题：`Hide and Seek`
- 支付矩阵 1：
  ```
       Ruth
       Upstairs  Downstairs
Ned Upstairs   1,0        0,1
     Downstairs 0,1        1,0
  ```
- 问题 (a)：`Is this a zero-sum game? Yes. What are the Nash equilibria in pure strategies? There are none.`
- 问题 (b)：`Find a Nash equilibrium in mixed strategies for this game. Ruth hides upstairs and Ned searches upstairs with probability 1/2; Ruth hides downstairs and Ned searches downstairs with probability 1/2.`
- 问题 (c) 描述：`After years of playing this game, Ned and Ruth think of a way to liven it up a little. Now if Ned finds Ruth upstairs, he gets two scoops of ice cream, but if he finds her downstairs, he gets one scoop. If Ned finds Ruth, she gets no ice cream, but if he doesn’t find her she gets one scoop. Fill in the payoffs in the graph below.`
- 标题：`Advanced Hide and Seek`
- 支付矩阵 2：
  ```
       Ruth
       Upstairs  Downstairs
Ned Upstairs   2,0        0,1
     Downstairs 0,1        1,0
  ```

## 图表分析与上文延续

### 基础 Hide and Seek 矩阵
- **行动逻辑与规模经济映射**：  
  此矩阵直接实现上文 Chicken game 的**空间化变体**，延续"行动匹配高风险"核心机制：  
  - 当 Ned 与 Ruth 选择同一楼层（行动匹配），Ruth 收益为 0 —— 构成 **规模灾难**（对应 Chicken 中双 Hawk 的 $(0,0)$）。  
  - 当选择不同楼层（行动错配），Ruth 收益 1 —— 体现上文"风险对冲需求"：Ruth 的隐藏策略需避免与 Ned 搜索路径同质化，防止规模过载（如 Ned 固定搜 Upstairs 时，若 Ruth 也总藏 Upstairs 将损失全部收益）。  
  - 与上文硬币游戏一致，该结构驱动 **被动随机化**：Ned 的搜索行为迫使 Ruth 随机化隐藏位置（50% 概率），而非主动设计偏好冲突的解决方案。

- **混合策略均衡的微观机制**：  
  问题 (b) 的 50-50 均衡是上文"**规模不经济性的临界缓冲**"的精准实证：  
  - 若一方偏离随机化（如 Ruth 总藏 Upstairs），Ned 固定搜 Upstairs 可获 100% 收益（破坏均衡）；但若 Ned 尝试固定搜 Upstairs，Ruth 立即转向 Downstairs 获得 1（使 Ned 收益归零）。  
  - 双方按 1/2 概率随机化（具象化上文公式 *Play each strategy with probability 1/2*），使任何纯策略偏离均无收益，从而 **内生化解规模失衡风险** —— 与上文硬币游戏同理，通过概率对称性确保均衡稳定性，无需外部干预。

### Advanced Hide and Seek 矩阵
- **支付不对称的动态校准**：  
  Upstairs 结局 Ned 收益从 1 升至 2，等价于上文 **"硬币偏向"场景**（如 80% heads）：  
  - Ruth 的收益结构未变（行动匹配仍损失 0），故需 Ned 维持 $q = 1/2$ 以保持无差异，延续上文"公平硬币"的随机化基准。  
  - 但 Ned 的收益函数变化（$2p$ vs $1-p$）迫使 Ruth 调整隐藏概率至 $p = 1/3$（隐含计算：$2p = 1-p \implies p = 1/3$），体现 **"均衡概率的自适应性"**：  
    > *规模灾难边界随收益差异动态收缩*  
    支付不对称未导致纯策略均衡（区别于上文简化案例），但通过概率重分布（Ruth 减少 Upstairs 隐藏频率）阻断 Ned 的单边优势，印证上文"混合策略对崩溃的阻断作用" —— 若 Ruth 偏离 $p = 1/3$，Ned 可利用支付差异获得超额收益。

- **与上文知识的连续性验证**：  
  - 此调整是上文 **"规模经济脆弱性内生化"** 的微观延伸：支付变化未引发系统崩溃，因混合策略自动调整概率窗口（$p$ 从 1/2 压缩至 1/3），将潜在 "成本递增点" 移至均衡路径之外。  
  - 奠定后续贝叶斯博弈分析基础：Ned 对 Upstairs 的偏好可视为 **"历史行动信号"**，Ruth 的 $p = 1/3$ 概率即上文预演的 **"声誉机制"** —— 通过随机化降低局部规模收益吸引力（如避免频繁隐藏 Downstairs 导致规模过载），呼应 "多参与者博弈的均衡筛选" 逻辑。

## 机制强化总结
本页矩阵将上文抽象机制**嵌入支付结构变化层**：  
- 基础版 50-50 均衡 + Advanced 版概率偏移，共同验证 **混合策略的核心功能是动态缓冲规模不经济性** —— 在零和互动中，随机化非解决冲突手段，而是通过概率校准使系统自适应高风险临界点，确保不经济性始终处于内生控制范围。  
- 与上文 Chicken 模型一脉相承：误协调成本源于策略匹配的规模灾难（Ruth 失去收益而非收益损失），而混合均衡通过扩散风险成本维持稳定性，为后续声誉机制提供可计算的微观基础。

---
### Page/Slide 14



### 提取内容：当前图片文字与公式

#### 文字内容：
- 页眉：`350 GAME THEORY (Ch. 28)`
- 问题 (d)：  
  `Are there any Nash equilibria in pure strategies? No. What mixed strategy equilibrium can you find? Ruth hides downstairs 2/3 of the time. Ned looks downstairs 1/2 the time. If both use equilibrium strategies, what fraction of the time will Ned find Ruth? 1/2.`
- 章节 `28.9 (1)`：  
  `Let’s have another look at the soccer example that was discussed in the introduction to this section. But this time, we will generalize the payoff matrix just a little bit. Suppose the payoff matrix is as follows.`
- 标题：`The Free Kick`
- 说明文本：  
  `Now the probability that the kicker will score if he kicks to the left and the goalie jumps to the right is p. We will want to see how the equilibrium probabilities change as p changes.`
- 子问题：  
  `(a) If the goalie jumps left with probability π_G, then if the kicker kicks right, his probability of scoring is π_G.`  
  `(b) If the goalie jumps left with probability π_G, then if the kicker kicks left, his probability of scoring is p(1 − π_G).`  
  `(c) Find the probability π_G that makes kicking left and kicking right lead to the same probability of scoring for the kicker. (Your answer will be a function of p.) π_G = p / (1 + p).`  
  `(d) If the kicker kicks left with probability π_K, then if the goalie jumps left, the probability that the kicker will not score is π_K.`

#### 公式与矩阵：
- 支付矩阵：
  ```
         Kicker
         Kick Left  Kick Right
  Goalie Jump Left   1,0        0,1
         Jump Right  1-p,p       1,0
  ```
- 关键公式：  
  `π_G = p / (1 + p)`

---

### 图表分析与上文延续

#### 支付矩阵的渐进演化含义
本页的点球博弈（*The Free Kick*）是上文 **Hide and Seek 案例的参数化延伸**，保留了混合策略均衡的核心逻辑，但通过参数 `p` 引入 **收益不对称的连续变化**，深化了上文 "规模灾难的内生缓冲" 机制：

1. **收益结构与规模灾难映射**：
   - 矩阵中 `(Jump Right, Kick Left)` 单元格的 `(1-p, p)` 体现 **不对称性参数化**：`p` 表示当守门员跳向右侧而踢球者踢向左侧时，踢球者的得分概率（对应上文 Advanced Hide and Seek 中 Ned 在 Upstairs 的收益从 1 升至 2 的离散调整）。
   - **匹配风险延续上文 "规模灾难"**：  
     - 当踢球者与守门员选择同侧（`Jump Left, Kick Left` 或 `Jump Right, Kick Right`），踢球者得分概率为 0（即规模过载导致收益归零，类比上文行动匹配时 Ruth 收益为 0）。  
     - 当选择异侧时，得分概率因 `p` 变化：异侧左（`Jump Right, Kick Left`）为 `p`，而异侧右（`Jump Left, Kick Right`）恒为 1——这构建了 **非对称风险敞口**，呼应上文 "支付不对称导致概率动态校准" 的机制。

2. **混合策略均衡的连续调整**：
   - 上文 Advanced Hide and Seek 中，Ned 的 Upstairs 收益提升迫使 Ruth 将隐藏概率从 `1/2` 压缩至 `1/3`（通过隐式方程 `2p = 1-p`）。  
   - 本页通过子问题 (c) 显式化该过程：  
     - 令踢球者对左右两侧无差异，需满足 `p(1 - π_G) = π_G`（由 (a) 和 (b) 推导），解得 `π_G = p / (1 + p)`。  
     - **参数 `p` 驱动概率连续变化**：  
       - 若 `p = 1`（对称情况），`π_G = 1/2`，匹配上文基础 Hide and Seek 的 50-50 均衡；  
       - 若 `p < 1`（踢球者左侧得分能力弱化），`π_G` 减小，守门员更少跳向左侧（避免资源误配）；  
       - 若 `p > 1`（理论可能），`π_G` 趋近 1，守门员高度集中防御左侧——**但混合均衡仍阻断纯策略崩溃**（如上文所述，单边优势会被随机化抵消）。  
     - 此即上文 "均衡概率的自适应性" 的实证：`p` 调整 `π_G` 以维持临界缓冲，确保规模不经济性（匹配损失）被概率扩散吸收。

3. **与上文知识的强化衔接**：
   - **规模灾难边界的动态收缩**：  
     上文指出支付不对称使 "成本递增点" 移至均衡路径外；本页中 `p` 变化直接 **量化均衡窗口的收缩**：  
     - `π_G = p/(1+p)` 的导数 `dπ_G/dp = 1/(1+p)^2 > 0` 表明，当 `p` 增大（左侧隐含规模收益提升），守门员需更频繁选择左侧以 **压缩踢球者的优势空间**，防止局部规模过载（类比 Ruth 减少 Upstairs 隐藏频率阻止 Ned 剥削）。  
   - **声誉机制的微观基础延续**：  
     子问题 (d) 中 `π_K`（踢球者踢左概率）与 `π_G` 的互动，预演了上文 "声誉机制"——代理方通过随机化降低对手的局部收益吸引力（如守门员调整 `π_G` 防止踢球者过度倾向高 `p` 侧），确保系统在零和互动中自适应高风险阈值。

#### 机制本质
- 本页将上文 **"混合策略作为规模不经济的动态缓冲器"** 理论推进至连续参数空间：  
  - 离散收益跳跃（如上文 Upstairs 收益=2）被替换为连续参数 `p`。  
  - 均衡概率 `π_G(p)` 显式展示 **概率校准如何实时吸收收益扰动**，使系统免于协调失败——这正是上文 "混合均衡通过概率对称性确保稳定性" 的深化（无需外部干预，仅靠内生随机化即可维持规模临界点控制）。  
- 为后续贝叶斯博弈铺垫：`p` 可视为 **历史信号**（如踢球者左侧能力提升的证据），而 `π_G = p/(1+p)` 体现上文 "均衡筛选" 中的理性预期——通过概率调整将潜在崩溃点推离均衡路径。

---
### Page/Slide 15



## 提取图片中的文字与公式

### 文字内容
- **(e)** If the kicker kicks left with probability $\pi_K$, then if the goalie jumps right, the probability that the kicker will not score is $(1-p)\pi_K + (1 - \pi_K)$.
- **(f)** Find the probability $\pi_K$ that makes the payoff to the goalie equal from jumping left or jumping right. $\frac{1}{1+p}$.
- **(g)** The variable $p$ tells us how good the kicker is at kicking the ball into the left side of the goal when it is undefended. As $p$ increases, does the equilibrium probability that the kicker kicks to the left increase or decrease? Decreases. Explain why this happens in a way that even a TV sports announcer might understand. The better the kicker’s weak side gets, the less often the goalie defends the kicker’s good side. So kicker can kick to good side more often.
- **28.10 (0)** Maynard’s Cross is a trendy bistro that specializes in carpaccio and other uncooked substances. Most people who come to Maynard’s come to see and be seen by other people of the kind who come to Maynard’s. There is, however, a hard core of 10 customers per evening who come for the carpaccio and don’t care how many other people come. The number of additional customers who appear at Maynard’s depends on how many people they expect to see. In particular, if people expect that the number of customers at Maynard’s in an evening will be $X$, then the number of people who actually come to Maynard’s is $Y = 10 + .8X$. In equilibrium, it must be true that the number of people who actually attend the restaurant is equal to the number who are expected to attend.
- **(a)** What two simultaneous equations must you solve to find the equilibrium attendance at Maynard’s? $y = 10 + .8x$ and $x = y$.
- **(b)** What is the equilibrium nightly attendance? $50$.
- **(c)** On the following axes, draw the lines that represent each of the two equations you mentioned in Part (a). Label the equilibrium attend-

### 公式
- **(e)** 不进球概率: $(1-p)\pi_K + (1 - \pi_K)$
- **(f)** 踢球者均衡策略: $\pi_K = \frac{1}{1+p}$
- **28.10 期望与实际关系**: $Y = 10 + 0.8X$
- **28.10 均衡方程**: $y = 10 + 0.8x$ 和 $x = y$
- **28.10 均衡解**: $50$

---

## 图表分析与上文知识延续

### 点球博弈均衡的双向适应性强化
本页 **(f)** 和 **(g)** 直接延伸上文对 **规模不对称参数 $p$ 的内生调整机制** 的分析，补全了混合策略均衡的 **双向视角**：  
- 上文核心结论 $\pi_G = p / (1 + p)$ 描述守门员防御左侧的均衡概率（$\pi_G$ 随 $p$ 增大而增大，即防御左侧频次上升）。  
- 本页 **(f)** 给出踢球者踢向左侧的均衡概率 $\pi_K = 1/(1 + p)$，揭示 **双向策略的对称动态**：  
  - $\pi_K$ 随 $p$ 增大而减小（$\frac{d\pi_K}{dp} = -\frac{1}{(1+p)^2} < 0$），与 $\pi_G$ 呈严格负相关（$\pi_G + \pi_K = 1$ 不成立，但二者通过 $p$ 耦合）。  
  - **经济含义**：当 $p$ 提升（踢球者左侧"弱侧"能力增强），守门员将防御重心向弱侧偏移（$\pi_G \uparrow$），导致踢球者 **减少使用弱侧**（$\pi_K \downarrow$），转而 **更频繁攻击强侧**（踢右概率 $1 - \pi_K \uparrow$）。  
- **(g)** 的直观解释深化了上文 "规模灾难的内生缓冲" 机制：  
  - "弱侧能力提升 → 守门员减少对强侧防御" 对应上文 "支付不对称导致概率动态校准"：上文指出当收益不对称时（如 Advanced Hide and Seek 中 Ned 的 Upstairs 收益提升），Ruth 会压缩高收益行动的概率以 **防止局部规模过载**；本页中 $p$ 增大类似收益不对称加剧，促使 $\pi_K$ 自动收缩以 **避免踢球者过度剥削强侧**，维持系统免于协调失败。  
  - 关键区别：本页以 **连续参数 $p$ 量化了弱侧改进的边际影响**，而非上文离散的收益跳跃。这证实混合策略通过 **概率双侧调整** 消除规模临界点（若 $\pi_K$ 不降，守门员会过度防御弱侧，导致强侧防御缺失而崩溃）。

> **机制延续性**：上文强调 $\pi_G = p/(1+p)$ 作为 "缓冲器" 将规模灾难推离均衡路径；本页 $\pi_K = 1/(1+p)$ 表明该缓冲 **同时作用于攻击方**——弱侧获利能力提升时，攻击方主动放弃部分收益以 **避免触发防御方的过度反应**，使系统在零和互动中保持对规模不经济性的鲁棒性。此为上文 "概率对称性确保稳定性" 的微观实现。

### Maynard 案例的有限关联性
本页 **28.10** 部分引入规模依赖型协调博弈，但与上文核心（混合策略缓冲规模灾难）仅有弱衔接：  
- **相似点**：均衡条件 $x = y$ 体现 "预期与实际一致"，类比上文混合均衡中行为概率使双方无差异的过程。  
- **关键差异**：Maynard 通过 **自证预期**（$Y = 10 + 0.8X$）实现协调，而点球博弈依赖 **随机化** 规避匹配风险。此处无规模灾难（如行动匹配导致收益归零），故无上文所述的 "内生缓冲" 需求；相反，它是 **单一均衡的确定性协调**，仅说明规模效应在非随机情境下的收敛性。  
- **衔接意义**：虽非混合策略延伸，但为后续章节（如贝叶斯学习中的预期形成）铺垫——上文指出 $p$ 可视为历史信号（如踢球者弱侧能力提升的证据），而 Maynard 的 $X$ 作为 "社会信号" 影响行为，共同体现 **理性预期对规模动态的筛选作用**。

---
### Page/Slide 16



### 当前图片内容解析

#### 1. 文字与公式提取  
**图表文字**：  
- 纵轴：`y`  
- 横轴：`x`  
- 线条标注：  
  - `Y=11+8X`（实际为 $Y = 11 + 0.8X$）  
  - `Y=10+8X`（实际为 $Y = 10 + 0.8X$）  
  - `X=Y`  

**正文文字与公式**：  
- **(d)**  
  - 问题：Suppose that one additional carpaccio enthusiast moves to the area. Like the other 10, he eats at Maynard’s every night no matter how many others eat there. Write down the new equations determining attendance at Maynard’s and solve for the new equilibrium number of customers.  
  - 方程与解：$ y = 11 + .8x $ and $ y = x $, so $ x = y = 55 $.  
- **(e)**  
  - 问题：Use a different color ink to draw a new line representing the equation that changed. How many additional customers did the new steady customer attract (besides himself)?  
  - 答案：$ 4 $.  
- **(f)**  
  - 问题：Suppose that everyone bases expectations about tonight’s attendance on last night’s attendance and that last night’s attendance is public knowledge. Then $ X_t = Y_{t-1} $, where $ X_t $ is expected attendance on day $ t $ and $ Y_{t-1} $ is actual attendance on day $ t-1 $. At any time $ t $, $ Y_t = 10 + .8X_t $. Suppose that on the first night that Maynard’s is open, attendance is 20. What will be attendance on the second night?  
  - 答案：$ 26 $.  
- **(g)**  
  - 问题：What will be the attendance on the third night?  
  - 答案：$ 30.8 $.  
- **(h)**  
  - 问题：Attendance will tend toward some limiting value. What is it?  
  - 答案：$ 50 $.  
- **28.11 (0)**  
  - 问题：Yogi’s Bar and Grill is frequented by unsociable types who hate crowds. If Yogi’s regular customers expect that the crowd at Yogi’s will be $ X $, then the number of people who show up at Yogi’s, $ Y $, will be the larger of the two numbers, $ 120 - 2X $ and 0. Thus $ Y = \max\{120 - 2X, 0\} $.  

**关键公式汇总**：  
$$
\begin{align*}
&Y = 10 + 0.8X \quad \text{(初始 attendance 函数)} \\
&Y = 11 + 0.8X \quad \text{(新增顾客后)} \\
&Y = X \quad \text{(均衡条件)} \\
&X_t = Y_{t-1} \quad \text{(适应性预期机制)} \\
&Y_t = 10 + 0.8X_t \quad \text{(动态调整方程)} \\
&Y = \max\{120 - 2X, 0\} \quad \text{(Yogi's Bar 需求函数)}
\end{align*}
$$

---

#### 2. 图表变化含义解析  
图表包含三条线：$Y = 10 + 0.8X$（初始实际 attendance 函数）、$Y = 11 + 0.8X$（新增顾客后）、和 $Y = X$（45° 线表示预期与实际一致的均衡路径）。结合上文知识点，关键变化含义如下：  

- **均衡移动的机制**：  
  - 上文指出均衡方程 $y = 10 + 0.8x$ 与 $x = y$ 的解为 50，对应图表中交点 $e$（坐标 $(50,50)$）。  
  - 新增外生冲击（d 问中额外顾客），使 $Y = 10 + 0.8X$ 上移至 $Y = 11 + 0.8X$。新均衡解为 $(55,55)$，**验证了上文"规模效应"在非随机协调中的作用**：外生需求增加通过自证预期（$Y_t$ 依赖 $X_t$）引发乘数效应。具体而言，新增 1 名顾客（$+1$ 直接冲击）导致均衡增加 5（$55 - 50 = 5$），但 (e) 答案 $4$ 表明：**实际新增顾客仅吸引 4 名额外参与者**，因冲击需经反馈循环（$Y = 10 + 0.8X$ 中斜率 $0.8$ 反映边际响应率）传导，体现了**规模放大效应的不完全性**（上文"社会信号影响行为"的核心逻辑）。

- **动态收敛过程（f–h 问）**：  
  - 以 $X_t = Y_{t-1}$ 模拟适应性预期，初始 $Y_0 = 20$：  
    - 次晚：$Y_1 = 10 + 0.8 \times 20 = 26$（f 问）  
    - 三晚：$Y_2 = 10 + 0.8 \times 26 = 30.8$（g 问）  
    - 极限：$\lim_{t \to \infty} Y_t = 50$（h 问）  
  - **与上文知识延续**：  
    - 此动态过程**具象化了上文"理性预期对规模动态的筛选作用"**。上文提及 $p$（点球博弈中弱侧能力参数）可视为历史信号；此处 $Y_{t-1}$ 作为历史信号驱动 $X_t$，且 $Y_t = 10 + 0.8X_t$ 的收敛性表明：**即使初始预期失调（$Y_0 = 20 \neq 50$），系统通过反馈自动趋向均衡**，无需混合策略随机化。  
    - 差异点：区别于点球博弈的"规模灾难缓冲"（需双向概率调整），Maynard 案例**仅依赖确定性预期调整**规避协调失败，印证上文"单一均衡的确定性协调"的稳定性。收敛至 50 的极限值，**直接呼应上文均衡解 $50$**，强调预期自洽性对规模效应的稳定化功能——若边际响应率 $0.8 > 1$ 则系统发散（但此处 $0.8 < 1$ 保证收敛），隐含"规模不经济"的自然约束。

- **图表外推意义**：  
  - $Y = X$ 线将图像分为两类区域：  
    - 上方（$Y > X$）：实际 attendance 低于预期，次日预期下调（如 $Y_0=20$ 时，$X_1=20$ 但 $Y_1=26 > X_1$，导致后续 $X_2=Y_1=26$）；  
    - 下方（$Y < X$）：实际高于预期，次日预期上调。  
  - **此动态机制延伸了上文"预期形成"的微观基础**：上文指出点球博弈中 $\pi_K = 1/(1+p)$ 利用概率抑制过度剥削，而此处 $Y = 10 + 0.8X$ 通过线性反馈实现类比功能——调整速率 $0.8$ 决定了收敛速度（斜率越小收敛越快），体现**规模调整的惯性**，为后续贝叶斯学习模型提供离散化参照。

---
### Page/Slide 17



### Extracted Content from Current Image

#### All Text
- **Header**: `NAME ________ 353`
- **Part (a)**:  
  `Solve for the equilibrium attendance at Yogi’s. Draw a diagram depicting this equilibrium on the axes below.`
- **Part (b)**:  
  `Suppose that people expect the number of customers on any given night to be the same as the number on the previous night. Suppose that 50 customers show up at Yogi’s on the first day of business. How many will show up on the second day? 20. The third day? 80. The fourth day? 0. The fifth day? 120. The ninety-ninth day? 120. The hundredth day? 0.`
- **Part (c)**:  
  `What would you say is wrong with this model if at least some of Yogi’s customers have memory spans of more than a day or two? They’d notice that last night’s attendance is not a good predictor of tonight’s. If attendance is low on odd-numbered days and high on even-numbered days, it would be smart to adjust by coming on odd-numbered days.`
- **Footer**:  
  `28.12 (2) Economic ideas and equilibrium analysis have many fascinating applications in biology. Popular discussions of natural selection and biological fitness often take it for granted that animal traits are selected for the benefit of the species. Modern thinking in biology emphasizes that individuals (or strictly speaking, genes) are the unit of selection. A mutant gene that induces an animal to behave in such a way as to help the`

#### All Formulas
- From the chart:  
  $Y = 120 - 2X$  
  $X = Y$
- Implied from context:  
  $Y = \max\{120 - 2X, 0\}$

---

### Chart Analysis: Dynamic Implications and Continuity with Previous Knowledge  
The chart depicts a two-equation system on axes where $x$ (expected attendance) and $y$ (actual attendance) both range from 0 to 80. Key elements and their interpretations, connected to prior concepts:

#### 1. **Static Equilibrium vs. Dynamic Instability**  
   - The intersection of $Y = \max\{120 - 2X, 0\}$ and $Y = X$ occurs at $(40, 40)$, derived from $X = 120 - 2X$ (solving $3X = 120$). This is the **static equilibrium**, where expected and actual attendance equalize.  
   - However, the demand function's slope ($-2$) has an absolute value **greater than 1**, violating the stability condition for convergence under adaptive expectations. *This directly contrasts with the previous Maynard case*, where the marginal response rate of $0.8 < 1$ ensured convergence to equilibrium (e.g., from $Y_0 = 20$, the system approached $Y^* = 50$). Here, $|dY/dX| = 2 > 1$ implies **dynamic instability**, leading to explosive oscillations.  

#### 2. **Oscillatory Behavior in Adaptive Adjustments**  
   - Part (b) illustrates the dynamic path:  
     - $Y_1 = 50$ (initial) $\rightarrow Y_2 = \max\{120 - 2 \times 50, 0\} = 20$  
     - $Y_3 = \max\{120 - 2 \times 20, 0\} = 80$ $\rightarrow Y_4 = \max\{120 - 2 \times 80, 0\} = 0$  
     - $Y_5 = \max\{120 - 2 \times 0, 0\} = 120$ $\rightarrow Y_6 = \max\{120 - 2 \times 120, 0\} = 0$  
     - For $t \geq 4$, attendance cycles between 0 (even $t$) and 120 (odd $t$).  
   - **Key implication**: The system avoids the static equilibrium $(40, 40)$ entirely. This divergence occurs because each feedback loop amplifies deviations:  
     - When $X_t$ rises, $Y_t$ falls more steeply (e.g., $X=80 \rightarrow Y=0$ is a larger drop than the $X=20 \rightarrow Y=80$ rise), increasing oscillation amplitude.  
     - *Continuity with prior knowledge*: The previous summary showed convergence when $|dY/dX| < 1$ (e.g., $Y = 10 + 0.8X$). Here, $|dY/dX| > 1$ confirms that **instability arises when marginal responsiveness exceeds unity**, mirroring the theoretical boundary for dynamic stability in coordinated expectation models.  

#### 3. **Role of Non-Linearity and Kink Point**  
   - The $\max\{120 - 2X, 0\}$ operator creates a kink at $X = 60$ (where $Y = 0$). For $X > 60$, actual attendance drops to 0, abruptly resetting expectations.  
     - In part (b), when $X_4 = 80 > 60$, $Y_4 = 0$, triggering $X_5 = 0$ and $Y_5 = 120$—a discontinuous jump that intensifies oscillations.  
   - *Continuity with prior knowledge*: The previous model used linear adjustments ($Y = 10 + 0.8X$), avoiding such kinks. Here, the non-linearity **exacerbates instability**, aligning with the summary’s emphasis on "size effects" but revealing a critical difference: **positive marginal responses (e.g., $+0.8$) stabilize, while negative/steep responses destabilize**.  

#### 4. **Practical Limitation in Expectation Formation**  
   - Part (c) notes that customers with multi-day memory would detect the odd-even cycle (e.g., high attendance on odd nights after $t=5$) and strategically shift attendance, breaking the adaptive expectation assumption.  
     - *Continuity with prior knowledge*: This echoes the summary’s discussion of "rational expectations as a screening mechanism." In the Maynard case, adaptive learning converged to equilibrium; here, **myopic adaptation fails** because system dynamics become predictable over multiple periods, enabling strategic coordination (e.g., attending on "low-attendance" nights). The model’s omission of memory spans parallels the summary’s critique of "incomplete information—induced fragility" but applies it to deterministic dynamics rather than probabilistic selection.  

#### Why This Matters for Microeconomic Theory  
The chart underscores a core principle from the previous summary: **equilibrium stability depends on the slope of the adjustment function relative to 1**. Here, the steep negative slope ($-2$) turns "self-fulfilling expectations" into a driver of disorder, contrasting with the neutral/positive slopes in prior coordination games (e.g., $Y = 11 + 0.8X$). The divergence pattern validates that **unbounded amplification can occur without randomization** (unlike the point game scenario in the summary), highlighting that deterministic systems with $|dY/dX| > 1$ require more sophisticated expectations (e.g., rational or strategic) to avoid coordination failure.

---
### Page/Slide 18



### Extracted Content from Current Image  

#### Text  
- **Page Header**: *354   GAME THEORY   (Ch. 28)*  
- **Biological Example**:  
  - *"A good illustration is a paper in the Journal of Theoretical Biology, 1979, by H. J. Brockmann, A. Grafen, and R. Dawkins, called 'Evolutionarily Stable Nesting Strategy in a Digger Wasp.'"*  
  - Females of *Sphex ichneumoneus* nest in underground burrows. Two strategies:  
    1. **Dig their own burrows** (5 days per nesting episode), hunting katydids to stock food.  
    2. **Invade others’ burrows** (4 days per nesting episode), adding to the stock; if the founder and invader meet, they fight (50% win probability).  
  - Let $D$ = number of wasps digging their own burrows; $I$ = number of wasps invading others’ burrows.  
  - Assumptions:  
    - Fraction of diggers invaded: $\frac{5}{4} \frac{I}{D}$ (with $\frac{5}{4} \frac{I}{D} < 1$).  
    - Half of invaded diggers win fights (keep burrows), half lose.  
    - Non-invaded diggers successfully lay eggs.  

#### Formulas  
1. Fraction of diggers who **lose** their burrows:  
   $$
   \frac{1}{2} \cdot \frac{5}{4} \frac{I}{D} = \frac{5}{8} \frac{I}{D}
   $$  
2. Fraction of diggers who **do not lose** their burrows:  
   $$
   1 - \frac{5}{8} \frac{I}{D}
   $$  
3. Expected successes over 40 days (8 nesting episodes for diggers):  
   $$
   8 - 5 \frac{I}{D}
   $$  

---

### Connection to Prior Knowledge  
The digger wasp model exemplifies a **biological application of evolutionary stability**, directly extending the summary’s focus on **equilibrium stability in deterministic systems**. While the prior analysis emphasized *expectation formation* in coordination games, this case replaces "adaptive expectations" with **natural selection** as the mechanism driving equilibrium.  

#### Critical Theoretical Link  
- The expected success function $8 - 5 \frac{I}{D}$ has a slope of **-5** with respect to the ratio $\frac{I}{D}$. This **steep negative slope** ($|d(\text{success})/d(I/D)| = 5 > 1$) mirrors the destabilizing dynamics in the prior summary, where $|dY/dX| > 1$ caused oscillations. However, here:  
  - Stability emerges via **evolutionary selection** rather than strategic coordination.  
  - Natural selection favors the strategy with higher expected reproductive success, leading to an equilibrium where both strategies (digging vs. invading) have equal fitness—i.e., when $8 - 5 \frac{I}{D} = \text{invader’s expected success}$.  

#### Contrast with Prior Models  
- Unlike the coordination game, where **myopic adaptation** spiraled into disorder (e.g., $Y = 120 - 2X$), the wasp model achieves stability through **long-run adaptation** via selection. The summary’s critique of "incomplete information—induced fragility" is recontextualized here: fragility arises if the 50-50 fight assumption or time-cost parameters are violated, but the model presumes these as fixed biological constraints.  
- The slope condition $|dY/dX| > 1$ remains a universal stability criterion, whether in economic expectation formation or biological strategy adaptation. Here, the steep slope accelerates convergence to equilibrium (via natural selection) rather than divergence, reflecting the **asymmetric role of nonlinear dynamics** across contexts.  

#### Practical Implication  
This underscores the summary’s core principle: **stability depends on the dynamic response rate relative to 1**. The wasp example generalizes it to evolutionary systems, showing that even with a destabilizing slope ($-5$), deterministic processes (e.g., natural selection) can override initial volatility to enforce equilibrium—highlighting the importance of **modeling the adjustment mechanism** (e.g., strategic coordination vs. biological selection) when predicting system behavior.

---
### Page/Slide 19



# 图片解析：黄蜂策略均衡的稳定性分析

## 文字与公式提取

### 文字内容
- **(b)** In 40 days, a wasp who chose to invade every time she had a chance would have time for 10 invasions. Assuming that she is successful half the time on average, her expected number of successes would be **5**. Write an equation that expresses the condition that wasps who always dig their own burrows do exactly as well as wasps who always invade burrows dug by others. **$8 - 5\frac{I}{D} = 5$**.

- **(c)** The equation you have just written should contain the expression $\frac{I}{D}$. Solve for the numerical value of $\frac{I}{D}$ that just equates the expected number of successes for diggers and invaders. The answer is **$\frac{3}{5}$**.

- **(d)** But there is a problem here: the equilibrium we found doesn't appear to be stable. On the axes below, use blue ink to graph the expected number of successes in a 40-day period for wasps that dig their own burrows every time where the number of successes is a function of $\frac{I}{D}$. Use black ink to graph the expected number of successes in a 40-day period for invaders. Notice that this number is the same for all values of $\frac{I}{D}$. Label the point where these two lines cross and notice that this is equilibrium. Just to the right of the crossing, where $\frac{I}{D}$ is just a little bit bigger than the equilibrium value, which line is higher, the blue or the black? **Black**. At this level of $\frac{I}{D}$, which is the more effective strategy for any individual wasp? **Invade**. Suppose that if one strategy is more effective than the other, the proportion of wasps adopting the more effective one increases. If, after being in equilibrium, the population got joggled just a little to the right of equilibrium, would the proportions of diggers and invaders return toward equilibrium or move further away? **Further away**.

### 公式列表
- 挖掘者策略的预期成功函数：$8 - 5\frac{I}{D}$
- 均衡条件方程：$8 - 5\frac{I}{D} = 5$
- 均衡解：$\frac{I}{D} = \frac{3}{5}$

## 图表解析

### 图表结构
- **纵轴**: Success (成功次数)
- **横轴**: $\frac{I}{D}$ (入侵者与挖掘者比例)
- **蓝色线**: 挖掘者策略的预期成功函数 $8 - 5\frac{I}{D}$，呈负斜率直线
- **黑色线**: 入侵者策略的预期成功次数，为恒定值5的水平线
- **交点e**: 均衡点，代表两种策略预期成功次数相等的状态

### 变化含义分析

图表直观展示了上文所强调的**斜率条件与系统稳定性**的核心关系：

1. **均衡点的确定性**:
   - 交点e处，$\frac{I}{D} = \frac{3}{5}$，两种策略达到适应度相等的状态
   - 此均衡由方程 $8 - 5\frac{I}{D} = 5$ 确定，是自然选择作用下策略比例的理论均衡点

2. **不稳定性机制**:
   - 蓝色线斜率 $-5$ 的绝对值大于1，与上文"斜率条件 $|d(\text{success})/d(I/D)| = 5 > 1$"完全吻合
   - 当系统轻微扰动至均衡点右侧（$\frac{I}{D}$ 略大于 $\frac{3}{5}$），黑色线高于蓝色线，表明**入侵策略更具优势**
   - 此时选择入侵的黄蜂比例将增加，进一步推高 $\frac{I}{D}$，导致系统**远离均衡**而非回归

3. **与上文理论的关联**:
   - 验证了"斜率绝对值大于1导致系统发散"的普遍准则
   - 展示了虽然自然选择理论上会驱使系统向均衡移动，但在此特定参数下，均衡却是**不稳定的**
   - 与上文"进化选择实现稳定性"的论断形成对比——该例中自然选择过程反而加速了系统偏离均衡

此图清晰印证了上文核心观点：**稳定性不仅取决于均衡的存在性，更取决于动态调整机制对扰动的响应速率**。当 $|d(\text{success})/d(I/D)| > 1$ 时，系统会放大初始扰动，即使存在理论均衡，系统也无法维持在该均衡点。

---
### Page/Slide 20



# 图表解析：稳定均衡的重构模型

## 文字与公式提取

### 文字内容
- 页码：`356`
- 章节标识：`GAME THEORY (Ch. 28)`
- 段落内容：  
  "(e) The authors noticed this likely instability and cast around for possible changes in the model that would lead to stability. They observed that an invading wasp does help to stock the burrow with katydids. This may save the founder some time. If founders win their battles often enough and get enough help with katydids from invaders, it might be that the expected number of eggs that a founder gets to lay is an increasing rather than a decreasing function of the number of invaders. On the axes below, show an equilibrium in which digging one's own burrow is an increasingly effective strategy as $\frac{I}{D}$ increases and in which the payoff to invading is constant over all ratios of $\frac{I}{D}$. Is this equilibrium stable? **Yes**."
- 坐标轴标签：  
  - 纵轴：`Success`  
  - 横轴：`$\frac{I}{D}$`
- 交点标签：`e`

### 隐含公式
- 挖掘者策略函数：$a + b\frac{I}{D}$（$b > 0$，表示随$\frac{I}{D}$增加而上升）
- 入侵者策略函数：$c$（常数，表示不随$\frac{I}{D}$变化）
- 均衡条件：$a + b\frac{I}{D} = c$

## 图表与理论解析

### 图表结构对比
| 项目 | 上文模型 | 当前模型 |
|------|----------|----------|
| **挖掘者策略线** | 负斜率直线 ($8 - 5\frac{I}{D}$) | **正斜率直线** |
| **入侵者策略线** | 水平线（恒定值5） | 水平线（恒定值） |
| **均衡点稳定性** | 不稳定 | **稳定** |
| **斜率条件** | $\vert -5 \vert > 1$ | $b < 1$（隐含稳定条件） |

### 变化含义分析

1. **模型重构的核心改进**：  
   上文讨论了挖掘者策略随$\frac{I}{D}$增加而**下降**导致的不稳定性。当前模型通过引入"入侵者帮助存粮(katydids)"机制，使挖掘者策略呈现**上升趋势**（"an increasing function of the number of invaders"）。这反映了"入侵者存在对挖掘者有利"的生物学假设——适度的入侵者能提高挖掘者的繁殖效率。

2. **稳定均衡的形成机制**：  
   - 在均衡点**左侧**（$\frac{I}{D} <$ 均衡值）：  
     水平线（入侵者）高于斜线上升线 → 个体倾向选择**入侵者策略** → $\frac{I}{D}$**增加** → 系统向均衡移动
   - 在均衡点**右侧**（$\frac{I}{D} >$ 均衡值）：  
     斜线上升线高于水平线 → 个体倾向选择**挖掘者策略** → $\frac{I}{D}$**减少** → 系统向均衡移动
   - 这种"向心力"效应与上文模型形成**本质对比**：上文因负斜率导致系统**发散**，当前因正斜率实现**收敛**

3. **与上文稳定条件的呼应**：  
   上文指出"稳定性取决于$\vert d(\text{success})/d(I/D) \vert$与1的大小关系"。本图虽未给出具体斜率值，但：
   - **正斜率**确保了动态调整方向与均衡点"吸引"方向一致
   - 隐含**斜率绝对值小于1**的条件（因均衡稳定），使微小扰动不会被放大
   - 验证了上文结论的普适性：**稳定与否由策略收益函数的斜率特性决定**，而非均衡点是否存在

4. **生物学意义**：  
   模型重构表明：当入侵行为对挖掘者产生**净增益**（而非损失）时，系统可形成稳定均衡。这解开了上文"为何不稳定"的疑问——通过重新设定收益函数，使自然选择机制导向均衡收敛而非发散，更符合生物进化的现实路径。
