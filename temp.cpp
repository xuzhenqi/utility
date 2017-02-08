#include <iostream>
#include "gflags/gflags.h"

using namespace google;

DEFINE_bool(verbose, false, "Display program name before message");
DEFINE_string(message, "Hello world!", "Message to print");

static bool IsNonEmptyMessage(const char *flagname, const std::string &value)
{
  return value[0] != '\0';

}

int main(int argc, char *argv[])
{
  SetUsageMessage("some usage message");
  SetVersionString("1.0.0");
  ParseCommandLineFlags(&argc, &argv, true);
  if (FLAGS_verbose) std::cout << ProgramInvocationShortName() << ": ";
  ShutDownCommandLineFlags();
  return 0;

}
