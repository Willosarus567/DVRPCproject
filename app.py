##from flask import FLASK, render_template, url_for, flash, redirect, request, abort 
import psycopg2

connection = psycopg2.connect(user = "",
                             password = "",
                             host = "",
                             port = "",
                             database = "") 
print("Database successfully opened")   

cursor = connection.cursor()
cursor.execute('''INSERT INTO weathersummaries2018 (RECORDNUM, PRCP, TAVG, TMAX, TMIN) 
                VALUES(1, 0, 13, 20, 6),
                (2, 0, 18, 24, 12),
                (3, 0, 22, 33, 13),
                (4, 0, 22, 33, 13),
                      (5, 0.25, 25, 29, 16),
                      (6, 0, 16, 17, 11),
                      (7, 0, 12, 16, 7),
                      (8, 0, 12, 19, 4),
                      (9, 0.06, 22, 33, 16),
                      (10, 0, 34, 45, 25),
                      (11, 0, 35, 44, 24),
                      (12, 0, 45, 59, 39),
                      (13, 1.42, 59, 64, 53),
                      (14, 0.05, 46, 61, 19),
                      (15, 0, 20, 27, 14),
                      (16, 0, 24, 34, 17),
                      (17, 0, 34, 45, 29),
                      (18, 0.07, 33, 40, 21),
                      (19, 0, 25, 36, 18),
                      (20, 0, 33, 46, 23),
                      (21, 0, 41, 57, 29),
                      (22, 0, 41, 53, 30),
                      (23, 0, 48, 62, 42),
                      (24, 0.46, 54, 62, 43),
                      (25, 0, 44, 45, 35),
                      (26, 0, 33, 37, 27),
                      (27, 0, 32, 42, 24),
                      (28, 0, 40, 59, 27),
                      (29, 0.4, 52, 56, 46),
                      (30, 0, 44, 47, 38),
                      (31, 0.14, 35, 38, 22),
                      (32, 0, 24, 33, 18),
                      (33, 0.03, 37, 47, 32),
                      (34, 0.17, 34, 40, 20),
                      (35, 0, 23, 31, 17),
                      (36, 0.86, 33, 38, 30),
                      (37, 0, 34, 38, 25),
                      (38, 0, 31, 38, 25),
                      (39, 0.82, 34, 50, 25),
                      (40, 0, 33, 36, 27),
                      (41, 0, 30, 39, 23),
                      (42, 0.41, 39, 50, 32),
                      (43, 1.68, 53, 65, 47),
                      (44, 0, 53, 61, 35),
                      (45, 0, 35, 43, 27),
                      (46, 0.05, 40, 52, 35),
                      (47, 0.25, 49, 61, 42),
                      (48, 0.33, 55, 60, 38),
                      (49, 0.4, 37, 42, 28),
                      (50, 0, 37, 46, 33),
                      (51, 0, 41, 49, 33),
                      (52, 0, 54, 72, 47),
                      (53, 0.01, 64, 77, 51),
                      (54, 0.06, 53, 58, 38),
                      (55, 0.23, 40, 45, 37),
                      (56, 0.06, 45, 50, 44),
                      (57, 0.66, 46, 48, 43),
                      (58, 0, 47, 51, 37),
                      (59, 0, 45, 56, 33),
                      (60, 0, 48, 61, 38),
                      (61, 0.56, 51, 58, 42),
                      (62, 0.86, 40, 45, 32),
                      (63, 0, 38, 46, 35),
                      (64, 0, 40, 48, 31),
                      (65, 0, 36, 47, 30),
                      (66, 0.23, 38, 48, 29),
                      (67, 1.28, 35, 36, 32),
                      (68, 0, 36, 40, 31),
                      (69, 0, 35, 42, 30),
                      (70, 0, 36, 44, 29),
                      (71, 0, 36, 46, 28),
                      (72, 0.06, 36, 43, 29),
                      (73, 0.03, 36, 42, 32),
                      (74, 0, 35, 41, 29),
                      (75, 0, 37, 46, 32),
                      (76, 0, 37, 42, 31),
                      (77, 0, 37, 48, 28),
                      (78, 0, 40, 50, 31),
                      (79, 0, 42, 52, 33),
                      (80, 0.4, 34, 35, 29),
                      (81, 1.06, 33, 36, 31),
                      (82, 0, 37, 48, 33),
                      (83, 0, 41, 48, 35),
                      (84, 0, 41, 49, 33),
                      (85, 0, 39, 47, 32),
                      (86, 0, 39, 49, 30),
                      (87, 0, 38, 47, 31),
                      (88, 0.02, 43, 50, 38),
                      (89, 0.08, 54, 74, 46),
                      (90, 0.16, 60, 70, 44),
                      (91, 0, 47, 57, 38),
                      (92, 0, 51, 62, 44),
                      (93, 0.12, 43, 49, 34),
                      (94, 0.08, 41, 47, 37),
                      (95, 0.06, 50, 67, 39),
                      (96, 0, 41, 47, 36),
                      (97, 0.03, 47, 64, 39),
                      (98, 0, 48, 58, 39),
                      (99, 0, 40, 46, 31),
                      (100, 0, 38, 45, 32),
                      (101, 0, 42, 50, 35),
                      (102, 0, 44, 53, 29),
                      (103, 0, 53, 71, 42),
                      (104, 0, 68, 84, 59),
                      (105, 0, 72, 83, 48),
                      (106, 0.56, 47, 49, 40),
                      (107, 2.28, 50, 66, 41),
                      (108, 0, 44, 46, 38),
                      (109, 0, 44, 56, 36),
                      (110, 0, 49, 51, 41),
                      (111, 0, 44, 54, 36),
                      (112, 0, 48, 60, 36),
                      (113, 0, 54, 66, 40),
                      (114, 0, 56, 70, 43),
                      (115, 0.11, 54, 64, 41),
                      (116, 0.16, 58, 68, 53),
                      (117, 0, 60, 67, 51),
                      (118, 0.25, 57, 59, 50),
                      (119, 0.14, 58, 74, 46),
                      (120, 0.15, 52, 56, 45),
                      (121, 0, 52, 68, 44),
                      (122, 0, 60, 79, 43),
                      (123, 0, 72, 88, 55),
                      (124, 0, 77, 91, 63),
                      (125, 0, 77, 89, 65),
                      (126, 0, 71, 75, 61),
                      (127, 0, 64, 70, 58),
                      (128, 0, 63, 75, 55),
                      (129, 0, 64, 77, 51),
                      (130, 0, 65, 79, 52),
                      (131, 0, 63, 80, 49),
                      (132, 0, 70, 77, 59),
                      (133, 1.49, 63, 72, 53),
                      (134, 0.49, 56, 57, 53),
                      (135, 0, 59, 75, 53),
                      (136, 0.55, 73, 89, 63),
                      (137, 0.25, 65, 68, 58),
                      (138, 0.36, 61, 68, 57),
                      (139, 0.02, 63, 65, 51),
                      (140, 0.74, 55, 69, 50),
                      (141, 0.01, 73, 84, 68),
                      (142, 0, 71, 79, 61),
                      (143, 0.35, 63, 66, 59),
                      (144, 0, 69, 80, 61),
                      (145, 0, 73, 84, 63),
                      (146, 0, 73, 86, 61),
                      (147, 0.85, 78, 89, 69),
                      (148, 0.08, 71, 77, 58),
                      (149, 0, 61, 71, 57),
                      (150, 0, 70, 82, 63),
                      (151, 0, 72, 81, 63),
                      (152, 0.02, 69, 82, 62),
                      (153, 0.06, 76, 85, 70),
                      (154, 0.25, 78, 87, 71),
                      (155, 0.61, 65, 71, 53),
                      (156, 0.24, 60, 74, 52),
                      (157, 0, 69, 80, 57),
                      (158, 0, 66, 72, 59),
                      (159, 0, 67, 76, 60),
                      (160, 0, 70, 82, 59),
                      (161, 0.01, 74, 85, 66),
                      (162, 0.77, 69, 73, 56),
                      (163, 0.69, 61, 70, 55),
                      (164, 0, 64, 76, 53),
                      (165, 0, 71, 81, 65),
                      (166, 0, 78, 86, 70),
                      (167, 0, 73, 80, 63),
                      (168, 0, 73, 84, 59),
                      (169, 0, 78, 90, 65),
                      (170, 0, 80, 93, 69),
                      (171, 0, 83, 88, 74),
                      (172, 0.29, 78, 86, 69),
                      (173, 0, 75, 82, 70),
                      (174, 0.16, 71, 73, 63),
                      (175, 0.01, 66, 73, 63),
                      (176, 0, 76, 89, 68),
                      (177, 0, 75, 82, 67),
                      (178, 0, 72, 81, 61),
                      (179, 0, 69, 74, 63),
                      (180, 0.25, 78, 88, 72),
                      (181, 0, 82, 91, 73),
                      (182, 0, 84, 95, 71),
                      (183, 0, 86, 95, 76),
                      (184, 0, 86, 97, 73),
                      (185, 0.01, 85, 98, 75),
                      (186, 0, 81, 94, 74),
                      (187, 0, 83, 94, 76),
                      (188, 0.1, 80, 85, 70),
                      (189, 0, 73, 79, 63),
                      (190, 0, 72, 85, 60),
                      (191, 0, 75, 87, 63),
                      (192, 0, 80, 93, 68),
                      (193, 0, 84, 90, 74),
                      (194, 0.15, 78, 88, 70),
                      (195, 0, 76, 88, 68),
                      (196, 0, 78, 90, 67),
                      (197, 0.38, 77, 83, 70),
                      (198, 0, 82, 95, 73),
                      (199, 0.07, 82, 94, 74),
                      (200, 0, 77, 87, 70),
                      (201, 0, 76, 86, 64),
                      (202, 0, 76, 87, 65),
                      (203, 0.74, 70, 77, 65),
                      (204, 0.24, 74, 87, 69),
                      (205, 0, 80, 86, 77),
                      (206, 0.08, 80, 87, 76),
                      (207, 1.14, 77, 83, 72),
                      (208, 0, 77, 87, 71),
                      (209, 0.15, 80, 90, 71),
                      (210, 0, 76, 87, 70),
                      (211, 0, 77, 85, 69),
                      (212, 0, 75, 78, 67),
                      (213, 0, 74, 82, 68),
                      (214, 0.41, 79, 89, 73),
                      (215, 0.08, 81, 89, 74),
                      (216, 0.51, 77, 86, 72),
                      (217, 0.1, 78, 87, 72),
                      (218, 0, 82, 92, 73),
                      (219, 0, 83, 92, 75),
                      (220, 0.05, 82, 92, 75),
                      (221, 0.02, 81, 92, 73),
                      (222, 0.04, 81, 89, 74),
                      (223, 0, 82, 91, 72),
                      (224, 0.79, 78, 85, 70),
                      (225, 0, 76, 86, 71),
                      (226, 0.52, 77, 84, 71),
                      (227, 0.73, 74, 83, 68),
                      (228, 0, 79, 89, 72),
                      (229, 0, 81, 89, 73),
                      (230, 0, 82, 93, 74),
                      (231, 0.34, 80, 88, 73),
                      (232, 0.34, 72, 74, 66),
                      (233, 0, 70, 78, 66),
                      (234, 0.02, 73, 81, 69),
                      (235, 0.05, 77, 84, 71),
                      (236, 0, 73, 79, 67),
                      (237, 0, 74, 83, 63),
                      (238, 0, 72, 81, 63),
                      (239, 0, 75, 86, 65),
                      (240, 0, 80, 90, 73),
                      (241, 0, 84, 94, 75),
                      (242, 0, 85, 95, 76),
                      (243, 0, 84, 90, 78),
                      (244, 0.11,77, 79, 69),
                      (245, 0.08, 72, 79, 69),
                      (246, 0, 76, 87, 70),
                      (247, 0, 81, 93, 74),
                      (248, 0, 84, 93, 74),
                      (249, 0, 85, 95, 75),
                      (250, 0.01, 84, 95, 77),
                      (251, 4.54, 79, 87, 71),
                      (252, 0.63, 69, 72, 61),
                      (253, 1.84, 60, 61, 56),
                      (254, 0.23, 62, 71, 55),
                      (255, 0, 68, 77, 63),
                      (256, 0, 75, 85, 71),
                      (257, 0, 75, 78, 70),
                      (258, 0, 71, 76, 68),
                      (259, 0, 72, 81, 66),
                      (260, 0, 73, 86, 65),
                      (261, 0.01, 72, 80, 65),
                      (262, 0.26, 76, 82, 68),
                      (263, 0, 75, 84, 67),
                      (264, 0, 71, 76, 66),
                      (265, 0, 70, 76, 66),
                      (266, 0.01, 72, 78, 63),
                      (267, 0.7, 62, 63, 59),
                      (268, 0.05, 63, 68, 61),
                      (269, 0.36, 69, 80, 62),
                      (270, 0.14, 76, 85, 71),
                      (271, 0.02, 69, 72, 61),
                      (272, 0.88, 64, 70, 58),
                      (273, 0, 65, 79, 57),
                      (274, 0, 65, 74, 55),
                      (275, 0, 69, 80, 60),
                      (276, 0.34, 72, 82, 65),
                      (277, 0.34, 72, 82, 65),
                      (278, 0.01, 71, 78, 61),
                      (279, 0.18, 70, 84, 61),
                      (280, 0, 67, 74, 63),
                      (281, 0, 66, 70, 63),
                      (282, 0, 72, 78, 68),
                      (283, 0.03, 70, 72, 66),
                      (284, 0, 73, 81, 69),
                      (285, 0, 74, 83, 68),
                      (286, 0.73, 76, 83, 70),
                      (287, 0.36, 65, 71, 52),
                      (288, 0.07, 53, 57, 49),
                      (289, 0, 51, 57, 45),
                      (290, 0.1, 60, 69, 54),
                      (291, 0, 58, 61, 50),
                      (292, 0, 56, 65, 48),
                      (293, 0, 49, 53, 42),
                      (294, 0, 50, 61, 41),
                      (295, 0.07, 58, 65, 50),
                      (296, 0, 50, 51, 39),
                      (297, 0, 46, 55, 38),
                      (298, 0, 55, 67, 48),
                      (299, 0, 51, 55, 42),
                      (300, 0, 45, 53, 38),
                      (301, 0.31, 45, 49, 39),
                      (302, 0.87, 49, 52, 47),
                      (303, 0, 49, 55, 46),
                      (304, 0.01, 53, 57, 44),
                      (305, 0, 49, 60, 40),
                      (306, 0, 53, 69, 39),
                      (307, 0, 61, 72, 51),
                      (308, 0.37, 69, 72, 57),
                      (309, 0.27, 58, 59, 45),
                      (310, 0, 49, 58, 38),
                      (311, 0.55, 50, 55, 45),
                      (312, 1.65, 54, 63, 51),
                      (313, 0, 57, 63, 48),
                      (314, 0, 53, 58, 43),
                      (315, 0.75, 47, 51, 39),
                      (316, 0, 45, 49, 33),
                      (317, 0, 37, 47, 30),
                      (318, 0.23, 40, 49, 31),
                      (319, 1.04, 46, 50, 43),
                      (320, 0, 41, 44, 33),
                      (321, 0.98, 33, 38, 30),
                      (322, 0.26, 39, 45, 34),
                      (323, 0, 42, 48, 35),
                      (324, 0, 40, 48, 32),
                      (325, 0, 42, 51, 33),
                      (326, 0.02, 45, 50, 39),
                      (327, 0, 40, 48, 32),
                      (328, 0, 29, 33, 20),
                      (329, 0, 24, 33, 16),
                      (330, 2.01, 35, 49, 27),
                      (331, 0.01, 49, 58, 39),
                      (332, 0.89, 47, 53, 40),
                      (333, 0, 42, 43, 35),
                      (334, 0, 37, 40, 35),
                      (335, 0, 38, 46, 33),
                      (336, 0, 38, 44, 35),
                      (337, 0.07, 41, 49, 32),
                      (338, 0.55, 49, 58, 43),
                      (339, 0, 53, 57, 43),
                      (340, 0, 42, 45, 30),
                      (341, 0.03, 30, 33, 25),
                      (342, 0, 33, 39, 27),
                      (343, 0, 37, 40, 28),
                      (344, 0, 30, 38, 23),
                      (345, 0, 31, 35, 27),
                      (346, 0, 32, 40, 26),
                      (347, 0, 33, 41, 24),
                      (348, 0, 36, 44, 31),
                      (349, 0, 39, 49, 32),
                      (350, 0.11, 42, 51, 36),
                      (351, 0.44, 49, 51, 47),
                      (352, 1.01, 44, 47, 38),
                      (353, 0, 42, 49, 38),
                      (354, 0, 40, 42, 30),
                      (355, 0, 34, 44, 25),
                      (356, 0.56, 36, 59, 28),
                      (357, 1.16, 58, 65, 53),
                      (358, 0.09, 48, 55, 41),
                      (359, 0, 41, 45, 37),
                      (360, 0.02, 41, 45, 36),
                      (361, 0, 37, 42, 30),
                      (362, 0, 37, 45, 29),
                      (363, 0, 38, 48, 30),
                      (364, 1.67, 49, 60, 41),
                      (365, 0, 50, 53, 39),
                      (366, 0, 40, 45, 34),
                      (367, 0.67, 38, 50, 32)''');


   
connection.commit()
print("Table info created")
connection.close()
print("PostgreSQL connection is closed")






