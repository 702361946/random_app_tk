# 须知
    第一次启动必跳配置错误,仅需重置一次即可

# 设置帮助
## 密码
    哪有什么密码,问题太多,已经废了)
## random_list(列表抽取)修改指南
    文本&数字(文本要加""),在文本&数字后面加","(英文逗号)
    符合json格式就行
    示例如下
    "random_list": [1,"aa","bb","222"]
## weight(权重)修改指南
    键(你要的): 值(整数)
    !!!
    所有键必须被""(英文双引号)包裹
    所有值必须为整数(可以被双引号包裹)
    !!!
    所有权重默认为1
    权重为0则不会抽到,为负数时虽不会报错,但强烈不建议使用负数
    所有"整数"都将被转化为整数,且不保留原来的"整数"(str)->(int)
    所以无法对纯数字文本取权重(后期可能会改)
    示例如下
    "weight": {"qwq": 10, "qaq": 0}

    目前的权重编辑并不能编辑数值
    请修改文件
## 模式输入
    键"mode"的值为下列值(str)的时候启用的模式
    "randint"整数(需求条件a<b,为什么,因为a>b没结果,a=b出值已知)
    "list"列表(空列表将返回None,所以没结果,所以列表要有最少一个值)

