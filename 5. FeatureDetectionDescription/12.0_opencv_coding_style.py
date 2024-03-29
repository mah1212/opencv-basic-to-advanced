The OpenCV Coding Style Guide

The document is a short guide on code style, used in OpenCV. The core libraries (core, imgproc, etc) are written in C++, so the document concerns only the С++ code style.
Files

All the functionality must be put into one or more .cpp and .hpp files into the appropriate module of OpenCV, or a new module should be created if the contributed functionality is a rather large piece of code, or if it does not fit any existing module.

    All the file names are written in lower case for better compatibility with both POSIX and Windows.
    C++ interface headers have .hpp extension
    Implementation files have .cpp extension
    The implementation is put into opencv/modules/<module_name>/src, interface is added to the header files in opencv/modules/<module_name>/include/opencv2/<module_name>. There is no need to add the files to the module explicitly, just rerun CMake and it will add the files automatically.
    Sample code in C++, if any, is put into opencv/samples/cpp (with exception of gpu and ocl modules, which have dedicated sample directories), sample code in Python – to opencv/samples/python2.
    Documentation is put into opencv/modules/<module_name>/doc, into one of the existing files or a new file/chapter is added there. In the latter case the file name should be listed in the TOC (table of content) file opencv/modules/<module_name>/doc/<module_name>.rst
    Tests are put to opencv/modules/<module_name>/test. When a new test source file is added, rerun CMake. If the test needs some data, put it to the separate top-level directory. For ml module the test data is put into opencv_extra/testdata/ml subdirectory, for other modules – to opencv_extra/testdata/cv subdirectory. Please, limit size of your test data files within a few megabytes, the smaller the better. If some existing test data can be used for your tests (like lena.jpg etc.), please, re-use it.

File Structure

Every source file, except for the samples, starts with license header:

// This file is part of OpenCV project.
// It is subject to the license terms in the LICENSE file found in the top-level directory
// of this distribution and at http://opencv.org/license.html.

OpenCV code license (BSD-compatible) can be found here.
The extra/different copyright clauses are possible (including adding your name into created file), as long as the license stays BSD-compatible.

Other rules for both header and implementation files include:

    All the functionality must be put into cv namespace, or, possibly, some nested namespace, e.g. cv::vslam
    Code lines should not be very long. Normally, they should be limited to 100 characters.
    No tabulation should be used. Set your editor to use spaces instead.
    Indentation is 4 spaces.
    Only English text (ASCII) is allowed. Do not put comments or string literals in other languages.
    Header files must use guarding macros, protecting the files from repeated inclusion:

#ifndef OPENCV_module_name_header_name_HPP
#define OPENCV_module_name_header_name_HPP
namespace cv { namespace mynamespace {
...
}}
#endif

    Source files must include precomp.hpp header before other headers, in order to make precompiled headers mechanism in Visual C++ work properly.

Naming conventions

    OpenCV uses mixed-case style identifiers for external functions, types and class methods.
    Class names start with a capital letter.
    methods’ and functions’ names start with a small latter, unless they are named after the author of the algorithm, e.g. cv::Sobel(), in which case they can start with a capital letter.
    Macros and enumeration constants are written with all capital letters. Words are separated by underscore.
    All external functions and classes must use CV_EXPORTS, otherwise there will be linking errors on Windows. For functions/classes which you want to expose in Python, Java etc. you should use CV_EXPORTS_W instead of CV_EXPORTS, but please be careful with overloaded functions and methods, with non-standard parameter types etc.

Designing functions and class interfaces

It is important to design function interface is a way, consistent with the rest of the library. The elements of function interface include:

    Functionality
    Name
    Return value
    Type of arguments
    Order of arguments
    Default values for some arguments

Functionality

The functionality must be well defined and non-redundant. The function should be easily embedded into different processing pipelines that use other OpenCV functions.
Name

The name should basically reflect the function purpose. There are a few common naming patterns in OpenCV:

    Majority of function names have form: <actionName><Object><Modifiers>, e.g. calibrateCamera, calcOpticalFlowPyrLK.
    Sometimes the function may be called by the algorithm name it implements or result object name it produces, e.g. Sobel, Canny, Rodrigues, sqrt, goodFeaturesToTrack.

Return value

It should be chosen to simplify function usage. Generally, a function that creates/computes a value should return it. It is the good practice to do so for the functions returning scalar values. However, in case of image processing function this would lead to frequent allocation/deallocation of large memory blocks. Image processing functions often modify an output image, which is passed as a parameter (by reference) instead of creating and returning result images.

Functions should not use return value for signaling about critical errors, such as null pointers, division by zero, bad argument range, unsupported image format etc. Instead, they should throw an exception, an instance of cv::Exception or its derivative class. On the other hand, it is recommended to use a return value for reporting quite normal run-time situations that can happen in a correctly working system (e.g. tracked object goes outside of the image etc.)
Types of arguments

Argument types are preferably chosen from the already existing set of OpenCV types: Mat for raster images and matrices, vector<Mat> for collection of images, vector<Point>, vector<Point2f>, vector<Point3f>, vector<KeyPoint> for point sets, contours or collections of key points, Scalar for 1- to 4-element numerical tuples (like colors, quaternions etc.) It is not recommended to use plain pointers and counters, because it makes the interface lower-level, meaning more probable typing errors, memory leaks etc. For passing complex objects into functions, methods, please, consider Ptr<> smart pointer template class.

A consistent argument order is important because it becomes easier to remember the order and it helps programmer to avoid errors, connecting with wrong argument order. The usual order is: <input parameters>, <output parameters>, <flags and optional parameters>.

Input parameters usually have const qualifiers. Large objects are normally passed by a constant reference; primitive types and small structures (int, double, Point, Rect) are passed by value.

Optional arguments often simplify function usage. Because C++ allows optional arguments in the end of parameters list only, it also may affect decisions on argument order—the most important flags go first and less important—after.

For example function and class declarations, take a look at http://github.com/opencv/opencv/blob/master/modules/core/include/opencv2/core/core.hpp.
Using InputArray, OutputArray etc.

In 2.4 we introduced new “proxy” datatypes in OpenCV to support multiple array types simultaneously. For example, in some cases it’s more convenient to represent a point set as vector, in other cases – as a matrix. In some cases it’s more convenient to store homography matrix as Mat, in other – as Matx33f. If a parameter of your function has type Mat, Matx<>, vector<Point...>, vector<Mat> or vector<vector<Point...> >, please, consider using InputArray, OutputArray etc. types instead.

    InputArray – used for input arrays; you can only read from the arrays and do not modify or reallocate them. For example, parameter of cv::determinant() function is InputArray.
    InputOutputArray – used for both input/output arrays, i.e. arrays which are modified inside the functions. For example, in all drawing functions, like cv::line, cv::drawContours etc. the image is of InputOutputArray type.
    OutputArray – used for output arrays. The function can not assume that the array has the proper size and type, or that its content is somehow initialized. Instead, it should call OutputArray::create() method to ensure the correct size and type. You can also call create() on input/output arrays, if you want, but normally you do not have to.

These types are called proxy classes because they are not real arrays. They just store pointers to the actual arrays and the “kind” of array (Mat, Matx, vector<> etc.). So when you see some function that takes such a parameter, it means that it can take Mat, Matx or vector<>. Since those Array types are proxy classes, you should not declare local variables of those types unless you are expert in C++ and know exactly what you are doing.

In fact, InputArray is the base class for OutputArray and InputOutputArray is synonym for OutputArray. But you should use the proper names in the function arguments to assist the automatic wrapper generators.

Inside the functions that take InputArray/InputOutputArray/OutputArray you just call .getMat() method to get the underlying matrix. In the case of OutputArray you should call OutputArray::create() method before .getMat().

User may want to omit certain input and/or output arrays. In this case he passes noArray() instead of the actual array. In the case of InputArray or InputOutputArray it can easily be checked with Mat::empty() method for the matrix that you retrieve with .getMat(). In the case of OutputArray you should use OutputArray::needed() method to check if user really wants this output array to be computed.
High-level C++ interface. Algorithms

In some cases you may want to represent your algorithm as a class, not a function. For example, the algorithm may include certain state that is updated with time (e.g. background/foreground subtractor with its background statistics). Or the algorithm may have too many parameters to put them into a single call. Some algorithms may have include several steps (e.g. training and prediction in machine learning methods) etc.

If you decide to make your algorithm a class, you should follow OpenCV Algorithm concept.
Rationale and principles of the Algorithm-based design

    We want our API to stay stable when the implementation changes.
    We want to preserve not only source-level compatibility, but possibly binary-level compatibility as well.
    We want to keep the header files clean and easily track changes in API.
    We want to keep our tools that parse OpenCV headers simple and robust (such as doc checker and automatic wrapper generators)
    We want OpenCV to build fast.

To address those goals, we physically separate interface and implementation part of our C++ classes. That is, we only expose interfaces, i.e. classes without constructors, without data members and with all purely virtual methods. The actual implementation is put into classes derived from those interfaces. The actual construction of the class is done by an exposed function (usually, a static create method). It returns smart pointer to the interface. There can be multiple “constructor” or “factory” functions, not necessarily placed in the same module. Users can add their own implementations of the same interface and provide the corresponding constructor functions. See calib3d module and the stereo correspondence algorithms (stereo matchers) as example of such classes.
Steps to make your class following this style

    Derive your class from Algorithm or from its direct or indirect derivative class, e.g. StereoMatcher if you add another stereo correspondence algorithm.
    Make abstract base class for your actual implementation, e.g.

...
namespace cv { namespace mynamespace {
class MyStereoMatcher : public StereoMatcher
{
public:
virtual void setLambda(double lambda) = 0;
virtual double getLambda() const = 0;
...
// static method to construct the algorithm instance as a smart pointer to the interface class.
// there can be several constructors
static Ptr<MyStereoMatcher> create(<params> ...);
};
}}

That is, put there extra methods and properties that your algorithm will have. “Getters” should start with “get” word, “Setters” – with “set”. You do not need to repeat declarations of virtual methods of StereoMatcher, Algorithm etc., since you will implement them in your actual class anyway.

    In .cpp file put a class that implements your interface and the constructor function:

/* <OpenCV license with your copyright added> */
#include "precomp.hpp"

namespace cv { namespace mynamespace {
class MyStereoMatcherImpl : MyStereoMatcher
{
MyStereoMatcherImpl(...) { ... }
virtual ~MyStereoMatcherImpl() { ... }
...
double getLambda() const { return lambda; } // implement getters and setters
void setLambda(double l) const { CV_Assert(l >= 0); lambda = l; }

void compute(InputArray _left, InputArray _right, OutputArray _disp) // implement necessary methods from StereoMatcher, Algorithm etc.
{
Mat left = _left.getMat(), right = _right.getMat();
_disp.create(left.size(), CV_16S);
Mat disp = _disp.getMat();
...
}
...
double lambda;
};

Ptr<MyStereoMatcher> MyStereoMatcher::create(<args>) { return makePtr<MyStereoMatcherImpl>(<args>); }
}}

That’s it. You class is ready.
Extending/modifying algorithms

Say, you contributed the new algorithm to OpenCV, which was implemented as shown above, and it was integrated.
Then, sometime later you want to modify it. What do you do?

    As long as you do not modify header, all the changes are fine. Just submit them as pull request.
    If you want to add some new properties to the algorithm or modify signatures of the methods and there was no official OpenCV release yet with your code included – that’s fine too; do your modifications and submit pull request.
    If the previous variant of your algorithm has been already released, then you actually can not modify interface. Create new interface, derived from the previous one, add more properties there and add new constructor function:

namespace cv { namespace mynamespace {

class MyStereoMatcher : public StereoMatcher {...};
CV_EXPORTS Ptr<MyStereoMatcher> createMyStereoMatcher(<params...>);

// new extended interface
class MyPyrStereoMatcher : public MyStereoMatcher
{
public:
// more properties ...
virtual void setNPyramidLevels(int nlevels) = 0;
virtual double getNPyramidLevels() const = 0;
...
};

// new contractor(s)
CV_EXPORTS Ptr<MyPyrStereoMatcher> createMyPyrStereoMatcher(<new_params...>);
}}

then modify the implementation class so that it derives from the new class (if you want to have one implementation class, not two), e.g. MyStereoMatcherImpl will be derived from MyPyrStereoMatcher. Everything else stays the same and thanks to some Ptr<> magic you can pass Ptr<MyPyrStereoMatcher> anywhere where you passed Ptr<MyStereoMatcher>.

That’s it. It means that OpenCV implements the concept of immutable API, the same thing as Microsoft does with COM.
Code Layout

There is a single strict coding guideline in OpenCV: each single file must use a consistent formatting style.

Currently used in OpenCV and recommended formatting style looks as follows:


if( a > 5 )
{
    int b = a*a;
    c = c > b ? c : b + 1;
}
else if( abs(a) < 5 )
{
    c--;
}
else
{
    printf( "a=%d is far to negative\n", a );
}

Other styles might be also accepted if only the above rule is met. That is, if one changes written by others code, he (she) should use the same coding style.
Portability, External Dependencies

OpenCV 4.0+ code must comply the C++ 11 standard.
The code of OpenCV 3.x and older versions must comply with the C++98 standard.
Using of C++ extensions should be avoided and it’s forbidden in to use it the external headers.

One should get rid of compiler-dependent or platform-dependent constructions and system calls, such as:

    Compiler pragma’s
    Specific keywords, e.g. __stdcall, __inline, __int64. Use CV_INLINE (or simple inline in C++ code), CV_STDCALL (try to avoid it if possible), int64, respectively, instead.
    Compiler extensions, e.g. special macros for min and max, overloaded macros etc.
    Inline assembly
    Unix or Win32-specific calls, e.g. bcopy, readdir, CreateFile, WaitForSingleObject etc.
    Concrete data sizes instead of @sizeof@’s (sizeof(int) rather than 4), byte order ( *(int*)"\x1\x2\x3\x4" is 0×01020304 or 0×04030201 or what?), simple char instead of signed char or unsigned char anywhere except for text strings. Use short forms uchar for unsigned char and schar for signed char. Use preprocessor directives for surrounding non-portable pieces of code.

Writing documentation on functions

The documentation for contributed functions is written using inline Doxygen comments. The documentation is built nightly and is uploaded to docs.opencv.org.

Use the existing documentation as example. You are also welcome to provide tutorials for large descriptive chunks of text with pictures, code samples etc.
Implementing tests

    For tests we use GoogleTest framework. Please, check the documentation at the project site.
    Each test source file should include test_precomp.hpp first.
    All the test code is put into opencv_test namespace.
    Declare your Google tests as following:

TEST(<module_name>_<tested_class_or_function>, <test_type>) { <test_body> }

For example:

TEST(Imgproc_Watershed, regression) { ... } 

    To access test data, use cvtest::TS::ptr()->get_data_path() method. For example, if you put your test file to opencv_extra/testdata/cv/myfacetracker/clip.avi, you can use cvtest::TS::ptr()->get_data_path() + "myfacetracker/clip.avi" to get full path to the file. To make it work properly, set the environment variable OPENCV_TEST_DATA_PATH to <your_local_copy_of_opencv_extra>/testdata
    Avoid including C++ standard library headers, like vector, list, map, limits, iostream, etc.
    Avoid using namespace std. Use std:: if necessary (common types are imported into opencv_test namespace).
    Don’t use std::tr1 namespace.
    Don’t include OpenCV headers for core/imgproc/highgui. These headers are included by ts.hpp.

Appendixes

Appendix A. References

The document is not a complete style guide. Far more detailed and well-written papers on this topic are listed below:

    Recommended C Style and Coding Standards (updated version of Indian Hill C Style and Coding Standards). Henry Spencer et al. Rev. 6.0, 1990.
    Programming in C++. Rules and Recommendations. Mats Henricson, Erik Nyquist. Ellemtel Communications Systems Laboratories. 1990-1992.
    GNU Coding Standards. Richard Stallman. GNU Project – Free Software Foundation. 2000
    Notes On Writing Portable Programs in C. A. Dolenc, A. Lemmke, D. Keppel, G.V. Reilly. 1990. Links to many of these documents can be found at http://www.softpanorama.org/Lang/c.html.

Appendix B. The brief list of rules

    Filenames are written in lower-case letters.
    Headers have .hpp extension.
    Implementation files have .cpp extension
    Every file includes BSD-compatible license in the beginning
    Do not use tabulation. Indentation is 4 spaces. Lines should not be much longer than ~100 characters.
    Keep consistent formatting style in each particular source file (especially if you modify the existing code).
    Each source file includes "precomp.hpp" as the first header.
    The code is put into cv or nested namespace (cv::vslam etc.). Test code is put into opencv_test namespace.
    Only English should be used in comments and string literals.
    External function names and data type names are written in mixed case. Classes start with capital letter, functions start with small letter. External macros are written in upper case.
    Use CV_EXPORTS macro within external functions and classes declarations. Use CV_EXPORTS_W for Python- and Java- wrappable API.
    Do not use conditional compilation in headers.
    Keep the external interface as compact as possible. Do not export internal-use classes or functions which are not essential and could be hidden.
    Exposed classes should be abstract, derived from Algorithm. The actual implementation must be hidden in .cpp.
    Try to make your code easily wrappable for Python, Java etc. That is, try not to introduce new types. Limit the use of callbacks.
    Consider use of InputArray/InputOutputArray/OutputArray for array parameters.
    Use CV_Error to report about incorrect parameters and/or use CV_Assert to verify some conditions, e.g. CV_Assert(inputImage.type() == CV_8UC3).
    Be compliant with the C/C++ standards. Avoid compiler-dependent, OS-dependent and platform-dependent constructions. Do not use C++ 11 and/or TR1 extensions yet.
    Try not to use malloc/free, new/delete. Use cv::Mat, std::vector, std::map, cv::AutoBuffer, cv::Ptr instead. Those classes handle the memory automatically.
    Provide GTest-based tests for your code.
    Provide documentation for your code as Doxygen comments. Tutorials are welcome.

© Copyright 2019, OpenCV team
Pages 96

    Home
        Changelog (older)
        New functionality discussion
            RGBD
            Documentation improvement plan
        Android
            Release Notes
            Building
        CiteOpenCV
        OpenCVLogo
    Deep Learning in OpenCV
        DNN Efficiency
        TensorFlow Object Detection API
        Intel's Deep Learning Inference Engine backend
    OpenCV 4
        Graph API (G-API)
    OpenCV 3
        OpenCL optimizations
        CPU optimizations
        Profiling OpenCV Applications
        Video capture and write benchmark
        MediaSDK encode/decode backend
        Building more compact applications with OpenCV
    Development process
        How to contribute
        Coding style guide
        Branches
        Evolution Proposals
        Contributors
        Tech guides:
            Working with Git
            Windows 7 guide
            Unix based guide
        Meeting notes
            2019
            2018
            2017
            2016
            2015
            2014
            2013
            2012
            2011
            2010
            2009
            2008
        QA for OpenCV
            Android tests
            Using performance tests
            Writing performance tests
    Tutorials
        CARMA platform
        Debug in Visual Studio
        Displaying multiple images
        Face detection
        POSIT
        WindowsRT
        АИСТ 2013 (ru)
    Computer Vision and Pattern Recognition
        2015
        2014
        2010
    OpenCV GSoC
        2019 Ideas List
        Our Application
        Previous Idea lists
            2018
            2017
            2016
            2015
            2014
            2011
    Vision challenge
    Workshops
        OpenCV_Talks

Clone this wiki locally

    © 2019 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help
