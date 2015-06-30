def listSkuProperties(str):
    return str.split(';')


def mergeSkuProperties(old, new):
    oldagr = listSkuProperties(old)
    newagr = [i for i in new.split(';') if len(i.strip()) > 0]
    agr = list(set(oldagr + newagr))
    return ';'.join(agr)
