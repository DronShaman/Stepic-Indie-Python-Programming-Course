# Программист Василий любит романтику — поэтому на этот Новый Год он решил освещать свою комнату свечами.
# У Василия есть a свечей. Когда Василий зажигает новую свечу, сначала она горит ровно один час, а затем тухнет.
# Василий — сообразительный малый, поэтому из b потухших свечей он умеет получать одну новую свечу. В последствии эту новую
# свечу (так же как и другие новые свечи) можно зажечь.
# Теперь Василию интересно, на сколько часов освещения хватит его свечек, если он будет действовать оптимальным образом.
# Помогите ему найти это число.

n = list(map(int, input().split()))
nosok = n[0]
day = n[1]
num = 0
takt = 0
while True:
    nosok -= 1
    num += 1
    if day == num:
        nosok += 1
        num = 0
    takt += 1
    if nosok == 0:
        print(takt)
        break
