#!/usr/bin/perl
print "Content-type: text/html\n\n";

#URL��Ͽ�� ver.2
#By Nomura Masayuki

require 'jcode.pl';
if ($ENV{'REQUEST_METHOD'} eq "POST") {
    read(STDIN, $str, $ENV{'CONTENT_LENGTH'});
} else {
    $str = $ENV{'QUERY_STRING'};
}

#
#ʸ�������ɥ��åȤʤ�
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
#�鴁E�āE
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
̾�����񤫤�EƤ���E���ǧ#
i

f ($url eq "" || $body eq "") { 
   print "<html><head><title>���ϥ��顼</title></head>\n"; 
   print "<body bgcolor=black text=white alink=red link=yellow vlink=green>ʪ��EΥ��ɥ�E��Ȳ����ɬ�����Ϥ��Ƥ�������<br>"; 
   print "<a href=\"http://venus13.aid.kyushu-id.ac.jp/~nomura/itai/momo.html\">�ᤁE/a></body></html>"; 
   exit (1);}
$

url = "http://$url";i

f ($urlname eq "") { 
   $urlname = $url}
#

#
��Ͽ���꤬�Ȥ�#
p

rint "<html><head><title>���꤬�Ȥ��������ޤ�</title></html>\n";p
rint "<body bgcolor=black text=white alink=red link=yellow vlink=green>�ʲ��Τ褦����Ͽ����Eޤ�����\n";p
rint "<br>ʪ��E��ɥ�E�:<br><strong>$url</strong>\n";p
rint "<br>ʪ��E�:<br><strong>$urlname</strong>\n";p
rint "<br>����E<br><strong><pre>$body</pre></strong></p>\n";p
rint "�ɤ��⤢�꤬�Ȥ��������ޤ�����\n";p
rint "<p><a href=\"http://venus13.aid.kyushu-id.ac.jp/~nomura/itai/index.html\">�ڡ�����</a></p></body></html>";#

#
�����˵�Ͽ#
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
