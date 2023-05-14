# Dependencies on matplotlib
import matplotlib.pyplot as plt
import numpy as np

import stage as stg
import light as l
import colour as col
import constants as c

# import smoke


def main():
    # Create a stage
    stageInfo = stg.StageDescriptor(500, 400, None)

    stage = stg.StageDraw(stageInfo)

    # Create lights
    light1 = l.Light(col.Colour("blue"), 100.0, 90, 10, 40)
    light2 = l.Light(col.Colour(["purple", "blue"]), 0.0, 90, 9, 25)

    lg = l.LightGroup([light1, light2])

    # # Create smoke
    # smokeMachine = smoke.SmokeMachine([250, 250], 45, 10)
    # smokeVolume = smoke.Volume(stageInfo)
    # smokeVolume.addMachine(smokeMachine)

    # for i in range(1):
    #     smokeVolume.simulate()
    # smokeVolume.draw(stage.sideAx)

    lg.drawTopDown(stageInfo, stage.topAx)
    lg.draw2D(stageInfo, stage.sideAx)

    plt.suptitle("STAGE VIEW", fontsize="18")
    plt.show()


if __name__ == "__main__":
    main()
