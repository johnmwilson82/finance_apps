# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FinanceAppGuiBase
###########################################################################

class FinanceAppGuiBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"YQL Finance App", pos = wx.DefaultPosition, size = wx.Size( 665,610 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Tickers = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		m_symbolsListChoices = []
		self.m_symbolsList = wx.CheckListBox( self.m_Tickers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_symbolsListChoices, 0|wx.NO_BORDER )
		bSizer7.Add( self.m_symbolsList, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_btnUpdateSymbols = wx.Button( self.m_Tickers, wx.ID_ANY, u"Update Symbols", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btnUpdateSymbols, 1, wx.ALL, 5 )
		
		m_marketChoiceChoices = [ u".L" ]
		self.m_marketChoice = wx.Choice( self.m_Tickers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_marketChoiceChoices, 0 )
		self.m_marketChoice.SetSelection( 0 )
		bSizer5.Add( self.m_marketChoice, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_txtStockProperties = wx.TextCtrl( self.m_Tickers, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.NO_BORDER )
		bSizer3.Add( self.m_txtStockProperties, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		m_industriesListChoices = []
		self.m_industriesList = wx.CheckListBox( self.m_Tickers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_industriesListChoices, 0|wx.NO_BORDER )
		bSizer4.Add( self.m_industriesList, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btnSelAllIndustries1 = wx.Button( self.m_Tickers, wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_btnSelAllIndustries1, 0, wx.ALL, 5 )
		
		m_sectorsListChoices = []
		self.m_sectorsList = wx.CheckListBox( self.m_Tickers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_sectorsListChoices, 0|wx.NO_BORDER )
		bSizer4.Add( self.m_sectorsList, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_btnUpdateSectors = wx.Button( self.m_Tickers, wx.ID_ANY, u"Update Sectors", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_btnUpdateSectors, 1, wx.ALL, 5 )
		
		self.m_btnSelAllSectors = wx.Button( self.m_Tickers, wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_btnSelAllSectors, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_Tickers.SetSizer( bSizer2 )
		self.m_Tickers.Layout()
		bSizer2.Fit( self.m_Tickers )
		self.m_notebook1.AddPage( self.m_Tickers, u"a page", False )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_symbolsList.Bind( wx.EVT_LISTBOX, self.onSelectSymbol )
		self.m_symbolsList.Bind( wx.EVT_CHECKLISTBOX, self.onCheckSymbol )
		self.m_btnUpdateSymbols.Bind( wx.EVT_BUTTON, self.onUpdateSymbolsClick )
		self.m_industriesList.Bind( wx.EVT_LISTBOX, self.onSelectSymbol )
		self.m_industriesList.Bind( wx.EVT_CHECKLISTBOX, self.onCheckSymbol )
		self.m_btnSelAllIndustries1.Bind( wx.EVT_BUTTON, self.onUpdateSymbolsClick )
		self.m_sectorsList.Bind( wx.EVT_CHECKLISTBOX, self.onSectorsListToggled )
		self.m_btnUpdateSectors.Bind( wx.EVT_BUTTON, self.onUpdateSectorsClick )
		self.m_btnSelAllSectors.Bind( wx.EVT_BUTTON, self.onUpdateSymbolsClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSelectSymbol( self, event ):
		event.Skip()
	
	def onCheckSymbol( self, event ):
		event.Skip()
	
	def onUpdateSymbolsClick( self, event ):
		event.Skip()
	
	
	
	
	def onSectorsListToggled( self, event ):
		event.Skip()
	
	def onUpdateSectorsClick( self, event ):
		event.Skip()
	
	

