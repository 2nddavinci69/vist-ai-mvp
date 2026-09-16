import math
class VISTAIAnalyzer:
def __init__(self, threshold=0.5):
self.threshold = threshold
def calculate_geometric_variance(self, expected_coords, actual_coords):
"""
Calculates the Euclidean distance between
the expected and actual geometric coordinates.
"""
distance = math.sqrt((expected_coords[0] - actual_coords[0])**2 +
(expected_coords[1] - actual_coords[1])**2)
return distance
def evaluate_output(self, expected_coords, actual_coords):
variance = self.calculate_geometric_variance(expected_coords, actual_coords)
if variance > self.threshold:
return {
"status": "FLAGGED",
"variance": variance,
"message": "Geometric inconsistency detected! Possible deepfake or AI distortion."
}
else:
return {
"status": "VERIFIED",
"variance": variance,
"message": "Output is geometrically consistent and secure."
}
# --- Demo Run for Testing ---
if __name__ == "__main__":
analyzer = VISTAIAnalyzer(threshold=1.5)

# Example expected and actual geometric points
expected = (10.0, 20.0)
actual_distorted = (12.5, 21.0) # Suspicious output

result = analyzer.evaluate_output(expected, actual_distorted)
print("--- VIST-AI Forensic Evaluation Report ---")
print(f"Status: {result['status']}")
print(f"Variance Score: {result['variance']:.2f}")
print(f"Details: {result['message']}")