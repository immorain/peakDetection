def getpeaks(y,x):
    #smooth 1x ma10 2x ma6 depends on data
    y_smooth = smooth(y, 10)
    y_smooth = smooth(y_smooth, 6)
    y_smooth = smooth(y_smooth, 6)

    smoothtable = pd.DataFrame()
    smoothtable['x'] = x
    smoothtable['y'] = y_smooth
    #get the y turning points
    idx_min, idx_max = turning_points(y_smooth)
    #add index 0 and last index. Sort Index
    idx_min.append(0)
    idx_min.append(len(smoothtable['y']) - 1)
    idx_min.sort()
    turning_point = []

    for i in range(len(idx_min)):
        if i > 0:
            tempdf = pd.DataFrame()
            tempdf['x'] = x
            tempdf['y'] = y
            #slicing tempdf based on 2 min values in idx_min list
            tempdf = tempdf[idx_min[i - 1]:idx_min[i]]
            #finding the index of maxvalue from original y.
            maxindex = tempdf['y'].idxmax(axis=0)
            turning_point.append((x[maxindex], max(tempdf.y)))

    return turning_point
  
  # https://stackoverflow.com/questions/19936033/finding-turning-points-of-an-array-in-python
  def turning_points(array):
    idx_max, idx_min = [], []
    if (len(array) < 3):
        return idx_min, idx_max

    NEUTRAL, RISING, FALLING = range(3)
    def get_state(a, b):
        if a < b: return RISING
        if a > b: return FALLING
        return NEUTRAL

    ps = get_state(array[0], array[1])
    begin = 1
    for i in range(2, len(array)):
        s = get_state(array[i - 1], array[i])
        if s != NEUTRAL:
            if ps != NEUTRAL and ps != s:
                if s == FALLING:
                    idx_max.append((begin + i - 1) // 2)
                else:
                    idx_min.append((begin + i - 1) // 2)
            begin = i
            ps = s

    return idx_min, idx_max
  
  # https://stackoverflow.com/questions/20618804/how-to-smooth-a-curve-in-the-right-way
  def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth
