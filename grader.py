def evaluate(env, policy_fn):
    total_reward = 0

    state = env.reset()

    for _ in range(50):
        action = policy_fn(state)
        state, reward, done = env.step(action)
        total_reward += reward

        if done:
            break

    return total_reward / 50
