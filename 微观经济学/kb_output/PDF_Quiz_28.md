# PDF_Quiz_28

### Page/Slide 1



# 提取内容

Quiz 28  
NAME__________  

Game Theory  

28.1 (See Problem 28.1.) Big Pig and Little Pig have two possible strategies, Press the Button, and Wait at the Trough. If both pigs choose Wait, both get 4. If both pigs press the button then Big Pig gets 5 and Little Pig gets 5. If Little Pig presses the button and Big Pig waits, then Big Pig gets 10 and Little Pig gets 0. Finally, if Big Pig presses and Little Pig waits, then Big Pig gets 4 and Little Pig gets 2. In Nash equilibrium,  

(a) Little Pig will get a payoff of 2 and Big Pig will get a payoff of 4.  

(b) Little Pig will get a payoff of 5 and Big Pig will get a payoff of 5.  

(c) both pigs will wait at the trough.  

(d) Little Pig will get a payoff of zero.  

(e) the pigs must be using mixed strategies.  

28.2 (See Problem 28.6.) Two players are engaged in a game of “chicken.” There are two possible strategies. Swerve and Drive Straight. A player who chooses to Swerve is called “Chicken” and gets a payoff of zero, regardless of what the other player does. A player who chooses to Drive Straight gets a payoff of 32 if the other player swerves and a payoff of -48 if the other player also chooses to Drive Straight. This game has two pure strategy equilibria and  

(a) a mixed strategy equilibrium in which each player swerves with probability 0.60 and drives straight with probability 0.40.  

(b) two mixed strategies in which players alternate between swerving and driving straight.  

(c) a mixed strategy equilibrium in which one player swerves with probability 0.60 and the other swerves with probability 0.40.  

(d) a mixed strategy in which each player swerves with probability 0.30 and drives straight with probability 0.70.  

# 解析

本Quiz聚焦博弈论中纳什均衡的识别，直接应用上文知识点（纯策略/混合策略均衡的判定逻辑）进行实操分析，无图表故无需图表解释。  

- **28.1 题解析**：  
  给定收益结构，唯一纯策略纳什均衡为 **(Wait, Wait)**。理由：当双方均选择 Wait 时，Big Pig 单方面转向 Press 无法提升收益（保持 4），而 Little Pig 转向 Press 会导致收益从 4 降至 0，故无偏离动机。选项 (c) 正确，其他选项对应非均衡状态（如 (a) 为 (Press, Wait) 但 Little Pig 有动机转向 Press）。此例印证上文“纯策略均衡需严格无单边改进空间”的结论。  

- **28.2 题解析**：  
  该胆小鬼博弈除两个纯策略均衡（(Swerve, Drive Straight) 和 (Drive Straight, Swerve)）外，存在**对称混合策略均衡**。计算得：玩家需以 0.60 概率 Swerve、0.40 概率 Drive Straight 时，双方期望收益相等（Swerve 收益恒为 0；Drive Straight 期望收益为 $ 0.60 \times 32 + 0.40 \times (-48) = 0 $）。选项 (a) 精确匹配此均衡，而 (c) 错误假设非对称概率，(d) 概率值计算偏差，均违背上文“混合策略均衡需满足无差异条件”的原理。  

上述解析严格基于上文知识点延伸，聚焦题目特定条件验证均衡存在性，未重复基础定义。

---
### Page/Slide 2



### 提取当前图片内容

#### 文字内容
```
504 GAME THEORY (Ch. 28)

(e) no mixed strategies.

28.3 The old Michigan football coach had only two strategies: run the ball to the left side of the line, and run the ball to the right side. The defense can concentrate either on the left side or the right side of Michigan’s line. If the opponent concentrates on the wrong side, Michigan is sure to gain at least 5 yards. If the defense defended the left side and Michigan ran left, Michigan would be stopped for no gain. But if the opponent defended the right side when Michigan ran right, Michigan would still gain at least 5 yards with probability 0.40. It is the last play of the game and Michigan needs to gain 5 yards to win. Both sides choose Nash equilibrium strategies. In Nash equilibrium, Michigan would

(a) be sure to run to the right side.

(b) run to the right side with probability 0.63.

(c) run to the right side with probability 0.77.

(d) run with equal probability to one side or the other.

(e) run to the right side with probability 0.60.

28.4 Suppose that in the Hawk-Dove game discussed in Problem 28.3, the payoff to each player is −4 if both play Hawk. If both play Dove, the payoff to each player is 1 and if one plays Hawk and the other plays Dove, the one that plays Hawk gets a payoff of 3 and the one that plays Dove gets 0. In equilibrium, we would expect Hawks and Doves to do equally well. This happens when the proportion of the total population that plays Hawk is

(a) 0.33.

(b) 0.17.

(c) 0.08.

(d) 0.67.

(e) 1.

28.5 (See Problem 28.11.) If the number of persons who attend the club meeting this week is X, then the number of people who will attend next week is 27 + 0.70X. What is a long-run equilibrium attendance for this club?

(a) 27

(b) 38.57

(c) 54

(d) 90

(e) 63
```

#### 公式
- 28.5 题中：$X_{\text{next}} = 27 + 0.70X$

---

### 解析

本部分延续上文对博弈论的解析框架，聚焦 **纯策略/混合策略均衡判定**（如 28.1-28.2 题）和 **动态均衡分析**，直接应用无差异条件与稳态求解逻辑。无图表故无需图表解释。

#### 28.3 题解析  
该问题为 **足球博弈中的混合策略纳什均衡**，需满足双方无偏离动机的无差异条件。  
- **关键参数**：  
  - Michigan 跑右时，防守方集中右则增益期望为 $0.40 \times 5 + 0.60 \times 0 = 2$；集中左则增益为 5。  
  - 跑左时，防守方集中左则增益为 0；集中右则增益为 5。  
- **均衡推导**：  
  设 $p$ 为 Michigan 跑右概率，$q$ 为防守方集中右概率。  
  - Michigan 无差异条件：$\text{E[左]} = \text{E[右]} \implies 5q = 5(1-q) + 2q \implies q = 0.625$。  
  - 防守方无差异条件：$\text{E[增益|D}_L\text{]} = \text{E[增益|D}_R\text{]} \implies 5p = 5(1-p) + 2p \implies p = 5/8 = 0.625$。  
  结果 $p \approx 0.63$，与选项 (b) 一致。此题验证上文 **“混合策略均衡需满足无差异条件”**，且概率计算直接延续 28.2 题的对称处理逻辑（但此处为非对称博弈，均衡概率由双方收益结构共同决定）。

#### 28.4 题解析  
基于 **Hawk-Dove 进化博弈**，延续 28.3 题的混合策略逻辑。  
- **均衡条件**：Hawk 和 Dove 均衡收益相等（$ \text{E}_\text{Hawk} = \text{E}_\text{Dove} $）。  
- **计算**：  
  设 $p$ 为 Hawk 比例，则  
  $
  \text{E}_\text{Hawk} = p \cdot (-4) + (1-p) \cdot 3, \quad \text{E}_\text{Dove} = p \cdot 0 + (1-p) \cdot 1
  $  
  令相等：$-4p + 3(1-p) = 1 - p \implies p = 1/3 \approx 0.33$。  
  选项 (a) 精确匹配。此例进一步说明上文 **“混合策略均衡收益等价性”** 原理，适用于群体博弈（比例即混合策略概率）。

#### 28.5 题解析  
问题为 **一维动态系统稳态求解**，延续纳什均衡的**长期无偏离特性**。  
- **稳态条件**：当 $X_{\text{next}} = X$（长期均衡），即  
  $
  X = 27 + 0.70X \implies X - 0.70X = 27 \implies X = 27 / 0.30 = 90
  $。  
  选项 (d) 正确。本题虽非标准博弈，但延续上文 **“均衡即策略/状态无变化点”** 的核心思想（如 28.1 题纯策略均衡的静态性），此处扩展至动态系统。
