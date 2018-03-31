import unittest #单元测试库

from mydict import Dict #

class TestDict(unittest.TestCase): #注意命名方法

    def test_init(self): #注意命名方法
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1) #unittest.TestCase提供各种判断条件     
        self.assertEqual(d.b, 'test')#class.assertEqual 断言相等
        self.assertTrue(isinstance(d, dict))#断言为真

    def test_key(self): #测试方法全部都需要以"test"开头
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

#   TestDict 中有多个test_xxx()测试方法

if __name__ == '__main__':
    unittest.main()
#有了以上两行，直接执行本脚本就能完成单元测试

# 若没有以上两行，可使用下列命令行完成单元测试
# python -m unittest mydict_test