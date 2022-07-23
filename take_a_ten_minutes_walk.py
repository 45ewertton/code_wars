def is_valid_walk(walk):
    step_n_s = 0
    step_e_w = 0

    if len(walk) != 10:
        return False

    else:
        for step in walk:
            if step == 'n' or step == 's':
                if step == 'n':
                    step = 1
                if step == 's':
                    step = -1
                step_n_s += step

            if step == 'e' or step == 'w':
                if step == 'e':
                    step = 1
                if step == 'w':
                    step = -1
                step_e_w += step

        if step_n_s == 0 and  step_e_w == 0:
            return True
            
        else:
            return False