// Generated from /Users/chao-xu21/Clong/translator/src/antlr/clong.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class clongParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, PAR=40, INT=41, DOUBLE=42, CHAR=43, STRING=44, LineComment=45, 
		BlockComment=46, DELIMITER=47;
	public static final int
		RULE_prog = 0, RULE_head = 1, RULE_include = 2, RULE_main = 3, RULE_body = 4, 
		RULE_func = 5, RULE_block = 6, RULE_printf = 7, RULE_gets = 8, RULE_strlen = 9, 
		RULE_returnFunc = 10, RULE_ifElse = 11, RULE_ifFunc = 12, RULE_elseif = 13, 
		RULE_elseFunc = 14, RULE_whileFunc = 15, RULE_forFunc = 16, RULE_initFunc = 17, 
		RULE_assignFunc = 18, RULE_initParam = 19, RULE_initArray = 20, RULE_assign = 21, 
		RULE_exp = 22, RULE_condition = 23, RULE_typeParam = 24, RULE_array = 25, 
		RULE_library = 26, RULE_paramName = 27, RULE_intm = 28, RULE_doublem = 29, 
		RULE_charm = 30, RULE_stringm = 31;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "head", "include", "main", "body", "func", "block", "printf", 
			"gets", "strlen", "returnFunc", "ifElse", "ifFunc", "elseif", "elseFunc", 
			"whileFunc", "forFunc", "initFunc", "assignFunc", "initParam", "initArray", 
			"assign", "exp", "condition", "typeParam", "array", "library", "paramName", 
			"intm", "doublem", "charm", "stringm"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'#include'", "'<'", "'>'", "'int'", "'void'", "'main'", "'()'", 
			"'{'", "'}'", "';'", "'printf'", "'('", "','", "')'", "'gets'", "'strlen'", 
			"'return'", "'if'", "'else'", "'while'", "'for'", "'='", "'['", "']'", 
			"'-'", "'+'", "'*'", "'/'", "'%'", "'>='", "'<='", "'=='", "'!='", "'!'", 
			"'&&'", "'||'", "'char'", "'double'", "'.h'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "PAR", "INT", "DOUBLE", "CHAR", "STRING", "LineComment", 
			"BlockComment", "DELIMITER"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "clong.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public clongParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public HeadContext head() {
			return getRuleContext(HeadContext.class,0);
		}
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			head();
			setState(65);
			main();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HeadContext extends ParserRuleContext {
		public List<IncludeContext> include() {
			return getRuleContexts(IncludeContext.class);
		}
		public IncludeContext include(int i) {
			return getRuleContext(IncludeContext.class,i);
		}
		public HeadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_head; }
	}

	public final HeadContext head() throws RecognitionException {
		HeadContext _localctx = new HeadContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_head);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(67);
				include();
				}
				}
				setState(72);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IncludeContext extends ParserRuleContext {
		public LibraryContext library() {
			return getRuleContext(LibraryContext.class,0);
		}
		public IncludeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include; }
	}

	public final IncludeContext include() throws RecognitionException {
		IncludeContext _localctx = new IncludeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_include);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			match(T__0);
			setState(74);
			match(T__1);
			setState(75);
			library();
			setState(76);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MainContext extends ParserRuleContext {
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			_la = _input.LA(1);
			if ( !(_la==T__3 || _la==T__4) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(79);
			match(T__5);
			setState(80);
			match(T__6);
			setState(81);
			match(T__7);
			setState(82);
			body();
			setState(83);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public List<FuncContext> func() {
			return getRuleContexts(FuncContext.class);
		}
		public FuncContext func(int i) {
			return getRuleContext(FuncContext.class,i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1511832127504L) != 0)) {
				{
				setState(89);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__10:
				case T__14:
				case T__15:
				case T__16:
					{
					setState(85);
					func();
					setState(86);
					match(T__9);
					}
					break;
				case T__3:
				case T__17:
				case T__19:
				case T__20:
				case T__36:
				case T__37:
				case PAR:
					{
					setState(88);
					block();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncContext extends ParserRuleContext {
		public PrintfContext printf() {
			return getRuleContext(PrintfContext.class,0);
		}
		public GetsContext gets() {
			return getRuleContext(GetsContext.class,0);
		}
		public StrlenContext strlen() {
			return getRuleContext(StrlenContext.class,0);
		}
		public ReturnFuncContext returnFunc() {
			return getRuleContext(ReturnFuncContext.class,0);
		}
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_func);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				{
				setState(94);
				printf();
				}
				break;
			case T__14:
				{
				setState(95);
				gets();
				}
				break;
			case T__15:
				{
				setState(96);
				strlen();
				}
				break;
			case T__16:
				{
				setState(97);
				returnFunc();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public IfElseContext ifElse() {
			return getRuleContext(IfElseContext.class,0);
		}
		public WhileFuncContext whileFunc() {
			return getRuleContext(WhileFuncContext.class,0);
		}
		public ForFuncContext forFunc() {
			return getRuleContext(ForFuncContext.class,0);
		}
		public InitParamContext initParam() {
			return getRuleContext(InitParamContext.class,0);
		}
		public InitArrayContext initArray() {
			return getRuleContext(InitArrayContext.class,0);
		}
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_block);
		try {
			setState(106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(100);
				ifElse();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(101);
				whileFunc();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(102);
				forFunc();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(103);
				initParam();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(104);
				initArray();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(105);
				assign();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintfContext extends ParserRuleContext {
		public StringmContext stringm() {
			return getRuleContext(StringmContext.class,0);
		}
		public ParamNameContext paramName() {
			return getRuleContext(ParamNameContext.class,0);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public PrintfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printf; }
	}

	public final PrintfContext printf() throws RecognitionException {
		PrintfContext _localctx = new PrintfContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_printf);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(T__10);
			setState(109);
			match(T__11);
			{
			setState(112);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING:
				{
				setState(110);
				stringm();
				}
				break;
			case PAR:
				{
				setState(111);
				paramName();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(118);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__12) {
				{
				{
				setState(114);
				match(T__12);
				setState(115);
				exp(0);
				}
				}
				setState(120);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(121);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GetsContext extends ParserRuleContext {
		public ParamNameContext paramName() {
			return getRuleContext(ParamNameContext.class,0);
		}
		public GetsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_gets; }
	}

	public final GetsContext gets() throws RecognitionException {
		GetsContext _localctx = new GetsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_gets);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(T__14);
			setState(124);
			match(T__11);
			setState(125);
			paramName();
			setState(126);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StrlenContext extends ParserRuleContext {
		public ParamNameContext paramName() {
			return getRuleContext(ParamNameContext.class,0);
		}
		public StrlenContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_strlen; }
	}

	public final StrlenContext strlen() throws RecognitionException {
		StrlenContext _localctx = new StrlenContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_strlen);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(T__15);
			setState(129);
			match(T__11);
			setState(130);
			paramName();
			setState(131);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnFuncContext extends ParserRuleContext {
		public IntmContext intm() {
			return getRuleContext(IntmContext.class,0);
		}
		public ReturnFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnFunc; }
	}

	public final ReturnFuncContext returnFunc() throws RecognitionException {
		ReturnFuncContext _localctx = new ReturnFuncContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_returnFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			match(T__16);
			setState(135);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(134);
				intm();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfElseContext extends ParserRuleContext {
		public IfFuncContext ifFunc() {
			return getRuleContext(IfFuncContext.class,0);
		}
		public List<ElseifContext> elseif() {
			return getRuleContexts(ElseifContext.class);
		}
		public ElseifContext elseif(int i) {
			return getRuleContext(ElseifContext.class,i);
		}
		public ElseFuncContext elseFunc() {
			return getRuleContext(ElseFuncContext.class,0);
		}
		public IfElseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifElse; }
	}

	public final IfElseContext ifElse() throws RecognitionException {
		IfElseContext _localctx = new IfElseContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_ifElse);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			ifFunc();
			setState(141);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(138);
					elseif();
					}
					} 
				}
				setState(143);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(145);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18) {
				{
				setState(144);
				elseFunc();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfFuncContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public IfFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifFunc; }
	}

	public final IfFuncContext ifFunc() throws RecognitionException {
		IfFuncContext _localctx = new IfFuncContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_ifFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			match(T__17);
			setState(148);
			match(T__11);
			setState(149);
			condition(0);
			setState(150);
			match(T__13);
			setState(151);
			match(T__7);
			setState(152);
			body();
			setState(153);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElseifContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ElseifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseif; }
	}

	public final ElseifContext elseif() throws RecognitionException {
		ElseifContext _localctx = new ElseifContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_elseif);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(T__18);
			setState(156);
			match(T__17);
			setState(157);
			match(T__11);
			setState(158);
			condition(0);
			setState(159);
			match(T__13);
			setState(160);
			match(T__7);
			setState(161);
			body();
			setState(162);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElseFuncContext extends ParserRuleContext {
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ElseFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseFunc; }
	}

	public final ElseFuncContext elseFunc() throws RecognitionException {
		ElseFuncContext _localctx = new ElseFuncContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_elseFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			match(T__18);
			setState(165);
			match(T__7);
			setState(166);
			body();
			setState(167);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileFuncContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public WhileFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileFunc; }
	}

	public final WhileFuncContext whileFunc() throws RecognitionException {
		WhileFuncContext _localctx = new WhileFuncContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_whileFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(T__19);
			setState(170);
			match(T__11);
			setState(171);
			condition(0);
			setState(172);
			match(T__13);
			setState(173);
			match(T__7);
			setState(174);
			body();
			setState(175);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForFuncContext extends ParserRuleContext {
		public InitFuncContext initFunc() {
			return getRuleContext(InitFuncContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public AssignFuncContext assignFunc() {
			return getRuleContext(AssignFuncContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ForFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forFunc; }
	}

	public final ForFuncContext forFunc() throws RecognitionException {
		ForFuncContext _localctx = new ForFuncContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_forFunc);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			match(T__20);
			setState(178);
			match(T__11);
			setState(179);
			initFunc();
			setState(180);
			match(T__9);
			setState(181);
			condition(0);
			setState(182);
			match(T__9);
			setState(183);
			assignFunc();
			setState(184);
			match(T__13);
			setState(185);
			match(T__7);
			setState(186);
			body();
			setState(187);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InitFuncContext extends ParserRuleContext {
		public ParamNameContext paramName() {
			return getRuleContext(ParamNameContext.class,0);
		}
		public TypeParamContext typeParam() {
			return getRuleContext(TypeParamContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public InitFuncContext initFunc() {
			return getRuleContext(InitFuncContext.class,0);
		}
		public InitFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initFunc; }
	}

	public final InitFuncContext initFunc() throws RecognitionException {
		InitFuncContext _localctx = new InitFuncContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_initFunc);
		int _la;
		try {
			setState(202);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
			case T__36:
			case T__37:
			case PAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(190);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 412316860432L) != 0)) {
					{
					setState(189);
					typeParam();
					}
				}

				setState(192);
				paramName();
				setState(195);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__21) {
					{
					setState(193);
					match(T__21);
					setState(194);
					exp(0);
					}
				}

				setState(199);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__12) {
					{
					setState(197);
					match(T__12);
					setState(198);
					initFunc();
					}
				}

				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignFuncContext extends ParserRuleContext {
		public ParamNameContext paramName() {
			return getRuleContext(ParamNameContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public AssignFuncContext assignFunc() {
			return getRuleContext(AssignFuncContext.class,0);
		}
		public AssignFuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignFunc; }
	}

	public final AssignFuncContext assignFunc() throws RecognitionException {
		AssignFuncContext _localctx = new AssignFuncContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_assignFunc);
		int _la;
		try {
			setState(212);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(204);
				paramName();
				setState(205);
				match(T__21);
				setState(206);
				exp(0);
				setState(209);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__12) {
					{
					setState(207);
					match(T__12);
					setState(208);
					assignFunc();
					}
				}

				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InitParamContext extends ParserRuleContext {
		public TypeParamContext typeParam() {
			return getRuleContext(TypeParamContext.class,0);
		}
		public List<ParamNameContext> paramName() {
			return getRuleContexts(ParamNameContext.class);
		}
		public ParamNameContext paramName(int i) {
			return getRuleContext(ParamNameContext.class,i);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public InitParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initParam; }
	}

	public final InitParamContext initParam() throws RecognitionException {
		InitParamContext _localctx = new InitParamContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_initParam);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			typeParam();
			setState(215);
			paramName();
			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__21) {
				{
				setState(216);
				match(T__21);
				setState(217);
				exp(0);
				}
			}

			setState(228);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__12) {
				{
				{
				setState(220);
				match(T__12);
				setState(221);
				paramName();
				setState(224);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__21) {
					{
					setState(222);
					match(T__21);
					setState(223);
					exp(0);
					}
				}

				}
				}
				setState(230);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(231);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InitArrayContext extends ParserRuleContext {
		public TypeParamContext typeParam() {
			return getRuleContext(TypeParamContext.class,0);
		}
		public ParamNameContext paramName() {
			return getRuleContext(ParamNameContext.class,0);
		}
		public IntmContext intm() {
			return getRuleContext(IntmContext.class,0);
		}
		public InitArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initArray; }
	}

	public final InitArrayContext initArray() throws RecognitionException {
		InitArrayContext _localctx = new InitArrayContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_initArray);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			typeParam();
			setState(234);
			paramName();
			setState(235);
			match(T__22);
			setState(236);
			intm();
			setState(237);
			match(T__23);
			setState(238);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public List<ParamNameContext> paramName() {
			return getRuleContexts(ParamNameContext.class);
		}
		public ParamNameContext paramName(int i) {
			return getRuleContext(ParamNameContext.class,i);
		}
		public List<ArrayContext> array() {
			return getRuleContexts(ArrayContext.class);
		}
		public ArrayContext array(int i) {
			return getRuleContext(ArrayContext.class,i);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_assign);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(246); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(242);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
					case 1:
						{
						setState(240);
						paramName();
						}
						break;
					case 2:
						{
						setState(241);
						array();
						}
						break;
					}
					setState(244);
					match(T__21);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(248); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(250);
			exp(0);
			}
			setState(252);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public Token op;
		public CharmContext charm() {
			return getRuleContext(CharmContext.class,0);
		}
		public StringmContext stringm() {
			return getRuleContext(StringmContext.class,0);
		}
		public ParamNameContext paramName() {
			return getRuleContext(ParamNameContext.class,0);
		}
		public IntmContext intm() {
			return getRuleContext(IntmContext.class,0);
		}
		public DoublemContext doublem() {
			return getRuleContext(DoublemContext.class,0);
		}
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		return exp(0);
	}

	private ExpContext exp(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpContext _localctx = new ExpContext(_ctx, _parentState);
		ExpContext _prevctx = _localctx;
		int _startState = 44;
		enterRecursionRule(_localctx, 44, RULE_exp, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				{
				setState(255);
				charm();
				}
				break;
			case 2:
				{
				setState(256);
				stringm();
				}
				break;
			case 3:
				{
				setState(257);
				paramName();
				}
				break;
			case 4:
				{
				setState(259);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__24) {
					{
					setState(258);
					((ExpContext)_localctx).op = match(T__24);
					}
				}

				setState(263);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT:
					{
					setState(261);
					intm();
					}
					break;
				case DOUBLE:
					{
					setState(262);
					doublem();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case 5:
				{
				setState(265);
				array();
				}
				break;
			case 6:
				{
				setState(266);
				func();
				}
				break;
			case 7:
				{
				setState(267);
				match(T__11);
				setState(268);
				exp(0);
				setState(269);
				match(T__13);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(278);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp);
					setState(273);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(274);
					((ExpContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1040187392L) != 0)) ) {
						((ExpContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(275);
					exp(2);
					}
					} 
				}
				setState(280);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public Token op;
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		return condition(0);
	}

	private ConditionContext condition(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ConditionContext _localctx = new ConditionContext(_ctx, _parentState);
		ConditionContext _prevctx = _localctx;
		int _startState = 46;
		enterRecursionRule(_localctx, 46, RULE_condition, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				setState(282);
				match(T__11);
				setState(283);
				condition(0);
				setState(284);
				match(T__13);
				}
				break;
			case 2:
				{
				setState(286);
				exp(0);
				setState(287);
				((ConditionContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 16106127372L) != 0)) ) {
					((ConditionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(288);
				exp(0);
				}
				break;
			case 3:
				{
				setState(290);
				match(T__33);
				setState(291);
				condition(2);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(299);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ConditionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_condition);
					setState(294);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(295);
					((ConditionContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__34 || _la==T__35) ) {
						((ConditionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(296);
					condition(2);
					}
					} 
				}
				setState(301);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeParamContext extends ParserRuleContext {
		public TypeParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeParam; }
	}

	public final TypeParamContext typeParam() throws RecognitionException {
		TypeParamContext _localctx = new TypeParamContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_typeParam);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 412316860432L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayContext extends ParserRuleContext {
		public ParamNameContext paramName() {
			return getRuleContext(ParamNameContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_array);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(304);
			paramName();
			setState(305);
			match(T__22);
			setState(306);
			exp(0);
			setState(307);
			match(T__23);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LibraryContext extends ParserRuleContext {
		public TerminalNode PAR() { return getToken(clongParser.PAR, 0); }
		public LibraryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_library; }
	}

	public final LibraryContext library() throws RecognitionException {
		LibraryContext _localctx = new LibraryContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_library);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(309);
			match(PAR);
			setState(311);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__38) {
				{
				setState(310);
				match(T__38);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamNameContext extends ParserRuleContext {
		public TerminalNode PAR() { return getToken(clongParser.PAR, 0); }
		public ParamNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramName; }
	}

	public final ParamNameContext paramName() throws RecognitionException {
		ParamNameContext _localctx = new ParamNameContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_paramName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(313);
			match(PAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IntmContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(clongParser.INT, 0); }
		public IntmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intm; }
	}

	public final IntmContext intm() throws RecognitionException {
		IntmContext _localctx = new IntmContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_intm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DoublemContext extends ParserRuleContext {
		public TerminalNode DOUBLE() { return getToken(clongParser.DOUBLE, 0); }
		public DoublemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doublem; }
	}

	public final DoublemContext doublem() throws RecognitionException {
		DoublemContext _localctx = new DoublemContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_doublem);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(317);
			match(DOUBLE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CharmContext extends ParserRuleContext {
		public TerminalNode CHAR() { return getToken(clongParser.CHAR, 0); }
		public CharmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_charm; }
	}

	public final CharmContext charm() throws RecognitionException {
		CharmContext _localctx = new CharmContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_charm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(319);
			match(CHAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringmContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(clongParser.STRING, 0); }
		public StringmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringm; }
	}

	public final StringmContext stringm() throws RecognitionException {
		StringmContext _localctx = new StringmContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_stringm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(321);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 22:
			return exp_sempred((ExpContext)_localctx, predIndex);
		case 23:
			return condition_sempred((ConditionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean exp_sempred(ExpContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean condition_sempred(ConditionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001/\u0144\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0005\u0001E\b\u0001\n\u0001\f\u0001H\t\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0005\u0004Z\b\u0004\n\u0004\f\u0004]\t\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005c\b\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006k\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0003\u0007q\b\u0007\u0001\u0007\u0001\u0007\u0005\u0007u\b\u0007\n\u0007"+
		"\f\u0007x\t\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0003"+
		"\n\u0088\b\n\u0001\u000b\u0001\u000b\u0005\u000b\u008c\b\u000b\n\u000b"+
		"\f\u000b\u008f\t\u000b\u0001\u000b\u0003\u000b\u0092\b\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0003\u0011\u00bf\b\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011"+
		"\u00c4\b\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00c8\b\u0011\u0001"+
		"\u0011\u0003\u0011\u00cb\b\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0003\u0012\u00d2\b\u0012\u0001\u0012\u0003\u0012\u00d5"+
		"\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00db"+
		"\b\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00e1"+
		"\b\u0013\u0005\u0013\u00e3\b\u0013\n\u0013\f\u0013\u00e6\t\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0003\u0015\u00f3"+
		"\b\u0015\u0001\u0015\u0001\u0015\u0004\u0015\u00f7\b\u0015\u000b\u0015"+
		"\f\u0015\u00f8\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u0104\b\u0016"+
		"\u0001\u0016\u0001\u0016\u0003\u0016\u0108\b\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u0110\b\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u0115\b\u0016\n\u0016"+
		"\f\u0016\u0118\t\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0003\u0017\u0125\b\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0005\u0017\u012a\b\u0017\n\u0017\f\u0017\u012d\t\u0017\u0001\u0018\u0001"+
		"\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u001a\u0001\u001a\u0003\u001a\u0138\b\u001a\u0001\u001b\u0001\u001b\u0001"+
		"\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0000\u0002,. \u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,."+
		"02468:<>\u0000\u0005\u0001\u0000\u0004\u0005\u0001\u0000\u0019\u001d\u0002"+
		"\u0000\u0002\u0003\u001e!\u0001\u0000#$\u0002\u0000\u0004\u0004%&\u014b"+
		"\u0000@\u0001\u0000\u0000\u0000\u0002F\u0001\u0000\u0000\u0000\u0004I"+
		"\u0001\u0000\u0000\u0000\u0006N\u0001\u0000\u0000\u0000\b[\u0001\u0000"+
		"\u0000\u0000\nb\u0001\u0000\u0000\u0000\fj\u0001\u0000\u0000\u0000\u000e"+
		"l\u0001\u0000\u0000\u0000\u0010{\u0001\u0000\u0000\u0000\u0012\u0080\u0001"+
		"\u0000\u0000\u0000\u0014\u0085\u0001\u0000\u0000\u0000\u0016\u0089\u0001"+
		"\u0000\u0000\u0000\u0018\u0093\u0001\u0000\u0000\u0000\u001a\u009b\u0001"+
		"\u0000\u0000\u0000\u001c\u00a4\u0001\u0000\u0000\u0000\u001e\u00a9\u0001"+
		"\u0000\u0000\u0000 \u00b1\u0001\u0000\u0000\u0000\"\u00ca\u0001\u0000"+
		"\u0000\u0000$\u00d4\u0001\u0000\u0000\u0000&\u00d6\u0001\u0000\u0000\u0000"+
		"(\u00e9\u0001\u0000\u0000\u0000*\u00f6\u0001\u0000\u0000\u0000,\u010f"+
		"\u0001\u0000\u0000\u0000.\u0124\u0001\u0000\u0000\u00000\u012e\u0001\u0000"+
		"\u0000\u00002\u0130\u0001\u0000\u0000\u00004\u0135\u0001\u0000\u0000\u0000"+
		"6\u0139\u0001\u0000\u0000\u00008\u013b\u0001\u0000\u0000\u0000:\u013d"+
		"\u0001\u0000\u0000\u0000<\u013f\u0001\u0000\u0000\u0000>\u0141\u0001\u0000"+
		"\u0000\u0000@A\u0003\u0002\u0001\u0000AB\u0003\u0006\u0003\u0000B\u0001"+
		"\u0001\u0000\u0000\u0000CE\u0003\u0004\u0002\u0000DC\u0001\u0000\u0000"+
		"\u0000EH\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000FG\u0001\u0000"+
		"\u0000\u0000G\u0003\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000"+
		"IJ\u0005\u0001\u0000\u0000JK\u0005\u0002\u0000\u0000KL\u00034\u001a\u0000"+
		"LM\u0005\u0003\u0000\u0000M\u0005\u0001\u0000\u0000\u0000NO\u0007\u0000"+
		"\u0000\u0000OP\u0005\u0006\u0000\u0000PQ\u0005\u0007\u0000\u0000QR\u0005"+
		"\b\u0000\u0000RS\u0003\b\u0004\u0000ST\u0005\t\u0000\u0000T\u0007\u0001"+
		"\u0000\u0000\u0000UV\u0003\n\u0005\u0000VW\u0005\n\u0000\u0000WZ\u0001"+
		"\u0000\u0000\u0000XZ\u0003\f\u0006\u0000YU\u0001\u0000\u0000\u0000YX\u0001"+
		"\u0000\u0000\u0000Z]\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000"+
		"[\\\u0001\u0000\u0000\u0000\\\t\u0001\u0000\u0000\u0000][\u0001\u0000"+
		"\u0000\u0000^c\u0003\u000e\u0007\u0000_c\u0003\u0010\b\u0000`c\u0003\u0012"+
		"\t\u0000ac\u0003\u0014\n\u0000b^\u0001\u0000\u0000\u0000b_\u0001\u0000"+
		"\u0000\u0000b`\u0001\u0000\u0000\u0000ba\u0001\u0000\u0000\u0000c\u000b"+
		"\u0001\u0000\u0000\u0000dk\u0003\u0016\u000b\u0000ek\u0003\u001e\u000f"+
		"\u0000fk\u0003 \u0010\u0000gk\u0003&\u0013\u0000hk\u0003(\u0014\u0000"+
		"ik\u0003*\u0015\u0000jd\u0001\u0000\u0000\u0000je\u0001\u0000\u0000\u0000"+
		"jf\u0001\u0000\u0000\u0000jg\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000"+
		"\u0000ji\u0001\u0000\u0000\u0000k\r\u0001\u0000\u0000\u0000lm\u0005\u000b"+
		"\u0000\u0000mp\u0005\f\u0000\u0000nq\u0003>\u001f\u0000oq\u00036\u001b"+
		"\u0000pn\u0001\u0000\u0000\u0000po\u0001\u0000\u0000\u0000qv\u0001\u0000"+
		"\u0000\u0000rs\u0005\r\u0000\u0000su\u0003,\u0016\u0000tr\u0001\u0000"+
		"\u0000\u0000ux\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000\u0000vw\u0001"+
		"\u0000\u0000\u0000wy\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000"+
		"yz\u0005\u000e\u0000\u0000z\u000f\u0001\u0000\u0000\u0000{|\u0005\u000f"+
		"\u0000\u0000|}\u0005\f\u0000\u0000}~\u00036\u001b\u0000~\u007f\u0005\u000e"+
		"\u0000\u0000\u007f\u0011\u0001\u0000\u0000\u0000\u0080\u0081\u0005\u0010"+
		"\u0000\u0000\u0081\u0082\u0005\f\u0000\u0000\u0082\u0083\u00036\u001b"+
		"\u0000\u0083\u0084\u0005\u000e\u0000\u0000\u0084\u0013\u0001\u0000\u0000"+
		"\u0000\u0085\u0087\u0005\u0011\u0000\u0000\u0086\u0088\u00038\u001c\u0000"+
		"\u0087\u0086\u0001\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000"+
		"\u0088\u0015\u0001\u0000\u0000\u0000\u0089\u008d\u0003\u0018\f\u0000\u008a"+
		"\u008c\u0003\u001a\r\u0000\u008b\u008a\u0001\u0000\u0000\u0000\u008c\u008f"+
		"\u0001\u0000\u0000\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008d\u008e"+
		"\u0001\u0000\u0000\u0000\u008e\u0091\u0001\u0000\u0000\u0000\u008f\u008d"+
		"\u0001\u0000\u0000\u0000\u0090\u0092\u0003\u001c\u000e\u0000\u0091\u0090"+
		"\u0001\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0017"+
		"\u0001\u0000\u0000\u0000\u0093\u0094\u0005\u0012\u0000\u0000\u0094\u0095"+
		"\u0005\f\u0000\u0000\u0095\u0096\u0003.\u0017\u0000\u0096\u0097\u0005"+
		"\u000e\u0000\u0000\u0097\u0098\u0005\b\u0000\u0000\u0098\u0099\u0003\b"+
		"\u0004\u0000\u0099\u009a\u0005\t\u0000\u0000\u009a\u0019\u0001\u0000\u0000"+
		"\u0000\u009b\u009c\u0005\u0013\u0000\u0000\u009c\u009d\u0005\u0012\u0000"+
		"\u0000\u009d\u009e\u0005\f\u0000\u0000\u009e\u009f\u0003.\u0017\u0000"+
		"\u009f\u00a0\u0005\u000e\u0000\u0000\u00a0\u00a1\u0005\b\u0000\u0000\u00a1"+
		"\u00a2\u0003\b\u0004\u0000\u00a2\u00a3\u0005\t\u0000\u0000\u00a3\u001b"+
		"\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005\u0013\u0000\u0000\u00a5\u00a6"+
		"\u0005\b\u0000\u0000\u00a6\u00a7\u0003\b\u0004\u0000\u00a7\u00a8\u0005"+
		"\t\u0000\u0000\u00a8\u001d\u0001\u0000\u0000\u0000\u00a9\u00aa\u0005\u0014"+
		"\u0000\u0000\u00aa\u00ab\u0005\f\u0000\u0000\u00ab\u00ac\u0003.\u0017"+
		"\u0000\u00ac\u00ad\u0005\u000e\u0000\u0000\u00ad\u00ae\u0005\b\u0000\u0000"+
		"\u00ae\u00af\u0003\b\u0004\u0000\u00af\u00b0\u0005\t\u0000\u0000\u00b0"+
		"\u001f\u0001\u0000\u0000\u0000\u00b1\u00b2\u0005\u0015\u0000\u0000\u00b2"+
		"\u00b3\u0005\f\u0000\u0000\u00b3\u00b4\u0003\"\u0011\u0000\u00b4\u00b5"+
		"\u0005\n\u0000\u0000\u00b5\u00b6\u0003.\u0017\u0000\u00b6\u00b7\u0005"+
		"\n\u0000\u0000\u00b7\u00b8\u0003$\u0012\u0000\u00b8\u00b9\u0005\u000e"+
		"\u0000\u0000\u00b9\u00ba\u0005\b\u0000\u0000\u00ba\u00bb\u0003\b\u0004"+
		"\u0000\u00bb\u00bc\u0005\t\u0000\u0000\u00bc!\u0001\u0000\u0000\u0000"+
		"\u00bd\u00bf\u00030\u0018\u0000\u00be\u00bd\u0001\u0000\u0000\u0000\u00be"+
		"\u00bf\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001\u0000\u0000\u0000\u00c0"+
		"\u00c3\u00036\u001b\u0000\u00c1\u00c2\u0005\u0016\u0000\u0000\u00c2\u00c4"+
		"\u0003,\u0016\u0000\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001"+
		"\u0000\u0000\u0000\u00c4\u00c7\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005"+
		"\r\u0000\u0000\u00c6\u00c8\u0003\"\u0011\u0000\u00c7\u00c5\u0001\u0000"+
		"\u0000\u0000\u00c7\u00c8\u0001\u0000\u0000\u0000\u00c8\u00cb\u0001\u0000"+
		"\u0000\u0000\u00c9\u00cb\u0001\u0000\u0000\u0000\u00ca\u00be\u0001\u0000"+
		"\u0000\u0000\u00ca\u00c9\u0001\u0000\u0000\u0000\u00cb#\u0001\u0000\u0000"+
		"\u0000\u00cc\u00cd\u00036\u001b\u0000\u00cd\u00ce\u0005\u0016\u0000\u0000"+
		"\u00ce\u00d1\u0003,\u0016\u0000\u00cf\u00d0\u0005\r\u0000\u0000\u00d0"+
		"\u00d2\u0003$\u0012\u0000\u00d1\u00cf\u0001\u0000\u0000\u0000\u00d1\u00d2"+
		"\u0001\u0000\u0000\u0000\u00d2\u00d5\u0001\u0000\u0000\u0000\u00d3\u00d5"+
		"\u0001\u0000\u0000\u0000\u00d4\u00cc\u0001\u0000\u0000\u0000\u00d4\u00d3"+
		"\u0001\u0000\u0000\u0000\u00d5%\u0001\u0000\u0000\u0000\u00d6\u00d7\u0003"+
		"0\u0018\u0000\u00d7\u00da\u00036\u001b\u0000\u00d8\u00d9\u0005\u0016\u0000"+
		"\u0000\u00d9\u00db\u0003,\u0016\u0000\u00da\u00d8\u0001\u0000\u0000\u0000"+
		"\u00da\u00db\u0001\u0000\u0000\u0000\u00db\u00e4\u0001\u0000\u0000\u0000"+
		"\u00dc\u00dd\u0005\r\u0000\u0000\u00dd\u00e0\u00036\u001b\u0000\u00de"+
		"\u00df\u0005\u0016\u0000\u0000\u00df\u00e1\u0003,\u0016\u0000\u00e0\u00de"+
		"\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001\u0000\u0000\u0000\u00e1\u00e3"+
		"\u0001\u0000\u0000\u0000\u00e2\u00dc\u0001\u0000\u0000\u0000\u00e3\u00e6"+
		"\u0001\u0000\u0000\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e5"+
		"\u0001\u0000\u0000\u0000\u00e5\u00e7\u0001\u0000\u0000\u0000\u00e6\u00e4"+
		"\u0001\u0000\u0000\u0000\u00e7\u00e8\u0005\n\u0000\u0000\u00e8\'\u0001"+
		"\u0000\u0000\u0000\u00e9\u00ea\u00030\u0018\u0000\u00ea\u00eb\u00036\u001b"+
		"\u0000\u00eb\u00ec\u0005\u0017\u0000\u0000\u00ec\u00ed\u00038\u001c\u0000"+
		"\u00ed\u00ee\u0005\u0018\u0000\u0000\u00ee\u00ef\u0005\n\u0000\u0000\u00ef"+
		")\u0001\u0000\u0000\u0000\u00f0\u00f3\u00036\u001b\u0000\u00f1\u00f3\u0003"+
		"2\u0019\u0000\u00f2\u00f0\u0001\u0000\u0000\u0000\u00f2\u00f1\u0001\u0000"+
		"\u0000\u0000\u00f3\u00f4\u0001\u0000\u0000\u0000\u00f4\u00f5\u0005\u0016"+
		"\u0000\u0000\u00f5\u00f7\u0001\u0000\u0000\u0000\u00f6\u00f2\u0001\u0000"+
		"\u0000\u0000\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8\u00f6\u0001\u0000"+
		"\u0000\u0000\u00f8\u00f9\u0001\u0000\u0000\u0000\u00f9\u00fa\u0001\u0000"+
		"\u0000\u0000\u00fa\u00fb\u0003,\u0016\u0000\u00fb\u00fc\u0001\u0000\u0000"+
		"\u0000\u00fc\u00fd\u0005\n\u0000\u0000\u00fd+\u0001\u0000\u0000\u0000"+
		"\u00fe\u00ff\u0006\u0016\uffff\uffff\u0000\u00ff\u0110\u0003<\u001e\u0000"+
		"\u0100\u0110\u0003>\u001f\u0000\u0101\u0110\u00036\u001b\u0000\u0102\u0104"+
		"\u0005\u0019\u0000\u0000\u0103\u0102\u0001\u0000\u0000\u0000\u0103\u0104"+
		"\u0001\u0000\u0000\u0000\u0104\u0107\u0001\u0000\u0000\u0000\u0105\u0108"+
		"\u00038\u001c\u0000\u0106\u0108\u0003:\u001d\u0000\u0107\u0105\u0001\u0000"+
		"\u0000\u0000\u0107\u0106\u0001\u0000\u0000\u0000\u0108\u0110\u0001\u0000"+
		"\u0000\u0000\u0109\u0110\u00032\u0019\u0000\u010a\u0110\u0003\n\u0005"+
		"\u0000\u010b\u010c\u0005\f\u0000\u0000\u010c\u010d\u0003,\u0016\u0000"+
		"\u010d\u010e\u0005\u000e\u0000\u0000\u010e\u0110\u0001\u0000\u0000\u0000"+
		"\u010f\u00fe\u0001\u0000\u0000\u0000\u010f\u0100\u0001\u0000\u0000\u0000"+
		"\u010f\u0101\u0001\u0000\u0000\u0000\u010f\u0103\u0001\u0000\u0000\u0000"+
		"\u010f\u0109\u0001\u0000\u0000\u0000\u010f\u010a\u0001\u0000\u0000\u0000"+
		"\u010f\u010b\u0001\u0000\u0000\u0000\u0110\u0116\u0001\u0000\u0000\u0000"+
		"\u0111\u0112\n\u0001\u0000\u0000\u0112\u0113\u0007\u0001\u0000\u0000\u0113"+
		"\u0115\u0003,\u0016\u0002\u0114\u0111\u0001\u0000\u0000\u0000\u0115\u0118"+
		"\u0001\u0000\u0000\u0000\u0116\u0114\u0001\u0000\u0000\u0000\u0116\u0117"+
		"\u0001\u0000\u0000\u0000\u0117-\u0001\u0000\u0000\u0000\u0118\u0116\u0001"+
		"\u0000\u0000\u0000\u0119\u011a\u0006\u0017\uffff\uffff\u0000\u011a\u011b"+
		"\u0005\f\u0000\u0000\u011b\u011c\u0003.\u0017\u0000\u011c\u011d\u0005"+
		"\u000e\u0000\u0000\u011d\u0125\u0001\u0000\u0000\u0000\u011e\u011f\u0003"+
		",\u0016\u0000\u011f\u0120\u0007\u0002\u0000\u0000\u0120\u0121\u0003,\u0016"+
		"\u0000\u0121\u0125\u0001\u0000\u0000\u0000\u0122\u0123\u0005\"\u0000\u0000"+
		"\u0123\u0125\u0003.\u0017\u0002\u0124\u0119\u0001\u0000\u0000\u0000\u0124"+
		"\u011e\u0001\u0000\u0000\u0000\u0124\u0122\u0001\u0000\u0000\u0000\u0125"+
		"\u012b\u0001\u0000\u0000\u0000\u0126\u0127\n\u0001\u0000\u0000\u0127\u0128"+
		"\u0007\u0003\u0000\u0000\u0128\u012a\u0003.\u0017\u0002\u0129\u0126\u0001"+
		"\u0000\u0000\u0000\u012a\u012d\u0001\u0000\u0000\u0000\u012b\u0129\u0001"+
		"\u0000\u0000\u0000\u012b\u012c\u0001\u0000\u0000\u0000\u012c/\u0001\u0000"+
		"\u0000\u0000\u012d\u012b\u0001\u0000\u0000\u0000\u012e\u012f\u0007\u0004"+
		"\u0000\u0000\u012f1\u0001\u0000\u0000\u0000\u0130\u0131\u00036\u001b\u0000"+
		"\u0131\u0132\u0005\u0017\u0000\u0000\u0132\u0133\u0003,\u0016\u0000\u0133"+
		"\u0134\u0005\u0018\u0000\u0000\u01343\u0001\u0000\u0000\u0000\u0135\u0137"+
		"\u0005(\u0000\u0000\u0136\u0138\u0005\'\u0000\u0000\u0137\u0136\u0001"+
		"\u0000\u0000\u0000\u0137\u0138\u0001\u0000\u0000\u0000\u01385\u0001\u0000"+
		"\u0000\u0000\u0139\u013a\u0005(\u0000\u0000\u013a7\u0001\u0000\u0000\u0000"+
		"\u013b\u013c\u0005)\u0000\u0000\u013c9\u0001\u0000\u0000\u0000\u013d\u013e"+
		"\u0005*\u0000\u0000\u013e;\u0001\u0000\u0000\u0000\u013f\u0140\u0005+"+
		"\u0000\u0000\u0140=\u0001\u0000\u0000\u0000\u0141\u0142\u0005,\u0000\u0000"+
		"\u0142?\u0001\u0000\u0000\u0000\u001cFY[bjpv\u0087\u008d\u0091\u00be\u00c3"+
		"\u00c7\u00ca\u00d1\u00d4\u00da\u00e0\u00e4\u00f2\u00f8\u0103\u0107\u010f"+
		"\u0116\u0124\u012b\u0137";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}