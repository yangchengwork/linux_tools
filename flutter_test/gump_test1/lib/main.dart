import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';  // 新增了这一行

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // final wordPair = new WordPair.random(); // 新增了这一行
    return new MaterialApp(
      title: 'Welcome to Flutter',
      home: new Scaffold(
        appBar: new AppBar(
          title: const Text('Gump to Flutter'),
        ),
        body: new Center(    // 这里把之前的 "const" 换成了 "new".
          //child: const Text('Hello World'),   // 我们不用这样的方式生成文字了
          // child: new Text(wordPair.asPascalCase),  // 这是新的文字生成方式
          child: new RandomWords(),                 // 修改成本行代码
        ),
      ),
    );
  }
}

class RandomWordsState extends State<RandomWords> {
  // TODO Add build method
  @override                                  // 新增代码片段 - 开始 ... 
  Widget build(BuildContext context) {
    final WordPair wordPair = new WordPair.random();
    return new Text(wordPair.asPascalCase);
  }                                          // ... 新增的代码片段 - 结束
}

class RandomWords extends StatefulWidget {
  @override
  RandomWordsState createState() => new RandomWordsState();
}