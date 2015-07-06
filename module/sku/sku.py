def listSkuProperties(str):
    return [i.upper() for i in str.split(';') if len(i.strip()) > 0]


def mergeSkuProperties(old, new):
    oldagr = listSkuProperties(old)
    newagr = [i.upper() for i in new.split(';') if len(i.strip()) > 0]
    agr = list(set(oldagr + newagr))
    return ';'.join(agr)
