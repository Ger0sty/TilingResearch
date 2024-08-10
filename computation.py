from collections import deque
import numpy as np
import math

class Node:
    def __init__(self, row, label): 
        self.label = label
        self.row = row
        self.adj_list = []
    
    def GetChildren(self):
        return self.adj_list
    
    def GetLabel(self):
        return self.label
    
    def AddChild(self, node):
        self.adj_list.append(node)

    def AddChildren(self, list):
        for item in list:
            self.AddChild(item)

    def GetAdjList(self):
        return self.adj_list

class Tree:
    def __init__(self, type, n, m):
        self.type = type
        self.code_list = []
        self.node_counter = 1
        self.n = n
        self.m = m
        self.root = Node(0, "")

        if (type == "a"):
            if (self.n == 1):
                node_1_0 = Node(1, "0")
                node_1_5 = Node(1, "5")
                node_1_7 = Node(1, "7")
                self.root.AddChildren([node_1_0, node_1_5, node_1_7])
            else: 
                node_1_0 = Node(1, "0")
                node_1_1 = Node(1, "1")
                node_1_5 = Node(1, "5")
                node_1_7 = Node(1, "7")
                self.root.AddChildren([node_1_0, node_1_1, node_1_5, node_1_7])
                queue = deque([node_1_0, node_1_1, node_1_5, node_1_7])
                for i in range ((n - 2) // 2):
                    node_00 = Node(i + 2, "00")
                    node_01 = Node(i + 2, "01")
                    node_05 = Node(i + 2, "05")
                    node_07 = Node(i + 2, "07")
                    node_20 = Node(i + 2, "20")
                    node_43 = Node(i + 2, "43")
                    node_60 = Node(i + 2, "60")
                    node_80 = Node(i + 2, "80")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_00, node_01, node_05, node_07, node_43, node_60, node_80])
                        elif (current_last_digit == "1"):
                            current_node.AddChild(node_20)
                        else:
                            current_node.AddChildren([node_00, node_01, node_05, node_07])
                    queue.append(node_00)
                    queue.append(node_01)
                    queue.append(node_05)
                    queue.append(node_07)
                    queue.append(node_20)
                    queue.append(node_43)
                    queue.append(node_60)
                    queue.append(node_80)
                if ((n != 1) & (n % 2 == 1)):
                    node_end_00 = Node((n + 1) // 2, "00")
                    node_end_05 = Node((n + 1) // 2, "05")
                    node_end_07 = Node((n + 1) // 2, "07")
                    node_end_20 = Node((n + 1) // 2, "20")
                    node_end_43 = Node((n + 1) // 2, "43")
                    node_end_60 = Node((n + 1) // 2, "60")
                    node_end_80 = Node((n + 1) // 2, "80")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_end_00, node_end_05, node_end_07, node_end_43, node_end_60, node_end_80])
                        elif (current_last_digit == "1"):
                            current_node.AddChild(node_end_20)
                        else:
                            current_node.AddChildren([node_end_00, node_end_05, node_end_07])
                elif (n != 1):    
                    node_0 = Node(n // 2, "0")
                    node_2 = Node(n // 2, "2")
                    node_6 = Node(n // 2, "6")
                    node_8 = Node(n // 2, "8")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_0, node_6, node_8])
                        elif (current_last_digit == "1"):
                            current_node.AddChild(node_2)
                        else:
                            current_node.AddChild(node_0)
        else:
            if (self.n == 1):
                node_1_0 = Node(1, "0")
                node_1_6 = Node(1, "6")
                node_1_8 = Node(1, "8")
                self.root.AddChildren([node_1_0, node_1_6, node_1_8])
            else:
                node_1_0 = Node(1, "0")
                node_1_4 = Node(1, "4")
                node_1_6 = Node(1, "6")
                node_1_8 = Node(1, "8")
                self.root.AddChildren([node_1_0, node_1_4, node_1_6, node_1_8])
                queue = deque([node_1_0, node_1_4, node_1_6, node_1_8])
                for i in range ((n - 2) // 2):
                    node_00 = Node(i + 2, "00")
                    node_04 = Node(i + 2, "04")
                    node_06 = Node(i + 2, "06")
                    node_08 = Node(i + 2, "08")
                    node_12 = Node(i + 2, "12")
                    node_30 = Node(i + 2, "30")
                    node_50 = Node(i + 2, "50")
                    node_70 = Node(i + 2, "70")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_00, node_04, node_06, node_08, node_12, node_50, node_70])
                        elif (current_last_digit == "4"):
                            current_node.AddChild(node_30)
                        else:
                            current_node.AddChildren([node_00, node_04, node_06, node_08])
                    queue.append(node_00)
                    queue.append(node_04)
                    queue.append(node_06)
                    queue.append(node_08)
                    queue.append(node_12)
                    queue.append(node_30)
                    queue.append(node_50)
                    queue.append(node_70)
                if ((n != 1) & (n % 2 == 1)):
                    node_end_00 = Node((n + 1) // 2, "00")
                    node_end_06 = Node((n + 1) // 2, "06")
                    node_end_08 = Node((n + 1) // 2, "08")
                    node_end_12 = Node((n + 1) // 2, "12")
                    node_end_30 = Node((n + 1) // 2, "30")
                    node_end_50 = Node((n + 1) // 2, "50")
                    node_end_70 = Node((n + 1) // 2, "70")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_end_00, node_end_06, node_end_08, node_end_12, node_end_50, node_end_70])
                        elif (current_last_digit == "4"):
                            current_node.AddChild(node_end_30)
                        else:
                            current_node.AddChildren([node_end_00, node_end_06, node_end_08])
                elif (n != 1):    
                    node_0 = Node(n // 2, "0")
                    node_3 = Node(n // 2, "3")
                    node_5 = Node(n // 2, "5")
                    node_7 = Node(n // 2, "7")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_0, node_5, node_7])
                        elif (current_last_digit == "4"):
                            current_node.AddChild(node_3)
                        else:
                            current_node.AddChild(node_0)
        
    
    def ProcessNode(self, current_node, current_list, current_string):
        children = current_node.GetChildren()
        current_string = current_string + current_node.GetLabel()
        if (len(children) == 0):
            current_list.append(current_string)
        else:
            for child in children:
                self.ProcessNode(child, current_list, current_string)
                
    
    def GetCodes(self):
        current_string = ""
        self.ProcessNode(self.root, self.code_list, current_string)
        return self.code_list

    def GetRoot(self):
        return self.root
    
    def GetType(self):
        return self.type

    def GetList(self):
        return self.code_list
    
    def GetN(self):
        return self.n
    
    def GetM(self):
        return self.m
    

class Interface:
    def __init__(self, n, m, prime_parity = "NotPrime"):
        self.n = n
        self.m = m
        self.prime_parity = prime_parity
        self.a_tree = Tree("a", n, m)
        self.aprime_tree = Tree("a\'", n, m)
        self.root_v = Node(0, "")
        self.root_w = Node(0, "")
        

        if (self.prime_parity == "Prime"):
            if (self.n == 1):
                node_1_7 = Node(1, "7")
                self.root_v.AddChild(node_1_7)
            else:
                node_1_1 = Node(1, "1")
                node_1_7 = Node(1, "7")
                self.root_v.AddChildren([node_1_1, node_1_7])
                queue = deque([node_1_1, node_1_7])
                for i in range ((self.n - 2) // 2):
                    node_01 = Node(i + 2, "01")
                    node_07 = Node(i + 2, "07")
                    node_20 = Node(i + 2, "20")
                    node_43 = Node(i + 2, "43")
                    node_60 = Node(i + 2, "60")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_01, node_07, node_43, node_60])
                        elif (current_last_digit == "1"):
                            current_node.AddChild(node_20)
                        else:
                            current_node.AddChildren([node_01, node_07])
                    queue.append(node_01)
                    queue.append(node_07)
                    queue.append(node_20)
                    queue.append(node_43)
                    queue.append(node_60)
                if (self.n % 2 == 1):
                    node_end_07 = Node((self.n + 1) // 2, "07")
                    node_end_20 = Node((self.n + 1) // 2, "20")
                    node_end_43 = Node((self.n + 1) // 2, "43")
                    node_end_60 = Node((self.n + 1) // 2, "60")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_end_07, node_end_43, node_end_60])
                        elif (current_last_digit == "1"):
                            current_node.AddChild(node_end_20)
                        else:
                            current_node.AddChild(node_end_07)
                else:    
                    node_2 = Node(self.n // 2, "2")
                    node_6 = Node(self.n // 2, "6")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChild(node_6)
                        elif (current_last_digit == "1"):
                            current_node.AddChild(node_2)
        else:
            if (self.n == 1):
                node_1_6 = Node(1, "6")
                self.root_v.AddChild(node_1_6)
            else:
                node_1_0 = Node(1, "0")
                node_1_4 = Node(1, "4")
                node_1_6 = Node(1, "6")
                self.root_v.AddChildren([node_1_0, node_1_4, node_1_6])
                queue = deque([node_1_0, node_1_4, node_1_6])
                for i in range ((self.n - 2) // 2):
                    node_00 = Node(i + 2, "00")
                    node_04 = Node(i + 2, "04")
                    node_06 = Node(i + 2, "06")
                    node_12 = Node(i + 2, "12")
                    node_30 = Node(i + 2, "30")
                    node_70 = Node(i + 2, "70")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_12, node_70])
                        elif (current_last_digit == "4"):
                            current_node.AddChild(node_30)
                        else:
                            current_node.AddChildren([node_00, node_04, node_06])
                    queue.append(node_00)
                    queue.append(node_04)
                    queue.append(node_06)
                    queue.append(node_12)
                    queue.append(node_30)
                    queue.append(node_70)
                if (self.n % 2 == 1):
                    node_end_06 = Node((self.n + 1) // 2, "06")
                    node_end_12 = Node((self.n + 1) // 2, "12")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChild(node_end_12)
                        elif (current_last_digit != "4"):
                            current_node.AddChild(node_end_06)
                else:    
                    node_0 = Node(self.n // 2, "0")
                    node_3 = Node(self.n // 2, "3")
                    node_7 = Node(self.n // 2, "7")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChild(node_7)
                        elif (current_last_digit == "4"):
                            current_node.AddChild(node_3)
                        else:
                            current_node.AddChild(node_0)

        if (((self.prime_parity == "Prime") & (m % 2 == 0)) | ((self.prime_parity != "Prime") & (m % 2 == 1))):
            if (self.n == 1):
                node_1_8 = Node(1, "8")
                self.root_w.AddChild(node_1_8)
            else:
                node_1_4 = Node(1, "4")
                node_1_8 = Node(1, "8")
                self.root_w.AddChildren([node_1_4, node_1_8])
                queue = deque([node_1_4, node_1_8])
                for i in range ((self.n - 2) // 2):
                    node_04 = Node(i + 2, "04")
                    node_08 = Node(i + 2, "08")
                    node_12 = Node(i + 2, "12")
                    node_30 = Node(i + 2, "30")
                    node_50 = Node(i + 2, "50")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_04, node_08, node_12, node_50])
                        elif (current_last_digit == "4"):
                            current_node.AddChild(node_30)
                        else:
                            current_node.AddChildren([node_04, node_08])
                    queue.append(node_04)
                    queue.append(node_08)
                    queue.append(node_12)
                    queue.append(node_30)
                    queue.append(node_50)
                if (self.n % 2 == 1):
                    node_end_08 = Node((self.n + 1) // 2, "08")
                    node_end_12 = Node((self.n + 1) // 2, "12")
                    node_end_30 = Node((self.n + 1) // 2, "30")
                    node_end_50 = Node((self.n + 1) // 2, "50")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_end_08, node_end_12, node_end_50])
                        elif (current_last_digit == "4"):
                            current_node.AddChild(node_end_30)
                        else:
                            current_node.AddChild(node_end_08)
                else:    
                    node_3 = Node(self.n // 2, "3")
                    node_5 = Node(self.n // 2, "5")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChild(node_5)
                        elif (current_last_digit == "4"):
                            current_node.AddChild(node_3)
        else:
            if (self.n == 1):
                node_1_5 = Node(1, "5")
                self.root_w.AddChild(node_1_5)
            else:
                node_1_0 = Node(1, "0")
                node_1_1 = Node(1, "1")
                node_1_5 = Node(1, "5")
                self.root_w.AddChildren([node_1_0, node_1_1, node_1_5])
                queue = deque([node_1_0, node_1_1, node_1_5])
                for i in range ((self.n - 2) // 2):
                    node_00 = Node(i + 2, "00")
                    node_01 = Node(i + 2, "01")
                    node_05 = Node(i + 2, "05")
                    node_20 = Node(i + 2, "20")
                    node_43 = Node(i + 2, "43")
                    node_80 = Node(i + 2, "80")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChildren([node_43, node_80])
                        elif (current_last_digit == "1"):
                            current_node.AddChild(node_20)
                        else:
                            current_node.AddChildren([node_00, node_01, node_05])
                    queue.append(node_00)
                    queue.append(node_01)
                    queue.append(node_05)
                    queue.append(node_20)
                    queue.append(node_43)
                    queue.append(node_80)
                if (self.n % 2 == 1):
                    node_end_05 = Node((self.n + 1) // 2, "05")
                    node_end_43 = Node((self.n + 1) // 2, "43")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChild(node_end_43)
                        elif (current_last_digit != "1"):
                            current_node.AddChild(node_end_05)
                else:    
                    node_0 = Node(self.n // 2, "0")
                    node_2 = Node(self.n // 2, "2")
                    node_8 = Node(self.n // 2, "8")
                    while (len(queue) != 0):
                        current_node = queue.popleft()
                        current_last_digit = current_node.GetLabel()[-1]
                        if (current_last_digit == "0"):
                            current_node.AddChild(node_8)
                        elif (current_last_digit == "1"):
                            current_node.AddChild(node_2)
                        else:
                            current_node.AddChild(node_0)

        #iterate through tree_v and tree_w
        self.v_list = []
        self.w_list = []
        self.MakeCodes(self.root_v, self.v_list)
        self.MakeCodes(self.root_w, self.w_list)
        self.a_codes = self.MakeACodes()
        self.aprime_codes = self.MakeAPrimeCodes()
        self.v_vector = self.MakeV()
        self.w_vector = self.MakeW()
        self.t_matrix = self.MakeT()
        self.ttilde_matrix = self.MakeTtilde()
        self.matrix_composition = self.MakeMatrixComposition()
                        
    def GetN(self):
        return self.n
    
    def GetM(self):
        return self.m
    
    def MakeACodes(self):
        return self.a_tree.GetCodes()
    
    def MakeAPrimeCodes(self):
        return self.aprime_tree.GetCodes()
    
    def GetACodes(self):
        return self.a_codes
    
    def GetAPrimeCodes(self):
        return self.aprime_codes
    
    def GetVCodes(self):
        return self.v_list
    
    def GetWCodes(self):
        return self.w_list
    
    def ProcessNode(self, current_node, current_list, current_string):
        children = current_node.GetChildren()
        current_string = current_string + current_node.GetLabel()
        if (len(children) == 0):
            if (len(current_string) == self.n):
                current_list.append(current_string)
        else:
            for child in children:
                self.ProcessNode(child, current_list, current_string)
                
    
    def MakeCodes(self, root, list):
        current_string = ""
        self.ProcessNode(root, list, current_string)
    
    def MakeV(self):
        v_codes = self.GetVCodes()
        v_matrix_list = []
        temp_codes = self.GetAPrimeCodes()
        if (self.prime_parity == "Prime"):
            temp_codes = self.GetACodes()
        for item in temp_codes:
            if (item in v_codes):
                v_matrix_list.append(1)
            else:
                v_matrix_list.append(0)

        return np.array(v_matrix_list)
    
    def MakeW(self):
        w_codes = self.GetWCodes()
        w_matrix_list = []
        temp_codes = self.GetACodes()
        if (((self.prime_parity == "Prime") & (self.GetM() % 2 == 0)) | ((self.prime_parity != "Prime") & (self.GetM() % 2 == 1))):
            temp_codes = self.GetAPrimeCodes()
        for item in temp_codes:
            if (item in w_codes):
                w_matrix_list.append(1)
            else:
                w_matrix_list.append(0)

        return np.array(w_matrix_list)
    
    def MakeT(self):
        a_codes = self.GetACodes()
        aprime_codes = self.GetAPrimeCodes()
        array_of_arrays = []
        for i in range (len(a_codes)):
            temp_array = []
            a_code = a_codes[i]
            for j in range (len(aprime_codes)):
                aprime_code = aprime_codes[j]
                if (self.CheckTCodes(a_code, aprime_code) == True):
                    temp_array.append(1)
                else:
                    temp_array.append(0)
            array_of_arrays.append(temp_array)

        return np.array(array_of_arrays)
    
    def CheckTCodes(self, a_code, aprime_code):
        for i in range (self.GetN() // 2):
            if (a_code[2 * i : 2 * i + 2] == "00"):
                if ((aprime_code[2 * i : 2 * i + 2] != "01") & (aprime_code[2 * i : 2 * i + 2] != "07") & (aprime_code[2 * i : 2 * i + 2] != "20") & (aprime_code[2 * i : 2 * i + 2] != "43") & (aprime_code[2 * i : 2 * i + 2] != "60")):
                    return False
            elif (a_code[2 * i : 2 * i + 2] == "06"):
                if (aprime_code[2 * i : 2 * i + 2] != "05"):
                    return False
            elif (a_code[2 * i : 2 * i + 2] == "70"):
                if (aprime_code[2 * i : 2 * i + 2] != "80"):
                    return False
            else:
                if (aprime_code[2 * i : 2 * i + 2] != "00"):
                    return False
        if (self.GetN() % 2 == 1):
            if (a_code[-1] == "0"):
                if ((aprime_code[-1] != "2") & (aprime_code[-1] != "6")):
                    return False
            elif (a_code[-1] == "7"):
                if (aprime_code[-1] != "8"):
                    return False
            else:
                if (aprime_code[-1] != "0"):
                    return False
        return True
        
    def MakeTtilde(self):
        a_codes = self.GetACodes()
        aprime_codes = self.GetAPrimeCodes()
        array_of_arrays = []
        for i in range (len(aprime_codes)):
            temp_array = []
            aprime_code = aprime_codes[i]
            for j in range (len(a_codes)):
                a_code = a_codes[j]
                if (self.CheckTPrimeCodes(a_code, aprime_code) == True):
                    temp_array.append(1)
                else:
                    temp_array.append(0)
            array_of_arrays.append(temp_array)

        return np.array(array_of_arrays)
    
    def CheckTPrimeCodes(self, a_code, aprime_code):
        if (aprime_code[0:1] == "0"):
            if ((a_code[0:1] != "1") & (a_code[0:1] != "7")):
                return False
        elif (aprime_code[0:1] == "6"):
            if (a_code[0:1] != "5"):
                return False
        else:
            if (a_code[0:1] != "0"):
                return False
            
        for i in range (math.ceil((self.GetN() - 2) / 2)):
            if (aprime_code[2 * i + 1 : 2 * i + 3] == "00"):
                if ((a_code[2 * i + 1 : 2 * i + 3] != "01") & (a_code[2 * i + 1 : 2 * i + 3] != "07") & (a_code[2 * i + 1 : 2 * i + 3] != "20") & (a_code[2 * i + 1 : 2 * i + 3] != "43") & (a_code[2 * i + 1 : 2 * i + 3] != "60")):
                    return False
            elif (aprime_code[2 * i + 1 : 2 * i + 3] == "06"):
                if (a_code[2 * i + 1 : 2 * i + 3] != "05"):
                    return False
            elif (aprime_code[2 * i + 1 : 2 * i + 3] == "70"):
                if (a_code[2 * i + 1 : 2 * i + 3] != "80"):
                    return False
            else:
                if (a_code[2 * i + 1 : 2 * i + 3] != "00"):
                    return False
        if (self.GetN() % 2 == 0):
            if (aprime_code[-1] == "0"):
                if ((a_code[-1] != "2") & (a_code[-1] != "6")):
                    return False
            elif (aprime_code[-1] == "7"):
                if (a_code[-1] != "8"):
                    return False
            else:
                if (a_code[-1] != "0"):
                    return False
        return True

    def GetPrimeParity(self):
        return self.prime_parity
    
    def GetV(self):
        return self.v_vector
    
    def GetW(self):
        return self.w_vector
    
    def GetT(self):
        return self.t_matrix
    
    def GetTtilde(self):
        return self.ttilde_matrix
    
    def MakeMatrixComposition(self):
        t_matrix = self.GetT()
        ttilde_matrix = self.GetTtilde()
        if (self.GetPrimeParity() == "Prime"):
            temp_matrix = ttilde_matrix @ t_matrix
            if (self.GetM() % 2 == 0):
                return np.matmul(t_matrix, np.linalg.matrix_power(temp_matrix, (self.GetM() - 2) // 2))
            else:
                return np.linalg.matrix_power(temp_matrix, (self.GetM() - 1) // 2)
        else:
            temp_matrix = t_matrix @ ttilde_matrix
            if (self.GetM() % 2 == 0):
                return np.matmul(ttilde_matrix, np.linalg.matrix_power(temp_matrix, (self.GetM() - 2) // 2))
            else:
                return np.linalg.matrix_power(temp_matrix, (self.GetM() - 1) // 2)
            
    def GetMatrixComposition(self):
        return self.matrix_composition
    
    def GetNumberTilings(self):
        return np.dot(self.GetW() ,np.dot(self.GetMatrixComposition(), self.GetV()))
    
    def GetLambdaMax(self):
        eigenvalues = np.linalg.eig(self.GetMatrixComposition())[0]
        return max(eigenvalues)


interface = Interface(8, 8, "Prime")
#print(interface.GetACodes())
#print(interface.GetAPrimeCodes())
#print(interface.GetT())
#print(interface.GetTtilde())
#print(interface.GetW())
#print(interface.GetV())
#print(interface.GetMatrixComposition())
print(interface.GetNumberTilings())
print(interface.GetLambdaMax())