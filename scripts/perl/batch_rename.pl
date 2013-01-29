#!/usr/bin/perl
use warnings;
#use strict;

sub rename_files{
   my $directory_name = shift @_

}


sub main{

}


my @directories = @ARGV;
my $filenumber = 1;
foreach $directory_name (@directories){
    print "NO.",$filenumber,"::",$directory_name,"\n";
    opendir DH, $directory_name or die "Cannot open $directory_name:$!";
    foreach $file (readdir DH){
        if ($file =~ /(?<number>\d{1})\.(?<type>\w*?)$/){
            my $newfile = $directory_name.'/'.$+{number} .".". $+{type};
            my $oldfile = $directory_name.'/'.$file;
            if (-e $newfile){
                warn "Cant't rename $oldfile to $newfile: $newfile exists\n";
            }
            elsif(rename $oldfile, $newfile){
                print $oldfile," => ",$newfile,"\n";
                #eval{
                #};
                #if ($@) {
                #    print "An error occoured ($@), continuing\n";
                #}
            }
            else{
                warn "rename $oldfile to $newfile failed: $!\n"
            }
        }
    }
    closedir DH;
    $filenumber++;
}
