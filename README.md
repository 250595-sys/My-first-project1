# My-first-project1
📖 Code & Logic Explanation

The project controls a Pioneer two-wheeled differential drive robot using dual analog light sensors (`A1` and `A2`) to follow a dark line path on a bright surface.
Sensor Reading & Motor Control Table

| Sensor `A1` (Left) | Sensor `A2` (Right) | Action   | Left Motor (`M3`) | Right Motor (`M4`) |
|                    |                     |          |                   |                    |
|  < 5    (On Line)  |   > 5  (Off Line)   |S Right   |      20%          |        40%         |
|  > 5    (Off Line) |   < 5  (On Line)    |S Left    |     40%           |        20%         |
|  > 5    (Off Line) |   > 5    (Off Line) |D Straight|     40%           |        40%         |
|  < 5    (On Line)  |   < 5    (On Line)  |D Straight|     40%           |        40%         |

⚙️ Step-by-Step Logic Breakdown

Infinite Execution Loop (`while bool(1):`)
The robot continually polls readings from both sensors attached to port `A1` and `A2` without stopping during operation.
Steer Right Condition (`A1 < 5 and A2 > 5`)
When the left sensor (`A1`) reads a value below `5`, it has detected the dark track boundary.
To correct heading and pivot right, motor `M3` power is reduced to 20% while motor `M4` is maintained at 40%.


Steer Left Condition (`A1 > 5 and A2 < 5`)
When the right sensor (`A2`) reads a value below `5`, the robot is drifting off-track to the left.
To correct heading and pivot left, motor `M4` power is reduced to 20% while motor `M3` is maintained at 40%.


Default Forward Movement (`else`)
When both sensors detect identical surface conditions (either both on the light background or both over a line node), equal power of 40% is delivered to both motors (`M3` and `M4`) to drive straight ahead.
<img width="1254" height="774" alt="image" src="https://github.com/user-attachments/assets/f39c6bf6-5e34-4ce8-b4e8-8bfe4029b550" />


