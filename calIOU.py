def calIOU(boxA, boxB): # 矩形由左上、右下两个顶点来确定
    boxA = [int(x) for x in boxA] # to int
    boxB = [int(x) for x in boxB]
	
    # 找到相交区域，相交区域左上点为A，右下点为B
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1]) # A点是两矩形左上顶点中，靠近右下的那个
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3]) # B点是两矩形右下顶点中，靠近左上的那个

    # 计算交集的面积，假如A不严格位于B的左上方，说明两个矩形没有交集，交集面积为0
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    #计算两矩形的面积
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    
    # 并集面积 = 两矩形面积之和 - 交集面积， IOU = 交集面积 / 并集面积
    iou = interArea / float(boxAArea + boxBArea - interArea)

    return iou
