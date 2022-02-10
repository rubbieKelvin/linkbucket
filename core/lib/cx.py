from string import digits

alpha = 'dZkyLBuopAwKCqrsaHejzbcXgfVWihIJNExDnTYFQStOGUlmRPvM'

def intToCrypt(value: int) -> str:
    value = str(value)
    res = ''
    alpha_ = alpha
    for i in value:
        if i in digits:
            i = int(i)
            res += ''.join(alpha_[i:i+2])
            alpha_ = alpha_[2:] + alpha_[:2]
    return res
