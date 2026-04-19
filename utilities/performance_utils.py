"""
Performance Monitoring Utilities
"""
import time
from functools import wraps
from utilities.logger import get_logger

logger = get_logger(__name__)

class PerformanceMonitor:
    """Monitor and log performance metrics"""
    
    @staticmethod
    def measure_time(func):
        """Decorator to measure function execution time"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            logger.info(f"{func.__name__} took {duration:.2f} seconds")
            return result
        return wrapper
    
    @staticmethod
    def log_timing(start_time, operation_name, threshold_seconds=None):
        """
        Log operation timing
        
        Args:
            start_time: Start time from time.time()
            operation_name: Name of the operation
            threshold_seconds: Warn if duration exceeds threshold
        """
        duration = time.time() - start_time
        logger.info(f"{operation_name} completed in {duration:.2f} seconds")
        
        if threshold_seconds and duration > threshold_seconds:
            logger.warning(f"{operation_name} exceeded threshold of {threshold_seconds}s")
        
        return duration
    
    @staticmethod
    def create_timer():
        """Create a context manager for timing blocks"""
        return _Timer()

class _Timer:
    """Context manager for timing code blocks"""
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.duration = time.time() - self.start
        logger.info(f"Operation took {self.duration:.2f} seconds")
