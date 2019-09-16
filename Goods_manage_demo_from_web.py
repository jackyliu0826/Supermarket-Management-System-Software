����#�߼�������

����#��ɾ�����Ƕ�����Ʒ�Ĳ�������Ʒ��Ϣ����������ƺͼ۸񣬿��Խ���Ϣ��װ�������У��ɴ���������������Goods��Ȼ�������ɾ�Ȳ���Ӧ�����ڹ���ϵͳ�Ĺ��ܣ����Խ���ع��ܷ�װ��ShopManager�൱�С��ڽ���ϵͳʱ��Ӧ�����Ȳ鿴֮ǰ�Ƿ��д洢��Ϣ������Ҫ��ȡ�ļ�д�뵽�ڴ��У���ɾ��������ͨ�������Ϊ���������Կ���ѡ���ֵ�dict���ݽṹ��Ϊ�ڴ�洢������Ȼ����ɾ���Ƕ����ֵ�Ĳ�������ϵͳ�˳�ʱ���ڽ����ݸ���д�뵽�ļ��У���������޸��ļ��������ύ��

����#����ʵ�ִ��룺

����#���ȴ��������Ʒ�����Goods��

class Goods(object):
����def __init__(self,id,name,price):
����	self.id = id
����	self.name = name
����	self.price = price
����def __str__(self):
����	info = "���:%s\t��Ʒ����:%s\t\t�۸�:%d"%(self.id,self.name,self.price)
����	return info

#��������Ʒ�����ĺ����ŵ�ShopManager�൱�У����ܰ�������Ա�Լ���ͨ�û��ģ��ڵ�¼����з���ѡ��
class ShopManager(object):
	def __init__(self,path):
����	# path:��ʾ��ȡ�ļ���·�� shopdic����ʾ����ڴ������
����	self.path = path
����	self.shopdic = self.readFileToDic()
����def readFileToDic(self):
����# ��ȡ�ļ���д�뵽�ֵ���
����	f = open(self.path, 'r', encoding='utf-8')
����	clist = f.readlines()
����	f.close()
����	index = 0
����	shopdic = {}
����	while index < len(clist):
����		ctlist = clist[index].replace('\n', "").split("|")   # ��ÿһ�е��ַ������зָ��ŵ��µ��б���
����		good = Goods(ctlist[0],ctlist[1],int(ctlist[2]))   # ��ÿ�е����ݴ�ŵ�һ��������
����		shopdic[good.id] = good   # �������ŵ�������
����		index = index + 1
����	return shopdic
����def writeContentFile(self):      # ���ڴ浱�е���Ϣд�뵽�ļ�����
����	str1 = ''
����	for key in self.shopdic.keys():
����		good = self.shopdic[key]
����		ele = good.id+"|"+good.name+"|"+str(good.price)+"\n"
����		str1 = str1 + ele
����		f = open(self.path, 'w', encoding='utf-8')
����		f.write(str1)
����		f.close()
����def addGoods(self):
����	id = input("�����������Ʒ���:>")# �����Ʒ�ķ���
����	if self.shopdic.get(id):
����		print("��Ʒ����Ѵ��ڣ�������ѡ��!")
����		return
����	name = input("�����������Ʒ����:>")
����	price = int(input("�����������Ʒ�۸�:>"))
����	good = Goods(id,name,price)
����	self.shopdic[id] = good
����	print("��ӳɹ�!")
����def deleteGoods(self):
����	# ɾ����Ʒ�ķ���
����	id = input("������ɾ����Ʒ���:>")
����	if self.shopdic.get(id):
����		del self.shopdic[id]
����		print("ɾ���ɹ�!")
����	else:
����		print("��Ʒ��Ų�����!")
����def showGoods(self):
����	# չʾ������Ʒ��Ϣ
����	print("="*40)
����	for key in self.shopdic.keys():
����		good = self.shopdic[key]
����		print(good)
����	print("="*40)
����def adminWork(self):
	����info = """
	����==========��ӭ����ú�Ŷ�����̳�==========
	�������빦�ܱ�ţ�������ѡ�����¹��ܣ�
	�������롰1������ʾ��Ʒ����Ϣ
	�������롰2���������Ʒ����Ϣ
	�������롰3����ɾ����Ʒ����Ϣ
	�������롰4�����˳�ϵͳ����
	����==========================================
	����"""
����	print(info)
����	while True:
����		code = input("�����빦�ܱ��:>")
����	if code == "1":
����		self.showGoods()
����	elif code == "2":
����		self.addGoods()
����	elif code == "3":
����		self.deleteGoods()
����	elif code == "4":
����		print("��л����ʹ�ã������˳�ϵͳ!!")
����		self.writeContentFile()
����		break
	����else:
	����	print("��������������������!!")
����def userWork(self):
����	print(" ==============��ӭ����ú�Ŷ�����̳�==============")
����	print("���������ź͹�������ѡ����Ʒ��������Ϊn�����")
����	self.showGoods()
	����total = 0
	����while True:
	����	id = input("�����빺����Ʒ���:>")
	����	if id == "n":
	����		print("���ι�����Ʒ������%dԪ����л���Ĺ���!"%(total))
	����		break
	����	if self.shopdic.get(id):
	����		good = self.shopdic[id]
	����		num = int(input("�����빺������:>"))
	����		total = total+good.price*num
	����	else:����������ҽԺ https://yyk.familydoctor.com.cn/20612/
	����		print("������Ʒ���������˶Ժ���������!")
����def login(self):
	����# ��¼����
	����print("==========��ӭ��¼�ú�Ŷ�����̳�==========")
	����uname = input("�������û���:>")
	����password = input("����������:>")
	����if uname == "admin":
	����	if password == "123456":
	����		print("��ӭ����admin����Ա")
	����		self.adminWork()
	����	else:
	����		print("����Ա������󣬵�¼ʧ��!")
	����else:
	����	print("��ӭ�㣬%s�û�"%(uname))
	����	#ִ���û��Ĺ�����
	����	self.userWork()
	#������ǿ���main����У����õ�¼���������Զ�ѡ����ع��ܡ�
if __name__ == '__main__':
����shopManage = ShopManager("shop.txt")
����shopManage.login()