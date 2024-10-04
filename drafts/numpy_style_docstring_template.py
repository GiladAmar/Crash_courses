1. Function
    1.  Summary
    2.  Deprecation warning (optional)
    3.  Extended summary (optional)
        clarify functionality
    4.  Parameters
        Description of the function arguments, keywords and respective types.
    5.  Returns/Yields
    6.  Raises (optional)
    7.  Warns (optional)
        Similar to Raises
    8.  Warnings (optional)
        For the coder
    9.  See Also (optional)
    10. Notes (optional)
        discuss implementation detail or background theory
    11. References (optional)
    12. Examples (optional)

    """
    Minimal docstring example
    
    Parameters
    ----------
    path : str
        Path to xls or xlsx file.

    Returns
    -------
    err_code : int
        Non-zero value indicates error code. Name is specified

    """

2. Class
    1.  Attributes
    2.  Methods
    * dont list private methods
    * dont list self as parameter

    class Example_object(exposure):
        """
        Array with associated photographic information.

        ...

        Attributes
        ----------
        exposure : float
            Exposure in seconds.

        Methods
        -------
        colorspace(c='rgb')
            Represent the photo in the given colorspace.
        """

3. Module
    1.  Summary
    2.  Extended summary (optional)
        
    3.  Routine listings (optional)
    4.  See also (optional)
    5.  Notes (optional)
        
    6.  References (optional)
    7.  Examples (optional)

    """
    Minimal docstring is summary.
    """

Complete function dosctring:
"""
    Simple summary
    
    Parameters
    ----------
    path : str
        Path to xls or xlsx file.
    engine : str (optional)
        Engine to use for writing. Optional parameter
    date_format : str, (default None which implies all-time)
    mode : {'w', 'a'}, default 'w'
        File mode to use (write or append).
    y
        description of `y` with no `:` since type is not specified
    x1, x2 : array_like
    Input arrays, description of `x1`, `x2`. 
    These are the same shape type and description so can be combined

    Returns
    -------
    int
        Description of anonymous integer return value. Name is not specified
    err_code : int
        Non-zero value indicates error code. Name is specified

    Yields: # same as Returns but for generator
    ------
    ...

    Raises
    ------
    LinAlgException
        If the matrix is not numerically invertible.
        Use only for non-obvious errors or high probability errors

    See Also
    --------
    average : Weighted average
    fft.fft2 : Function in diff module
    scipy.random.norm : Function in diff package

    Notes
    -----
    None of the methods and properties are considered public.
    For compatibility with CSV writers, ExcelWriter serializes lists
    and dicts to strings before writing.
    
    References
    ------
    .. [1] O. McNoleg, "Fuzzy-logic" Computers & Geosciences, vol. 22,
   pp. 585-588, 1996 (cited in text elsewhere with `[1]_`)

    Examples
    --------
    Default usage:
    >>> with ExcelWriter('path_to_file.xlsx') as writer:
    ...     df.to_excel(writer)
    To write to separate sheets in a single file:
    >>> with ExcelWriter('path_to_file.xlsx') as writer:
    ...     df1.to_excel(writer, sheet_name='Sheet1')
    ...     df2.to_excel(writer, sheet_name='Sheet2')
"""