try:
    import Box2D
    from gym.envs.box2d.lunar_lander import LunarLander
    from gym.envs.box2d.lunar_lander import LunarLanderContinuous
    from gym.envs.box2d.lunar_lander import LunarLanderRandomZone
    from gym.envs.box2d.lunar_lander import LunarLanderMoreRandStart
    from gym.envs.box2d.lunar_lander import LunarLanderLimitedFuel
    from gym.envs.box2d.lunar_lander import LunarLanderMovingZone
    from gym.envs.box2d.bipedal_walker import BipedalWalker, BipedalWalkerHardcore
    from gym.envs.box2d.car_racing import CarRacing
except ImportError:
    Box2D = None
