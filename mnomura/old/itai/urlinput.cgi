#!/usr/bin/perl
print "Content-type: text/html\n\n";

#URL登録板 ver.2
#By Nomura Masayuki

require 'jcode.pl';
if ($ENV{'REQUEST_METHOD'} eq "POST") {
    read(STDIN, $str, $ENV{'CONTENT_LENGTH'});
} else {
    $str = $ENV{'QUERY_STRING'};
}

#
#文字コードセットなど
#

@part = split('&', $str);
foreach $i (@part) {
    ($variable, $value) = split('=', $i);
    $value =~ tr/+/ /;
    $value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
    &jcode'convert(*value, 'euc');
    $value =~ s/</&lt;/g;
    $value =~ s/>/&gt;/g;
    $value =~ s/\015\012/\n/g;
    $value =~ s/\015/\n/g;
    $value =~ s/\012/\n/g;
    $cgi{$variable} = $value;
}

#
#初��E瀋�E
$

nkf = "/usr/local/bin/nkf -e";$
logfile = "/home/nomura/public_html/itai/index.html";$
tmp = "/tmp/nomura-itai-log.tmp";$
cat = $cgi{'cat'};$
url = $cgi{'url'};$
urlname = $cgi{'urlname'};$
body = $cgi{'body'};$
body =~ s/\n/<br>\n/g;c

hop($date = `date`);#

#
名前が書か��E討△�E�確認#
i

f ($url eq "" || $body eq "") { 
   print "<html><head><title>入力エラー</title></head>\n"; 
   print "<body bgcolor=black text=white alink=red link=yellow vlink=green>物��E離▲疋�E垢伐鮴發鷲�ず入力してください<br>"; 
   print "<a href=\"http://venus13.aid.kyushu-id.ac.jp/~nomura/itai/momo.html\">戻��E/a></body></html>"; 
   exit (1);}
$

url = "http://$url";i

f ($urlname eq "") { 
   $urlname = $url}
#

#
登録ありがとう#
p

rint "<html><head><title>ありがとうございます</title></html>\n";p
rint "<body bgcolor=black text=white alink=red link=yellow vlink=green>以下のように登録さ��E泙靴拭�\n";p
rint "<br>物��E▲疋�E�:<br><strong>$url</strong>\n";p
rint "<br>物��E�:<br><strong>$urlname</strong>\n";p
rint "<br>解��E<br><strong><pre>$body</pre></strong></p>\n";p
rint "どうもありがとうございました。\n";p
rint "<p><a href=\"http://venus13.aid.kyushu-id.ac.jp/~nomura/itai/index.html\">ページへ</a></p></body></html>";#

#
��前に記録#
o

pen (TMP, ">$tmp");o
pen (FILE, "$nkf < $logfile |");w

hile (<FILE>) { 
   if (/<!--$cat-->/) { 
       print TMP "<!--$cat-->\n"; 
       print TMP "<dt><font size=\"+1\"><a href=\"$url\">$urlname</a></font>\n"; 
       print TMP "<font size=\"-1\">($date)</font>\n"; 
       print TMP "<dd>$body<br><br>\n"; 
   } 
   else { 
       print TMP $_; 
   }}
o

pen (TMP, "<$tmp");o
pen (FILE, "|$nkf > $logfile");w
hile(<TMP>) { 
   print FILE $_;}
c
lose(FILE);c
lose(TMP);u
nlink "$tmp";
