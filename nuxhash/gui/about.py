import wx
from wx.lib.agw.hyperlink import HyperLinkCtrl


WEBSITE = 'https://github.com/YoRyan/nuxhash'
LICENSE = 'https://www.gnu.org/licenses/gpl-3.0.html'


class AboutScreen(wx.Panel):

    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        h_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        self.SetSizer(h_sizer)
        v_sizer = wx.BoxSizer(orient=wx.VERTICAL)
        h_sizer.Add(v_sizer, wx.SizerFlags().Proportion(1.0)
                                            .Align(wx.ALIGN_CENTER))

        appName = wx.StaticText(self, label='nuxhash', style=wx.ALIGN_CENTER)
        appName.SetFont(self.GetFont().Scale(2.5))
        v_sizer.Add(appName, wx.SizerFlags().Expand())

        v_sizer.AddSpacer(15)

        v_sizer.Add(wx.StaticText(self, label='A NiceHash client for Linux.',
                                  style=wx.ALIGN_CENTER),
                    wx.SizerFlags().Expand())

        v_sizer.AddSpacer(15)

        copyright = wx.StaticText(self, label='Copyright © 2018\nRyan Young',
                                  style=wx.ALIGN_CENTER)
        copyright.SetFont(self.GetFont().Scale(0.8))
        v_sizer.Add(copyright, wx.SizerFlags().Expand())

        v_sizer.AddSpacer(30)

        links = wx.BoxSizer(orient=wx.HORIZONTAL)
        links.Add(HyperLinkCtrl(self, label='Website', URL=WEBSITE))
        links.AddSpacer(30)
        links.Add(HyperLinkCtrl(self, label='License', URL=LICENSE))
        v_sizer.Add(links, wx.SizerFlags().Align(wx.ALIGN_CENTER))
