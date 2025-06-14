void main() {
  // Student Information input data
  String studentName = "Alex Vizuete";
  int studentID = 1023;
  List<int> grades = [85, 90, 78, 92];
  Map<String, String> subjectCodes = {"math": "MTH101", "science": "SCI102"};
  bool isEnrolled = true;
  const double maxScore = 100.0;
  double total = 0.0;
  double average = 0.0;
  String result = "";
  String comment = null;

  // Print basic info
  print("Evaluating: $studentName (ID: $studentID)");
  print("Enrolled: $isEnrolled");

  // Calculate total
  for (int i = 0; i < grades.length; i++) {
    total += grades[i];
  }

  average = total / grades.length;

  if (average >= 90) {
    result = "Excellent";
  } else if (average >= 80 && average < 90) {
    result = "Good";
  } else if (average >= 70) {
    result = "Fair";
  } else {
    result = "Fail";
  }

// RP
  if (result == "Fail") {
    comment = "Needs improvement";
  }

  // Final output
  print("Average score: $average");
  print("Result: $result");
  if (comment != null) {
    print("Comment: $comment");
  }
}
