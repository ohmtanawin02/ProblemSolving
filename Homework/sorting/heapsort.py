import timeit


def heapify(nlist, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and nlist[i] < nlist[l]:
        largest = l
    if r < n and nlist[largest] < nlist[r]:
        largest = r
    if largest != i:
        nlist[i], nlist[largest] = nlist[largest], nlist[i]
        heapify(nlist, n, largest)


def heapSort(nlist):
    n = len(nlist)

    for i in range(n, 0, -1):
        heapify(nlist, n, i)
    for i in range(n-1, 0, -1):
        nlist[i], nlist[0] = nlist[0], nlist[i]
        heapify(nlist, i, 0)


#nlist = [6, 3, 5, 7, 2, 10, 9, 4, 1, 8]
#nlist = [94, 58, 99, 6, 15, 67, 49, 63, 22, 84, 53, 88, 13, 14, 3, 91, 56, 78, 43, 19, 95, 97, 85, 36, 41, 9, 29, 7, 51, 11, 68, 20, 21, 38, 75, 79, 89, 5, 62, 40, 74, 55, 64, 87, 47, 70, 52, 76, 50,82, 60, 27, 34, 72, 32, 80, 45, 26, 44, 39, 66, 2, 73, 31, 12, 10, 1, 17, 16, 18, 90, 24, 42, 83, 71, 86, 48, 59, 93, 65, 46, 57, 8, 25, 37, 96, 4, 28, 54, 61, 81, 23, 77, 33, 92, 30, 69, 35, 98, 100]
nlist = [334, 47, 863, 945, 252, 325, 546, 880, 233, 576, 103, 881, 123, 166, 38, 724, 360, 535, 742, 786, 196, 529, 791, 200, 749, 644, 853, 611, 73, 840, 602, 74, 187, 440, 224, 114, 929, 76, 752, 302, 345, 35, 136, 733, 433, 987, 266, 978, 854, 931, 983, 147, 69, 928, 793, 997, 331, 193, 383, 651, 547, 963, 445, 545, 470, 500, 127, 901, 554, 887, 808, 833, 697, 462, 280, 967, 553, 313, 721, 159, 29, 93, 42, 176, 947, 386, 676, 932, 450, 316, 746, 506, 422, 399, 725, 750, 391, 171, 444, 803, 215, 292, 483, 806, 734, 212, 525, 23, 489, 623, 191, 548, 139, 558, 384, 211, 707, 119, 912, 61, 299, 768, 87, 760, 686, 965, 780, 75, 530, 54, 933, 99, 976, 916, 387, 228, 285, 34, 15, 834, 914, 747, 60, 324, 174, 268, 277, 567, 219, 473, 37, 990, 585, 243, 472, 709, 438, 813, 779, 133, 157, 744, 439, 979, 327, 801, 658, 303, 671, 275, 807, 790, 515, 643, 667, 487, 883, 146, 107, 859, 347, 355, 753, 884, 90, 83, 941, 731, 244, 730, 449, 528, 852, 906, 181, 455, 96, 536, 738, 394, 84, 544, 597, 78, 381, 961, 946, 177, 826, 624, 369, 645, 377, 475, 857, 293, 178, 284, 741, 262, 195, 800, 870, 41, 207, 810, 26, 769, 7, 503, 714, 259, 839, 326, 811, 885, 886, 818, 981, 411, 392, 851, 371, 678, 582, 718, 339, 672, 649, 908, 681, 155, 541, 823, 596, 496, 95, 509, 897, 442, 309, 112, 899, 51, 677, 144, 13, 415, 507, 740, 358, 56, 622, 145, 691, 429, 610, 781, 352, 301, 105, 923, 256, 598, 614, 631, 949, 809, 634, 113, 232, 918, 527, 18, 419, 321, 650, 167, 831, 944, 32, 484, 149, 551, 160, 537, 873, 751, 942, 457, 362, 21, 837, 150, 380, 584, 234, 860, 367, 847, 323, 116, 867, 640, 606, 468, 646, 418, 971, 549, 756, 728, 269, 289, 395, 288, 594, 578, 695, 223, 477, 357, 495, 111, 431, 843, 319, 141, 46, 566, 683, 784, 627, 587, 491, 612, 253, 637, 192, 267, 306, 168, 770, 374, 539, 980, 930, 968, 214, 40, 898, 531, 349, 385, 579, 172, 454, 249, 902, 426, 891, 639, 647, 560, 363, 821, 573, 943, 659, 206, 63, 134, 336, 341, 70, 985, 814, 842, 315, 761, 49, 348, 261, 603, 251, 950, 463, 789, 340, 227, 453, 448, 629, 882, 657, 393, 3, 337, 446, 799, 283, 700, 948, 479, 788, 732, 102, 151, 745, 592, 924, 481, 372, 295, 543, 238, 572, 247, 689, 152, 564, 926, 194, 921, 24, 100, 425, 792, 213, 346, 88, 743, 571, 20, 101, 452, 180, 432, 877, 523, 820, 595, 704, 71, 626, 350, 97, 759, 848, 199, 508, 669, 600, 708, 403, 618, 516, 467, 1000, 510, 726, 812, 68, 427, 693, 248, 128, 281, 486, 414, 366, 257, 173, 169, 835, 81, 699, 11, 664, 973, 604, 542, 118, 131, 716, 79, 526, 935, 406, 258, 875, 464, 33, 758, 653, 577, 561, 986, 722, 605, 822, 62, 17, 675, 255, 962, 727, 461, 163, 896, 186, 903, 121, 522, 104, 44, 956, 354, 361, 994, 620, 59, 209, 845, 702, 680, 959, 601, 278, 513, 390, 436, 170, 368, 158, 217, 89, 48, 825, 469, 241, 474, 934, 72, 294, 764, 684, 126, 296, 661, 290, 236, 992, 98, 593, 208, 656, 135, 869, 499, 905, 165, 557, 888, 999, 471, 977, 970, 364, 701, 305, 287, 521, 900, 922, 108, 456, 312, 568, 776, 92, 663, 22, 53, 488, 711, 242, 777, 375, 254, 913, 502, 570, 221, 441, 590, 229, 216, 774, 638, 505, 322, 555, 379, 201, 655, 938, 710, 849, 27, 30, 434, 850, 291, 654, 828, 359, 960, 185, 164, 569, 304, 534, 190, 685, 356, 335, 802, 417, 282, 872, 989, 580, 10, 796, 785, 226, 57, 66, 533, 124, 767, 591, 179, 910, 250, 156, 703, 565, 485, 329, 239, 430, 478, 31, 816, 871, 351, 625, 416, 762, 866, 690, 696, 86, 408, 260, 55, 82, 6, 197, 122, 719, 125, 995, 552, 45, 494, 276, 237, 679, 964, 138, 713, 589, 787, 398, 161, 668, 460, 365, 698, 559, 830, 50, 613, 771, 766, 298, 332, 706, 636, 920, 404, 715, 300, 688, 889, 184, 735, 401, 140, 353, 778, 308, 39, 550, 162, 203, 879, 342, 320, 608, 273, 182, 670, 957, 757, 198, 142, 153, 855, 642, 904, 19, 482, 619, 52, 497, 466, 615, 958, 423, 858, 410, 492, 984, 274, 189, 616, 574, 110, 333, 951, 575, 132, 775, 424, 271, 925, 665, 754, 498, 765, 617, 520, 64, 674, 264, 115, 286, 421, 588, 129, 25, 694, 607, 338, 330, 955, 736, 641, 846, 459, 563, 687, 501, 314, 397, 65, 682, 8, 310, 97, 865, 817, 402, 297, 245, 705, 4, 841, 272, 856, 975, 210, 878, 94, 844, 874, 480, 937, 609, 599, 85, 370, 67, 117, 836, 729, 712, 797, 130, 517, 407, 838, 428, 91, 773, 317, 443, 511, 936, 953, 235, 490, 514, 318, 562, 927, 717, 892, 532, 524, 692, 628, 109, 890, 465, 458, 720, 755, 225, 832, 175, 586, 493, 80, 972,819, 240, 723, 954, 183, 988, 556, 632, 893, 137, 909, 378, 396, 435, 14, 409, 540, 804, 952, 583, 621, 246, 795, 783, 344, 413, 660, 279, 2, 894, 630, 58, 154, 204, 120, 915, 412, 805, 106, 748, 824, 662, 328, 772, 231, 405, 188, 230, 917, 827, 829, 389, 382, 911, 519, 666, 270, 504, 12, 538, 739, 633, 966, 9, 939, 307, 16, 36, 263, 993, 202, 895, 265, 77, 982, 388, 205, 476, 868, 376, 220, 648, 43, 998, 876, 673, 222, 974, 635, 512, 437, 400, 919, 148, 991, 794, 969, 864, 862, 343, 311, 581, 996, 652, 218, 447, 373, 815, 518, 5, 861, 1, 798, 420, 782, 28, 737, 143, 763, 940, 451]


def heap_time():
    SETUP_CODE = '''
from __main__ import heapSort
'''
    TEST_CODE = '''
nlist = [94, 58, 99, 6, 15, 67, 49, 63, 22, 84, 53, 88, 13, 14, 3, 91, 56, 78, 43, 19, 95, 97, 85, 36, 41, 9, 29, 7, 51, 11, 68, 20, 21, 38, 75, 79, 89, 5, 62, 40, 74, 55, 64, 87, 47, 70, 52, 76, 50,
         82, 60, 27, 34, 72, 32, 80, 45, 26, 44, 39, 66, 2, 73, 31, 12, 10, 1, 17, 16, 18, 90, 24, 42, 83, 71, 86, 48, 59, 93, 65, 46, 57, 8, 25, 37, 96, 4, 28, 54, 61, 81, 23, 77, 33, 92, 30, 69, 35, 98, 100]
'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=5,
                          number=10000)
    print(times)
    print('Heap time: {}'.format(min(times)))


if __name__ == "__main__":
    heap_time()
    n = len(nlist)
    print(nlist)
